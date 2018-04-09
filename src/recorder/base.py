class BaseRecorder:
    def __init__(self):
        self.r = []
        pass

    def record(self, step, guess, word, numFails):
        self.r.append(guess)
        pass

    def report(self):
        print('--- Base Recorder Report ---')
        for guess in self.r:
            print("\t%s" % guess)
        print('----------------------------')
