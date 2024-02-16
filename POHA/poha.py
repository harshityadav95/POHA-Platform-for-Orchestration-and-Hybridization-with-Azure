import streamlit as st
import os

import env_local
## other dependencies
# from vis_helpers import sidebar, authors, visualisation, main_page
# from vis_helpers import pca, rsd, enhancement_factor

from ui_pages import sidebar, author, vm, main_page, policy, resource_group, builddetails, workflowtracker


def main():
    sidebar.sidebar_head()

    module_type = st.sidebar.selectbox("Select Module",
                                       ['Main Page', 'Workflow Tracker', 'Policy', 'Virtual Machine', 'Resource Group',
                                        'RSD', 'Azure Cheat Sheet'])

    if module_type == 'Main Page':
        main_page.main_page()
    elif module_type == 'Workflow Tracker':
        workflowtracker.workflowtracker()
    elif module_type == 'Policy':
        policy.main()
    elif module_type == 'Virtual Machine':
        vm.main()
    elif module_type == 'Resource Group':
        resource_group.main()

    author.show_developers()
    builddetails.builddetailsfooter()


if __name__ == '__main__':
    env_local.loadEnvironmentVariables()
    main()
    print("POHA Load Complete")
