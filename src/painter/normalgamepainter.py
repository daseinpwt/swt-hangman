from .base import BasePainter

class NormalGamePainter(BasePainter):

    def __init__(self, mask):
        self.mask = mask

    def draw_current_state(self, numFails):
        print()
        if numFails == 0:
            self.zero_fails()

        elif numFails == 1:
            self.one_fails()

        elif numFails == 2:
            self.two_fails()

        elif numFails == 3:
            self.three_fails()

        elif numFails == 4:
            self.four_fails()

        elif numFails == 5:
            self.five_fails()

        elif numFails == 6:
            self.six_fails()

        elif numFails == 7:
            self.seven_fails()
        print()

    def zero_fails(self):
        print('...........')
        print('...........')
        print('...........')
        print('...........')
        print('...........')
        print('...........')
        print('...........')
        print('...........')
        print('...........')
        print('...........')

    def one_fails(self):
        print('..-------..')
        print('........|..')
        print('........|..')
        print('........|..')
        print('........|..')
        print('........|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')

    def two_fails(self):
        print('..-------..')
        print('........|..')
        print('....O...|..')
        print('........|..')
        print('........|..')
        print('........|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')

    def three_fails(self):
        print('..-------..')
        print('........|..')
        print('....O...|..')
        print('....|...|..')
        print('....|...|..')
        print('........|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')

    def four_fails(self):
        print('..-------..')
        print('........|..')
        print('....O...|..')
        print('....|/..|..')
        print('....|...|..')
        print('........|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')

    def five_fails(self):
        print('..-------..')
        print('........|..')
        print('....O...|..')
        print('...\\|/..|..')
        print('....|...|..')
        print('........|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')

    def six_fails(self):
        print('..-------..')
        print('........|..')
        print('....O...|..')
        print('...\\|/..|..')
        print('....|...|..')
        print('.....\\..|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')

    def seven_fails(self):
        print('..-------..')
        print('........|..')
        print('....O...|..')
        print('...\\|/..|..')
        print('....|...|..')
        print('.../.\\..|..')
        print('........|..')
        print('._________.')
        print('.|.......|.')
