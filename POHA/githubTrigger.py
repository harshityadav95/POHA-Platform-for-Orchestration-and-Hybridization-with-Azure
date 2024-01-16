import streamlit as st
import requests
import json

# Streamlit widgets to accept inputs
st.title('GitHub API Request App')
token = st.text_input('Enter your token')
owner = st.text_input('Enter the owner')
repo = st.text_input('Enter the repo')
workflow_id = st.text_input('Enter the workflow ID')
ref = st.text_input('Enter the ref')


if st.button('Make Request'):
    # Use the inputs in the API request
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
    data = {
        "ref": ref

    }

    # Make the request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Display the response
    if response.status_code == 204:
        st.write("Success Run")
    else:
        st.write(f"Request failed with status code {response.status_code}")