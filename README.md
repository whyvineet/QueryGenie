# QueryGenie

QueryGenie is a Telegram bot integrated with the Gemini API that assists Telegram users. It can generate responses to user queries using a generative AI model.

## Project Structure

```bash
QueryGenie/
├── bot.py
├── config.py
├── handlers.py
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
* **chat**: Handles incoming user messages, generates a response using the generative AI model, and replies to the user.

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
   ```
4. **Set Up Environment Variables** :

   * Create a `.env` file in the project root.
   * Add your Telegram bot token and Gemini API key:
     ```
     TOKEN=your-telegram-bot-token
     API_KEY=your-gemini-api-key
     ```
5. **Run the Bot** :

   ```
   python bot.py
   ```

## Usage

* **Start the Bot**: Send the `/start` command to the bot to initialize the conversation.
* **Chat with the Bot**: Send any text message to the bot, and it will respond using the generative AI model.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
