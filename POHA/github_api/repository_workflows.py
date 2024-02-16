import datetime
import os
import requests
import json
import streamlit as st
import pandas as pd
import time

# Recipie Name
workflow_id = "dynamic-run-name.yml"

token = os.environ.get("SECRET_GITHUB_TOKEN")
owner = os.environ.get("REPO_OWNER")
repo = os.environ.get("REPOSITORY_NAME")
ref = os.environ.get("BRANCH_NAME")

owner = "harshityadav95"
workflow_id = "dynamic-run-name.yml"
ref = "main"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28"
}
url = "https://api.github.com/repos/" + str(owner) + "/" + str(repo) + "/actions/workflows"


def list_all_repository_workflows():
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    st.write(response.json())

    workflows = response.json()["workflows"]

    with st.status("Downloading data...", expanded=True) as status:
        st.write("Searching for data...")
        time.sleep(2)
        st.write("Found URL.")
        time.sleep(1)
        st.write("Downloading data...")
        time.sleep(1)
        status.update(label="Download complete!", state="complete", expanded=False)

    st.button('Rerun')

    filtered_workflows = [
        {

            "badge_url": workflow["badge_url"],
            "name": workflow["name"],


            "state": workflow["state"],
            "html_url": workflow["html_url"]
        }
        for workflow in workflows
    ]
    # Create the DataFrame
    df = pd.DataFrame(filtered_workflows)

    def color_state(state):
        if state == "active":
            return "background-color: green"
        else:
            return ""

    # Style the "state" column using the custom function
    df = df.style.map(color_state, subset=["state"])

    # Display the DataFrame in Streamlit
    st.title("GitHub Actions Workflows")
    st.dataframe(df)

    cols=st.columns(1)

    with cols[0]:

        st.data_editor(
            df,
            column_config={
                "html_url": st.column_config.LinkColumn(
                    "Recipie",
                    display_text="Github YML",
                ),
                "badge_url": st.column_config.ImageColumn(label="Status",width="large")



            },
            hide_index=False,
            use_container_width=True
        )

    # Display the response
    if response.status_code == 200:
        st.write("Success Run")
    else:
        st.write(f"Request failed with status code {response.status_code}")

    return "hello"
