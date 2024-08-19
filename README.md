# Langchain Demo with LLaMa 3.1 and GPT-4o

This project demonstrates the use of Langchain to create a simple API server that interacts with both LLaMa 3.1 and GPT-4o models. It includes a Streamlit-based client for easy interaction with the models.

## Features

- FastAPI server that handles requests for both LLaMa 3.1 and GPT-4o models
- Streamlit client for user-friendly interaction
- Asynchronous processing for LLaMa 3.1 to prevent UI blocking
- Server status check functionality

## Prerequisites

- Python 3.7+
- OpenAI API key
- Ollama with LLaMa 3.1 model installed

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/langchain-demo.git
   cd langchain-demo
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Start the server:
   ```
   python app.py
   ```

2. In a new terminal, start the Streamlit client:
   ```
   streamlit run client.py
   ```

3. Open your web browser and navigate to `http://localhost:8501` to interact with the Streamlit app.

## Project Structure

- `app.py`: FastAPI server that handles requests to the language models
- `client.py`: Streamlit client for user interaction
- `requirements.txt`: List of Python dependencies