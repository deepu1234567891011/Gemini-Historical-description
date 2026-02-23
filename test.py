from google.genai import Client

# Paste your REAL API key here
client = Client(api_key="AIzaSyAtBnx8cJK0y9b9QajG9wcl7oL6dpM5EXE")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Tell me about Taj Mahal"
)

print(response.text)