from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import InlineQueryResultAudio
import os
updater = Updater(token='287399290:AAEP25_SsZlAwoeB14JW348yNKE2cQJYsxU')
dispatcher = updater.dispatcher

#sprueche = [name[0:-4] for name in os.listdir("./stoll-klangbrett/data") if name.endswith(".mp3")]
#print(sprueche)

sprueche = {'1938': "1938",
 '90prozent': "90 Prozent", 
 'allesistvorhersehbar': "Alles ist vorhersehbar", 
 'ameisen': "Ameisen", 
 'auszerirdische' : "Auszerirdische", 
 'bernd_ruhe': "Bernd, Ruhe!", 
 'blut': "Blut", 
 'buchbestseller': "Bestseller", 
 'bullen': "Bullen", 
 'corioliskraft':"Corioliskraft", 
 'dasistganzwichtig': "Das ist ganz wichtig", 
 'Dastaunensiewas':"Da staunen Sie, was?", 
 'dastauntihrwas':"Da staunt ihr, was?", 
 'derelektrojude':"Der Elektrojude", 
 'derTisch':"Der Tisch", 
 'desinformation':"Desinformation", 
 'Deutscherraumflugab1938':"Deutscher Raumflug ab 1934", 
 'diesonneistkalt': "Die Sonne ist kalt", 
 'dillgurke':"Dillgurke", 
 'facebook':"Facebook", 
 'geheimnis':"Geheimnis", 
 'geheimwissen': "Geheimwissen", 
 'handys':"Handys", 
 'IchBegrueszeSie':"Ich begruesze Sie", 
 'implosionsstrudel':"Implosionsstudel", 
 'implosionstechnologie':"Implosionstechnologie", 
 'informationsquelle':"Informationsquelle", 
 'internetistscheisse':"Internet ist scheisze", 
 'kaltefusion':"Kalte Fusion", 
 'keinproblem':"Kein Problem", 
 'keinsiencefiction':"Kein Science-Ficition", 
 'klarne': "Klar, ne", 
 'kopfzumdenkenbenutzen':"Kopf zum Denken benutzen", 
 'kraftmassebeschleunigung':"Kraft Masse Beschleunigung", 
 'lachen':"Kann ich nur lachen", 
 'magieistphysik':"Magie", 
 'meingott':"Mein Gott", 
 'microwellenstrahler':"Mikrowellenstrahler", 
 'MicrowelleScalarwelle': "Mikrowelle, Skalarwelle", 
 'mussmanwissen':"Musz man wissen", 
 'PhysikMathematikPhilosophie':"Physik, Mathematik, Philosophie", 
 'promovierternaturwisschenschaftler':"Mein Name ist Stoll", 
 'quetschmetall':"Quetschmetall", 
 'Ruhedahinten':"Ruhe dahinten",
 'schnee': "Schnee", 
 'schwachsinn':"Schwachsinn", 
 'schwarzesonne':"Schwarze Sonne", 
 'silentium':"Silentium", 
 'soeinfachistdas': "So einfach ist das", 
 'stellewelle':"Stellewelle", 
 'stoll_hehe':"hehe", 
 'strafplanet':"Strafplanet", 
 'tee':"Tee", 
 'transmedialekontakte': "Transmediale Kontakte", 
 'tuermitkraft':"Tuer mit Kraft", 
 'universum':"Universum", 
 'unvollkommen':"Unvollkommen", 
 'vergessensies':"Vergessen Sie\'s", 
 'warsteiner':"Wer hat Warsteiner bestellt?", 
 'wert':"Wert", 
 'werweiszdas':"Wer weisz dasz?", 
 'wiederholung':"Wiederholung", 
 'wiederkeiner':"Wieder keiner", 
 'wissenauchdiewenigsten':"Wissen auch die wenigsten", 
 'wissenumdiewahrephysik':"Wissen um die wahre Physik", 
 'wkf':"Wetterkrieg$fuehrung",
 'wortzufall':"Zufall", 
 'zeit':"Zeit"}



def inline_audio(bot, update):
    query = update.inline_query.query
    if not query:
        return
    result = finde_passende_sprueche(str(query).lower().replace(" ", ""))
    bot.answerInlineQuery(update.inline_query.id, result)


def finde_passende_sprueche(eingabe):
    #print("Eingabe: {}".format(eingabe))
    result = list()
    for spruch in sprueche:
        if (eingabe in spruch.lower().replace(" ", "")) or (eingabe in sprueche[spruch].lower().replace(" ", "")):
            #print("Spruch: {}".format(spruch))
            github_url = "http://raw.githubusercontent.com/23x/stoll-klangbrett/master/data/{}.mp3".format(spruch)
            result.append(
                InlineQueryResultAudio(
                    id=spruch,
                    audio_url=github_url,
                    title=sprueche[spruch]
                )
            )
    return result

inline_audio_handler = InlineQueryHandler(inline_audio)
dispatcher.add_handler(inline_audio_handler)


def hilfe_command(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Gebe @axelstollbot + eine gesuchten Spruch ein. Beispielsweise @axelstoll physik")

help_command_handler = CommandHandler('hilfe', hilfe_command)
dispatcher.add_handler(help_command_handler)


updater.start_polling()
raw_input("Press Enter to continue...")
updater.stop()
