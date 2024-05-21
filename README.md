# GPT Next Token Generator, RAG, and Function Calling Demos

This repository demonstrates how large language models (LLMs) like GPT-4o predict the next token by adjusting the `temperature` and `top_p` parameters. The next token prediction demo is deployed using Streamlit and can be accessed from the link below:   
 [![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://navigating-genai.streamlit.app/)

It also shows  how to run a basic Retrieval Augmented Generation (RAG) pipeline from scratch. Open the demo in Google Colab from the link below:   
<a href="https://colab.research.google.com/github/Farhad-Davaripour/Navigating_GenAI/blob/main/rag/basic_rag_demo.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
</a>

Furthermore, a demo of a basic function calling is provided in this repository, which could be accessed in the Google Colab from the link below:   
<a href="https://colab.research.google.com/github/Farhad-Davaripour/Navigating_GenAI/blob/main/function_calling/function_calling_demo.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
</a>

## Features

- Generate responses using OpenAI's GPT-4o model.
- Adjust `temperature` and `top_p` parameters to see their impact on token prediction.
- Visualize log probabilities of predicted tokens.
- Parse and retrieve text chunks from a PDF document to respond to a domain specific query.
- Create a custom agent to avoid hallucination and improve the capabilities of LLMs

## OpenAI API Keys
In order to run the basic_rag_demo the API key to gpt-40 could be created/retrieved form the link below:
[OpenAI API Key](https://platform.openai.com/docs/overview)

`Note`: Once you logged into OpenAI platform, find the API key from the sidebar:

## License
This project is licensed under the MIT License.
