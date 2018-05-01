import os
import datetime
import uuid
from utility.singleton import Singleton

class BaseRecorder(metaclass=Singleton):
    
    def __init__(self):
        self.id = uuid.uuid4()
        self.name = ''
        self.word = ''
        self.selected_letters = []

        # The final string stored in this variable will be written to text file
        self.data = ""

        # The current time we use to generate unique text file
        self.set_current_time()

    def set_current_time(self):
        now = datetime.datetime.now()
        self.current_time = "{}{}{}{}".format(now.day, now.month, now.year, now.second)

    # Saves data to text file
    def write_to_text(self, score, win):
        win_text = "lose"
        if win:
            win_text = "win"

        self.data += "{},{},{},{},{},{},{}\n".format(self.id, self.name, self.word, score, self.selected_letters, len(self.selected_letters), win_text)
        filename = self.format_filename("leaderbord_{}".format(self.current_time))

        with open(filename, 'w') as f:
            f.write(self.data)

    def get_highscores(self):
        pass

    def calculate_score(self, word, steps, number_of_fails, win):
        success = steps - number_of_fails
        success_ratio = success / steps
        return int(success_ratio * 1 / len(word) * 1000 * (win + 0.5))

    def format_filename(self, filename):
        extention = ".txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return "{}/reports/{}{}".format(dir_path, filename, extention)