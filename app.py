import streamlit as st
import plotly.express as px
import backend

st.title( f"Weather forecast for the next days" )
location = st.text_input( "Location: ", placeholder = "London")

if location == "":
    location = "London"

number_of_days = st.slider( "Forecasted days: ", min_value = 1, max_value = 5 )
data_view = st.selectbox( "Select data to view: ", ( "Temperature", "Sky" ) )

if data_view == "Temperature":
    st.subheader( f"{data_view} for the next {number_of_days} days in {location}" )

    data = backend.get_data( location = location )

    time, temperatures = backend.extract_time_and_temps( data = data, forecast_days = number_of_days )

    chart = backend.generate_chart( x_data = time, y_data = temperatures, x_label = "Time", y_label = "Temperature (C)")

    st.plotly_chart( chart )
    
elif data_view == "Sky":
    st.subheader( "Feature Coming Soon..." )
    
else:
    st.subheader( "Application failure!" )