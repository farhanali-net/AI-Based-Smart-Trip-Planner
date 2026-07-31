from google.genai import types
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from datetime import datetime, timedelta
import requests
import json
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

print("Current Directory:", os.getcwd())
print("Gemini Key:", GEMINI_API_KEY)
print("Weather Key:", OPENWEATHER_API_KEY)
print("Pexels Key:", PEXELS_API_KEY)

app = Flask(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)

# ==========================
# Allowed Destinations
# AI should ONLY recommend these
# ==========================

DESTINATIONS = [

    "Hunza Valley",
    "Skardu",
    "Fairy Meadows",
    "Deosai National Park",
    "Khaplu",
    "Shigar",
    "Attabad Lake",
    "Passu",
    "Khunjerab Pass",
    "Nagar Valley",
    "Naltar Valley",
    "Rama Lake",
    "Satpara Lake",
    "Shangrila Resort",
    "Upper Kachura Lake",
    "Lower Kachura Lake",

    "Swat Valley",
    "Kalam Valley",
    "Malam Jabba",
    "Mahodand Lake",
    "Kumrat Valley",
    "Chitral",
    "Ayun Valley",
    "Garam Chashma",

    "Naran",
    "Kaghan Valley",
    "Lake Saif-ul-Malook",
    "Babusar Top",
    "Shogran",
    "Siri Paye Meadows",

    "Neelum Valley",
    "Arang Kel",
    "Keran",
    "Sharda",
    "Muzaffarabad"

]

# ==========================
# Home Route
# ==========================

@app.route("/")
def home():
    return render_template("index.html")

# ==========================
# Weather Function
# ==========================

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},PK"
        f"&appid={OPENWEATHER_API_KEY}"
        f"&units=metric"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "Weather unavailable"

        data = response.json()

        return (
            f"{data['weather'][0]['main']} | "
            f"{data['main']['temp']}°C | "
            f"Humidity {data['main']['humidity']}%"
        )

    except Exception:

        return "Weather unavailable"

# ==========================
# Pexels Image Function
# ==========================

def get_image(destination):
    

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": destination + " Pakistan",
        "per_page": 1
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg"

        photos = response.json().get("photos", [])

        if not photos:
            return "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg"

        return photos[0]["src"]["large"]

    except Exception:

        return "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg"
    
    # ==========================
# Gemini AI Function
# ==========================

def generate_ai_trip(user_data):

    prompt = f"""
You are an expert travel planner for Northern Pakistan.

IMPORTANT RULES

1. Recommend ONLY destinations from this list:

{', '.join(DESTINATIONS)}

2. Never recommend any destination outside Pakistan.

3. Choose the BEST destination based on:
- Budget
- Number of travel days
- Travel style
- Preferred weather
- User interests

4. Recommend suitable travel dates based on:
- Best season
- Current year (2026)
- Number of travel days

5. Estimate the total travel budget.

6. Return ONLY valid JSON.

User Details

Name: {user_data["name"]}

Departure City: {user_data["departure_city"]}

Preferred Destination: {user_data["preferred_destination"]}

Budget: {user_data["budget"]} PKR

Days: {user_data["days"]}

Travelers: {user_data["travelers"]}

Travel Style: {user_data["travel_style"]}

Preferred Weather: {user_data["weather"]}

Interests:
{', '.join(user_data["interests"])}

Return ONLY this JSON:

{{
  "recommended_dates":"",
  "destination":"",
  "reason":"",
  "best_season":"",
  "estimated_budget":"",
  "itinerary":[
    {{
      "day":"Day 1",
      "plan":""
    }}
  ],
  "hotels":[
    ""
  ],
  "restaurants":[
    ""
  ],
  "packing":[
    ""
  ],
  "safety":[
    ""
  ],
  "travel_tips":[
    ""
  ],
  "local_foods":[
    ""
  ]
}}
"""

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=0.7,

                response_mime_type="application/json"

            )

        )

        return json.loads(response.text)

    except Exception as e:

        print("Gemini Error:", e)

        return {

            "recommended_dates": "15 September 2026 - 20 September 2026",

            "destination": "Hunza Valley",

            "reason": "Unable to contact Gemini API.",

            "best_season": "April - October",

            "estimated_budget": "50000 PKR",

            "itinerary": [

                {
                    "day": "Day 1",
                    "plan": "Travel from Islamabad to Hunza and check into your hotel."
                },
                {
                    "day": "Day 2",
                    "plan": "Visit Baltit Fort, Altit Fort, and Karimabad Bazaar."
                }

            ],

            "hotels": [

                "Serena Hunza",
                "Eagle's Nest Hotel"

            ],

            "restaurants": [

                "Cafe De Hunza",
                "Rainbow Restaurant"

            ],

            "packing": [

                "Warm Jacket",
                "Comfortable Shoes",
                "Power Bank",
                "Sunglasses"

            ],

            "safety": [

                "Carry your CNIC.",
                "Keep emergency contacts saved.",
                "Check road conditions before traveling."

            ],

            "travel_tips": [

                "Start your journey early in the morning.",
                "Carry sufficient cash.",
                "Download offline Google Maps.",
                "Book hotels in advance during peak season."

            ],

            "local_foods": [

                "Chapshuro",
                "Mamtu",
                "Yak Karahi",
                "Hunza Walnut Cake"

            ]

        }
        # ==========================
# Generate Trip Route
# ==========================

@app.route("/generate-trip", methods=["POST"])
def generate_trip():

    try:

        data = request.get_json()

        user_data = {
            "name": data.get("name", ""),
            "departure_city": data.get("departure_city", ""),
            "preferred_destination": data.get("preferred_destination", ""),
            "budget": data.get("budget", ""),
            "days": data.get("days", ""),
            "travelers": data.get("travelers", ""),
            "travel_style": data.get("travel_style", ""),
            "weather": data.get("weather", ""),
            "interests": data.get("interests", [])
        }

        # Generate AI itinerary
        trip = generate_ai_trip(user_data)
        
    

        # Destination
        destination = trip.get("destination", "Hunza Valley")

        # Live weather
        trip["weather"] = get_weather(destination)

        # Destination image
        trip["image"] = get_image(destination)

        # Frontend compatibility
        trip["budget"] = trip.get("estimated_budget", "N/A")

        # Ensure these fields always exist
        trip["recommended_dates"] = trip.get(
            "recommended_dates",
            "Dates will be recommended by AI."
        )

        trip["travel_tips"] = trip.get(
            "travel_tips",
            []
        )

        trip["local_foods"] = trip.get(
            "local_foods",
            []
        )

        trip["hotels"] = trip.get(
            "hotels",
            []
        )

        trip["restaurants"] = trip.get(
            "restaurants",
            []
        )

        trip["packing"] = trip.get(
            "packing",
            []
        )

        trip["safety"] = trip.get(
            "safety",
            []
        )

        trip["itinerary"] = trip.get(
            "itinerary",
            []
        )

        return jsonify(trip)

    except Exception as e:

        print("Generate Trip Error:", e)

        return jsonify({
            "error": str(e)
        }), 500


# ==========================
# Run Flask
# ==========================

if __name__ == "__main__":
    app.run(debug=True)