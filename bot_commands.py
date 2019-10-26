import bot_library

def ask_bot(text, bot_token, chat_id):
    if text=="/listatalk":
        bot_library.send_text(bot_token,chat_id," 10:05 - Back to the AI \n 10:25 - No Hat Conference, io c'ero \n 10:35 - Prove pratiche di machine learning \n 10:50 - Il mio primo bot per telegram \n 11:00 - Il progetto common voice \n 11:25 - Sandwich machine \n 11:35 -  Riconoscimento targhe, sembra facile \n 11:45 - 20 Anni di Linux Day a Brescia ")
    elif text=="/orario":
        bot_library.send_text(bot_token,chat_id,"Sabato 26/10 ore 10:00-12:00 e 14:00-18:00 al Musil di Rodengo Saiano")
    elif text=="/volantino":
        bot_library.send_image(bot_token, chat_id, "volantino.jpg", caption=None)
    else:
        if (text=="/start"):
            bot_library.send_text(bot_token,chat_id,"/Benvenuto al Linux Day!")
        else:
            bot_library.send_text(bot_token,chat_id,"comando "+text+ " sconosciuto")
        bot_library.send_text(bot_token,chat_id,"lista comandi:")
        bot_library.send_text(bot_token,chat_id,"/listatalk")
        bot_library.send_text(bot_token,chat_id,"/orario")
        bot_library.send_text(bot_token,chat_id,"/volantino")
