from datetime import datetime
import os

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

        with open("logs/activity.log",
                   "a",
                   encoding="utf-8"
                ) as log_file:
            log_file.write(final_message + "\n")
