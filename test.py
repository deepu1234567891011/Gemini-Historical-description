from google.genai import Client

# Paste your REAL API key here
client = Client(api_key="AIzaSyCxxrF6zOFnCrtunAokQdMJfJgB3iDKLBU")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Tell me about Taj Mahal"
)

print(response.text)
