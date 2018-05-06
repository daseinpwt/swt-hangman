import os
import subprocess

class BaseController:
    def clear_console(self):
        if os.name in ('nt', 'dos'):
            os.system('CLS')
        elif os.name in ('linux', 'osx', 'posix'):
            subprocess.call('clear')
        else:
            print('\n' * 119)
