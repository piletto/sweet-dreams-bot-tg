import config
import telebot
from random import choice

token = "8881740248:AAGLVzx8UajCPQQQkRbKmAtf8Pcr-S56URY"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hai, I'm sweet dreams bot.\
""")


@bot.message_handler(commands=['info'])
def info_command(message):
    bot.reply_to(message, """\
I'm your sweet bot!!
I can tell a random joke or fact for uu <3
I can flip a coin for uu
By the way, I can repeat after you!! Tell me anything and I'll repeat it!! ^^
Just tell me what to do)\
""")

@bot.message_handler(commands=['fact'])
def info_command(message):
    fact = choice(["Space is completely silent because sound cannot travel in a vacuum", "One day on Venus is longer than one year on Venus", "Neutron stars are so dense that a teaspoon of their material weighs billions of tons", "A space suit costs around $12 million to make", "The Moon is slowly drifting away from Earth, about 3.8 cm per year", "A year on Mercury is just 88 Earth days long", "There's a planet made of diamonds (55 Cancri e)", "The observable universe is around 93 billion light-years in diameter", "You can't burp in space — there's no gravity to separate gas from liquid in your stomach", "If two pieces of the same metal touch in space, they will permanently bond (cold welding)", "Your stomach gets a new lining every 3–4 days to prevent it from digesting itself", "The human nose can detect over 1 trillion scents", "You can't breathe and swallow at the same time", "Babies have around 270 bones at birth, but adults have 206", "Your body has more bacteria than human cells", "The strongest muscle in your body (by weight) is the masseter — your jaw muscle", "Fingernails grow faster than toenails", "The human brain uses about 20% of the body's total energy", "You produce enough saliva in a year to fill two bathtubs", "Your bones are five times stronger than steel of the same density", "Octopuses have three hearts and blue blood", "Cows have best friends and get stressed when separated", "Elephants can recognise themselves in mirrors — a sign of self-awareness", "Frogs can freeze completely and thaw back to life", "Turritopsis dohrnii, a jellyfish species, can potentially live forever", "A shrimp's heart is in its head", "Rats and mice laugh when tickled, but in frequencies humans can't hear", "Some turtles can breathe through their butts", "Sea otters hold hands while sleeping so they don't drift apart", "Sloths are so slow that algae grow on their fur", "Honey never spoils — archaeologists found edible honey in Egyptian tombs", "Bananas are berries, but strawberries aren't", "Apples float because they're 25% air", "Ketchup was once sold as medicine in the 1800s", "Peanuts are not nuts — they're legumes", "Cheese is the most stolen food in the world", "One fast food burger may contain meat from 100 different cows", "White chocolate isn't chocolate — it has no cocoa", "The word 'queue' is the only word in English pronounced the same way when the last four letters are removed", "The dot over an 'i' is called a tittle", "Oxford University is older than the Aztec Empire", "The shortest war in history lasted less than an hour (Anglo-Zanzibar War)", "The first recorded vending machine sold holy water", "Crows can recognize human faces", "The Moon has moonquakes", "A group of porcupines is called a prickle", "Some fish can change gender", "Cotton candy was created by a dentist", "Clouds can weigh more than a million pounds", "Blue whales are so big that an adult human could swim through their veins", "Sloths can hold their breath up to 40 minutes", "It's impossible to hum while holding your nose", "Lobsters taste with their feet", "Before toilet paper was invented, Americans used corn cobs", "Goats have emotional intelligence", "The Eiffel Tower can be 15 cm taller in the summer", "Canada has more lakes than the rest of the world combined", "A group of flamingos is called a flamboyance", "Petrichor is the smell of rain", "Nintendo was founded in 1889"])
    bot.reply_to(message, fact)

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["FEMBOY", "CATGIRL"])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['joke'])
def coin_handler(message):
    joke = choice(["Parallel lines have so much in common — it's a shame they'll never meet", "I told my wife she should embrace her mistakes — she hugged me", "Why don't scientists trust atoms? Because they make up everything", "I'm reading a book about anti-gravity — it's impossible to put down", "Why did the scarecrow win an award? He was outstanding in his field", "I used to hate facial hair, but then it grew on me", "Why don't skeletons fight each other? They don't have the guts", "I'm on a seafood diet — I see food and I eat it", "Why did the math book look sad? It had too many problems", "I would tell you a joke about the unemployed, but none of them work", "Why can't your nose be 12 inches long? Because then it would be a foot", "I broke up with my calculator — I can count on myself now", "Why did the coffee call the police? It got mugged", "I'm friends with 25 letters of the alphabet — I don't know Y", "Why don't eggs tell jokes? They'd crack each other up", "The past, present, and future walked into a bar — it was tense", "I only know 25 letters of the alphabet too — I forgot U as well", "Why did the bicycle fall over? It was two-tired", "What do you call a fake noodle? An impasta", "I'm terrified of elevators, so I'm taking steps to avoid them", "Why did the golfer bring two pairs of pants? In case he got a hole in one", "I asked the gym trainer if he could teach me to do the splits — he said how flexible are you? I said I can't make Tuesdays", "Why don't programmers like nature? It has too many bugs", "I told a chemistry joke, but there was no reaction", "What's a vampire's favourite fruit? A neck-tarine", "Why did the man fall down the well? He couldn't see that well", "I used to play piano by ear, but now I use my hands", "What do you call a bear with no teeth? A gummy bear", "Why did the tomato turn red? Because it saw the salad dressing", "I'm not lazy, I'm on energy-saving mode"])
    bot.reply_to(message, joke)

@bot.message_handler(commands=['weather'])
def send_welcome(message):
    bot.reply_to(message, """\
It's sweet day! <3\
""")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Commands:
/start
/info
/fact
/coin
/help
/joke
/weather\
""")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()