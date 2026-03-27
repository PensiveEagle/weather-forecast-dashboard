import streamlit as st

st.title( f"Weather forecast for the next days" )
location = st.text_input( "Location: " )
number_of_days = st.slider( "Forecasted days: ", min_value = 1, max_value = 5 )
data_view = st.selectbox( "Select data to view: ", ( "Temperature", "Sky" ) )
st.subheader( f"{data_view} for the next {number_of_days} days in {location}" )