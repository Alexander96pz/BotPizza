from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import *
import sys
import re
import os
import rutas.picante as picantes
from api_key import API_KEY, KEY
# Controladores de Comandos
# comand /start
def start(update, context):
    # Mensaje Inicial
    if "mode" not in context.chat_data:
        context.chat_data["mode"] = 0
    update.message.reply_text("Hola que tal!")
    update.message.reply_text("Por favor seleccione la preferencia de Pizza")
    update.message.reply_text("Con Picante /picante.")

def picante(update, context):

        context.chat_data["mode"] = 1
        options = [
            #                     nombre en el boton, value = "python"   
            InlineKeyboardButton("Muy Picante", callback_data="Hot"),
            InlineKeyboardButton("Medio Picante", callback_data="Medium"),
            InlineKeyboardButton("Suave Picante", callback_data="Mild"),
            ]
        update.message.reply_text("Por favor seleccione el nivel de Picante:",reply_markup=InlineKeyboardMarkup.from_column(options))
       
# Message handlers
def default(update, context):
   
    pass


# Callback handlers //seleccion del interprete button
# mode 1
def button(update, context):
    # print(context.chat_data)
    # if "mode" in context.chat_data and context.chat_data["mode"] == 1 and "container" not in context.chat_data:
        query = update.callback_query
        # print(query)
        message = query.message
        # print(message)
        lang = query.data
        print(lang)
        message.edit_reply_markup()  # remueve los botones
        nivel = {
            "Hot": "Muy Picantes",
            "Medium": "Medios Picantes ",
            "Mild": "Suave Picante"
        }[lang]
        pizzas=picantes.getPizzasPicante(lang)
        listPizzas = []
            #                     nombre en el boton, value = "python"  
        for name in pizzas:
            listPizzas.append(InlineKeyboardButton(name, callback_data=name))
                # InlineKeyboardButton("Medio Picante", callback_data="Medium"),
                # InlineKeyboardButton("Suave Picante", callback_data="Mild"),
        # ]
        # salida del interprete
        message.reply_text("De Pizzas " + nivel + " te ofrecemos",reply_markup=InlineKeyboardMarkup.from_column(listPizzas))
# mezcla de funciones
def drop_data(update, context):
   pass


def drop_command(message, command):
    """
    Given a message text, drops the command prefix from the string.
    """
    return message[len(command) + 1:]


# Initializacion del bot
def main():
    # Log stdout //nos ayudara a saber cuando y porque no funcionan las cosas
    # logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
    # actualizaciones provenientes de telegram
    updater = Updater(API_KEY, use_context=True)
    # despachador nos permite clasificar las actualizaciones 
    dp = updater.dispatcher
    # Add handlers//controladores
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("picante", picante))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CallbackQueryHandler(button))
    

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()