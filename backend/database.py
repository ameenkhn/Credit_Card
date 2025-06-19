from sqlalchemy import create_engine, Column, Integer, String, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./credit_cards.db")

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    logger.error(f"Failed to initialize database engine: {e}")
    raise

class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    issuer = Column(String)
    annual_fee = Column(Float)
    joining_fee = Column(Float)
    reward_type = Column(String)
    reward_rate = Column(Float)
    eligibility_criteria = Column(JSON)
    key_benefits = Column(JSON)
    apply_link = Column(String)

# Comprehensive dataset of Indian credit cards
SAMPLE_CARDS = [
    {
        "name": "HDFC Regalia",
        "issuer": "HDFC Bank",
        "annual_fee": 2500,
        "joining_fee": 2500,
        "reward_type": "Travel Points",
        "reward_rate": 4.0,
        "eligibility_criteria": {
            "minimum_income": 1200000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Golf Program"
        ],
        "apply_link": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-credit-card"
    },
    {
        "name": "Amex Platinum",
        "issuer": "American Express",
        "annual_fee": 60000,
        "joining_fee": 60000,
        "reward_type": "Membership Rewards",
        "reward_rate": 5.0,
        "eligibility_criteria": {
            "minimum_income": 1800000,
            "credit_score": 800
        },
        "key_benefits": [
            "Premium Airport Lounge Access",
            "Hotel Status Upgrades",
            "Concierge Service",
            "Travel Insurance",
            "Golf Program"
        ],
        "apply_link": "https://www.americanexpress.com/in/credit-cards/platinum-card"
    },
    {
        "name": "ICICI Amazon Pay",
        "issuer": "ICICI Bank",
        "annual_fee": 0,
        "joining_fee": 0,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 600000,
            "credit_score": 700
        },
        "key_benefits": [
            "No Annual Fee",
            "Amazon Pay Cashback",
            "Fuel Surcharge Waiver",
            "Zero Foreign Currency Markup"
        ],
        "apply_link": "https://www.icicibank.com/Personal-Banking/cards/credit-card/amazon-pay-credit-card/index.page"
    },
    {
        "name": "SBI SimplyCLICK",
        "issuer": "State Bank of India",
        "annual_fee": 499,
        "joining_fee": 499,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 300000,
            "credit_score": 650
        },
        "key_benefits": [
            "Online Shopping Rewards",
            "BookMyShow Offers",
            "Fuel Surcharge Waiver",
            "Welcome Benefits"
        ],
        "apply_link": "https://www.sbicard.com/en/personal/credit-cards/rewards/simplyclick.page"
    },
    {
        "name": "Axis Magnus",
        "issuer": "Axis Bank",
        "annual_fee": 10000,
        "joining_fee": 10000,
        "reward_type": "Travel Points",
        "reward_rate": 4.5,
        "eligibility_criteria": {
            "minimum_income": 1500000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Golf Program",
            "Priority Pass"
        ],
        "apply_link": "https://www.axisbank.com/retail/cards/credit-card/magnus-credit-card/features-benefits"
    },
    {
        "name": "Citi Cashback",
        "issuer": "Citibank",
        "annual_fee": 1000,
        "joining_fee": 1000,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 600000,
            "credit_score": 700
        },
        "key_benefits": [
            "Unlimited Cashback",
            "Fuel Surcharge Waiver",
            "Zero Foreign Currency Markup",
            "Welcome Benefits"
        ],
        "apply_link": "https://www.citibank.co.in/credit-card/cashback-credit-card"
    },
    {
        "name": "HDFC Millennia",
        "issuer": "HDFC Bank",
        "annual_fee": 1000,
        "joining_fee": 1000,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 600000,
            "credit_score": 700
        },
        "key_benefits": [
            "Cashback on Online Shopping",
            "Fuel Surcharge Waiver",
            "Welcome Benefits",
            "Zero Foreign Currency Markup"
        ],
        "apply_link": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/millennia-credit-card"
    },
    {
        "name": "ICICI Coral",
        "issuer": "ICICI Bank",
        "annual_fee": 500,
        "joining_fee": 500,
        "reward_type": "Reward Points",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 300000,
            "credit_score": 650
        },
        "key_benefits": [
            "Fuel Surcharge Waiver",
            "Welcome Benefits",
            "Zero Foreign Currency Markup",
            "Airport Lounge Access"
        ],
        "apply_link": "https://www.icicibank.com/Personal-Banking/cards/credit-card/coral-credit-card/index.page"
    },
    {
        "name": "Axis Ace",
        "issuer": "Axis Bank",
        "annual_fee": 499,
        "joining_fee": 499,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 300000,
            "credit_score": 650
        },
        "key_benefits": [
            "Google Pay Cashback",
            "Fuel Surcharge Waiver",
            "Welcome Benefits",
            "Zero Foreign Currency Markup"
        ],
        "apply_link": "https://www.axisbank.com/retail/cards/credit-card/ace-credit-card/features-benefits"
    },
    {
        "name": "SBI Elite",
        "issuer": "State Bank of India",
        "annual_fee": 4999,
        "joining_fee": 4999,
        "reward_type": "Reward Points",
        "reward_rate": 3.0,
        "eligibility_criteria": {
            "minimum_income": 1200000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Golf Program"
        ],
        "apply_link": "https://www.sbicard.com/en/personal/credit-cards/travel/elite.page"
    },
    {
        "name": "HDFC Diners Club Black",
        "issuer": "HDFC Bank",
        "annual_fee": 10000,
        "joining_fee": 10000,
        "reward_type": "Reward Points",
        "reward_rate": 4.0,
        "eligibility_criteria": {
            "minimum_income": 1500000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Golf Program",
            "Priority Pass"
        ],
        "apply_link": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-club-black-credit-card"
    },
    {
        "name": "ICICI Sapphiro",
        "issuer": "ICICI Bank",
        "annual_fee": 3500,
        "joining_fee": 3500,
        "reward_type": "Reward Points",
        "reward_rate": 3.0,
        "eligibility_criteria": {
            "minimum_income": 900000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Golf Program"
        ],
        "apply_link": "https://www.icicibank.com/Personal-Banking/cards/credit-card/sapphiro-credit-card/index.page"
    },
    {
        "name": "Axis Vistara",
        "issuer": "Axis Bank",
        "annual_fee": 3000,
        "joining_fee": 3000,
        "reward_type": "Club Vistara Points",
        "reward_rate": 4.0,
        "eligibility_criteria": {
            "minimum_income": 900000,
            "credit_score": 750
        },
        "key_benefits": [
            "Club Vistara Points",
            "Airport Lounge Access",
            "Travel Insurance",
            "Priority Check-in"
        ],
        "apply_link": "https://www.axisbank.com/retail/cards/credit-card/vistara-credit-card/features-benefits"
    },
    {
        "name": "Citi Prestige",
        "issuer": "Citibank",
        "annual_fee": 15000,
        "joining_fee": 15000,
        "reward_type": "Reward Points",
        "reward_rate": 4.0,
        "eligibility_criteria": {
            "minimum_income": 1500000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Golf Program",
            "Priority Pass"
        ],
        "apply_link": "https://www.citibank.co.in/credit-card/prestige-credit-card"
    },
    {
        "name": "HDFC Freedom",
        "issuer": "HDFC Bank",
        "annual_fee": 500,
        "joining_fee": 500,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 300000,
            "credit_score": 650
        },
        "key_benefits": [
            "Online Shopping Cashback",
            "Fuel Surcharge Waiver",
            "Welcome Benefits",
            "Zero Foreign Currency Markup"
        ],
        "apply_link": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/freedom-credit-card"
    },
    {
        "name": "SBI Prime",
        "issuer": "State Bank of India",
        "annual_fee": 2999,
        "joining_fee": 2999,
        "reward_type": "Reward Points",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 900000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Welcome Benefits"
        ],
        "apply_link": "https://www.sbicard.com/en/personal/credit-cards/rewards/prime.page"
    },
    {
        "name": "ICICI Rubyx",
        "issuer": "ICICI Bank",
        "annual_fee": 3000,
        "joining_fee": 3000,
        "reward_type": "Reward Points",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 900000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Welcome Benefits"
        ],
        "apply_link": "https://www.icicibank.com/Personal-Banking/cards/credit-card/rubyx-credit-card/index.page"
    },
    {
        "name": "Axis Flipkart",
        "issuer": "Axis Bank",
        "annual_fee": 499,
        "joining_fee": 499,
        "reward_type": "Cashback",
        "reward_rate": 2.0,
        "eligibility_criteria": {
            "minimum_income": 300000,
            "credit_score": 650
        },
        "key_benefits": [
            "Flipkart Cashback",
            "Fuel Surcharge Waiver",
            "Welcome Benefits",
            "Zero Foreign Currency Markup"
        ],
        "apply_link": "https://www.axisbank.com/retail/cards/credit-card/flipkart-credit-card/features-benefits"
    },
    {
        "name": "HDFC Business Regalia",
        "issuer": "HDFC Bank",
        "annual_fee": 5000,
        "joining_fee": 5000,
        "reward_type": "Reward Points",
        "reward_rate": 3.0,
        "eligibility_criteria": {
            "minimum_income": 1500000,
            "credit_score": 750
        },
        "key_benefits": [
            "Airport Lounge Access",
            "Travel Insurance",
            "Concierge Service",
            "Business Expense Management"
        ],
        "apply_link": "https://www.hdfcbank.com/personal/pay/cards/credit-cards/business-regalia-credit-card"
    },
    {
        "name": "SBI BPCL Octane",
        "issuer": "State Bank of India",
        "annual_fee": 1499,
        "joining_fee": 1499,
        "reward_type": "Fuel Points",
        "reward_rate": 3.0,
        "eligibility_criteria": {
            "minimum_income": 600000,
            "credit_score": 700
        },
        "key_benefits": [
            "Fuel Surcharge Waiver",
            "BPCL Fuel Points",
            "Welcome Benefits",
            "Zero Foreign Currency Markup"
        ],
        "apply_link": "https://www.sbicard.com/en/personal/credit-cards/fuel/bpcl-octane.page"
    }
]

def init_db():
    try:
        logger.info("Initializing database...")
        Base.metadata.create_all(bind=engine)
        db = SessionLocal()
        
        # Check if we already have cards
        existing_cards = db.query(CreditCard).count()
        if existing_cards == 0:
            logger.info("Adding sample credit cards to database...")
            for card_data in SAMPLE_CARDS:
                card = CreditCard(**card_data)
                db.add(card)
            db.commit()
            logger.info(f"Added {len(SAMPLE_CARDS)} sample cards to database")
        else:
            logger.info(f"Database already contains {existing_cards} cards")
            
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        if db:
            db.rollback()
        raise
    finally:
        if db:
            db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        raise
    finally:
        db.close() 