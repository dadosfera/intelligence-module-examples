import streamlit as st

class DataApp():
    def update_visibility():
        hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .element-container{opacity:1 !important}
            </style>
            """
        return st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    def add_logo():
        return st.markdown(
            """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("https://cdn-images-1.medium.com/max/1200/1*OPrCFbKQFOeL0QKCuDeR1g.png");
                    background-repeat: no-repeat;
                    padding-top: 30px;
                    background-position: 50% 20%;
                    background-size: 25%;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
    
    def update_page_config(page_title, favicon_img_link):
        return st.set_page_config(page_title=page_title, page_icon=favicon_img_link, layout="wide")

