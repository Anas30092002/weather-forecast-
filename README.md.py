import matplotlib.pyplot as plt
from datetime import datetime

def plot_temperature_trend(forecast):
    dates = []
    temperatures = []

    for item in forecast:
        dates.append(datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S"))
        temperatures.append(item['temperature'])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o')
    plt.title('5-Day Temperature Trend')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()