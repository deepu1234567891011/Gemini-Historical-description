import streamlit as st
import random
from google.genai import Client

# ===============================
# 🔑 Gemini API Key
# ===============================
API_KEY = "AIzaSyC3y0Ut1MxXgGu9ED5PDdgAN2nXhuBsG3s"
import random
from google.genai import Client

# ===============================
# 🔑 Gemini API Key
# ===============================
API_KEY = "YOUR_GEMINI_API_KEY"

client = Client(api_key=API_KEY)

# ===============================
# 📜 Historical Facts
# ===============================
historical_facts = [
    "Tutankhamun became Pharaoh at age 9.",
    "The Taj Mahal took 22 years to build.",
    "Leonardo da Vinci wrote in mirror writing.",
    "The Great Wall of China is over 13,000 miles long.",
    "Ancient Egyptians used gold because it never tarnishes.",
]

# ===============================
# 🤖 Generate Description
# ===============================
def generate_description(topic, word_count):

    prompt = f"""
    Write a detailed historical artifact description about {topic}.
    The description should be approximately {word_count} words.
    Include historical background, cultural significance, and interesting facts.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",   # ✅ CORRECT MODEL
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# ===============================
# 🎨 Streamlit UI
# ===============================
st.title("🏺 Gemini Historical Artifact Description App")

topic = st.text_input("Enter Artifact Name or Historical Topic:")

word_count = st.number_input(
    "Enter Desired Word Count:",
    min_value=50,
    max_value=2000,
    value=200
)

fact = random.choice(historical_facts)
st.info(f"📜 Historical Fact: {fact}")

if st.button("Generate Artifact Description"):

    if topic:

        with st.spinner("Generating description..."):
            result = generate_description(topic, word_count)

        st.success("Description Generated Successfully!")
        st.write(result)

    else:
        st.warning("Please enter artifact name.")
import random
from google.genai import Client

# ===============================
# 🔑 Gemini API Key
# ===============================
API_KEY = "YOUR_GEMINI_API_KEY"

client = Client(api_key=API_KEY)

# ===============================
# 📜 Historical Facts
# ===============================
historical_facts = [
    "Tutankhamun became Pharaoh at age 9.",
    "The Taj Mahal took 22 years to build.",
    "Leonardo da Vinci wrote in mirror writing.",
    "The Great Wall of China is over 13,000 miles long.",
    "Ancient Egyptians used gold because it never tarnishes.",
]

# ===============================
# 🤖 Generate Description
# ===============================
def generate_description(topic, word_count):

    prompt = f"""
    Write a detailed historical artifact description about {topic}.
    The description should be approximately {word_count} words.
    Include historical background, cultural significance, and interesting facts.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",   # ✅ CORRECT MODEL
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# ===============================
# 🎨 Streamlit UI
# ===============================
st.title("🏺 Gemini Historical Artifact Description App")

topic = st.text_input("Enter Artifact Name or Historical Topic:")

word_count = st.number_input(
    "Enter Desired Word Count:",
    min_value=50,
    max_value=2000,
    value=200
)

fact = random.choice(historical_facts)
st.info(f"📜 Historical Fact: {fact}")

if st.button("Generate Artifact Description"):

    if topic:

        with st.spinner("Generating description..."):
            result = generate_description(topic, word_count)

        st.success("Description Generated Successfully!")
        st.write(result)

    else:
        st.warning("Please enter artifact name.")"

client = Client(api_key=API_KEY)

# ===============================
# 📜 Historical Facts
# ===============================
historical_facts = [
    "Tutankhamun became Pharaoh at age 9.",
    "The Taj Mahal took 22 years to build.",
    "Leonardo da Vinci wrote in mirror writing.",
    "The Great Wall of China is over 13,000 miles long.",
    "Ancient Egyptians used gold because it never tarnishes.",
]

# ===============================
# 🤖 Generate Description
# ===============================
def generate_description(topic, word_count):

    prompt = f"""
    Write a detailed historical artifact description about {topic}.
    The description should be approximately {word_count} words.
    Include historical background, cultural significance, and interesting facts.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",   # ✅ CORRECT MODEL
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# ===============================
# 🎨 Streamlit UI
# ===============================
st.title("🏺 Gemini Historical Artifact Description App")

topic = st.text_input("Enter Artifact Name or Historical Topic:")

word_count = st.number_input(
    "Enter Desired Word Count:",
    min_value=50,
    max_value=2000,
    value=200
)

fact = random.choice(historical_facts)
st.info(f"📜 Historical Fact: {fact}")

if st.button("Generate Artifact Description"):

    if topic:

        with st.spinner("Generating description..."):
            result = generate_description(topic, word_count)

        st.success("Description Generated Successfully!")
        st.write(result)

    else:
        st.warning("Please enter artifact name.")