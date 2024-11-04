# Discord Bot with Gemini API Integration

## Overview
This project is a powerful and customizable Discord bot built using Python. It integrates with the Gemini API to provide conversational AI features directly within Discord servers. The bot is designed for versatility and ease of use, making it a valuable addition to any server looking for smart automation, real-time interactions, and enhanced user engagement.

## Features
- **Conversational AI Integration**: Utilizes the Gemini API for natural, context-aware interactions.
- **Commandless Input Support**: Users can chat naturally without needing command prefixes for certain actions.
- **Customizable Functionality**: Easily extend or modify features for tailored user experiences.
- **Modular Code Structure**: Commands and API interactions are organized for maintainability and scalability.
- **Environment Variable Management**: Secure storage of API keys and other sensitive information using `.env` files.

## Getting Started

1. **API Keys**:
    - Create a `.env` file in the root directory and add the following keys:
      ```
      DISCORD_TOKEN=your_discord_token
      GEMINI_API_KEY=your_gemini_api_key
      ```

2. **Run the Bot**:
    ```bash
    python bot.py
    ```

## Project Structure

- **bot.py**: Main entry point for the bot.
- **.env**: Holds API keys and configuration variables.

##  libraries need to be install

  - pip install discord.py
  - pip install requests
  - pip install google-generativeai
  - pip install python-dotenv
