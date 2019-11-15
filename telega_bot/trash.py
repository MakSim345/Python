
#@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print "get_text_message - enter."
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

