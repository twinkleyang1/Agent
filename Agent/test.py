from google import genai

client = genai.Client(api_key="AIzaSyDXah-KLRKJQYyBsdCxQ2gFQ271u3DPD4U")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)