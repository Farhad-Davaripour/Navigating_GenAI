[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://navigating-genai.streamlit.app/)

# GPT Response Generator Demo

This repository demonstrates how large language models (LLMs) like GPT-4o predict the next token by manipulating the `temperature` and `top_p` parameters. This demo is designed for teaching students about LLM behavior and token prediction.



## Features

- Generate responses using OpenAI's GPT-4o model.
- Adjust `temperature` and `top_p` parameters to see their impact on token prediction.
- Visualize log probabilities of predicted tokens.

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

## Running the App Locally

Run the Streamlit app:
```bash
streamlit run app.py
```

Open your browser and go to [http://localhost:8501](http://localhost:8501) to access the dashboard.

## How It Works
1. Adjust the parameters (max_tokens, temperature, top_p, top_logprobs, n) using the sidebar sliders.
2. Enter a prompt and generate responses.
3. View the generated responses and visualize the log probabilities of predicted tokens.

## Code Overview
- **app.py**: The main Streamlit app for generating and displaying responses.
- **core.py**: Contains core functions for message creation, response generation, data extraction, and plotting.

## License
This project is licensed under the MIT License.
