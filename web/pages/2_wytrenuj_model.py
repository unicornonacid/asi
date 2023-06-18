import streamlit as st
import time
import numpy as np
import subprocess



def train_model(option):
    
    if option is None or option=="":
        p = subprocess.Popen(["cd ../kedro;kedro run --tags=split,train,evaluate "], stdout=subprocess.PIPE,shell=True)
    else:
        p = subprocess.Popen(["cd ../kedro;kedro run --tags=split,train,evaluate --load-version=clean_data:"+option], stdout=subprocess.PIPE,shell=True)
    

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    perc=0
    while p.poll() is None:
        st.write("```"+str(p.stdout.readline(),"utf-8").strip()+"```")
        status_text.text("%i%% Complete" % perc)
        progress_bar.progress(perc)
        perc+=1
        time.sleep(0.05)
    progress_bar.progress(100)
    status_text.text("%i%% Complete" % 100)

    for x in p.stdout.readlines():
        st.write("```"+str(x,"utf-8").strip()+"```")

    p = subprocess.Popen(["ls -trh ../kedro/data/06_models/regressor.pickle  | tail -n 1"], stdout=subprocess.PIPE,shell=True)
    
    while p.poll() is None:
        time.sleep(0.05)

    return "## Model wytrenowany. Jego identyfikator to:\n"+str(p.stdout.readline(),"utf-8").strip()

st.set_page_config(page_title="Trenowanie modelu")


p = subprocess.Popen(["ls -trh ../kedro/data/05_model_input/clean.csv"], stdout=subprocess.PIPE,shell=True)

while p.poll() is None:
    time.sleep(0.05)

lines=p.stdout.readlines()
lines=map(lambda x: str(x,"utf-8").strip(),lines)

option = st.sidebar.selectbox(label="wybierz dane",options=lines)

if st.sidebar.button("trenuj model"):
    st.write(train_model(option))
