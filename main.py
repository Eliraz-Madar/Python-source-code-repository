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
		
		i = 0
		for line in data:
			print(f"line {i+1}: {line}")
			if i+1 == 14:
				result, error = my_language.run('<stdin>', line,i)

			result, error = my_language.run('<stdin>', line,i)
			i+=1
			
				
			# handle result
			if error:
				# error	
				if result != None:			
					if result[0] != "EOF":
						continue
					else:
						print("here")
						print(error.as_string())
						break
			elif result:
				# success
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
			elif result:
				print(result)
			
