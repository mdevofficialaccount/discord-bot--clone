import discord 
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asyncio

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

botstatus = cycle(["command activate = !", "join https://discord.gg/sg4Qwgun if you need help","or type !hlp", "made by= theholyhuub"])
            
@tasks.loop(seconds=5)
async def changestatus():
    await client.change_presence(activity=discord.Game(next(botstatus)))

@client.event
async def on_ready():
    print("*beep* *beep* *beep*")
    print("Ready and running")
    changestatus.start()

@client.command()
async def ping(ctx):
    bot_latency = round(client.latency * 1000) 
    await ctx.send(f"pong! {bot_latency} ms.")

@client.command()
async def pong(ctx):
    while True:
        await ctx.author.send("pong!")

@client.command()
async def sigma(ctx):
    await ctx.send("balz")

@client.command()
async def hlp(ctx):
    embed_message = discord.Embed(title="HELP", description="Here are some commands", color=discord.Color.random())
    embed_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
    embed_message.set_thumbnail(url=ctx.guild.icon)
    embed_message.set_image(url="https://murraywoodswimandracquetclub.org/wp-content/uploads/2014/05/help.jpg")
    embed_message.add_field(name="Command list:", value="!ping to see the ping of the bot. !pong lets you spam yourself! and !deez for a meme:) ", inline=False)
    embed_message.set_footer(text="Ask if something does not work!", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed_message)

@client.command()
async def deez(ctx):
    embed_message = discord.Embed(title="NUTS", description="Good taste man", color=discord.Color.random())
    embed_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
    embed_message.set_thumbnail(url=ctx.guild.icon)
    embed_message.set_image(url="https://www.tubefilter.com/wp-content/uploads/2023/02/mr-beast-deez-nuts.jpg")
    embed_message.add_field(name="Times this command was used:", value="69,420,69", inline=False)
    embed_message.set_footer(text="Jimi says deeznuts", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed_message)

@client.command()
async def clear(ctx, count: int):
    await ctx.channel.purge(limit=count)
    await ctx.send(f"{count} message(s) deleted!")

@client.command()
async def kick(ctx, member: discord.Member, *, modreason):
    await ctx.guild.kick(member)
    kick_embed = discord.Embed(title="Success!", color=discord.Color.green())
    kick_embed.add_field(name="Kicked:", value=f"{member.mention} by {ctx.author.mention}.", inline=False)
    kick_embed.add_field(name="Reason:", value=modreason, inline=False)
    await ctx.send(embed=kick_embed)

@client.command()
async def ban(ctx, member: discord.Member, *, modreason):
    await ctx.guild.ban(member)
    ban_embed = discord.Embed(title="Success!", color=discord.Color.green())
    ban_embed.add_field(name="Banned:", value=f"{member.mention} by {ctx.author.mention}.", inline=False)
    ban_embed.add_field(name="Reason:", value=modreason, inline=False)
    await ctx.send(embed=ban_embed)

@client.command()
async def lockdown(ctx):
    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send("You don't have permission to do this!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send("🔒 This channel has been locked!")

@client.command()
async def unlock(ctx):
    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send("You don't have permission to do this!")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            await ctx.channel.set_permissions(role, overwrite=overwrite)
    await ctx.send("🔓 This channel has been unlocked!")

@client.command()
async def shutdown(ctx):
    shutdown_embed = discord.Embed(title="Success!", color=discord.Color.green())
    shutdown_embed.add_field(name="Shutting down the bot!", value=f"Shut down by {ctx.author.mention}.", inline=False)
    await ctx.send(embed=shutdown_embed)
    await client.close()

client.run("put your own webhook here!")
