import discord
from discord_slash import SlashCommand
import keep_alive
import os

bot_token = os.environ['bot_token']
client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print("Conected to ArcherBot!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the RetroArcher server"))

    

# Commands
@slash.slash(name="metadata", description="metadata",)
async def _ping(ctx): 
    await ctx.send(f"https://github.com/RetroArcher/RetroArcher.bundle/wiki/Metadata")


@slash.slash(name="videos", description="videos",)
async def _ping(ctx): 
    await ctx.send(f"Under Construction")


@slash.slash(name="roms", description="roms",)
async def _ping(ctx): 
    await ctx.send(f"https://github.com/RetroArcher/RetroArcher.bundle/wiki/Scanning-Games-and-Roms")


@slash.slash(name="python", description="python",)
async def _ping(ctx): 
    await ctx.send(f"Under Construction")


@slash.slash(name="github", description="github",)
async def _ping(ctx): 
    await ctx.send(f"https://github.com/RetroArcher")


@slash.slash(name="donate", description="donate",)
async def _ping(ctx): 
        embedVar = discord.Embed(title="Donate", color=0xE5A00D)
        embedVar.add_field(name="Github", value="[Link](https://github.com/sponsors/ReenigneArcher)", inline=False)
        embedVar.add_field(name="Patreon", value="[Link](https://www.patreon.com/ReenigneArcher?fan_landing=true)", inline=False)
        embedVar.add_field(name="Paypal", value="[Link](https://paypal.me/ReenigneArcher)", inline=False)
        await ctx.send(embed=embedVar)


# Start the server
keep_alive.keep_alive()

# Login the bot
client.run(bot_token)