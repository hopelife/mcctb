import configparser
import time
from autotrading.pusher.base_pusher import Pusher
from telethon import TelegramClient

class PushTelegram(Pusher):

    def __init__(self):
        """텔레그램으로 메시지를 보내기 위한 PushTelegram 클래스입니다.
        config.ini파일로 부터 api_id와 api_hash를 읽어옵니다. 
        TelegramClient 생성시 app name과 api_id, api_hash를 파라미터로 전달합니다.
        """
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        api_id = config['TELEGRAM']['api_id']
        api_hash = config['TELEGRAM']['api_hash']
        print(api_id)
        print(api_hash)
        #self.telegram = TelegramClient("auto-trading", api_id, api_hash)
        # self.telegram = TelegramClient("CryptoCurrency Trading Bot", api_id, api_hash)
        self.telegram = TelegramClient("MCCTB", api_id, api_hash)
        time.sleep(5)
        assert self.telegram
        self.telegram.connect()
        
    def send_message(self, username=None, message=None):
        """
        Args:
            username(str): 보낼 유저명
            message(str): 보낼 메시지
        """
        self.telegram.send_message(username, message)


# async with TelegramClient(session_name, api_id, api_hash) as client:
#    await client.send_message('me', 'Hello, myself!')
#    print(await client.download_profile_photo('me'))

#    @client.on(events.NewMessage(pattern='(?i).*Hello'))
#    async def handler(event):
#       await event.reply('Hey!')

#    #await client.run_until_disconnected()
