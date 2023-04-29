import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

TOKEN = "TOKEN"
GROUP_ID = GROUP_ID
WEEKDAYS = ("Понедельник", "Вторник", "Среда", "Четверг",
            "Пятница", "Суббота", "Воскресенье")


def main():
    vk_session = vk_api.VkApi(token=TOKEN)

    longpollVK = VkBotLongPoll(vk_session, GROUP_ID)
    for event in longpollVK.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            msg_text = event.obj.message["text"]
            usr_id = event.obj.message["from_id"]
            vk = vk_session.get_api()
            if any(map(lambda word: word in msg_text.lower(), ("время", "число", "дата", "день"))):
                dt = datetime.datetime.now()
                msg = f"Сейчас {dt.hour}:{dt.minute}:{dt.second}, {dt.day}.{dt.month}.{dt.year}, {WEEKDAYS[dt.weekday()]}"
                vk.messages.send(user_id=usr_id, message=msg,
                                 random_id=random.randint(0, 2 ** 64))
            else:
                msg = "Вы можете узнать текущие дату и время, для этого в Вашем сообщении должно быть одно из слов: время, дата, число, день"
                vk.messages.send(user_id=usr_id, message=msg, random_id=random.randint(0, 2 ** 64))


if __name__ == "__main__":
    main()
