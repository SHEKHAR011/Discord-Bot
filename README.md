# Discord Bot Project

This project is a Discord bot written in Python that integrates with three APIs to provide conversational AI responses(Gemini), real-time weather updates, and currency conversions.

## Features

- **AI Conversations**: Engage in conversations with the bot using responses powered by the Gemini API.
- **Weather Updates**: Get real-time weather updates by entering the name of a city.
- **Currency Conversion**: Convert amounts between different currencies using live exchange rates.

## Commands

### AI Chat
- **Description**: The bot responds to general prompts using the Gemini API.
- **Usage**: Simply type your message, and the bot will reply.

### Weather
- **Description**: Fetches current weather details for a specified city.
- **Usage**: `!weather <city>`
- **Example**: `!weather London`

### Currency Conversion
- **Description**: Converts an amount from one currency to another.
- **Usage**: `!convert <amount> <from_currency> <to_currency>`
- **Example**: `!convert 100 USD EUR`


## Getting Started

1. **API Keys**:
    - Create a `.env` file in the root directory and add the following keys:
      ```
      DISCORD_TOKEN=your_discord_token
      GEMINI_API_KEY=your_gemini_api_key
      WEATHER_API_KEY=your_weather_api_key
      CURRENCY_API_KEY=your_currency_api_key
      ```

2. **Run the Bot**:
    ```bash
    python bot.py
    ```

## Project Structure

- **bot.py**: Main entry point for the bot.
- **.env**: Holds API keys and configuration variables.

  ##  libraries need to be install
  
  pip install discord.py
  pip install requests
  pip install google-generativeai
  pip install python-dotenv
  pip install pycopy-audioop



  
