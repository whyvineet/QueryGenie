from telegram import Update
from telegram.ext import ContextTypes
from config import logger
from genai_client import generate_content
from utils import structure_message
from weather import get_weather

# Initialize chat histories
chat_histories = {}

ROLE_SYSTEM = "system"
ROLE_USER = "user"
ROLE_ASSISTANT = "assistant"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id

    # Initialize chat history for the user
    chat_histories[user_id] = []

    # Add system message with role description
    role_description = "You are QueryGenie: a telegram bot integrated with Gemini API to assist users on Telegram (developed by Vineet Kumar)."
    chat_histories[user_id].append(structure_message(ROLE_SYSTEM, role_description))

    system_message = "I'm QueryGenie and here to assist with your queries. Feel free to ask me anything, and I'll do my best to provide you with the information you need. Let's get started!"
    chat_histories[user_id].append(structure_message(ROLE_SYSTEM, system_message))

    await update.message.reply_text(system_message)

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    
    if not context.args:
        await update.message.reply_text("Please provide a city name. Usage: /weather <city>")
        return
    
    city = ' '.join(context.args)
    weather_info = get_weather(city)
    
    # Log the weather request
    logger.info(f"User ({user_id}) requested weather for {city}")
    
    await update.message.reply_text(weather_info)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_message = update.message.text

    # Log incoming user message
    logger.info(f"User ({user_id}): {user_message}")

    # Store the user's message in chat history
    chat_histories[user_id].append(structure_message(ROLE_USER, user_message))

    # Generate response using chat history
    full_prompt = "\n".join([msg['content'] for msg in chat_histories[user_id]])
    response_text = generate_content(full_prompt)

    # Store the bot's response in chat history
    chat_histories[user_id].append(structure_message(ROLE_ASSISTANT, response_text))

    # Log the bot's response
    logger.info(f"Bot: {response_text}")

    await update.message.reply_text(response_text)