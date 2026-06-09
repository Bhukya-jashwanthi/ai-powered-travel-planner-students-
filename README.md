# AI-Powered Student Travel Planner 🌍✈️

Planning trips can be incredibly time-consuming and expensive, especially for students operating on strict financial constraints. Traditional travel applications often provide generic, costly suggestions. 

The **AI-Powered Student Travel Planner** is a responsive web application designed to solve this problem. By combining user preferences with generative AI, it creates customized, budget-friendly, day-by-day itineraries tailored specifically for low-budget student travelers.

---

## 🚀 Features

- **Budget-Centric Optimization:** Automatically prioritizes affordable accommodation, food, and sightseeing options based on specific student financial limits.
- **Dynamic Itinerary Generation:** Leverages advanced generative AI to create customized, day-by-day schedules in real time.
- **Tailored Inputs:** Accepts user-defined variables including destination, trip duration, maximum budget constraints, and personal activity preferences.
- **No Generic Suggestions:** Eliminates cookie-cutter travel plans by generating unique itineraries dynamically centered around user constraints.

---

## 🛠️ Tech Stack

- **Frontend Interface:** [Streamlit](https://streamlit.io/) (Python-based web framework)
- **Backend Core:** Python
- **Generative AI Engine:** Google Gemini API
- **Data Structuring:** JSON Parsing & Data Formats

---

## 💻 How to Run the Project

Follow these steps to set up and run the web application locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/ai-student-travel-planner.git](https://github.com/your-username/ai-student-travel-planner.git)
cd ai-student-travel-planner
```
2. Install Required Dependencies
Ensure you have Python installed, then run:

Bash
pip install streamlit google-generativeai
3. Set Up Your Gemini API Key
Make sure you have a valid API key from Google AI Studio. You can set it as an environment variable or include it securely within your configuration files.

4. Launch the Web Application
Run the Streamlit application using the terminal:

Bash
streamlit run app.py
