from .base import BasePainter

class HardGamePainter(BasePainter):

    def draw_current_state(self, numFails):
        print()
        if numFails == 0:
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')

        elif numFails == 1:
            print('..-------..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')

        elif numFails == 2:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('........|..')
            print('........|..')

        elif numFails == 3:
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('.../.\\..|..')
            print('........|..')
        print()