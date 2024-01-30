import streamlit as st
from ui_helpers import ui_utils


def sidebar_head():

    st.set_page_config(
        page_title="POHA ",
        page_icon="images/poha_icon.png",
        layout="wide",
        initial_sidebar_state="auto"
    )

    #st.set_option('deprecation.showfileUploaderEncoding', False)

    # POHA logo
    html_code = ui_utils.show_poha_logo(100, [1, 1, 1, 1], margin=[0, 0, 0, 0])
    st.sidebar.markdown(html_code, unsafe_allow_html=True)
    st.sidebar.markdown('')
    st.sidebar.markdown('')

def print_widget_labels(widget_title, margin_top=5, margin_bottom=10):
    """
    Prints Widget label on the sidebar and lets adjust its margins easily
    :param widget_title: Str
    """
    st.sidebar.markdown(
        f"""<p style="font-weight:500; margin-top:{margin_top}px;margin-bottom:{margin_bottom}px">{widget_title}</p>""",
        unsafe_allow_html=True)

