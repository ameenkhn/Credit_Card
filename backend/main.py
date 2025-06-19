from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict
import openai
import os
from dotenv import load_dotenv
from recommendation_engine import RecommendationEngine
from database import init_db, get_db
from sqlalchemy.orm import Session
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize the database
init_db()

app = FastAPI(title="Credit Card Recommendation API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3002"],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize recommendation engine
try:
    recommendation_engine = RecommendationEngine()
except Exception as e:
    logger.error(f"Failed to initialize recommendation engine: {e}")
    raise

class UserPreferences(BaseModel):
    monthly_income: float = Field(..., gt=0, description="Monthly income in INR")
    spending_habits: Dict[str, float] = Field(..., description="Spending habits by category")
    preferred_benefits: List[str] = Field(..., min_items=1, description="List of preferred benefits")
    existing_cards: Optional[List[str]] = Field(None, description="List of existing credit cards")
    credit_score: Optional[int] = Field(None, ge=300, le=850, description="Credit score (300-850)")

    @validator('spending_habits')
    def validate_spending_habits(cls, v):
        if not v:
            raise ValueError("Spending habits cannot be empty")
        if any(amount < 0 for amount in v.values()):
            raise ValueError("Spending amounts cannot be negative")
        return v

    @validator('preferred_benefits')
    def validate_preferred_benefits(cls, v):
        if not v:
            raise ValueError("At least one preferred benefit is required")
        return v

class CardRecommendation(BaseModel):
    name: str
    issuer: str
    annual_fee: float
    reward_type: str
    reward_rate: float
    key_benefits: List[str]
    estimated_rewards: float
    recommendation_reason: str
    apply_link: str

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error handler caught: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc)}
    )

@app.get("/")
async def read_root():
    return {"message": "Credit Card Recommendation API", "status": "running"}

@app.get("/health")
async def health_check():
    try:
        # Test database connection
        db = next(get_db())
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {"status": "unhealthy", "error": str(e)}

@app.post("/recommend", response_model=List[CardRecommendation])
async def get_recommendations(preferences: UserPreferences, db: Session = Depends(get_db)):
    try:
        logger.info(f"Received recommendation request: {preferences.dict()}")
        recommendations = recommendation_engine.get_recommendations(preferences.dict())
        
        if not recommendations:
            logger.warning("No recommendations found for the given preferences")
            raise HTTPException(
                status_code=404,
                detail="No suitable credit cards found for your preferences"
            )
            
        logger.info(f"Generated {len(recommendations)} recommendations")
        return recommendations
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error in get_recommendations: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing your request: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 