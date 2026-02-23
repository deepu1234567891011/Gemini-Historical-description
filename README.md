🏺 Gemini Historical Artifact Description App 📌 Project Overview

The Gemini Historical Artifact Description App is an AI-powered web application that generates detailed and informative descriptions of historical artifacts and historical topics. Users can enter the name of an artifact, specify the desired word count, and optionally upload an image. The AI then generates a structured and engaging description including historical background, cultural significance, and interesting facts.

This project is built using Python, Streamlit, and AI API integration.

🚀 Features

Generate detailed historical artifact descriptions

Custom word count selection

Upload artifact images (optional)

Displays random historical facts

User-friendly web interface

Secure API key management using environment variables

Fast AI-powered content generation

🛠️ Technologies Used

Python

Streamlit

OpenRouter API

Requests

Python-dotenv

📂 Project Structure gemini-historical-artifact-description/ │ ├── app.py ├── requirements.txt ├── .env ├── README.md ⚙️ Installation and Setup 1️⃣ Clone the Repository git clone https://github.com/yourusername/gemini-historical-artifact-description.git cd gemini-historical-artifact-description 2️⃣ Install Required Libraries pip install -r requirements.txt 3️⃣ Add API Key

Create a .env file and add:

OPENROUTER_API_KEY=your_api_key_here 4️⃣ Run the Application streamlit run app.py 🖥️ How to Use

Enter an artifact name or historical topic

Select desired word count

Upload artifact image (optional)

Click Generate Artifact Description

View the AI-generated result

📸 Sample Input

Topic: Taj Mahal Word Count: 200

📄 Sample Output

The Taj Mahal is one of the most iconic monuments in the world. Built in the 17th century by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal, it stands as a symbol of love and architectural brilliance. Constructed using white marble and precious stones, the monument reflects a blend of Persian, Islamic, and Indian architectural styles. The Taj Mahal remains a UNESCO World Heritage Site and attracts millions of visitors every year.

🌐 Deployment

This application can be deployed for free using Streamlit Cloud.

🎯 Project Objective

This project demonstrates:

AI integration in web applications

Streamlit-based frontend development

API handling and environment variable management

Real-world AI project implementation

👨‍💻 Author

Your Name B.Tech Student | Python Developer | AI Enthusiast

⭐ Future Enhancements

Download generated description as PDF

Multi-language support

Improved UI/UX design

Image-based artifact recognition
