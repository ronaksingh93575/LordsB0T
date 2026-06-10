import threading
import time


class FarmingEngine:

    def __init__(self):

        self.running = False
        self.thread = None

    def bot_loop(self):

        while self.running:

            print("Searching for resource nodes...")

            time.sleep(5)

            print("Sending troops...")

            time.sleep(5)

            print("Gathering resources...")

            time.sleep(5)

    def start(self):

        if not self.running:

            self.running = True

            self.thread = threading.Thread(
                target=self.bot_loop,
                daemon=True
            )

            self.thread.start()

    def stop(self):

        self.running = False