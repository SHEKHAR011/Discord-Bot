import discord
from discord.ext import commands
import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API keys
GENAI_API_KEY = os.getenv("GENAI_API_KEY")  # Set this in your .env file
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Set this in your .env file
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")  # Set this in your .env file
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



# Weather command
@bot.command()
async def weather(ctx, *, city: str):

    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data['cod'] != 200:
        await ctx.send(f"Could not find weather for {city}.")
        return

    main = data['main']
    weather_desc = data['weather'][0]['description']
    temperature = main['temp']
    
    await ctx.send(f"Weather in {city}: {temperature}°C, {weather_desc.capitalize()}")






@bot.command(name='convert')
async def convert(ctx, amount: float, from_currency: str, to_currency: str):
    try:
        # Build URL with the API key and base currency
        url = f"https://v6.exchangerate-api.com/v6/{(EXCHANGE_RATE_API_KEY)}/latest/{from_currency.upper()}"
        
        response = requests.get(url)
        
        if response.status_code != 200:
            await ctx.send("Currency not supported or invalid.")
            return

        data = response.json()
        if 'conversion_rates' not in data or to_currency.upper() not in data['conversion_rates']:
            await ctx.send("Target currency not supported or invalid.")
            return

        # Get conversion rate and calculate
        rate = data['conversion_rates'][to_currency.upper()]
        converted_amount = amount * rate
        await ctx.send(f"{amount} {from_currency.upper()} is equal to {converted_amount:.2f} {to_currency.upper()}.")
        
    except Exception as e:
        await ctx.send("There was an error processing your request. Please try again later.")




# Chat bot functionality
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # If the message content is related to weather or convert, skip processing
    if message.content.startswith("!weather") or message.content.startswith("!convert"):
        # Process the command without generating additional output
        await bot.process_commands(message)
        return

    # Print the user's message to the terminal (for tracking Gemini inputs)
    print(f"User asked Gemini: {message.content}")
    
    await message.channel.send("Thinking...")

    try:
        # Generate a response using the Generative AI model
        response = model.generate_content(message.content)
        
        # Extract the generated text
        chat_response = response.text

        # Split the text into chunks if it's too long
        max_length = 2000
        if len(chat_response) > max_length:
            chunks = [chat_response[i:i + max_length] for i in range(0, len(chat_response), max_length)]
            for chunk in chunks:
                await message.channel.send(chunk)
        else:
            await message.channel.send(chat_response)
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")

    await bot.process_commands(message)  # Process other commands



# Run the bot with your token
bot.run(DISCORD_TOKEN)  # Replace with your actual Discord bot token
