from tkinter import *


def digits_of(number):
    return [int(i) for i in str(number)]


def checksum_luhn(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]  # From right
    even_digits = digits[-2::-2]  # From right
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10


def is_valid(card_number):
    return checksum_luhn(card_number) == 0


def cc(card_number):
    res = ""
    try:
        if is_valid(card_number) and 12 <= len(card_number) <= 19:
            res = "\nThis is a valid credit card number."
            if card_number[0:1] == "4":
                res += "\nType: Visa card."
            elif card_number[0:2] == "34" or card_number[0:2] == "37":
                res += "\nType: American Express (AMEX) card."
            elif card_number[0:2] == "36":
                res += "\nType: Diner’s Club International card."
            elif card_number[0:2] == "51" or card_number[0:2] == "52" or card_number[0:2] == "53" or card_number[0:2] == "54" or card_number[0:2] == "55":
                res += "\nType: Mastercard."
            elif card_number[0:4] == "6011":
                res += "\nType: Discover card."
        else:
            res = "\nINVALID, Credit card number."

    except ValueError:
        res = "\nErr! Credit card number should be numeric. Try again."
    except:
        res = "Unexpected error:" + sys.exc_info()[0]
        raise
    return res


def ccValid():
    res = cc(str(ment.get()))
    mlabel2.config(text=res)
    return

top = Tk()
ment = StringVar()

top.geometry('400x350+500+300')
top.title('CC validator')

mlabel = Label(top, text="Enter the credit card number", font="Verdana 14 bold").pack()
mentry = Entry(top, textvariable=ment, font="Verdana 12").pack()
mbutton = Button(top, text='OK', command=ccValid, fg='white', bg='black', font="Verdana 10").pack()
mlabel2 = Label(top, text="", font=("Verdana", 12))
mlabel2.pack(side="top")
top.mainloop()

# Valid visa: 4024007166505189