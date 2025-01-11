from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN; Final = 7157625326:AAFw1vu3M4-lBhSk3PpSzVDws_gIcQ5R2Ss
BOT_USERNAME: Final = '@CoachingAssistant_Bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Hi there! Thank you for your interest in taking up this assignment. I have a few questions for you.
                                    - What is your name
                                    - What is your age
                                    - What is your gender
                                    - Years of Coaching Experience
                                    - Badminton Accolades (Can include participation):
                                    - Number of students currently:
                                    - Paylah!/Paynow Number:
                                    - Do send over a short video of you playing/coaching the sport:
                                    
                                    Thank you for your patience in answering these questions!)

# Responses


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type #finding out the type of message and chat, whether it is group chat or private chat
    text: str = update.message.text #message that is incoming

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"') #useful debugging, messages that are incoming to the bot

    if message_type = 'group':              #group messages with username tagged then will be replied to
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return

    else:
        response: str = handle_response(text)


    print('Bot:', reponse)      #useful for debugging
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE): #to find out what error caused the actual error
    print(f'Update {update} caused error {context.error}')