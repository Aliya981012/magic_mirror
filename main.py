import telebot
from telebot import types
from time import sleep
token = '6557832075:AAHp968xIlrdi_iNvo0t8Uie-JTHmzBqKX0'

bot = telebot.TeleBot(token)



#СПИСОК ИНФОРМАЦИИ ПРО ЮЗЕРА
user_info = []
user_os = []

'''ПРЯМОУГОЛЬНИК'''

#СПИСОК КАРТИНОК
#джинсы
#на данный момент Slim Medium straight, Regular medium straight
jeans_images_rectangle_men_front = ['https://i.yapx.cc/XrJ5M.png', 'https://i.yapx.cc/XrJ5K.png']


jeans_images_rectangle_men_back = ['https://i.yapx.cc/XrVPC.png','https://i.yapx.cc/XrN0r.png']


#СПИСОК КРАТКИХ ОПИСАНИЙ джинс
jeans_short_rectangle_men = ['Slim. Прилегающие, но в меру просторные брюки. Для людей с пропорциональной фигурой. Скрывают мелкие недостатки. Не подходят людям, склонным к полноте.',
                             'Regular. Классический прямой крой, чуть сужающийся книзу. Для мужчин с любой фигурой.']

'''КОНЕЦ ПРЯМОУГОЛЬНИКА'''
#


'''ТРЕУГОЛЬНИК'''
#СПИСОК КАРТИНОК
#джинсы
#на данный момент Regular MS, Loose MS, Relaxed MS

jeans_images_triangle_men_front = ['https://i.yapx.cc/XrJ5K.png','https://i.yapx.cc/XrWw4.png','https://i.yapx.cc/XrWw1.png']


jeans_images_triangle_men_back = ['https://i.yapx.cc/XrN0r.png','https://i.yapx.cc/XrWw2.png','https://i.yapx.cc/XrWwz.png']


#СПИСОК КРАТКИХ ОПИСАНИЙ джинс
jeans_short_triangle_men = ['Regular. Классический прямой крой, чуть сужающийся книзу. Для мужчин с любой фигурой.',
                            'Loose. Мешковатый фасон для полной свободы движения. Ткань практически не соприкасается с кожей. Не подходит полным людям и людям низкого роста.',
                            'Relaxed. Более свободная модель, чем классика. Не прилегают к телу. Хорошо подойдет рослым людям. Не рекомендуется для склонных к полноте.'
                            ]
'''КОНЕЦ ТРЕУГОЛЬНИКА'''



'''ТРАПЕЦИЯ'''
#СПИСОК КАРТИНОК
#джинсы
#на данный момент Slim MS, Regular MS, Relaxed MS

jeans_images_trap_men_front = ['https://i.yapx.cc/XrJ5M.png', 'https://i.yapx.cc/XrJ5K.png','https://i.yapx.cc/XrWw1.png']


jeans_images_trap_men_back = ['https://i.yapx.cc/XrVPC.png','https://i.yapx.cc/XrN0r.png','https://i.yapx.cc/XrWwz.png']


#СПИСОК КРАТКИХ ОПИСАНИЙ джинс
jeans_short_trap_men = ['Slim. Прилегающие, но в меру просторные брюки. Для людей с пропорциональной фигурой. Скрывают мелкие недостатки. Не подходят людям, склонным к полноте.',
                        'Regular. Классический прямой крой, чуть сужающийся книзу. Для мужчин с любой фигурой.',
                            'Relaxed. Более свободная модель, чем классика. Не прилегают к телу. Хорошо подойдет рослым людям. Не рекомендуется для склонных к полноте.']
'''КОНЕЦ ТРАПЕЦИИ'''

'''ОВАЛ'''
#СПИСОК КАРТИНОК
#джинсы
#на данный момент  Loose MS, Relaxed MS

jeans_images_ell_men_front = ['https://i.yapx.cc/XrWw4.png','https://i.yapx.cc/XrWw1.png']


jeans_images_ell_men_back = ['https://i.yapx.cc/XrWw2.png','https://i.yapx.cc/XrWwz.png']


#СПИСОК КРАТКИХ ОПИСАНИЙ джинс
jeans_short_ell_men = ['Loose. Мешковатый фасон для полной свободы движения. Ткань практически не соприкасается с кожей. Не подходит полным людям и людям низкого роста.',
                            'Relaxed. Более свободная модель, чем классика. Не прилегают к телу. Хорошо подойдет рослым людям. Не рекомендуется для склонных к полноте.'
                            ]
'''КОНЕЦ ОВАЛА'''


'''ПЕРЕВЕРНУТЫЙ ТРЕУГОЛЬНИК'''
#СПИСОК КАРТИНОК
#джинсы
#на данный момент Regular MS, Relaxed MS

jeans_images_revtri_men_front = ['https://i.yapx.cc/XrJ5K.png','https://i.yapx.cc/XrWw1.png']


jeans_images_revtri_men_back = ['https://i.yapx.cc/XrN0r.png','https://i.yapx.cc/XrWwz.png']


#СПИСОК КРАТКИХ ОПИСАНИЙ джинс
jeans_short_revtri_men = ['Regular. Классический прямой крой, чуть сужающийся книзу. Для мужчин с любой фигурой.',
                            'Relaxed. Более свободная модель, чем классика. Не прилегают к телу. Хорошо подойдет рослым людям. Не рекомендуется для склонных к полноте.'
                            ]
'''ПЕРЕВЕРНУТЫЙ ТРЕУГОЛЬНИК'''


#футболки ЛОНГСЛИВ_КРУГ, КЛАССИКА_КРУГЛЫЙ_ВЫРЕЗ,СВОБОДНЫЙ КРОЙ

shirts_images = ['https://i.yapx.cc/XrMAu.png', 'https://i.yapx.cc/XrMAy.png','https://i.yapx.cc/XrMAw.png']

shirt_images_longsleeve = ['https://i.yapx.cc/XrMAu.png', ]
#СПИСОК ОПИСАНИЙ ДЛЯ КАЖДЫХ ДЖИНС ПО ОТДЕЛЬНОСТИ
jeans_description_regular_medium_straight = ['Regular.Посадка Medium. Средняя посадка на уровне бедер или чуть выше. Покрой низа Straight. Популярный классический фасон с небольшим сужением может заменять кэжл брюки.',
                                             'С чем носить: клетчатые и однотонные рубашки, футболки, поло, блейзеры, вязаные кардиганы, пуловеры. Обувь:любая.']

jeans_description_slim_medium_straight = ['Slim. Посадка Medium. Средняя посадка на уровне бедер или чуть выше. Покрой низа Straight. Популярный классический фасон с небольшим сужением может заменять кэжл брюки',
                                     'С чем носить: короткие футболки, зауженные поло, рубашки классика, рубашки кэжл. Верхняя одежда: тренч, бомбер. Обувь: мокасины, кеды, кроссовки.']

jeans_description_relaxed_medium_straight = ['Relaxed.Посадка Medium. Средняя посадка на уровне бедер или чуть выше. Покрой низа Straight. Популярный классический фасон с небольшим сужением может заменять кэжл брюки.',
                                             'С чем носить: худи, свитшоты. Объемный верх. Обувь: ботинки на шнуровке, кеды, мокасины. ']

jeans_description_loose_medium_straight = ['Loose.Посадка Medium. Средняя посадка на уровне бедер или чуть выше. Покрой низа Straight. Популярный классический фасон с небольшим сужением может заменять кэжл брюки.',
                                             'С чем носить: просторные толстовки, джемперы оверсайз, мешковатые футболки. Верхняя одежда: бомбер, куртка оверсайз, тренч прямого кроя. Обувь: высокие кроссовки, высокие кеды.']


#СПИСОК КАРТИНОК ПО ОТДЕЛЬНОСТИ
#list  = #front, back
jeans_images_slim_medium_straight = ['https://i.yapx.cc/XrJ5M.png', 'https://i.yapx.cc/XrVPC.png']

jeans_images_regular_medium_straight = ['https://i.yapx.cc/XrJ5K.png','https://i.yapx.cc/XrN0r.png']

jeans_images_relaxed_medium_straight = ['https://i.yapx.cc/XrWw1.png', 'https://i.yapx.cc/XrWwz.png']

jeans_images_loose_medium_straight = ['https://i.yapx.cc/XrWw4.png','https://i.yapx.cc/XrWw2.png']

#СПИСОК КРАТКИХ ОПИСАНИЙ футболок
shirts_short = ['Лонгслив. Классическая универсальная футболка с длинным рукавом и круглым вырезом. Подходит всем.',
                'Классика. Универсальная футболка по фигуре с короткими рукавами и круглым вырезом. Не подходит полным людям в качестве одного слоя.',
                'Свободный крой. Футболка с коротким рукавом прямого кроя. Подходит для всех.']

shirts_description = ['Лонгслив. C чем носить: кардиган с круглым и треугольным вырезом, пиджак/блейзер, рубашки (tapered|regular fit), не застегивая, толстовка на молнии, джинсовая куртка, жилет.',
                      'Классика. C чем носить: кардиган с круглым и треугольным вырезом, пиджак/блейзер, рубашки (tapered|regular fit), не застегивая, толстовка на молнии, джинсовая куртка, жилет.',
                      'Свободный крой. C чем носить:рубашки (tapered|regular fit), не застегивая, толстовка на молнии, джинсовая куртка, жилет.']


#ОБРАБОТКА КОМАНД
@bot.message_handler(commands=['start'])
def starting(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('начать',callback_data='start'))
    bot.send_message(message.chat.id,text='Привет! Я Ваш виртуальный стилист. Я помогу Вам узнать, какие джинсы Вам подходят, основываясь на Ваших параметрах, а также подберу к ним верх, исходя из стилистических решений. Давайте начнем!',reply_markup=markup)

#обработка сообщений 
@bot.message_handler()
def any_message(message):
    if 'прив' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('начать',callback_data='start'))
        bot.send_message(message.chat.id,text='Привет! Я Ваш виртуальный стилист. Я помогу Вам узнать, какие джинсы Вам подходят, основываясь на Ваших параметрах, а также подберу к ним верх, исходя из стилистических решений. Давайте начнем!', reply_markup=markup)
    else:
        user_os.append(message.text)
        bot.send_message(message.chat.id,'Спасибо за Вашу обратную связь!')
        

#обработка любого контента
@bot.message_handler(content_types= ['photo', 'video','audio'])
def any_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('начать', callback_data='start'))
    bot.send_message(message.chat.id,text='Привет! Я Ваш виртуальный стилист. Я помогу Вам узнать, какие джинсы Вам подходят, основываясь на Ваших параметрах, а также подберу к ним верх, исходя из стилистических решений. Давайте начнем!', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)

#КНОПКА СТАРТ
def callback_handling(callback):
    if callback.data == 'start':
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('прямоугольник',callback_data='rectangle')
        btn2 = types.InlineKeyboardButton('треугольник',callback_data='tri')
        btn3 = types.InlineKeyboardButton('трапеция',callback_data='trap')
        btn4 = types.InlineKeyboardButton('овал',callback_data='ell')
        btn5 = types.InlineKeyboardButton('перевернутый треугольник',callback_data='rev_tri')
        m.row(btn1,btn2)
        m.row(btn3,btn4)
        m.row(btn5)
        bot.send_photo(callback.message.chat.id,'https://avatars.mds.yandex.net/i?id=01f706986ff02606e5ef7dd48ea5e767_l-5334658-images-thumbs&n=13')
        bot.send_message(callback.message.chat.id,'Выберите какой тип фигуры Вам больше подходит:',reply_markup=m)
        #КОНЕЦ
        
        
        
    #ОБРАБОТКА ТИПОВ ФИГУР
    #КНОПКА ПРЯМОУГОЛЬНИК 
    if callback.data == 'rectangle':
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('slim',callback_data='slim_medium_straight')
        btn2 = types.InlineKeyboardButton('regular',callback_data='regular_medium_straight')
        btn3 = types.InlineKeyboardButton('вернуться к выбору типа фигуры',callback_data='start')
        m.row(btn1,btn2)
        m.row(btn3)
        bot.send_message(callback.message.chat.id,'Вашему типу фигуры подойдут следующие джинсы:')
        for i in range(2):
            bot.send_photo(callback.message.chat.id, jeans_images_rectangle_men_front[i])
            bot.send_message(callback.message.chat.id,jeans_short_rectangle_men[i])
        bot.send_message(callback.message.chat.id,'Выберите, какие из джинс Вас заинтересовали:',reply_markup=m)
        #КОНЕЦ
    
    #КНОПКА ТРЕУГОЛЬНИК 
    if callback.data == 'tri':
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('regular',callback_data='regular_medium_straight')
        btn2 = types.InlineKeyboardButton('loose',callback_data='loose_medium_straight')
        btn3 = types.InlineKeyboardButton('relaxed',callback_data='relaxed_medium_straight')
        btn4 = types.InlineKeyboardButton('вернуться к выбору типа фигуры',callback_data='start')
        m.row(btn1,btn2,btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'Вашему типу фигуры подойдут следующие джинсы:')
        for i in range(3):
            bot.send_photo(callback.message.chat.id, jeans_images_triangle_men_front[i])
            bot.send_message(callback.message.chat.id,jeans_short_triangle_men[i])
        bot.send_message(callback.message.chat.id,'Выберите, какие из джинс Вас заинтересовали:',reply_markup=m)
        #КОНЕЦ
    
    #КНОПКА ТРАПЕЦИЯ 
    if callback.data == 'trap':
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('slim',callback_data='slim_medium_straight')
        btn2 = types.InlineKeyboardButton('regular',callback_data='regular_medium_straight')
        btn3 = types.InlineKeyboardButton('relaxed',callback_data='relaxed_medium_straight')
        btn4 = types.InlineKeyboardButton('вернуться к выбору типа фигуры',callback_data='start')
        m.row(btn1,btn2,btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'Вашему типу фигуры подойдут следующие джинсы:')
        for i in range(3):
            bot.send_photo(callback.message.chat.id, jeans_images_trap_men_front[i])
            bot.send_message(callback.message.chat.id,jeans_short_trap_men[i])
        bot.send_message(callback.message.chat.id,'Выберите, какие из джинс Вас заинтересовали:',reply_markup=m)
        #КОНЕЦ
    
    #КНОПКА ОВАЛ
    if callback.data == 'ell':
        m = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('loose',callback_data='loose_medium_straight')
        btn3 = types.InlineKeyboardButton('relaxed',callback_data='relaxed_medium_straight')
        btn4 = types.InlineKeyboardButton('вернуться к выбору типа фигуры',callback_data='start')
        m.row(btn2,btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'Вашему типу фигуры подойдут следующие джинсы:')
        for i in range(2):
            bot.send_photo(callback.message.chat.id, jeans_images_ell_men_front[i])
            bot.send_message(callback.message.chat.id,jeans_short_ell_men[i])
        bot.send_message(callback.message.chat.id,'Выберите, какие из джинс Вас заинтересовали:',reply_markup=m)
        #КОНЕЦ
        
    #КНОПКА ПЕРЕВЕРНУТЫЙ ТРЕУГОЛЬНИК 
    if callback.data == 'rev_tri':
        m = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton('regular',callback_data='regular_medium_straight')
        btn3 = types.InlineKeyboardButton('relaxed',callback_data='relaxed_medium_straight')
        btn4 = types.InlineKeyboardButton('вернуться к выбору типа фигуры',callback_data='start')
        m.row(btn2,btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'Вашему типу фигуры подойдут следующие джинсы:')
        for i in range(2):
            bot.send_photo(callback.message.chat.id, jeans_images_revtri_men_front[i])
            bot.send_message(callback.message.chat.id,jeans_short_revtri_men[i])
        bot.send_message(callback.message.chat.id,'Выберите, какие из джинс Вас заинтересовали:',reply_markup=m)
        #КОНЕЦ
        
    #ОБРАБОТКА ДЖИНС
    #КНОПКА SLIM MEDIUM STRAIGHT  
    if callback.data == 'slim_medium_straight':
        user_info.append('slim_medium_straight')
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('лонгслив',callback_data='longsleeve_round')
        btn2 = types.InlineKeyboardButton('классика',callback_data='classic_round')
        btn3 = types.InlineKeyboardButton('свободный крой',callback_data='free')
        btn4 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
        m.row(btn1,btn2)
        m.row(btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'К этим джинсам подойдут следующие футболки:')
        for i in range(3):
            bot.send_photo(callback.message.chat.id, shirts_images[i])
            bot.send_message(callback.message.chat.id,shirts_short[i])
        bot.send_message(callback.message.chat.id,'Выберите, какая из футболок Вас заинтересовала:',reply_markup=m)
        #КОНЕЦ
        
    #КНОПКА REGULAR MEDIUM STRAIGHT  
    if callback.data == 'regular_medium_straight':
        user_info.append('regular_medium_straight') #DANGER IF THEY PICKED WRONGLY
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('лонгслив',callback_data='longsleeve_round')
        btn2 = types.InlineKeyboardButton('классика',callback_data='classic_round')
        btn3 = types.InlineKeyboardButton('свободный крой',callback_data='free')
        btn4 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
        m.row(btn1,btn2)
        m.row(btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'К этим джинсам подойдут следующие футболки:')
        for i in range(3):
            bot.send_photo(callback.message.chat.id, shirts_images[i])
            bot.send_message(callback.message.chat.id,shirts_short[i])
        bot.send_message(callback.message.chat.id,'Выберите, какая из футболок Вас заинтересовала:',reply_markup=m)
        #КОНЕЦ
    
    #КНОПКА LOOSE MEDIUM STRAIGHT  
    if callback.data == 'loose_medium_straight':
        user_info.append('loose_medium_straight')
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('лонгслив',callback_data='longsleeve_round')
        btn2 = types.InlineKeyboardButton('классика',callback_data='classic_round')
        btn3 = types.InlineKeyboardButton('свободный крой',callback_data='free')
        btn4 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
        m.row(btn1,btn2)
        m.row(btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'К этим джинсам подойдут следующие футболки:')
        for i in range(3):
            bot.send_photo(callback.message.chat.id, shirts_images[i])
            bot.send_message(callback.message.chat.id,shirts_short[i])
        bot.send_message(callback.message.chat.id,'Выберите, какая из футболок Вас заинтересовала:',reply_markup=m)
        #КОНЕЦ
    if callback.data == 'relaxed_medium_straight':
        user_info.append('relaxed_medium_straight')
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('лонгслив',callback_data='longsleeve_round')
        btn2 = types.InlineKeyboardButton('классика',callback_data='classic_round')
        btn3 = types.InlineKeyboardButton('свободный крой',callback_data='free')
        btn4 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
        m.row(btn1,btn2)
        m.row(btn3)
        m.row(btn4)
        bot.send_message(callback.message.chat.id,'К этим джинсам подойдут следующие футболки:')
        for i in range(3):
            bot.send_photo(callback.message.chat.id, shirts_images[i])
            bot.send_message(callback.message.chat.id,shirts_short[i])
        bot.send_message(callback.message.chat.id,'Выберите, какая из футболок Вас заинтересовала:',reply_markup=m)
        #КОНЕЦ
    
    #ОБРАБОТКА ВЕРХА 
    if callback.data == 'longsleeve_round':
        user_info.append('longsleeve_round')
        bot.send_message(callback.message.chat.id,'Ваш получившийся выбор:')
        bot.send_photo(callback.message.chat.id, shirts_images[0])
        bot.send_message(callback.message.chat.id,shirts_description[0])
        if 'slim_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_slim_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_slim_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'regular_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_regular_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_regular_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'loose_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_loose_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_loose_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'relaxed_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_relaxed_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_relaxed_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
            
            
    if callback.data == 'classic_round':
        user_info.append('classic_round')
        bot.send_message(callback.message.chat.id,'Ваш получившийся выбор:')
        bot.send_photo(callback.message.chat.id, shirts_images[1])
        bot.send_message(callback.message.chat.id,shirts_description[1])
        if 'slim_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_slim_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_slim_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'regular_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_regular_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_regular_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'loose_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_loose_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_loose_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'relaxed_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_relaxed_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_relaxed_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
            
            
    if callback.data == 'free':
        user_info.append('free')
        bot.send_message(callback.message.chat.id,'Ваш получившийся выбор:')
        bot.send_photo(callback.message.chat.id, shirts_images[2])
        bot.send_message(callback.message.chat.id,shirts_description[2])
        if 'slim_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_slim_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_slim_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'regular_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_regular_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_regular_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'loose_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_loose_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_loose_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
        if 'relaxed_medium_straight' in user_info:
            for i in range(2):
                bot.send_photo(callback.message.chat.id, jeans_images_relaxed_medium_straight[i])
                bot.send_message(callback.message.chat.id,jeans_description_relaxed_medium_straight[i])
            m = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('завершить',callback_data='end')
            btn2 = types.InlineKeyboardButton('вернуться к типам фигуры',callback_data='start')
            m.add(btn1)
            m.add(btn2)
            bot.send_message(callback.message.chat.id,'Выберите слудующее действие:',reply_markup=m)
    
    #ОЦЕНКА БОТА 
    if callback.data == 'end':
        m = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1',callback_data='os1')
        btn2 = types.InlineKeyboardButton('2',callback_data='os2')
        btn3 = types.InlineKeyboardButton('3',callback_data='os3')
        btn4 = types.InlineKeyboardButton('4',callback_data='os4')
        btn5 = types.InlineKeyboardButton('5',callback_data='os5')
        m.row(btn1,btn2,btn3)
        m.row(btn4,btn5)
        bot.send_message(callback.message.chat.id,'Пожалуйста, оцените, насколько Вам понравился подбор одежды:',reply_markup=m)
        
    
    
    
    
    
bot.polling(non_stop=True)