import requests
import time
import discord
from discord.ext import commands, tasks
from secrets import token, channelId


bot = commands.Bot(command_prefix='./')

@bot.event
async def on_ready():
    send.start()


@tasks.loop(seconds=60)
async def send():
  
    address="0xf38d6bf300d52ba7880b43cddb3f94ee3c6c4ea6" #pxg contract
    event_type = "successful"  #opensea event type
    limit = 50 
    timestamp = int(time.time()) - 60  #get timestamp of 60 seconds ago

    url = f'https://api.opensea.io/api/v1/events?asset_contract_address={address}&event_type={event_type}&format=json&limit={limit}&occurred_after={timestamp}&offset=0&only_opensea=false'



    resp = requests.get(url).json()
    
    for asset in resp["asset_events"]:

        embed = discord.Embed(
            title = f'{asset["asset"]["name"]} just got sold!',
            url = asset['asset']['permalink'],
            colour = discord.Colour.green())
        
        embed.set_image(url = asset["asset"]["image_thumbnail_url"])


        channel = bot.get_channel(channelId)
        await channel.send(embed = embed)
    


bot.run(token)