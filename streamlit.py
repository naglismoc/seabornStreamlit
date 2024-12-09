import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.write("demo pristatymo vaizdas")

# Input widgets
name = st.text_input("prisistatyk!")
age = st.number_input("kiek tau metu?")
st.write(f'labas {name} kuriam yra {age} metu')

# Displaying data
st.subheader("Random Data Table")
df = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])
st.dataframe(df)

# Line chart
st.subheader("Line Chart")
st.line_chart(df)

# Interactive checkbox
if st.checkbox("Show Histogram"):
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(df["A"], bins=10, color="blue", alpha=0.7)
    st.pyplot(fig)

# Sidebar functionality
st.sidebar.title("Sidebar")
option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You selected: {option}")


# File upload
st.subheader("File Upload")
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Uploaded DataFrame:")
    st.dataframe(uploaded_df)


# # Title for the app
st.title("Matplotlib Plot in Streamlit")

# Input sliders for customization
x_start = st.slider("Start of X-axis", -10, 0, -5)
x_end = st.slider("End of X-axis", 1, 20, 10)
num_points = st.slider("Number of Points", 10, 1000, 100)

# Generate data
x = np.linspace(x_start, x_end, num_points)
y = np.sin(x)

# Create a Matplotlib plot
fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)", color="blue")
ax.set_title("Sine Wave")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Radio Buttons
radio_choice = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {radio_choice}")


# Multiselect
multi_choice = st.multiselect("Select multiple", ["Option A", "Option B", "Option C"])
st.write(f"You selected: {multi_choice}")


# Slider
slider_value = st.slider("Select a range", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

# Selectbox
select_choice = st.selectbox("Select one", ["Choice 1", "Choice 2", "Choice 3"])
st.write(f"You selected: {select_choice}")


# Button
if st.button("Click Me!"):
    st.write("Button clicked!")

# Title
st.title("Streamlit Functionalities Demo")
# Header and Subheader
st.header("Interactive Widgets")
st.subheader("Text and Input Components")


# Charts
st.header("Chart Visualizations")
data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])

st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)


# Map
st.header("Map Example")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)
