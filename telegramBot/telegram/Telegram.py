from .configs import URL
from ..models import Post
import json
import requests
import random
from urllib.parse import quote
import time
class TelegramBot:
    def __init__(self,content):
        self.url=URL
        self.content=content['message']
        self.first_name = self.content['from']['first_name']
        if 'last_name' in self.content['from']:
            self.last_name = self.content['from']['last_name']
        else:
            self.last_name=''
        self.text= self.content['text']
        self.chat_id=self.content['chat']['id']
    

    def send_message(self,text):
        print()
        print()
        print()
        x=URL + f'sendMessage?chat_id={self.chat_id}&text={quote(text)}'
        print(x)
        print()
        print()

        res = requests.get(x)

        print(res)
        print()
        time.sleep(0.5)
        return True if res.status_code==200 else False
    
    def make_text(self,obj):
        return f"""
            {obj.first_name} {obj.last_name} میگه:
            {obj.body}
        """

    def action(self):
        if self.text == '/شروع':
            ans = """
                متن دلخواهت رو بنویس یا با دستور /بخون به شکل تصادفی ۵ تا از متن هایی که بقیه نوشتن رو بخون.
            """
            return self.send_message(ans)
        elif self.text == '/بخون':
            objs = Post.objects.all()
            if len(objs)>5:
                r = [random.randint(0,len(objs)-1) for _ in range(5)]
                for i in r:
                    t = self.make_text(objs[i])
                    self.send_message(t)
            else:
                for i in objs:
                    t = self.make_text(i)
                    self.send_message(t)
            return True
        else:
            p = Post(first_name=self.first_name,
            last_name=self.last_name,body=self.text)
            p.save()
            ans = 'ممنون که پست گذاشتی!'
            self.send_message(ans)
            return True



