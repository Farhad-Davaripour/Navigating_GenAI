import streamlit as st
from core.core import create_message_text, generate_response, process_and_plot

# Define sliders in the sidebar
max_tokens = st.sidebar.slider("Max Tokens", min_value=1, max_value=100, value=1, step=1)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
top_p = st.sidebar.slider("Top P", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
top_logprobs = st.sidebar.slider("Top Logprobs", min_value=1, max_value=10, value=5, step=1)
n = st.sidebar.slider("Number of Completions (n)", min_value=1, max_value=10, value=5, step=1)


# Create a function for generating and displaying responses
def generate_and_display_responses(prompt):
    message = create_message_text(prompt)
    response = generate_response(message, max_tokens, temperature, top_p, top_logprobs, n)

    # Print all completions
    st.subheader("Generated Responses")
    for idx, choice in enumerate(response.choices):
        st.write(f"Completion {idx + 1}: {choice.message.content}")

    # Process and plot
    st.subheader("Response Plot")
    fig = process_and_plot(response)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)

# Streamlit app layout
st.title("GPT Response Generator")

st.info(
    """
    This dashboard generates responses using a transformer neural network based on the provided prompt.
    """
)

# User input for the prompt
prompt = st.text_input("Enter your prompt:", "where do I live? respond with only one word. Example: California.")

if st.button("Generate Response"):
    generate_and_display_responses(prompt)