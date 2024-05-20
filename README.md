# RAG and GPT Next Token Generator Demo

This repository demonstrates how to run a basic Retrieval Augmented Generation (RAG) pipeline from scratch. Furthermore, it shows how large language models (LLMs) like GPT-4o predict the next token by adjusting the `temperature` and `top_p` parameters. The next token prediction demo is deployed using Streamlit and can be accessed from the link below:

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://navigating-genai.streamlit.app/)

## Features

- Generate responses using OpenAI's GPT-4o model.
- Adjust `temperature` and `top_p` parameters to see their impact on token prediction.
- Visualize log probabilities of predicted tokens.
- Parse and retrieve text chunks from a PDF document to respond to a domain specific query.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Farhad-Davaripour/Navigating_GenAI.git
   cd Navigating_GenAI
    ```
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
3. Set up your environment variables:
Create a .env file and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

## Running the Streamlit App

Run the Streamlit app:
```bash
streamlit run app.py
```

Open your browser and go to [http://localhost:8501](http://localhost:8501) to access the dashboard.

Alternatively the next token prediction app is accessible via this [link](https://navigating-genai.streamlit.app/)

## License
This project is licensed under the MIT License.
