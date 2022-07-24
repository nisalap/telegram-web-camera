"""
Telegram Bot Python Script
"""
from telegram.ext import Updater, CommandHandler
from Camera import Camera


class Bot:
    """
    This is the main Bot class that initiates the bot
    Use webhook approach for a better performance on low spec and low data
    """

    def __init__(self):
        """
        Initialize the Bot
        """
        print("Intializing the bot...")
        self.token = "<your bot token here>"

        # If using webhook, add the https public url below
        self.is_webhook = False
        self.public_url = ""
        self.port = 8000

        if self.is_webhook and (self.public_url is None or self.port is None):
            print("Missing public URL or Port")
            raise Exception()

        self.updater = Updater(token=self.token, use_context=True)
        self.register_handlers()
        self.camera = Camera()

    def run(self):
        """
        Starts the bot
        """
        print("Starting the Bot")

        if self.is_webhook:
            print("Bot: {} Webhook: {} Public URL: {} Port: {}".format(self.bot, self.is_webhook, self.public_url, self.port))
            self.updater.start_webhook(listen="0.0.0.0", port=self.port, url_path=self.token,
                                       webhook_url=self.public_url + "/" + self.token)
            self.updater.idle()
        else:
            print("Bot: {} Webhook: {}".format(self.token, self.is_webhook))
            self.updater.start_polling()
            self.updater.idle()

    def register_handlers(self):
        """
        Register message receivers here
        :return:
        """
        self.updater.dispatcher.add_handler(CommandHandler("start", self.start))
        self.updater.dispatcher.add_handler(CommandHandler("get", self.get_photo))

    def initialize(self):
        """
        Bot related initiations
        :return:
        """
        pass

    def get_dispatcher(self):
        """
        Returns the dispatcher to be used
        """
        return self.dispatcher

    def start(self, update, context):
        first_name = update.message.chat.first_name
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Hey \N{waving hand sign} {},\nThis is the Demo Bot".format(first_name))

    def get_photo(self, update, context):
        self.camera.capture()
        with open("image.jpg", 'rb') as image:
            context.bot.send_photo(chat_id=update.effective_chat.id,
                                   caption="Photo",
                                   photo=image)



