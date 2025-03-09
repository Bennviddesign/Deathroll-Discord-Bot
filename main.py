# Discord Deathroll Bot
# Created by Bennviddesign
# GitHub Repo: https://github.com/Bennviddesign/Deathroll-Discord-Bot
# Author GitHub: https://github.com/Bennviddesign
# License: MIT

import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()

# Create intents
intents = discord.Intents.default()
intents.message_content = True  # Enable intents to read message content

# Create the bot with a prefix (e.g., "!")
bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to keep track of the game's status for each server
games = {}

@bot.event
async def on_ready():
    print(f"The bot is online as {bot.user}")

@bot.command(name="deathroll")
async def startdeathroll(ctx, opponent: discord.Member):
    """Starts a death roll between two players."""
    if opponent == ctx.author:
        await ctx.send("You cannot play against yourself!")
        return

    server_id = ctx.guild.id
    games[server_id] = {
        "game_active": True,
        "max_roll": 1000,
        "current_player": ctx.author,
        "other_player": opponent
    }

    await ctx.send(f"Death Roll begins between {ctx.author.mention} and {opponent.mention}! First roll: 1-1000")

@bot.command(name="roll")
async def deathroll(ctx, roll_value: int):
    """Rolls a number between 1 and the specified value."""
    server_id = ctx.guild.id

    if server_id not in games or not games[server_id]["game_active"]:
        await ctx.send("No active Death Roll game. Start a new game with !deathroll.")
        return

    game = games[server_id]

    if ctx.author != game["current_player"]:
        await ctx.send(f"It's not your turn! It's {game['current_player'].mention}'s turn.")
        return

    if roll_value != game["max_roll"]:
        await ctx.send(f"You must roll with the max value {game['max_roll']}.")
        return

    roll = random.randint(1, game["max_roll"])
    await ctx.send(f"{game['current_player'].mention} rolls: **{roll}** (1-{game['max_roll']})")

    if roll == 1:
        await ctx.send(f"{game['current_player'].mention} rolled 1 and loses! {game['other_player'].mention} wins!")
        game["game_active"] = False
    else:
        game["max_roll"] = roll
        game["current_player"], game["other_player"] = game["other_player"], game["current_player"]
        await ctx.send(f"Now it's {game['current_player'].mention}'s turn to roll! Use the command !roll {game['max_roll']}")

# Retrieve your bot's token from the Discord Developer Portal from the .env file
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
