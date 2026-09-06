import my_language

import sys


def main(filename):
	# check for validity
	if not filename.endswith(".lambda"):
		print("only work with .lambda files")
		exit(1)

	# read content
	with open(filename, "r") as file:
		data = file.read().splitlines()

		for i, line in enumerate(data):
			print(f"line {i+1}: {line}")
			result, error = my_language.run(filename, line, i)

			# handle result
			if error:
				print(error.as_string())
			elif result is not None:
				print(result)


if __name__ == "__main__":

	arguments = sys.argv

	if len(arguments) == 2:
		runnable = arguments[1]
		main(runnable)
	else:
		while True:
			text = input('basic > ')
			result, error = my_language.run('<stdin>', text)

			if error:
				print(error.as_string())
			elif result is not None:
				print(result)