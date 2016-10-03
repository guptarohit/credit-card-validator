def digits_of(number):
    return [int(i) for i in str(number)]

def checksum_luhn(card_number):
	digits = digits_of(card_number)
	odd_digits = digits[-1::-2] # From right
	even_digits = digits[-2::-2] # From right
	total = sum(odd_digits)
	for digit in even_digits:
		total += sum(digits_of(2 * digit))
	return total % 10

def is_valid(card_number):
	return checksum_luhn(card_number) == 0

choice = 'y'

while choice == 'y' or choice == 'Y':
	try:
		card_number = input("\nEnter the credit card number: ")
		#TODO use reg-ex instead for pattern matching
		if is_valid(card_number) and 12 <= len(card_number) and len(card_number) <= 19:
			print("\nThis is a valid credit card number.")
			if card_number[0:1] == "4":
				print("Type: Visa card.")
			elif card_number[0:2] == "34" or card_number[0:2] == "37":
				print("Type: American Express (AMEX) card.")
			elif card_number[0:2] == "36":
				print("Type: Diner’s Club International card.")
			elif card_number[0:2] == "51" or card_number[0:2] == "52" or card_number[0:2] == "53" or card_number[0:2] == "54" or card_number[0:2] == "55":
				print("Type: Mastercard.")
			elif card_number[0:4] == "6011":
				print("Type: Discover card.")
		else:
			print("\nInvalid!! Credit card number.")

		choice = input("\nWant to check again? (y/n): ")
	except ValueError:
		print("\nErr! Credit card number should be numeric. Try again.")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise
