from langchain_milvus import Milvus
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import csv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
print(f"OpenAI API Key: {openai_api_key}")  # Debugging step to verify API key
if not openai_api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

# Initialize the components
embedding = OpenAIEmbeddings(api_key=openai_api_key)
vectorstore = Milvus(embedding_function=embedding, collection_name="books_index")

# Function to load documents from the CSV file
def load_documents_from_csv(file_path):
    documents = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            content = f"Title: {row['title']}\nAuthor: {row['author']}\nDescription: {row['description']}"
            documents.append({"content": content, "metadata": {"title": row['title'], "author": row['author']}})
    return documents

# Load book data from CSV
books_data = load_documents_from_csv("data/books.csv")

# Index the book data
for doc in books_data:
    vectorstore.add_document(doc)

print("Book data indexed successfully.")
