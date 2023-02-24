from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from textblob import TextBlob
import openai

# Set up the chatbot
bot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english.movies')

# Set up the OpenAI API
openai.api_key = "YOUR_API_KEY"

# Set up the conversation history dictionary
conversation_history = {}


# Define a function to respond to user messages
def respond(user_id, message):
    # Use the previous message to inform the response
    if user_id in conversation_history:
        previous_message = conversation_history[user_id]
        response = bot.get_response(message, previous_message.text)
    else:
        response = bot.get_response(message)
    conversation_history[user_id] = response

    # Perform sentiment analysis on the user's message
    sentiment = TextBlob(message).sentiment.polarity
    if sentiment > 0:
        sentiment_response = "I'm glad to hear that!"
    elif sentiment < 0:
        sentiment_response = "I'm sorry to hear that. Is there anything I can do to help?"
    else:
        sentiment_response = "Interesting. Tell me more!"

    # Use GPT-3 to generate a more sophisticated response
    gpt_response = openai.Completion.create(
        engine="davinci", prompt=message, max_tokens=60
    )
    gpt_response = gpt_response.choices[0].text.strip()

    # Display the responses to the user and ask for feedback
    response = f"{response}\n{sentiment_response}\n{gpt_response}\nPlease rate my response (1-5):"
    feedback = input(response)

    # Use the feedback to improve the chatbot's training
    trainer.train([message, feedback])

    return feedback


# Start the chatbot loop
while True:
    user_id = input("Enter user ID:")
    message = input("Enter message:")
    response = respond(user_id, message)
    print(f"Response: {response}")
