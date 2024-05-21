# RAG and GPT Next Token Generator Demo

This repository demonstrates how to run a basic Retrieval Augmented Generation (RAG) pipeline from scratch. Furthermore, it shows how large language models (LLMs) like GPT-4o predict the next token by adjusting the `temperature` and `top_p` parameters. The next token prediction demo is deployed using Streamlit and can be accessed from the link below:

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://navigating-genai.streamlit.app/)

## Features

- Generate responses using OpenAI's GPT-4o model.
- Adjust `temperature` and `top_p` parameters to see their impact on token prediction.
- Visualize log probabilities of predicted tokens.
- Parse and retrieve text chunks from a PDF document to respond to a domain specific query.

## OpenAI API Keys
In order to run the basic_rag_demo the API key to gpt-40 could be created/retrieved form the link below:
[OpenAI API Key](https://platform.openai.com/docs/overview)

`Note`: Once you logged into OpenAI platform, find the API key from the sidebar:

## License
This project is licensed under the MIT License.
