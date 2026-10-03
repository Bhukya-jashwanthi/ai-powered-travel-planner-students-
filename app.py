import os
import time

import streamlit as st
from google import genai
from google.genai import types


# -----------------------------
# App configuration
# -----------------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide",
)

MODEL_NAME = "gemini-3.8-flash"

SYSTEM_PROMPT = """
You are an intelligent travel assistant helping students plan trips.

Create practical, personalized travel plans based on the user's destination,
trip duration, budget, interests, accommodation preference, and requirements.

Be clear and realistic. Organize the itinerary day by day and include:
- Morning, afternoon, and evening activities
- Food and dining suggestions
- Accommodation suggestions
- Local transportation guidance
- Estimated budget categories
- Useful travel tips

Do not claim that prices, opening hours, availability, or travel conditions
are guaranteed. Remind users to verify current information before booking.
"""


# -----------------------------
# Get Gemini API key securely
# -----------------------------
api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error(
        "Gemini API key not found. Please add GEMINI_API_KEY "
        "to .streamlit/secrets.toml."
    )
    st.stop()

client = genai.Client(api_key=api_key)


# -----------------------------
# Generate itinerary
# -----------------------------
def generate_itinerary(
    location,
    duration,
    budget,
    interests,
    accommodation,
    additional_notes,
):
    prompt = f"""
Create a personalized student travel itinerary.

Destination: {location}
Trip duration: {duration} days
Budget: {budget}
Interests: {interests}
Accommodation preference: {accommodation}
Additional requirements: {additional_notes or "None"}

Return the answer in this structure:

# Trip Overview
Briefly describe the trip.

# Day 1
## Morning
## Afternoon
## Evening

Repeat the same structure for every day.

# Food Recommendations
Suggest suitable local foods and dining options.

# Accommodation
Suggest suitable types of accommodation for the stated budget.

# Transportation
Explain practical ways to travel around the destination.

# Estimated Budget
Break the budget into:
- Accommodation
- Food
- Transportation
- Activities
- Miscellaneous

# Student Travel Tips
Give useful practical tips.

Keep the recommendations appropriate for a student and the stated budget.
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.7,
                ),
            )
            return response.text
        except Exception as e:
            if "503" in str(e) and attempt < 2:
                time.sleep(5)
            else:
                raise


# -----------------------------
# Streamlit interface
# -----------------------------
st.title("🌍 AI Travel Planner for Students")
st.write(
    "Plan a personalized trip based on your destination, budget, "
    "interests, and travel preferences."
)

with st.form("travel_planner_form"):
    location = st.text_input(
        "Where are you planning to travel?",
        placeholder="Example: Paris, Bali, Tokyo",
    )

    duration = st.slider(
        "How many days will your trip last?",
        min_value=1,
        max_value=30,
        value=5,
    )

    budget = st.selectbox(
        "What's your budget?",
        ["Low", "Moderate", "High"],
    )

    interests = st.text_area(
        "What are your interests?",
        placeholder="Example: culture, adventure, food, beaches",
    )

    accommodation = st.selectbox(
        "Preferred accommodation type",
        ["Budget", "Mid-range", "Luxury", "Unique stays"],
    )

    additional_notes = st.text_area(
        "Any specific requirements or preferences?",
        placeholder="Example: vegetarian food, accessibility, student discounts",
    )

    submitted = st.form_submit_button("✨ Generate Itinerary")


# -----------------------------
# Generate result
# -----------------------------
if submitted:
    if not location.strip():
        st.warning("Please enter a destination.")

    elif not interests.strip():
        st.warning("Please enter at least one interest.")

    else:
        with st.spinner("Planning your trip..."):
            try:
                itinerary = generate_itinerary(
                    location=location,
                    duration=duration,
                    budget=budget,
                    interests=interests,
                    accommodation=accommodation,
                    additional_notes=additional_notes,
                )

                st.success("Your itinerary is ready!")
                st.markdown(itinerary)

                st.info(
                    "Travel prices, opening hours, availability, and local "
                    "conditions can change. Verify important details before booking."
                )

            except Exception as e:
                st.error(
                    "Something went wrong while generating your itinerary."
                )
                st.caption(f"Error details: {e}")
                