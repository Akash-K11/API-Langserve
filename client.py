import requests
import streamlit as st

def get_gpt4o_response(input_text):
    try:
        response = requests.post(
            "http://127.0.0.1:8080/gpt/invoke",
            json={'input': {'query': input_text}},
            timeout=30
        )
        response.raise_for_status()
        return response.json()['output']['content']
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to GPT-4o API: {str(e)}")
        return None

def get_llama31_response(input_text):
    try:
        response = requests.post(
            "http://127.0.0.1:8080/llama/invoke",
            json={'input': {'query': input_text}},
            timeout=120
        )
        response.raise_for_status()
        return response.json()['output']
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to LLaMa3.1 API: {str(e)}")
        return None

st.title('Langchain Demo With LLaMa 3.1 and GPT-4o API')

input_text = st.text_input("Enter your query")

if input_text:
    st.subheader("GPT-4o Response:")
    gpt4o_response = get_gpt4o_response(input_text)
    if gpt4o_response:
        st.write(gpt4o_response)
    
    st.subheader("LLaMa 3.1 Response:")
    llama31_response = get_llama31_response(input_text)
    if llama31_response:
        st.write(llama31_response)

# section to check server status
if st.button("Enter"):
    try:
        response = requests.get("http://127.0.0.1:8080")
        if response.status_code == 200:
            data = response.json()
            st.success(f"Server is running and accessible! Message: {data.get('message', 'No message provided')}")
        else:
            st.warning(f"Server returned unexpected status code: {response.status_code}")
            st.text(f"Response content: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Unable to connect to the server: {str(e)}")