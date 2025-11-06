# Getty Provenance Chatbot

This project is a Streamlit-based chatbot that uses GPT-4 to convert natural language queries into SPARQL and fetch data from the Getty Provenance Index.

## Setup Instructions

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your OpenAI API key (do not commit `.env`):

```bash
cp .env.example .env
# edit .env and set OPENAI_API_KEY
```

4. Run the app using `bash start.sh`

## Project Structure

- `backend/`: FastAPI server and query logic
- `frontend/`: Streamlit UI
- `tests/`: Pytest test suite
- `.env`: Environment variables
- `start.sh`: Startup script

Testing notes:
- The test suite is configured to mock external network calls to OpenAI and the Getty SPARQL endpoint so tests run without credentials or network access. If you prefer to run integration tests against the real services, update the tests and provide a live `OPENAI_API_KEY` in your `.env`.
