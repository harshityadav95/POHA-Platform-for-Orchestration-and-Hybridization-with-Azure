
import streamlit as st

authors_css = """
        style='
        display: block;
        margin-bottom: 0px;
        margin-top: 0px;
        padding-top: 0px;
        font-weight: 400;
        font-size:1.1em;
        color:#DBBD8A;
        filter: brightness(85%);
        text-align: center;
        text-decoration: none;
        '
"""

def made_by():

    st.sidebar.header(f"\n\n\n")
    st.sidebar.markdown(f"\n\n\n")

    st.sidebar.markdown(
        '<p ' + authors_css + '>' + 'By:</p>',
        unsafe_allow_html=True)
    st.sidebar.markdown(f"\n\n\n")

def made_by_harshit():

    st.sidebar.markdown(
        '<a ' + authors_css + ' target="_blank" href="https://harshityadav.in/about/">' + 'Harshit Yadav</a>',
        unsafe_allow_html=True,
        )

def contact_developers():
    st.markdown(
        "<a " + authors_css + ' href="mailto:harshityadav[at]outlook.com" target=_blank>' + "Harshit Yadav</a>",
        unsafe_allow_html=True,
        )


def show_developers():
    """
    Shows all the links and mails to developers
    :return:
    """
    contact_developers()
    made_by()
    made_by_harshit()


