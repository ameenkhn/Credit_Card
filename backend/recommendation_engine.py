import openai
from typing import List, Dict, Optional
from database import SessionLocal, CreditCard
import os
from dotenv import load_dotenv
from contextlib import contextmanager
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

class RecommendationEngine:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("OPENAI_API_KEY environment variable is not set")
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        try:
            # Set the API key directly
            openai.api_key = api_key
            logger.info("Successfully initialized OpenAI client")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise

    @contextmanager
    def get_db_session(self):
        db = SessionLocal()
        try:
            yield db
        except Exception as e:
            logger.error(f"Database session error: {e}")
            raise
        finally:
            db.close()

    def get_all_cards(self) -> List[Dict]:
        try:
            with self.get_db_session() as db:
                cards = db.query(CreditCard).all()
                logger.info(f"Retrieved {len(cards)} cards from database")
                return [
                    {
                        "name": card.name,
                        "issuer": card.issuer,
                        "annual_fee": card.annual_fee,
                        "reward_type": card.reward_type,
                        "reward_rate": card.reward_rate,
                        "key_benefits": card.key_benefits,
                        "eligibility_criteria": card.eligibility_criteria,
                        "apply_link": card.apply_link
                    }
                    for card in cards
                ]
        except Exception as e:
            logger.error(f"Error getting all cards: {e}")
            return []

    def analyze_preferences(self, preferences: Dict) -> str:
        try:
            prompt = f"""
            Analyze the following user preferences for credit card recommendations:
            
            Monthly Income: ₹{preferences.get('monthly_income', 0)}
            Spending Habits: {preferences.get('spending_habits', {})}
            Preferred Benefits: {preferences.get('preferred_benefits', [])}
            Existing Cards: {preferences.get('existing_cards', 'None')}
            Credit Score: {preferences.get('credit_score', 'Unknown')}
            
            Based on these preferences, what type of credit card would be most suitable?
            Consider:
            1. Income eligibility
            2. Spending patterns
            3. Desired benefits
            4. Credit score requirements
            
            Provide a brief analysis in 2-3 sentences.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            analysis = response.choices[0].message.content
            logger.info("Successfully generated preference analysis")
            return analysis
        except Exception as e:
            logger.error(f"Error in analyze_preferences: {e}")
            return "Unable to analyze preferences at this time."

    def get_recommendations(self, preferences: Dict) -> List[Dict]:
        try:
            # Validate preferences
            if not preferences.get('monthly_income'):
                raise ValueError("Monthly income is required")
            if not preferences.get('spending_habits'):
                raise ValueError("Spending habits are required")
            if not preferences.get('preferred_benefits'):
                raise ValueError("Preferred benefits are required")

            # Get all cards
            all_cards = self.get_all_cards()
            if not all_cards:
                logger.warning("No credit cards found in database")
                return []
            
            # Get AI analysis
            analysis = self.analyze_preferences(preferences)
            logger.info("Generated AI analysis of preferences")
            
            # Filter cards based on basic criteria
            eligible_cards = []
            for card in all_cards:
                try:
                    if self._is_eligible(card, preferences):
                        # Calculate estimated rewards
                        estimated_rewards = self._calculate_rewards(card, preferences)
                        card['estimated_rewards'] = estimated_rewards
                        card['recommendation_reason'] = self._generate_recommendation_reason(card, preferences)
                        eligible_cards.append(card)
                        logger.info(f"Added {card['name']} to eligible cards")
                except Exception as e:
                    logger.error(f"Error processing card {card.get('name', 'Unknown')}: {e}")
                    continue
            
            # Sort by estimated rewards
            eligible_cards.sort(key=lambda x: x.get('estimated_rewards', 0), reverse=True)
            logger.info(f"Found {len(eligible_cards)} eligible cards")
            
            # Return top 3 cards
            return eligible_cards[:3]
        except Exception as e:
            logger.error(f"Error in get_recommendations: {e}")
            raise

    def _is_eligible(self, card: Dict, preferences: Dict) -> bool:
        try:
            # Basic eligibility check
            min_income = card.get('eligibility_criteria', {}).get('minimum_income', float('inf'))
            if preferences.get('monthly_income', 0) * 12 < min_income:
                logger.debug(f"Card {card['name']} rejected due to income requirement")
                return False
                
            if preferences.get('credit_score'):
                min_score = card.get('eligibility_criteria', {}).get('credit_score', 0)
                if preferences['credit_score'] < min_score:
                    logger.debug(f"Card {card['name']} rejected due to credit score requirement")
                    return False
                    
            return True
        except Exception as e:
            logger.error(f"Error in _is_eligible: {e}")
            return False

    def _calculate_rewards(self, card: Dict, preferences: Dict) -> float:
        try:
            # Simple reward calculation based on spending habits
            spending_habits = preferences.get('spending_habits', {})
            if not spending_habits:
                return 0.0
                
            total_spending = sum(spending_habits.values())
            annual_spending = total_spending * 12
            reward_rate = card.get('reward_rate', 0)
            estimated_rewards = (annual_spending * reward_rate) / 100
            logger.debug(f"Calculated estimated rewards for {card['name']}: ₹{estimated_rewards}")
            return estimated_rewards
        except Exception as e:
            logger.error(f"Error in _calculate_rewards: {e}")
            return 0.0

    def _generate_recommendation_reason(self, card: Dict, preferences: Dict) -> str:
        try:
            prompt = f"""
            Generate a brief recommendation reason for this credit card based on user preferences:
            
            Card: {card.get('name', 'Unknown')}
            User Preferences:
            - Monthly Income: ₹{preferences.get('monthly_income', 0)}
            - Spending Habits: {preferences.get('spending_habits', {})}
            - Preferred Benefits: {preferences.get('preferred_benefits', [])}
            
            Keep it concise and highlight the most relevant benefits for this user.
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            reason = response.choices[0].message.content
            logger.debug(f"Generated recommendation reason for {card['name']}")
            return reason
        except Exception as e:
            logger.error(f"Error in _generate_recommendation_reason: {e}")
            return "Unable to generate recommendation reason at this time." 