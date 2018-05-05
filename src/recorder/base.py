import glob
import os
import sys
import datetime
import uuid
from utility.singleton import Singleton
from recorder.report import Report

class BaseRecorder(metaclass=Singleton):

    def __init__(self):
        self.id = uuid.uuid4()
        self.name = ''
        self.word = ''
        self.selected_letters = []
        self.score_list = []
        self.top_amount = 5

        # The final string stored in this variable will be written to text file
        self.data = ""

        # The current time we use to generate unique text file
        self.set_current_time()

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(os.path.realpath(__file__))

        self.reports_dir = application_path + '/reports'
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)

    def set_current_time(self):
        now = datetime.datetime.now()
        self.current_time = "{}{}{}{}".format(now.day, now.month, now.year, now.second)

    def read_files(self):
        extention = ".txt"
        with_name = "leaderbord_"
        path = "{}/{}*{}".format(self.reports_dir, with_name, extention)
        files = glob.glob(path)
        for file in files:
            f = open(file, 'r')
            self.read_lines(f)
            # print ('%s' % f.readlines())
            f.close()
        # self.report()

    def report(self, steps, number_of_fails, game_list):
        score = self.calculate_score(self.word, steps, number_of_fails, game_list[len(game_list)-1])
        if game_list[len(game_list)-1]:
            game = "WON"
        else: game = "LOST"

        self.data += "{},{},{},{},{},{},{}\n".format(self.id, self.name, self.word, score, self.selected_letters, len(self.selected_letters), game)
        filename = self.format_filename("leaderbord_{}".format(self.current_time))

        with open(filename, 'w') as f:
            f.write(self.data)

        print('--- Base Recorder Report ---')
        print("You", game, "game", len(game_list))
        print("Out of", steps, "turns, you guessed", steps-number_of_fails, "right", "-> success rate", (int)(self.calculate_success_ratio(steps,number_of_fails)*100), "%" )
        print("Points:", score)
        print("Winrate:", int(game_list.count(1)/len(game_list)*100), "%")
        print('----------------------------')

    def show_highscores(self):
        self.score_list = []
        self.read_files()

        self.score_list.sort(key = lambda x: x.score)
        self.score_list.reverse()
        if len(self.score_list) == 0:
            print("No highscores available \n")
            return

        print("HIGHSCORES")
        print('----------------------------')

        i = 0
        while i <= (len(self.score_list)-1) and i < 5:
            print("{}, {}".format(self.score_list[i].score,self.score_list[i].name))
            i += 1

        print('----------------------------\n')

    def read_lines(self, f):
        for line in f:
            currentline = line.split(",")
            x = Report(str(currentline[0]), str(currentline[1]), str(currentline[2]), int(currentline[3]), str(currentline[4]), str(currentline[5]), str(currentline[6]))
            self.score_list.append(x)

    def calculate_score(self, word, steps, number_of_fails, win):
        return int(self.calculate_success_ratio(steps, number_of_fails) * 1 / len(word) * 1000 * (win + 0.5))

    def calculate_success_ratio(self, steps, number_of_fails):
        return (steps - number_of_fails) / steps

    def format_filename(self, filename):
        extention = ".txt"
        return "{}/{}{}".format(self.reports_dir, filename, extention)
