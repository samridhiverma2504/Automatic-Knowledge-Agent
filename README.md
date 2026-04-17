# Query Classification with Gemini

This project uses the Gemini API to classify research paper search queries into one of three categories:
- **Navigational**: searching for a specific known paper  
- **Semantic**: searching for papers about a topic or concept  
- **Metadata**: searching using attributes such as author, year, venue, or citation count  

The script evaluates Gemini’s performance on a labeled test set and reports overall classification accuracy.

## Features

- Uses the Gemini API through the `google-genai` Python SDK
- Loads the API key securely from a `.env` file
- Shuffles test queries before evaluation
- Prints the model’s prediction alongside the expected label
- Computes final accuracy over the full test set
- Supports prompt variants with or without examples
