# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

plen = nr_letters + nr_symbols + nr_numbers
libtotlen = 0
pas = ''
alpflag = 0
numflag = 0
speflag = 0


while (len(pas) < plen):

    lib = [letters, numbers, symbols]

    if alpflag == nr_letters:
        lib.remove(letters)

    if numflag == nr_numbers:
        lib.remove(numbers)

    if speflag == nr_symbols:
        lib.remove(symbols)

    idk1 = random.randint(0, len(lib) - 1)
    idk2 = random.randint(0, len(lib[idk1]) - 1)
    idk = lib[idk1][idk2]

    if idk.isalpha() == True:
        alpflag += 1

    elif idk.isnumeric() == True:
        numflag += 1

    else:
        speflag += 1

    pas = pas + idk

print(pas)



#function to calculate combined total length of lists inside lists i.e nested lists
'''
def nesttotlen(list1):
  totlen = 0
  for i in range(0, len(list1)):
      totlen = totlen + len(list1[i])

  return totlen
'''