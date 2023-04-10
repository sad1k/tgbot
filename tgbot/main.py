import telebot
import speech_recognition as sr

# replace YOUR_TOKEN with your Telegram bot token
bot = telebot.TeleBot('6178553448:AAGOsXavLAQBiDKzbcm2vuRV8yV67eSqwjA')

# handler for the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! I can convert MP3 files to text. To use me, simply upload an MP3 file and reply to it with the /convert command.")

# handler for the /help command
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "To use this bot, simply upload an MP3 file and reply to it with the /convert command.")

# handler for the /convert command
@bot.message_handler(commands=['convert'])
def handle_convert_audio(message):
    try:
        # get the audio file ID from the message
        audio_file_id = message.reply_to_message.audio.file_id

        # download the audio file from Telegram
        file_info = bot.get_file(audio_file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # convert audio to text using SpeechRecognition
        r = sr.Recognizer()
        audio_file = sr.AudioData(downloaded_file)
        text = r.recognize_google(audio_file)

        # send the text response to the user
        bot.reply_to(message.reply_to_message, text)

    except Exception as e:
        print(e)
        bot.reply_to(message, "Sorry, something went wrong. Please try again later.")

# start the bot
bot.polling()