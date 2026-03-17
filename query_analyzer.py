from google import genai
from dotenv import load_dotenv
from test_queries import test_queries

import os
import random

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def query_analyze(query):
    response = client.models.generate_content(
        model = "gemini-3.1-flash-lite-preview",
        contents = 
        #without examples
        f"""
        Classify "{query}" into one of the three categories:    
        Navigational: searching for a specific known paper 
        Semantic: searching for papers about a topic or concept 
        Metadata: searching based on author, year, venue, or citation count 
        Respond with a single word from the three: Navigational, Semantic, Metadata
        """
        #with examples
        # f"""
        # Classify "{query}" into one of the three categories: 
        # Navigational: searching for a specific known paper (eg. "the BERT paper", "TensorFlow paper by Abadi et al.")
        # Semantic: searching for papers about a topic or concept (eg. "autograd", "image classification with deep learning")
        # Metadata: searching based on author, year, venue, or citation count (eg. "papers by ACL", "2023 papers about back propagation")
        # Respond with a single word from the three: Navigational, Semantic, Metadata
        # """
    )
    return response.text

# shuffling the queries so that the queries from each category are mixed
user_queries = random.sample(test_queries, len(test_queries))

correct_answers = 0

for query, expected in user_queries:
    result = query_analyze(query)
    print(f"\nQuery: {query}")
    print(f"LLM Response: {result} | Expected: {expected}")

    if(result == expected):
        correct_answers += 1
    
accuracy = (correct_answers/len(user_queries)) * 100
print(f"\nAccuracy: {accuracy} \n")