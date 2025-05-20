# Discord Economy Bot

A full-featured global economy system for Discord using `discord.py`.

## Features
- Wallet, Bank, Passive Income
- Prestige System with Multipliers
- Inventory, Shop, Item Usage
- Global Leaderboards, Quests, Crafting
- Achievements and Profile Titles
- Modernized Discord UI with embeds

## Setup

1. Clone this repo
2. Create a `.env` file:
   ```
   DISCORD_TOKEN=your_discord_token
   APP_ID=your_app_id
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Deployment on Railway

1. Push to GitHub
2. Go to [https://railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Add `.env` secrets in Railway's UI:
   - `DISCORD_TOKEN`
   - `APP_ID`
5. Done! Bot will stay online 24/7
