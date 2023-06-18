import streamlit as st
import time
import numpy as np
import subprocess



def data_drift(option):
    
    if option is None or option=="":
        p = subprocess.Popen(["cd ../kedro;kedro run --tags=data_drift_check"], stdout=subprocess.PIPE,shell=True)
    else:
        p = subprocess.Popen(["cd ../kedro;kedro run --tags=data_drift_check --load-version=clean_data:"+option], stdout=subprocess.PIPE,shell=True)
    

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

    p = subprocess.Popen(["cp ../kedro/data_drift_report.html static/data_drift_report.html" ], stdout=subprocess.PIPE,shell=True)

    while p.poll() is None:
        time.sleep(0.05)

    page="".join(open("static/data_drift_report.html").readlines())
    st.components.v1.html(page,width=1000,height=2000)   

    
st.set_page_config(page_title="Sprawdzenie data drift")


p = subprocess.Popen(["ls -trh ../kedro/data/05_model_input/clean.csv"], stdout=subprocess.PIPE,shell=True)

while p.poll() is None:
    time.sleep(0.05)

lines=p.stdout.readlines()
lines=map(lambda x: str(x,"utf-8").strip(),lines)

option = st.sidebar.selectbox(label="wybierz dane",options=lines)


if st.sidebar.button("sprawdź data drift"):
    st.write(data_drift(option))
