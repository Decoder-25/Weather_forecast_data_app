import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=7,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
    temperature = [10, 12, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
