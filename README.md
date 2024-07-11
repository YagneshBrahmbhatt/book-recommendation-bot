# Book Recommendation Bot
# Live Video demonstration link: https://youtu.be/kRnjx-1Aibk
Book Recommendation Bot

Welcome to the Book Recommendation Bot! This application provides personalized book recommendations based on your reading preferences or favorite genres. It features a Streamlit frontend and a FastAPI backend.

## Features

- **Personalized Recommendations**: Enter your reading preferences and receive customized book suggestions.
- **Interactive UI**: User-friendly interface built with Streamlit.
- **Advanced NLP**: Utilizes OpenAI's language model and HuggingFace embeddings for high-quality recommendations.
- **Scalable Backend**: Powered by FastAPI and ChromaDB for efficient data processing and retrieval.

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Install Dependencies
``
pip install -r requirements.txt
``

### Set Up Environment Variables
Create a .env file in the project root and add your OpenAI API key:
``
OPENAI_API_KEY=your_openai_api_key
``

### Run the FastAPI Backend

``
uvicorn main:app --reload
``
### Run the Streamlit Frontend
``
streamlit run app.py
``
### Usage

    Open your browser and navigate to http://localhost:8501 to access the Streamlit interface.
    Enter your reading preferences or favorite genres in the text input field.
    Click the "Find Books!" button to receive personalized book recommendations.

## Project Structure
```
book-recommendation-bot/
├── app.py                # Streamlit frontend
├── main.py               # FastAPI backend
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

### Clone the Repository

```
git clone https://github.com/Yagneshbrahmbhatt/book-recommendation-bot.git
cd book-recommendation-bot
```


