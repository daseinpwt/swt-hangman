class BaseRecorder:
    def __init__(self):

        # mockupname
        self.name='Kwame'
        # mockupname 
        
        self.player_scores=[]
        self.f_name='leaderbord.txt'
        self.f_name_p='highscores.txt'
        self.delimiter=','
        self.top=5
        pass

    def record(self, step, guess, guessed_letters, word, num_fails, games, wins, check_win):
        self.letters_used=guessed_letters
        self.len_word=len(guess)
        self.successes=step-num_fails
        self.success_ratio=(int)(self.successes/step*100)
        self.turns=step
        self.games_played=games
        if check_win:
            self.win_var=1
            self.game='WON'
        else:
            self.game='LOST'
            self.win_var=0
        self.game_ratio=(int)(wins/self.games_played*100)
        self.score=int(self.success_ratio/100*(1/self.len_word)*1000*(self.win_var+0.5))
        self.write_scores(self.score, self.player_scores, self.f_name, self.delimiter)
        self.read_scores(self.f_name, self.delimiter)

        pass

    def report(self):
        print('--- Base Recorder Report ---')
        print("You", self.game, "game", self.games_played)
        print("Out of", self.turns, "turns, you guessed", self.successes, "right", "->succesrate", self.success_ratio, "%" )
        print("Letters guessed:", self.letters_used)
        print("points:", self.score,)
        print("Winrate:", self.game_ratio, "%")
        print('----------------------------')
        # total=0
        # for score in self.scores:
        #     total+=score
        # score=total/len(self.scores)
        # print(score)

    def write_scores(self, score, scores, filename, splitter):
        scores.append((score, self.name))
        with open (filename, 'w') as f:
            for s in scores:
                f.write(splitter.join(map(str, s))+ '\n')\
                
    def read_scores(self, filename, splitter):
        self.scores=[]
        self.names=[]
        
        with open(filename) as f:
            for score in f:
                score, name= score.strip().split(splitter)
                self.scores.append(int(score))
                self.names.append(name)
        return self.scores, self.names

