import streamlit as st

from github_api import repository_workflows, single_workflow


def workflowtracker():
    st.write('## Recipie Excecution Tracker')
    t1, t2 = st.tabs(['All Workflows', 'Cleanup Workflow '])
    with t1:
        github_access_key = st.text_input(
            "Github Access Key1:",
            type="password",
            help="You can find details on how to generate Github Token for Access[Github](https://github.com/).",
        )
        if st.button('Make Request'):
            repository_workflows.list_all_repository_workflows()


    with t2:
        if st.button('Run'):
            single_workflow.list_single_repository_workflow_run()




