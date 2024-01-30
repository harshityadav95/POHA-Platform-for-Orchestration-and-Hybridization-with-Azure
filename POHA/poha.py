import streamlit as st
import os

## other dependencies
#from vis_helpers import sidebar, authors, visualisation, main_page
#from vis_helpers import pca, rsd, enhancement_factor

from ui_helpers import sidebar, author, vm, main_page, policy, resource_group


def main():
    sidebar.sidebar_head()

    analysis_type = st.sidebar.selectbox("Select Action", ['Main Page', 'Policy', 'Virtual Machine', 'Resource Group', 'RSD'])

    if analysis_type == 'Main Page':
        main_page.main_page()
    if analysis_type == 'Policy':
        policy.main()
    elif analysis_type == 'Virtual Machine':
        vm.main()
    elif analysis_type == 'Resource Group':
        resource_group.main()

    author.show_developers()

if __name__ == '__main__':
    main()

    print("Streamlit Load Complete")
