import streamlit as st
import plotly.express as px

st.title( f"Weather forecast for the next days" )
location = st.text_input( "Location: " )
number_of_days = st.slider( "Forecasted days: ", min_value = 1, max_value = 5 )
data_view = st.selectbox( "Select data to view: ", ( "Temperature", "Sky" ) )
st.subheader( f"{data_view} for the next {number_of_days} days in {location}" )


dates = ["2022-10-25", "2022-10-26", "2022-10-27"]
temperatures = ["23", "09", "15"]
chart = px.line( x = dates, y = temperatures, labels = {"x": "Date", "y": "Temperature (C)"})
st.plotly_chart( chart )