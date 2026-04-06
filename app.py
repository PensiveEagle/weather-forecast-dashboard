import streamlit as st
import plotly.express as px
import backend
from dotenv import load_dotenv
from os import getenv

load_dotenv()
weather_api_key = str( getenv( "OPEN_WEATHER_API_KEY" ) )

st.title( f"Weather forecast for the next days" )
location = st.text_input( "Location: ", placeholder = "London")

if location == "":
    location = "London"

number_of_days = st.slider( "Forecasted days: ", min_value = 1, max_value = 5, value = 3 )
data_view = st.selectbox( "Select data to view: ", ( "Temperature", "Sky" ) )

if data_view == "Temperature":
    chart_type = st.selectbox( "Select type of chart: ", ( "Line Chart", "Bar Chart" ) )
    
    st.subheader( f"{chart_type} Showing Temperature in {location} for the Next {number_of_days} Days" )

    data = backend.get_data( location = location, api_key = weather_api_key )

    time, temperatures = backend.extract_time_and_temps( data = data, forecast_days = number_of_days )

    chart = backend.generate_chart( x_data = time, y_data = temperatures, x_label = "Time", y_label = "Temperature (C)", type = chart_type)

    st.plotly_chart( chart )
    
elif data_view == "Sky":
    st.subheader( "Feature Coming Soon..." )
    
else:
    st.subheader( "Application failure!" )