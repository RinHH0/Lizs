import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkApi

session = VkApi(token="vk1.a.BEe8pDf5L8-0Iohwnr3VD2RZRtjRpxYJkLtN2ELCp91cx8XzBGNQWdNbAa8ugjdHpo2vYly7fVxvcpsX56NQ_teiSPlMX9d-n3ftp5F3YTFNHf7t1rMm5W564pdTUHKub3IDCP1jYcC4LbnZ-eYSRODWoBxg-4N5wT-rf6ZdXE3bYDiDv80PJBcX5qbHqZP2lThJrcuXwYS0waDlOJzklg")
session_api = session.get_api()
longpoll = VkLongPoll(session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f"Сообщение пришло в: {str(datetime.now())}")
            print(f"Текст сообщения: {str(event.text)}")
            responce = event.text.lower()
            if event.from_user and not event.from_me:
                if responce.find('Привет')>= 0 or responce.find('Здравствуй') >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет!",
                            "random_id": 0,
                        },
                    )
                elif responce.find('как дела')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Хорошо",
                            "random_id": 0,
                        },
                    )

                elif responce.find('пока')>= 0 or responce.find('до свидания') >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "До свидания",
                            "random_id": 0,
                        },
                    )
                    
                elif responce.find('как дела')>= 0 or responce.find('мне грустно') >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "sticker_id": 73059,
                            "random_id": 0,
                        },
                    )

                elif responce.find('собака')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "photo-201636725_457269365",
                            "random_id": 0,
                        },
                    )
                
                elif responce.find('фото')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "photo-208320358_457295906",
                            "random_id": 0,
                        },
                    )

                elif responce.find('видео')>= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "rb_clickid=165534569-1723107730-1731449615",
                            "random_id": 0,
                        },
                    )


