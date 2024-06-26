from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_AI_KEY"]

#Set up Flask app
app = Flask(__name__)

#Define the home page
@app.route('/') # if / is the main page 5000, however if I put main, it will show the the same url but with 5000/main
def home():
    return render_template("index.html")

#Define the chatbot route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    #Get the message input from the user
    user_input = request.form["message"]

    # Use the OpenAI AI to generate a response
    prompt = f"User: {user_input}\nChatbot: "
    
    #Save current session conversation
    chat_history = []

    # Chabot especification
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frenquency_penanlty=0,
        stop=["\nUser", "\nChatbot: "]

    )

    # Extract the response text from the OpenAI API 
    bot_response = response.choices[0].text.strip()

    # Add the user input and bot to the chat history
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")
    
    # render the Chatbot template with the response text
    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response,
    )

if __name__ == '__main__':
    app.run(debug=True)