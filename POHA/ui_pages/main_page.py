import streamlit as st
from ui_pages import ui_utils



def main_page():
    poha_logo = ui_utils.show_poha_logo(width=65, padding=[0, 6, 20, 25], margin=[0, 0, 30, 0])
    st.markdown(poha_logo, unsafe_allow_html=True)

    # cols = st.columns((1, 6, 1))
    # with cols[1]:
    #     st.subheader("A Platform for Orchestration & Hybridization with Azure")

    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.title("FAQ")

    st.markdown("#### General")
    with st.expander("What is POHA?", expanded=False):
        st.markdown(
            "POHA is a developer friendly portal that is designed to supercharge the productivity of the platform enginners working on Azure by utilizing prebuilt Recipies for orchestrating things on azure")

    with st.expander("Why use POHA instead of Local Scripts"):
        st.markdown(
            "GPT Lab aims to be the \"GitLab\" for your favorite prompts, allowing you to save and reuse your favorite prompts as AI Assistants. This eliminates the need to retype the same prompt every time you want to use it. Additionally, you can share your AI Assistants with others without revealing your exact prompt. Since you're using your own Github API key, you don't have to worry about Chat GPT being at capacity.")

    with st.expander("What is an Github API Key and why do I need one?"):
        st.markdown(
            "An Github API key is a unique credential that allows you to interact with OpeAI's GPT models. It also serves as your identifier in GPT Lab, allowing us to remember the AI Assistants you have created.")

    with st.expander("How can I get an Github API Key?"):
        st.markdown(
            "You can obtain an Github API Key by creating one on the Github website: https://platform.Github.com/account/api-keys")

    with st.expander("Why do I need to enter my Github API key each time I use the app?"):
        st.markdown(
            "For security reasons, your actual Github Key is not stored on our servers. Our application only uses it during the duration of your sessions to interact with Github. To keep track of your information, we use a secure one-way hashing algorithm to store a hashed version of your Github API Key, which becomes your unique identifier in our backend data store. This helps ensure the confidentiality and security of your information.")

    with st.expander("MYTH: A developer portal and an internal developer platform are the same thing"):
        st.markdown(
            "Currently, GPT Lab itself is free to use. However, you will incur costs for interacting with the Github GPT models, as each API call to the model will be charged. The cost per call is relatively low, and under normal usage, the cost should be minimal. You have full control over the usage and cost of the model, as you are using your own API key. You can monitor your usage and costs through the Github dashboard and adjust your usage accordingly to stay within your budget. The backend infrastructure costs are currently covered by us, and any donation through the \"Buy Me a Coffee\" link is greatly appreciated!")

    with st.expander(
            "2. MYTH: We don't need an internal developer platform"):
        st.markdown(
            "This error typically indicates you have hit your maximum monthly spend (hard limit) for the API. However, you will likely see this error if you have a free trial API key. For optimal chatting experience, we recommend upgrading to a pay-as-you-go API key by entering your billing information [here](https://platform.Github.com/account/billing/overview). You can learn more about Github API rate limits [here](https://platform.Github.com/docs/guides/rate-limits/overview).")

    st.markdown("#### AI Assistant Design")

    with st.expander("3. MYTH: Platform engineering is “just advanced DevOps""):
        st.markdown("You can create your AI Assistant in the Lab.")

    with st.expander("4. MYTH: Platform engineering is just automation"):
        st.markdown(
            "The initial prompt is the most crucial part of the AI Assistant design, as it sets the context for the conversation and guides the AI's responses. It is the hidden set of instructions for the AI. The initial prompt should clearly convey the topic or task that you would like the AI to focus on during the conversation.")

    with st.expander("5. MYTH: Platform engineering is just the latest fad"):
        st.markdown("""
        Yes, here are few tips to creating effective prompts:  \n
        * Familiarize yourself with the best practices for prompt engineering, as outlined in this Github article: https://help.Github.com/en/articles/6654000-best-practices-for-prompt-engineering-with-Github-api  \n
        * When creating a prompt for a GPT Lab AI Assistant, make sure to include instructions for the Assistant to introduce itself to the user first. This helps ensure a smooth and engaging chat session.  
        * Test out your prompt in the Lab to ensure it accurately conveys the desired topic or task.   
        """)

    st.markdown("#### Privacy, Platform Guidelines, and Intellectual Property")

    with st.expander("How does GPT Lab ensure the security of my information?"):
        st.markdown("""We use the SHA-256 PBKDF2 algorithm, a highly secure one-way hashing algorithm, to hash your Github API Key and store it securely. This ensures that your key is protected and cannot be used for any unauthorized purposes. 

    Additionally, we use a symmetric AES-128 encryption algorithm, with a unique key for each user, to encrypt your chat transcripts with the AI Assistants.""")

    with st.expander("Are there any restrictions on the type of AI Assistants that can be created in GPT Lab?"):
        st.markdown("""
        Our Terms of Use have outlined some common sense restrictions you should follow. Please review our Terms of Use, available on the Terms page, for more information. 
        Additionally, since our AI Assistants use the Github language models, you should also comply with the [Github Usage policies](https://platform.Github.com/docs/usage-policies).  \n
        We recommend avoiding creating AI Assistants for use in heavily regulated fields, as the legal and ethical implications of such applications can be complex and far-reaching.  \n
        Please note that GPT Lab does not assume any liability for the use of the AI Assistants you create using the platform. It is your responsibility to ensure that your AI Assistant complies with all applicable laws and regulations, and to use the platform at your own risk.
        """)

    cols = st.columns((3, 3, 1))
    with cols[1]:
        # st.subheader("By")
        # st.markdown("Tier 0 Team")
        st.markdown("")
        st.markdown("")
        st.markdown("")

    st.markdown("""
    #### Reference :
    - [5 myths about platform engineering: what it is and what it isn’t](https://cloud.google.com/blog/products/application-development/common-myths-about-platform-engineering)
    """)



