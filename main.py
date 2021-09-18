import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['BOT-TOKEN']
DISABLEAMIIBOID = os.environ['DISABLE-AMIIBO-ID']
ENABLEAMIIBOID = os.environ.get('ENABLE-AMIIBO-ID', None)
APIKEY = os.environ['AMIIBOTS-API-KEY']
USERID = os.environ['USER-ID']
USER = os.environ['TWITCH-USERNAME']
PINGCHANNEL = int(os.environ['PING-CHANNEL-ID'])
SHOUTBOXID = int(os.environ['SHOUTBOX-ID'])
RATINGORMATCHES = os.environ.get('RATING-OR-MATCHES', None)

BASE_URL = 'https://www.amiibots.com/api/amiibo/'
OLD_AMIIBO_URL = BASE_URL+DISABLEAMIIBOID
NEW_AMIIBO_URL = BASE_URL+ENABLEAMIIBOID
if 'Bearer' in APIKEY: 
    HEADERS = {'Authorization': APIKEY}
else:
    HEADERS = {'Authorization': f'Bearer {APIKEY}'}
MATCH_TURN_OFF_NUMBERS = [30, 50, 100, 150]
amiibo_data_name = requests.get(OLD_AMIIBO_URL, headers=HEADERS)
amiiboname = amiibo_data_name.json()['data']['name']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        activity = discord.Game(name=f'Pinging {USER} when their amiibo finish their amiibots run!')
        await client.change_presence(status=discord.Status.idle, activity=activity)
    async def on_message(self, message):
        if message.author == client.user:
            return
        if (USERID in message.content or USER in message.content) and amiiboname in message.content and message.channel.id == SHOUTBOXID and (RATING-OR-MATCHES = 'Matches' or None):
            amiibo_data = requests.get(OLD_AMIIBO_URL, headers=HEADERS)
            amiibo = amiibo_data.json()['data']
            if amiibo['total_matches'] + 1 in MATCH_TURN_OFF_NUMBERS:
                disablepayload = {'is_active': False}
                disabled_amiibo = requests.put(OLD_AMIIBO_URL, headers=HEADERS, json=disablepayload)
                message_send_channel = client.get_channel(PINGCHANNEL)
                await message_send_channel.send(f"<@{USERID}> Your amiibo, {amiibo['name']}, finished its run with {amiibo['total_matches'] + 1} matches!")
                if ENABLEAMIIBOID is not None:
                    enablepayload = {'is_active': True}
                    enableamiibo = requests.put(NEW_AMIIBO_URL, headers=HEADERS, json=enablepayload)
            if ENABLEAMIIBOID is not None and RATING-OR-MATCHES = 'Rating':
                newamiibo = requests.get(NEW_AMIIBO_URL, headers=HEADERS)
                oldamiibo = requests.get(OLD_AMIIBO_URL, headers=HEADERS)
                if oldamiibo.json()['data']['rating'] <= newamiibo.json()['data']['rating']:
                   disablepayload = {'is_active': False}
                   enablepayload = {'is_active': True}
                   disableoldamiibo =  requests.put(OLD_AMIIBO_URL, headers=HEADERS, json=disablepayload)
                   enablenewamiibo = requests.put(NEW_AMIIBO_URL, headers=HEADERS, json=enablepayload)
                   message_send_channel.send(f"<@{USERID}> your amiibo have swithed due to rating changes"

client = MyClient()
client.run(TOKEN)
