from datetime import datetime

class Logger:

    callback = None

    @classmethod
    def set_callback(cls, callback):
        cls.callback = callback

    @classmethod
    def log(cls, message):

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        final_message = (
            f"[{timestamp}] {message}"
        )

        print(final_message)

        if cls.callback:
            cls.callback(final_message)