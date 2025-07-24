import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

# Replace this with your actual OpenWeatherMap API key
API_KEY = "your_api_key_here"
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(API_URL, params=params)
    data = response.json()

    if data.get("cod") != 200:
        messagebox.showerror("Error", f"City not found: {city}")
        return

    temp = data["main"]["temp"]
    condition = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    weather_info = (
        f"Weather in {city.title()}:\n"
        f"Temperature: {temp}°C\n"
        f"Condition: {condition}\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind} m/s"
    )
    result_label.config(text=weather_info)

# Create app window
app = tk.Tk()
app.title("Weather App")
app.geometry("500x400")
app.resizable(False, False)

# === Load and set background image ===
try:
    bg_img = Image.open("weather_bg.jpg")  # Optional image in same directory
    bg_img = bg_img.resize((500, 400))
    bg_photo = ImageTk.PhotoImage(bg_img)

    bg_label = tk.Label(app, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    app.config(bg="#87ceeb")  # fallback sky blue color

# === UI Elements ===
title_label = tk.Label(app, text="Weather App", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#333333")
title_label.pack(pady=10)

city_entry = tk.Entry(app, font=("Helvetica", 14), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Accra")

search_btn = tk.Button(app, text="Check Weather", command=get_weather, font=("Helvetica", 12), bg="#4CAF50", fg="white")
search_btn.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 14), bg="#ffffff", justify="center")
result_label.pack(pady=20)

# Start the app
app.mainloop()
