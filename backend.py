import requests
import plotly.express as px

def get_data( location: str = "London") -> dict:
    if location == "":
        location = "London"
    
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=uk&include=hours&key=5UQAJNJT6DRHMMD7CEQEJBDLC&contentType=flatjson"
    response = requests.get( url )
    json_data = response.json()
    data = json_data["hours"]
    
    return data
    
def extract_time_and_temps( data: dict, forecast_days: int = 1) -> tuple:
    forcast_hours = forecast_days * 24
    
    time = data["datetime"][0:forcast_hours]
    temperatures = data["temp"][0:forcast_hours]
    
    return ( time, temperatures )

def generate_chart( x_data: list, y_data: list, x_label: str, y_label: str, type: str = "line" ):
    if type == "line":
        chart = px.line( x = x_data, y = y_data, labels = {"x": x_label, "y": y_label})
        
    return chart


if __name__ == "__main__":
    data = get_data()
    time, temperatures = extract_time_and_temps( data )
    
    print( time )
    print()
    print( temperatures )
    