import streamlit as st
import pickle
import os.path


filename = os.path.abspath(os.path.dirname(__file__)) + "/../../kedro/data/07_models/sklearn_model"
model = pickle.load(open(filename, 'rb'))
fruits = """Apple
Aronia
Banana
Bearberry
Blackberry
Blackcurrant
Blueberry
Cantaloupe
Citron
Clementine
Coconut
Guava
Lime
Lychee
Mango
Orange
Peach
Plum
Quince
Raspberry
Redcurrant
Sambucus
Strawberries""".splitlines()
fruits = [fruit.strip() for fruit in fruits]

def main():
    st.set_page_config(page_title="Juice conversion app")
    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    parameters = []

    with overview:
        st.title("Juice conversion app")

    with left:
        sex_d = {0: "Kobieta", 1: "Mężczyzna"}
        sex_radio = st.radio("Płeć", list(sex_d.keys()), format_func=lambda x: sex_d[x])
        age_slider = st.slider("Wiek", value=18, min_value=18, max_value=100)

        parameters.append(sex_radio)
        parameters.append(age_slider)

    with right:
        for fruit in fruits:
            parameters.append(st.slider(fruit, value=0, min_value=0, max_value=300))

    data = [parameters]
    survival = model.predict(data)
    s_confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Czy klient kupi sok?")
        st.subheader(("Tak" if survival[0] == 1 else "Nie"))
        st.write("Dokładność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))


if __name__ == "__main__":
    main()
