import discord
from discord.ext import commands
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API keys
GENAI_API_KEY = os.getenv("GENAI_API_KEY")  # Set this in your .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # Set this in your .env file

# Configure the API key directly
genai.configure(api_key=GENAI_API_KEY)

# Create a model instance for Gemini
model = genai.GenerativeModel("gemini-1.5-flash")

# Set up the bot with intents
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Chat bot functionality
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Print the user's message to the terminal (for tracking Gemini inputs)
    print(f"User asked Gemini: {message.content}")

    await message.channel.send("Thinking...")

    try:
        # Generate a response using the Generative AI model
        response = model.generate_content(message.content)

        # Extract the generated text
        chat_response = response.text

        # Log the response to the terminal
        print(f"Gemini responded: {chat_response}")

        # Split the text into chunks if it's too long
        max_length = 2000
        if len(chat_response) > max_length:
            chunks = [
                chat_response[i : i + max_length]
                for i in range(0, len(chat_response), max_length)
            ]
            for chunk in chunks:
                await message.channel.send(chunk)
        else:
            await message.channel.send(chat_response)
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")

    await bot.process_commands(message)  # Process other commands

# Run the bot with your token
bot.run(DISCORD_TOKEN)  # Replace with your actual Discord bot token
