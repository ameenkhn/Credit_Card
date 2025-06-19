# Credit Card Recommendation System

A web-based, AI-powered credit card recommendation system that helps users find the best credit cards based on their preferences and spending habits.

## Features

- Conversational agent powered by OpenAI GPT
- Dynamic question flow to understand user preferences
- Personalized credit card recommendations
- Mobile-responsive UI
- Real-time reward calculations
- Detailed card comparisons

## Tech Stack

### Backend
- Python 3.8+
- FastAPI
- SQLAlchemy
- OpenAI API
- SQLite (can be upgraded to PostgreSQL)

### Frontend
- React
- TypeScript
- Material-UI
- Axios

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key
```

4. Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Usage

1. Open http://localhost:3000 in your browser
2. Follow the step-by-step questionnaire:
   - Enter your monthly income
   - Specify your spending habits
   - Select preferred benefits
3. View personalized credit card recommendations
4. Compare cards and apply for the best match

## API Documentation

The API documentation is available at http://localhost:8000/docs when the backend server is running.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License 