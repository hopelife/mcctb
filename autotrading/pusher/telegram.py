import os
import configparser
import time
from autotrading.pusher.base_pusher import Pusher
from telethon import TelegramClient
# from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

class PushTelegram(Pusher):

    def __init__(self):
        """텔레그램으로 메시지를 보내기 위한 PushTelegram 클래스입니다.
        config.ini파일로 부터 api_id와 api_hash를 읽어옵니다. 
        """
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../conf/config.ini")))
        self.api_id = config['TELEGRAM']['api_id']
        self.api_hash = config['TELEGRAM']['api_hash']
        # string = '1196837536:AAFGN_iZmULxlVqr-PvzvqkSHTfJgu4NT20'
        # self.api_session = StringSession(string)

    # def send_message(self, sessionname='1', username=None, message=None):
    #     """
    #     Args:
    #         username(str): 보낼 유저명
    #         message(str): 보낼 메시지
    #     """
    #     with TelegramClient(sessionname, self.api_id, self.api_hash) as client:
    #         client.send_message(username, message)
    #         # print(client.download_profile_photo('moon_dev_bot'))

    #         # @client.on(events.NewMessage(pattern='(?i).*Hello'))
    #         # async def handler(event):
    #         #    await event.reply('Hey!')

    #     client.run_until_disconnected()


    def send_message(self, sessionname='1', username=None, message=None):
        """
        Args:
            username(str): 보낼 유저명
            message(str): 보낼 메시지
        """
        async def send():
            # async with TelegramClient(self.api_session, self.api_id, self.api_hash) as client:
            async with TelegramClient('+8201082422032', self.api_id, self.api_hash) as client:
                await client.send_message(username, message)
                #    print(await client.download_profile_photo('moon_dev_bot'))

                #    @client.on(events.NewMessage(pattern='(?i).*Hello'))
                #    async def handler(event):
                #        await event.reply('Hey!')

                await client.run_until_disconnected()

        # Otherwise
        asyncio.run(send())