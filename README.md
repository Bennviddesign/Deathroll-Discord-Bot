# Discord Deathroll Bot

A simple and interactive Discord bot that enables users to challenge each other in the game of Deathroll. Players take turns rolling a dice, with the maximum roll decreasing each time, until someone rolls a 1 and loses. Includes easy setup, bot token management, and customizable permissions.

## Prerequisites

Before setting up the bot, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (latest version recommended)
- A code editor (e.g., [VS Code](https://code.visualstudio.com/))

## Installation

Follow these steps to set up and run the bot:

1. **Clone or download the repository**
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Install dependencies**
   ```sh
   pip install discord.py python-dotenv
   ```
3. **Create a **`.env`** file in the root directory**
   - This file will store your bot token securely.

## Setting Up a Discord Bot

1. **Create a Discord bot account:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name.
2. **Configure OAuth2 settings:**
   - Navigate to "OAuth2" → "OAuth2 URL Generator".
   - Select "bot" under "Scopes".
   - Scroll down to "Bot Permissions" and choose necessary permissions (e.g., "Send Messages", "Manage Messages", "Read Message History").
   - Copy the generated URL and save it. This will be used to invite the bot to your server.
3. **Retrieve and store the bot token:**
   - Go to "Bot" → "Token" and click "Reset Token".
   - Copy the new token and store it in the `.env` file as follows:
     ```env
     DISCORD_BOT_TOKEN=your_token_here
     ```

## Running the Bot

To start the bot, execute:

```sh
python main.py
```

## How to Play

1. Challenge another user by typing:
   ```
   !deathroll <username>
   ```
2. Start rolling with:
   ```
   !roll <number>
   ```

Enjoy playing Deathroll with your friends on Discord!
