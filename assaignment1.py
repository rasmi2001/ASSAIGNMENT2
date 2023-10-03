import requests
API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
def get_weather_data(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to retrieve weather data. Check the API URL.")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def get_temperature(data, target_time):
    for entry in data["list"]:
        if entry["dt_txt"] == target_time:
            return entry["main"]["temp"]
    return None

def get_wind_speed(data, target_time):
    for entry in data["list"]:
        if entry["dt_txt"] == target_time:
            return entry["wind"]["speed"]
    return None

def get_pressure(data, target_time):
    for entry in data["list"]:
        if entry["dt_txt"] == target_time:
            return entry["main"]["pressure"]
    return None

def main():
    data = get_weather_data(API_URL)

    if not data:
        return

    print("What would you like to know about the weather?")
    print("1. Temperature")
    print("2. Wind speed")
    print("3. Pressure")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        target_time = input("Enter a date and time (e.g., '2023-10-03 12:00:00'): ")
        temperature = get_temperature(data, target_time)
        if temperature is not None:
            print(f"The temperature at {target_time} is {temperature} degrees Celsius.")
        else:
            print("No data available for the specified date and time.")
    elif choice == "2":
        target_time = input("Enter a date and time (e.g., '2023-10-03 12:00:00'): ")
        wind_speed = get_wind_speed(data, target_time)
        if wind_speed is not None:
            print(f"The wind speed at {target_time} is {wind_speed} meters per second.")
        else:
            print("No data available for the specified date and time.")
    elif choice == "3":
        target_time = input("Enter a date and time (e.g., '2023-10-03 12:00:00'): ")
        pressure = get_pressure(data, target_time)
        if pressure is not None:
            print(f"The pressure at {target_time} is {pressure} hectopascals.")
        else:
            print("No data available for the specified date and time.")
    elif choice == "0":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()