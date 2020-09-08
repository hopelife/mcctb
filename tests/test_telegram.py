from telethon.sync import TelegramClient, events

api_id = 1342041
api_hash = '8ed6c7c08f31ba7dd4f6c76baf0ec5b2'

with TelegramClient('name', api_id, api_hash) as client:
   client.send_message('moon_dev_bot', 'Hello, myself!!!!')
   # print(client.download_profile_photo('moon_dev_bot'))

   # @client.on(events.NewMessage(pattern='(?i).*Hello'))
   # async def handler(event):
   #    await event.reply('Hey!')

   client.run_until_disconnected()

# import asyncio
# from telethon import TelegramClient, events

# session_name = 'MCCTB'
# api_id = 1342041
# api_hash = '8ed6c7c08f31ba7dd4f6c76baf0ec5b2'

# async def main():
#     async with TelegramClient(session_name, api_id, api_hash) as client:
#        await client.send_message('moon_dev_bot', 'Hello, myself!')
#     #    print(await client.download_profile_photo('moon_dev_bot'))

#     #    @client.on(events.NewMessage(pattern='(?i).*Hello'))
#     #    async def handler(event):
#     #        await event.reply('Hey!')

#        await client.run_until_disconnected()

# # Otherwise
# asyncio.run(main())