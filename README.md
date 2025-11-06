# Getty Provenance Chatbot

This project is a Streamlit-based chatbot that uses GPT-4 to convert natural language queries into SPARQL and fetch data from the Getty Provenance Index.

## Setup Instructions

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Add your OpenAI API key to a `.env` file
4. Run the app using `bash start.sh`

## Project Structure

- `backend/`: FastAPI server and query logic
- `frontend/`: Streamlit UI
- `tests/`: Pytest test suite
- `.env`: Environment variables
- `start.sh`: Startup script
