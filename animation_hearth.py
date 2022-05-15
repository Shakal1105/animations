from pyrogram import Client, filters
import random
from time import sleep

class Automess():
    def __init__(self):
        
        self.api_id = 9958356
        self.api_hash = "8895b2a2b674f00658660440ef8adcbb"
        # Конфиг
        self.prefix = ["+", "-", "^-^"]

        self.start = True

        self.app()

        ################################################################3

    def app(self):
        user = Client('Automessage', self.api_id, self.api_hash)

        user.start()

        user.stop()

        print('@Shakal11052002 is working...')
        
        @user.on_message(filters.command('hearth'.lower(), prefixes=self.prefix) & filters.me)
        def serdesko(user, message):
        	self.start= True
        	message_id = message.message_id
        	user.edit_message_text(message.chat.id, message_id=message_id, text="♥️♥️♥️♥️♥️\n                   ♥️\n                   ♥️\n♥️♥️♥️♥️♥️\n                   ♥️\n                   ♥️\n                   ♥️\n♥️♥️♥️♥️♥️")
        	sleep(1)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="🧡🧡🧡🧡🧡\n                   🧡\n                   🧡\n🧡🧡🧡🧡🧡\n🧡\n🧡\n🧡🧡🧡🧡🧡")
        	sleep(1)
        	user.edit_message_text(message.chat.id, message_id=message_id, text="⁡‌᠎        💚💚\n         💚💚\n         💚💚\n         💚💚\n         💚💚\n         💚💚\n         💚💚")
        	while self.start:
        		sleep(1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text=" ⁢‌⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n\n             ❤️")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n\n                🧡\n           🧡❤️🧡\n                🧡")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                  💛\n             💛🧡💛\n        💛🧡❤️🧡💛\n             💛🧡💛\n                  💛")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                 💚\n            💚💛💚\n       💚💛🧡💛💚\n  💚💛🧡❤️🧡💛💚\n       💚💛🧡💛💚\n            💚💛💚\n                 💚")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                    💙\n               💙💚💙\n          💙💚💛💚💙\n     💙💚💛🧡💛💚💙\n💙💚💛🧡❤️🧡💛💚💙\n     💙💚💛🧡💛💚💙\n          💙💚💛💚💙\n               💙💚💙\n                    💙")
        		sleep(0.5)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢⁡⁢⁢﻿⁠⁢⁣᠎⁢﻿⁢⁢⁣᠎⁢﻿⁣\n                         💜\n                    💜💙💜\n               💜💙💚💙💜\n          💜💙💚💛💚💙💜\n     💜💙💚💛🧡💛💚💙💜\n💜💙💚💛🧡❤️🧡💛💚💙💜\n     💜💙💚💛🧡💛💚💙💜\n          💜💙💚💛💚💙💜\n               💜💙💚💙💜\n                    💜💙💜\n                         💜")
        		sleep(1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Ми")
        		sleep(0.2)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВ")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ с")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ соз")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ созда")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ создан.")
        		sleep(1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ созда")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ соз")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️БВИ")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Мир ЛІ♥️")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="Ми")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢ ⁢‌⁢")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢Ти")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢Ти чудо")
        		sleep(0.1)
        		user.edit_message_text(message.chat.id, message_id=message_id, text="⁢‌⁢ ⁢‌⁢Ти чудова(ий)")
        		sleep(3)
        		user.edit_message_text(message.chat.id, message_id=message_id, text='hearth')
        		self.start=False
        		break

        @user.on_message(filters.text & filters.private)
        def otvet_private(user, message):
            if message.text == 'stop':
            	self.start = False

        user.run()

if __name__ == "__main__":
    Automess()