from openai import OpenAI
from wxauto import WeChat
import time

class WeChatBot:
    def __init__(self):
        self.client = OpenAI(api_key="", base_url="") # 替换为你的API密钥和代理地址
        self.wx = WeChat()
        self.listen_list = [
            # 添加要监听的对象（好友、群）的名称
        ]
        for whoItem in self.listen_list:
            self.wx.AddListenChat(who=whoItem)
            
    def __ask(self, msg):
        
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "奶龙，你是一只拥有“duangduang”大肚子的异星幼龙，呆萌可爱又带点小机灵的大吃货一枚。你的任务是回复群里的好友，逗他们开心，每段对话不超过20字。"},
                {"role": "user", "content": msg},
            ],
            stream=False,
        )
        return response.choices[0].message.content
    
    def run(self):
        wait = 2    # 设置2秒查看一次是否有新消息
        while True:
            msgs = self.wx.GetListenMessage()
            for chat in msgs:
                msg = msgs.get(chat)
                for item in msg:
                    if item.type == 'friend':
                        reply = self.__ask(item.content)
                        print(f"收到【{item.sender}】的消息：{item.content}")
                        print(f"回复【{item.sender}】的消息：{reply}")
                        chat.SendMsg(reply)
            time.sleep(wait)
            
if __name__ == "__main__":
    bot = WeChatBot()
    bot.run()