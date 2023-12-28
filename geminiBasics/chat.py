import google.generativeai as genai
from apiKey import key
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat()
while True:
    message=input("You: ")
    response=chat.send_message(message)
    print("Gemini: "+response.text)