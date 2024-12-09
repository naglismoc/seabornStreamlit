import streamlit as st

import matplotlib.pyplot as plt
from MatplotForImport import create_plot

st.title("Zemiau .py failas, kuri uzkroviau per koda")

fig = create_plot()
st.pyplot(fig)


# File uploader for .py files
uploaded_files = st.file_uploader(
    "Upload Python files with Matplotlib code", type="py", accept_multiple_files=True
)
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.subheader(f"Executing: {uploaded_file.name}")
        # Read and decode the contents of each uploaded file
        code = uploaded_file.read().decode("utf-8")
        # Wrap execution to capture Matplotlib output
        try:
            plt.figure()  # Create a new figure for each file
            # Execute the uploaded Python code
            exec(code)
            # Display the Matplotlib figure in Streamlit
            st.pyplot(plt.gcf())
        except Exception as e:
            st.error(f"Error in {uploaded_file.name}: {e}")
