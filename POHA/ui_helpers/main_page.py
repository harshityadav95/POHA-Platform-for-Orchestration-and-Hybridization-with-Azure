import streamlit as st
from ui_helpers import ui_utils


def main_page():
    poha_logo = ui_utils.show_poha_logo(width=65, padding=[0, 6, 20, 25], margin=[0, 0, 30, 0])
    st.markdown(poha_logo, unsafe_allow_html=True)

    cols = st.columns((1, 6, 1))
    with cols[1]:
        st.subheader("A Platform for Orchestration & Hybridization with Azure")

    cols = st.columns((3, 3, 1))
    with cols[1]:
        # st.subheader("By")
        # st.markdown("Tier 0 Team")
        st.markdown("")
        st.markdown("")
        st.markdown("")

