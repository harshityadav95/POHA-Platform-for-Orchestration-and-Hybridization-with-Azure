import datetime
import os
import requests
import json
import streamlit as st
import pandas as pd
import time

import env_local

env_local.loadEnvironmentVariables()
token = os.environ.get("SECRET_GITHUB_TOKEN")
owner = os.environ.get("REPO_OWNER")
repo = os.environ.get("REPOSITORY_NAME")
ref = os.environ.get("BRANCH_NAME")

workflow_id = "create-json-artifacts.yml"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28"
}

url = "https://api.github.com/repos/" + str(owner) + "/" + str(repo) + "/actions/workflows/" + str(
    workflow_id) + "/runs?actor=" + str(owner)

print(url)


def list_single_repository_workflow_run():
    payload = {}
    print(url)
    count = 0
    response = ""
    with st.status("Checking workflow runs...", expanded=True) as status:
        st.write("Searching for data...")
        response = requests.request("GET", url, headers=headers, data=payload)
        st.write(response.json())
        if response.ok:
            count += 1


        else:

            status.update(label="No Data Found!", state="error", expanded=True)

        st.write("Found URL.")
        count+=1

        st.write("Downloading data...")
        count+=1
        status.update(label="Complete!", state="complete", expanded=False)

    st.button('Rerun')



    if count >= 1:
        workflows = response.json()["workflow_runs"]
        filtered_workflows = [
            {

                "name": workflow["name"],
                "id": workflow["id"],
                "status": workflow["status"],
                "conclusion": workflow["conclusion"],
                "workflow_url": workflow["workflow_url"]
            }
            for workflow in workflows
        ]
        # Create the DataFrame
        df = pd.DataFrame(filtered_workflows)

        # Display the DataFrame in Streamlit
        st.title("All Workflow Runs")


        cols = st.columns(1)

        with cols[0]:
            st.data_editor(
                df,
                column_config={
                    "workflow_url": st.column_config.LinkColumn(
                        "Logs",
                        display_text="Workflow Logs",
                    ),

                },
                hide_index=False,
                use_container_width=True
            )

    if count >= 2:
        workflows = response.json()["workflow_runs"]
        filtered_workflows = [
            {

                "name": workflow["name"],
                "id": workflow["id"],
                "status": workflow["status"],
                "conclusion": workflow["conclusion"],
                "workflow_url": workflow["workflow_url"]
            }
            for workflow in workflows
        ]
        # Create the DataFrame
        df = pd.DataFrame(filtered_workflows)

        # Display the DataFrame in Streamlit
        st.title("All Workflow Runs")


        cols = st.columns(1)

        with cols[0]:
            st.data_editor(
                df.head(1),
                column_config={
                    "workflow_url": st.column_config.LinkColumn(
                        "Logs",
                        display_text="Workflow Logs",
                    ),

                },
                hide_index=False,
                use_container_width=True
            )

    if count >= 3:
        workflows = response.json()["workflow_runs"]
        filtered_workflows = [
            {

                "name": workflow["name"],
                "id": workflow["id"],
                "status": workflow["status"],
                "conclusion": workflow["conclusion"],
                "workflow_url": workflow["workflow_url"]
            }
            for workflow in workflows
        ]
        # Create the DataFrame
        df = pd.DataFrame(filtered_workflows)

        # Display the DataFrame in Streamlit
        st.title("All Workflow Runs")


        cols = st.columns(1)

        with cols[0]:
            st.data_editor(
                df.head(1),
                column_config={
                    "workflow_url": st.column_config.LinkColumn(
                        "Logs",
                        display_text="Workflow Logs",
                    ),

                },
                hide_index=False,
                use_container_width=True
            )

    # # Display the response
    # if response.status_code == 200:
    #     st.write("Success Run")
    # else:
    #     st.write(f"Request failed with status code {response.status_code}")

    return "hello"
