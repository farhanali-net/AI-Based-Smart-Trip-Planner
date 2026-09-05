# AI-Based Smart Trip Planner for Northern Pakistan 

An AI-powered travel planning web application developed as a **University Tech Expo Project**. The system uses **Google Gemini AI** to generate personalized travel itineraries based on user preferences and integrates live weather information and destination images through external APIs.

---

## Project Overview

AI-Based Smart Trip Planner helps tourists discover the most suitable destinations in **Northern Pakistan**, especially **Gilgit-Baltistan**. Users enter their travel preferences such as budget, travel style, weather preference, and interests. The application then generates a personalized day-wise itinerary with destination recommendations, estimated budget, weather updates, hotels, restaurants, safety tips, packing checklist, and local food suggestions.

---

## Features

- AI-powered personalized trip recommendations using Google Gemini
- Day-wise travel itinerary generation
- Estimated travel budget
- Live weather updates using OpenWeather API
- Destination images from Pexels API
- Hotel and restaurant recommendations
- Packing checklist based on the destination
- Safety tips and travel advice
- Local food recommendations
- Responsive user interface
- Database-free architecture using external APIs

---

## Technology Stack

| Category | Technology |
|----------|------------|
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python, Flask |
| **AI / LLM** | Google Gemini API |
| **Weather API** | OpenWeather API |
| **Image API** | Pexels API |
| **Environment** | VS Code |
| **Version Control** | Git & GitHub |

---

## 📸 Project Screenshots

### Homepage

<img width="1350" height="604" alt="homepage" src="https://github.com/user-attachments/assets/a20832c1-0242-45f1-ad1f-1d0e7d4ce02b" />


---

### AI Trip Planner Form

<img width="329" height="492" alt="planner-form" src="https://github.com/user-attachments/assets/c12e8bf6-82f3-4714-b46f-233f6159a941" />

---

### Generated Trip Results

<img width="617" height="494" alt="trip-results" src="https://github.com/user-attachments/assets/3ecc34d7-3f5b-4ffd-a4f4-cfcc1583e1c6" />

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/farhanali-net/AI-Based-Smart-Trip-Planner.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Based-Smart-Trip-Planner
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
PEXELS_API_KEY=YOUR_PEXELS_API_KEY
```

### 7. Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Project Structure

```text
AI-Based-Smart-Trip-Planner/
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore
├── .env.example
│
├── static/
│   ├── images/
│   └── screenshots/
│
├── templates/
│   └── index.html
```

---

## APIs Used

| API | Purpose |
|------|---------|
| **Google Gemini API** | Generates personalized travel itineraries using AI |
| **OpenWeather API** | Provides live weather information |
| **Pexels API** | Displays destination images |

---

## Future Improvements

- User authentication and profiles
- Save trip history
- Interactive maps integration
- Trip booking
- Hotel and transport booking
- AI travel chatbot
- Multi-language support
- PDF itinerary export

---

## Author

**Farhan Ali**  
**BSCS 6C**  
**University Tech Expo Project**

---

## License

This project is licensed under the MIT License.
