# GPT Next Token Generator, RAG, and Function Calling Demos

This repository includes four demos as follows:

1. `Next Token Generator`: This demo illustrates how large language models (LLMs) like GPT-4o predict the next token by adjusting the `temperature` and `top_p` parameters. The next token prediction demo is deployed using Streamlit and can be accessed from the link below:   
 [![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://navigating-genai.streamlit.app/)

2. `Prompt Engineering`: In this demo, the students learn how to use prompt engineering techniques to guid the model in retrieving desired output:   
<a href="https://colab.research.google.com/github/Farhad-Davaripour/Navigating_GenAI/blob/main/prompt_engineering/prompt_engineering_demo.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
</a>

3. `Retrieval Augmented Generation (RAG)`: This example shows how to run a basic RAG pipeline from scratch. Open the demo in Google Colab from the link below:   
<a href="https://colab.research.google.com/github/Farhad-Davaripour/Navigating_GenAI/blob/main/rag/basic_rag_demo.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
</a>

4. `Function Calling`: This demo provides an example of a basic function calling, which could be accessed in the Google Colab from the link below:   
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
