
import vk
import time
import random


token = "" # token vk (IPA)

print('///')
print('Working...')
print('By Envi_Despair.')
print('///')

quotes = ['А пакетик бесплатный?', 'Продал душу дьявола.', 'Таки кошерно.', 'Не буди во мне еврея.', 'Встретил цыганку, осталась должна.', 'А помнишь, у меня на жилетке была маленькая золотая цепочка?', 'Мои любимые конфеты? Чужие.', 'Хотел отправить с конвертом деньги, но, прости, уже запечатал.', 'Шекель в радость, чефир в сладость.']
genres = ['метал', 'гитара', 'классика', 'пианино', 'рок', 'рэп', 'народная', 'традиционная']
session = vk.Session(token)
#  session = vk.AuthSession(app_id='5637513', user_login='+79281502588', user_password='fatfadedfuckface', scope='messages,friends,audio')
api = vk.API(session)

while (True):
    try:
        messages = api.messages.get()
        messages = [(m['uid'], m['mid'], m['body'])
                    for m in messages[1:] if m['read_state'] == 0]

        for m in messages:
            user_id = m[0]
            messages_id = m[1]
            command = m[2]
            audios = api.audio.search(q='хава нагила ' + str(command), auto_complete=0, lyrisc=0, performer_only=0,
                                      search_own=0, count=2)
            if str(audios)=='[0]':
                api.messages.send(user_id=user_id,
                                  message=random.choice(quotes) + ' /// Прости, равви, но я таки не слышал такого. Попробуй другое, может "' + random.choice(genres) + '"?')
                break
            mediaId = audios[1]['aid']
            ownerId = audios[1]['owner_id']
            api.messages.send(user_id=user_id, attachment='audio' + str(ownerId) + '_' + str(mediaId))

        ids = ', '.join([str(m[1]) for m in messages])

        if ids:
            api.messages.markAsRead(message_ids=ids)

        time.sleep(3)

    except:
        api.messages.send(user_id=user_id, message=random.choice(quotes) + ' Прости, равви, но я такого еще не встречал.')
        pass
