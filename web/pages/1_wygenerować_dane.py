import streamlit as st
import time
import numpy as np
import subprocess



def generate_data():
    cmd = "type python"
    p = subprocess.Popen(["cd ../kedro;kedro run --tags=generate,clean"], stdout=subprocess.PIPE,shell=True)
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    perc=0
    while p.poll() is None:
        st.write("```"+str(p.stdout.readline(),"utf-8").strip()+"```")
        status_text.text("%i%% Complete" % perc)
        progress_bar.progress(perc)
        perc+=1
        if perc>100:
            perc=99
        time.sleep(0.05)
    progress_bar.progress(100)
    status_text.text("%i%% Complete" % 100)

    for x in p.stdout.readlines():
        st.write("```"+str(x,"utf-8").strip()+"```")

    p = subprocess.Popen(["ls -trh ../kedro/data/05_model_input/clean.csv/  | tail -n 1"], stdout=subprocess.PIPE,shell=True)
    
    while p.poll() is None:
        time.sleep(0.05)

    return "## Plik wygenerowany. Jego identyfikator to:\n"+str(p.stdout.readline(),"utf-8").strip()

st.set_page_config(page_title="Generowanie danych")


if st.sidebar.button("Generuj"):
    st.write(generate_data())
    
