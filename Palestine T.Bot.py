import telebot
from telebot import types
bot = telebot.TeleBot('')

# Localized text
messages = {
    'start': 'أهلا بك في بوت عن تاريخ فلسطين. ماذا تريد أن تعرف عن تاريخ فلسطين في الفترة بين 1942-1950؟',
    'repeat': 'هل تريد السؤال عن شيء اخر؟',
    'exit' : 'تذكر دائما أن المعركة مستمرة حتى يتحرر المسجد الأقصى المبارك. السلام عليكم',
    'help': 'هذا البوت سيساعدك على فهم جزء من تاريخ فلسطين في الفترة بين 1942-1950. اكتب /start للبدء.',
    'events': 'أهم الأحداث في الفترة بين 1942-1950',
    'people': 'أهم الشخصيات في الفترة بين 1942-1950',
    'martyrs': 'لا يوجد ذكر لشهداء معينيين في هذه الفترة حيث بلغ عدد الشهداء الفلسطينيين في معارك النكبة حسب عدة مصادر تاريخية نحو 15 ألف شهيد، بينما بلغ عدد الشهداءالعرب من 3500 إلى 7000 شهيد',
    'event_x': '''لم تشهد الأراضي الفلسطينية في الفترة المذكورة أحداثاً كبيرة بنفس سخونة الأحداث في الفترة السابقة، والسبب في ذلك يرجع إلى القبضة الحديدية التي تعاملت بها سلطات الاحتلال البريطاني مع الحركة الوطنية وغياب أغلب قادتها إما بسبب السجن أو اضطرارهم للخروج إلى سوريا ولبنان بعد أن ضاقت بهم سبل المقاومة من الداخل. وبعد الحرب العالمية الثانية (1945) عاش العرب والشعب الفلسطيني آمالاً جديدة، رسم فيها خيالهم قصوراً للحرية والاستقلال نظير وقوفهم مع بريطانيا، لكن أحداث الأيام التي تلت الحرب أحالت تلك الأماني إلى أوهام، فبدأت بوادر العمل المسلح تظهر في الأراضي الفلسطينية من جديد.

وفي 29/1/1945 أعلنت بريطانيا أنها ستبقي باب الهجرة اليهودية مفتوحاً، مخالفة بذلك وعودها التي قطعتها على نفسها من قبل بتنظيم تلك الهجرة، ولكي تخفف من وقع الصدمة على العرب أعلنت عن تشكيل لجنة بريطانية أميركية، ووافقت اللجنة العربية العليا على التعاون مع اللجنة الأنجلو أمريكية في 20/4/1945، وجاء بيان تلك اللجنة لينص على السماح لمائة ألف مهاجر يهودي جديد بالدخول إلى فلسطين، وحرية انتقال الأراضي لليهود، وبقاء الانتداب البريطاني على فلسطين.

وأدت هذه التوصيات إلى اندلاع المظاهرات في فلسطين وبعض الدول العربية، واستدعى الأمر عقد اجتماع قمة عربي في أنشاص بمصر يومي 28 و29/5/1946 خلص الملوك والرؤساء العرب فيه إلى بيان إنشائي لا تدعمه آليات تنفيذية، وأكدوا على بدهيات لم تكن بحاجة إلى مثل هذا الاجتماع للتأكيد عليها. من ذلك على سبيل المثال "اعتبار القضية الفلسطينية قضية العرب جميعاً" و"فلسطين عربية ينبغي مساعدتها للحفاظ على عروبتها"، ومناشدة بريطانيا والولايات المتحدة بأن يكونا أكثر نزاهة في التعامل مع القضية الفلسطينية.''',
    'event_w': '''نشبت الحرب في 15/5/1948 بسبب قرار تقسيم فلسطين الصادر عن الأمم المتحدة في 29/12/1947، حيث دعت جامعة الدول العربية إلى اجتماع في القاهرة تم الإعلان فيه أن الحكومات العربية ترفض هذا القرار وأنها ستتخذ تدابير كفيلة بإحباطه.

كانت الحركة الصهيونية قد تمكنت من بناء قوة عسكرية كبيرة ضمن عدة منظمات عسكرية أهمها الهاغاناه، كما تمكنت بدعم من سلطات الانتداب البريطاني من  إنشاء صناعة عسكرية. أما على الجانب الآخر فكان الطرف العربي مكونا من الثوار الفلسطينيين، وجيش الجهاد المقدس، وجيش الإنقاذ، وقوات المتطوعين المصريين. كما تقرر إنشاء جيوش عربية على حدود فلسطين دون دخولها إلى الأراضي الفلسطينية والاكتفاء فقط بدعم الفلسطينيين والمتطوعين.

في تلك الأثناء أعلنت بريطانيا عن رغبتها في الانسحاب من فلسطين بتاريخ أقصاه 15/5/1948، وحدث خلال تلك الفترة مجموعة من المذابح قامت بها جماعات صهيونية مسلحة، فاتخذت الدول العربية قراراً بدخول جيوشها إلى فلسطين، وبدأت حشد القوات على الجبهات الرئيسية في مصر والأردن والعراق وسوريا ولبنان. وكانت السمة البارزة لتلك الحشود هي عدم التنسيق فيما بينها، فقد كان لكل جيش هدف مستقل، كما كانت بداية العمليات أيضا تفتقد إلى التنسيق، مما حرم الجيوش العربية من عامل المفاجأة في تحقيق انتصارات عسكرية. ويضاف إلى هذه الثغرات العسكرية عامل ضعف أساسي يتمثل في تحكم بريطانيا في تسليح الجيوش العربية.

ورغم كل تلك الثغرات فإن الجيوش العربية حينما دخلت فلسطين في 15/5/1948 حققت انتصارات معتبرة، فالقوات المصرية حققت نجاحات ملموسة في القطاع الجنوبي، وتقدم الجيشان الأردني والعراقي قليلاً لكنهما عادا وتوقفا بعد فترة قصيرة من بدء العمليات ولم يتجاوزا المناطق التي حددت لهما، كما تمكن الجيش السوري وجيش الإنقاذ من السيطرة على معظم الجليل، ولم يكن الجيش اللبناني بعيدا عن عكا.''',
    'event_z': '''بادرت القيادات الإسرائيلية إلى إعلان قيام دولة إسرائيل يوم 14 مايو/أيار عام 1948 بعيد انسحاب الانتداب البريطاني، ودعت يهود الشتات للعودة إلى "الوطن"، مطالبة إياهم بدعم الدولة الوليدة التي سارعت الولايات المتحدة والاتحاد السوفياتي إلى الاعتراف بها بعد دقائق من إعلانها.

انسحبت بريطانيا من فلسطين يوم 14 مايو/أيار 1948، وأعلن ديفيد بن غوريون في اليوم نفسه قيام الدولة الإسرائيلية وعودة الشعب اليهودي إلى ما أسماه أرضه التاريخية.
''',
    'person_a': 'بعد إقامة إسرائيل عام 1948 أصبح بن غوريون أول رئيس وزراء لها، وعمل فور توليه منصبه الجديد عام 1948 على توحيد العديد من المنظمات الدفاعية التي كانت موجودة آنذاك في قوات واحدة أطلق عليها قوات الدفاع الإسرائيلية IDF.'
}

@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    news = types.InlineKeyboardButton('أهم الأحداث', callback_data='news')
    people = types.InlineKeyboardButton('أهم الشخصيات', callback_data='people')
    martyrs = types.InlineKeyboardButton('أهم الشهداء', callback_data='martyrs')

    markup.add(news, people, martyrs)
    bot.send_message(message.chat.id, messages['start'], reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.send_message(message.chat.id, messages['help'])

@bot.message_handler(commands=['repeat'])
def repeat_bot(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    n = types.InlineKeyboardButton('لا', callback_data='n')
    y = types.InlineKeyboardButton('نعم', callback_data='y')

    markup.add(n, y)
    
    bot.send_message(message.chat.id, messages['repeat'], reply_markup=markup)



@bot.message_handler(commands=['news'])
def news_bot(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    x = types.InlineKeyboardButton('المقاومة الفلسطينية (1940-1947)', callback_data='x')
    w = types.InlineKeyboardButton('النكبة 1948', callback_data='w')
    z = types.InlineKeyboardButton('اعلان دولة اسراءيل', callback_data='z')

    markup.add(x, w, z)
    
    bot.send_message(message.chat.id, messages['events'], reply_markup=markup)

@bot.message_handler(commands=['people'])
def people_bot(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    a = types.InlineKeyboardButton('دافيد بن غوريون', callback_data='a')

    markup.add(a)
    
    bot.send_message(message.chat.id, messages['people'], reply_markup=markup)

@bot.message_handler(commands=['martyrs'])
def martyrs_bot(message):
    bot.send_message(message.chat.id, messages['martyrs'])


@bot.callback_query_handler(func=lambda call: True)
def reply(callback):
    if callback.message:
        if callback.data == 'news':
            news_bot(callback.message)
            repeat_bot(callback.message)
        elif callback.data == 'people':
            people_bot(callback.message)
            repeat_bot(callback.message)
        elif callback.data == 'martyrs':
            martyrs_bot(callback.message)
            repeat_bot(callback.message)
        elif callback.data == 'x':
            bot.send_message(callback.message.chat.id, messages['event_x'])
            repeat_bot(callback.message)
        elif callback.data == 'w':
            bot.send_message(callback.message.chat.id, messages['event_w'])
            repeat_bot(callback.message)
        elif callback.data == 'z':
            bot.send_message(callback.message.chat.id, messages['event_z'])
            repeat_bot(callback.message)
        elif callback.data == 'a':
            bot.send_message(callback.message.chat.id, messages['person_a'])
            repeat_bot(callback.message)
        elif callback.data =='y':
            start_bot(callback.message)
        elif callback.data == 'n':
            bot.send_message(callback.message.chat.id, messages['exit'])
bot.polling()
