import csv
import io

import streamlit as st




uploaded_file = st.file_uploader("ikelk faila", type=['csv'])

if uploaded_file is not None:
    data = []

    file_content = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    csv_reader = csv.reader(file_content)

    #jeigu yra headeriai tada atkomentuojam sita eilute
    next(csv_reader)

    for row in csv_reader:
        data.append(row) #tolimesniems darbams, pasiverciu i pitono koda
        st.write(row) #alternatyva, iskart printint jei to uztenka

