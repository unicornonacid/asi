import streamlit as st
import pickle
import os.path


def main():
    st.set_page_config(
    page_title="CD app",
    page_icon="👋")

    st.sidebar.success("Wybierz, co chcesz zrobić")

    # add_selectbox = st.sidebar.selectbox(
    # "Co chcesz zrobić?",
    # ("wygeneruj dane",
    #  "wytrenuj model",
    #  "wdróż model na produkcję",
    #  "sprawdź data drift",
    #  )     
    # )
    st.sidebar.markdown(
"""## przydatne linki
- [modelowanie](https://localhost:4040/)
- [promehteus](http://localhost:9090/)
- [MLflow](https://localhost:8080/)
""")

    st.markdown(
        """
        # Aplikacja do zarządzania cyklem życia modelu
        ## co możesz zrobić?
        
    """
    )


if __name__ == "__main__":
    main()
