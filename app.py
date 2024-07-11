from flask import Flask, request, jsonify, render_template
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_milvus import Milvus
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
print(f"OpenAI API Key: {openai_api_key}")  # For verification
if not openai_api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

# Initialize the components
embedding = OpenAIEmbeddings(api_key=openai_api_key)
vectorstore = Milvus(embedding_function=embedding, collection_name="books_index")
llm = OpenAI(api_key=openai_api_key, temperature=0.9)
template = "You are a helpful assistant that recommends books based on user preferences.\nUser: {user_input}\nAssistant:"

prompt = PromptTemplate.from_template(template)
chain = LLMChain(prompt=prompt, llm=llm, vectorstore=vectorstore)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json.get('user_input')
    if not user_input:
        return jsonify({'error': 'Invalid input'}), 400

    response = chain.run(user_input)
    return jsonify({'recommendation': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
