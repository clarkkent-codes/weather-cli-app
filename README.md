# Weather CLI App

A simple Python CLI Weather App that fetches the current weather using Open-Meteo's API
and **Geopy** for retrieving latitude/longitude

## Features
- Enter a city name to get current weather
- Shows latitude, longitude, temperature, and condition
- Handles invalid/unknown city names with error messages

## Tech Stack
- Python
- Geopy
- Open-Meteo API
- Requests (with caching & retries)

## Screenshot
Correct usage<br>
<img width="298" height="100" alt="image" src="https://github.com/user-attachments/assets/28d9b3dc-4ef5-43f1-8763-4bc4cef2bc4e" />
<br>
Not a real City<br>
<img width="456" height="120" alt="image" src="https://github.com/user-attachments/assets/b3426cdf-76b6-499c-a444-8c160c165c04" />

## Usage
```bash
pip install -r requirements.txt
```

```bash
python weatherapp.py
```
or you can run it using your preferred IDE
