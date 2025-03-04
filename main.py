import sys
from weather import get_current_weather, get_5_day_forecast
from visualization import plot_temperature_trend  # Fixed import

def main():
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key

    if len(sys.argv) < 2:
        print("Usage: python main.py <city_name>")
        return

    city = sys.argv[1]

    # Get current weather
    print("\nFetching current weather...")
    current_weather = get_current_weather(city, api_key)
    print(current_weather)

    # Get 5-day forecast
    print("\nFetching 5-day forecast...")
    forecast = get_5_day_forecast(city, api_key)
    print(forecast)

    # Plot temperature trend
    plot_temperature_trend(forecast)

if __name__ == "__main__":
    main()
