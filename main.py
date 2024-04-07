from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a command handler for the '/start' command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the Patient Assignment Bot. Please enter your name.')

# Define a message handler for the patient's name
def handle_name(update: Update, context: CallbackContext):
    # Store the patient's name and ask for the problem description
    context.user_data['name'] = update.message.text
    update.message.reply_text('Thank you. Now, please describe your problem.')

# Define a message handler for the problem description
def handle_problem(update: Update, context: CallbackContext):
    # Store the problem description and confirm the registration
    context.user_data['problem'] = update.message.text
    update.message.reply_text('Your problem has been recorded. You will be assigned to a doctor shortly.')

# Main function to tie the commands and start the bot
def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_name, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_problem, pass_user_data=True))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()