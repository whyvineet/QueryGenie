# QueryGenie

QueryGenie is a Telegram bot integrated with the Gemini API that assists Telegram users. It can generate responses to user queries using a generative AI model.

## Project Structure

```bash
QueryGenie/
├── bot.py
├── config.py
├── handlers.py
├── weather.py
├── genai_client.py
├── utils.py
├── LICENSE
└── README.md
```

## Files Overview

### `bot.py`

This is the main entry point for the Telegram bot. It configures and runs the bot.

* **Imports**: Necessary modules and handlers.
* **ApplicationBuilder**: Builds the application with the Telegram bot token.
* **CommandHandler**: Handles the `/start` command.
* **MessageHandler**: Handles text messages that are not commands.
* **run_polling**: Starts the bot by polling for new updates.

### `config.py`

Configures the environment and logging.

* **dotenv**: Loads environment variables from a `.env` file.
* **TOKEN** : Telegram bot token.
* **API_KEY**: API key for the generative AI model.
* **logging**: Configures logging for debugging and information purposes.

### `genai_client.py`

Handles interaction with the generative AI model from the Gemini API.

* **genai**: Configures the generative model with the provided API key.
* **generate_content**: Generates content based on a provided prompt.

### `handlers.py`

Defines handlers for the Telegram bot commands and messages.

* **start**: Initializes chat history and sends a welcome message to the user.
* **weather**: Handles the `/weather` command, fetching and returning weather information for a specified city.
* **chat**: Handles incoming user messages, generates a response using the generative AI model, and replies to the user.

### `weather.py`

Manages weather-related functionality using an external weather API.

* Uses the `requests` library to make API calls
* Fetches real-time weather data for a specified city
* Formats and returns weather information to the user

### `utils.py`

Provides utility functions.

* **structure_message**: Structures messages with a specified role and content.

## Setup Instructions

1. **Clone the Repository** :

   ```
   git clone https://github.com/whyvineet/QueryGenie.git
   cd QueryGenie
   ```
2. **Create and Activate a Virtual Environment** :

   ```
   python -m virtualenv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
3. **Install Dependencies** :

   ```
   pip install python-telegram-bot --upgrade
   pip install python-dotenv
   pip install -q -U google-generativeai
   pip install requests
   ```
4. **Set Up Environment Variables** :

   * Create a `.env` file in the project root.
   * Add your Telegram bot token and Gemini API key:
     ```
     TOKEN=your-telegram-bot-token
     API_KEY=your-gemini-api-key
     WEATHER_API_KEY=your-openweather-api-key
     ```
5. **Run the Bot** :

   ```
   python bot.py
   ```

## Usage

* **Start the Bot**: Send the `/start` command to the bot to initialize the conversation.
* **Get Weather Information**: Use the `/weather` command followed by a city name to get current weather information. For example: `/weather Mumbai`
  - The bot will respond with the current temperature and weather description for the specified city.
* **Chat with the Bot**: Send any text message to the bot, and it will respond using the generative AI model.
* **Continuous Conversation**: The bot maintains context, so you can have ongoing conversations about various topics.

## Error Handling

The bot includes error handling for various scenarios:
* If the weather command is used incorrectly, the bot will provide instructions on proper usage.
* If there's an issue fetching weather data, the bot will inform the user of the problem.
* For any other errors, the bot will provide a friendly error message and encourage the user to try again.

## Learn More

For a detailed explanation of how QueryGenie works and how you can create a similar bot, check out the article titled [Creating a Telegram Chatbot Powered by Gemini AI](https://www.geeksforgeeks.org/creating-a-telegram-chatbot-powered-by-gemini-ai/) by Vineet Kumar on GeeksforGeeks. The article walks you through the entire process, from setting up your development environment to deploying the bot, making it easier to understand the concepts behind QueryGenie.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
