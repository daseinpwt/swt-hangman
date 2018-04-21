import os

class ConsoleOperator:

	def clear_console(self):
		if os.name == 'nt':
			os.system('cls')
		if os.name =='mac' or os.name == 'posix':
			os.system('clear')
