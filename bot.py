import discord
from discord.ext import commands
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


genai.configure(api_key=GENAI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"User asked Gemini: {message.content}")

    await message.channel.send("Thinking...")

    try:

        response = model.generate_content(message.content)

        chat_response = response.text

        print(f"Gemini responded: {chat_response}")

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

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
