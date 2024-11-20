import random
# All characters to be used in password
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l"
,"m","n","o","p","q","r","s","t","u","v","w","x","y","z"
,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
,'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number=["1","2","3","4","5","6","7","8","9","0"]

symbol=["!","@","#","$","%","&"]

#Displaying a welcome message
print("Welcome to Password Generator\n\n")

#Taking no characters to be wanted
number_of_alphabet=int(input("Enter how many alphabets you want: \n"))
number_of_numbers=int(input("Enter how many numbers you want: \n"))
number_of_symbols=int(input("Enter how many symbols you want: \n"))


#Creating a variable to store generated string with random alphabets
alphabets_in_pass=""
for i in range (0,number_of_alphabet):
    alphabets_in_pass+=alphabet[random.randint(0,len(alphabet)-1)]


#Creating a variable to store generated string with random numbers
numbers_in_pass=""
for i in range (0,number_of_numbers):
    numbers_in_pass+=number[random.randint(0,len(number)-1)]


#Creating a variable to store generated string with random symbols
symbols_in_pass=""
for i in range (0,number_of_symbols):
    symbols_in_pass+=symbol[random.randint(0,len(symbol)-1)]


#Combining the three variables to create password
password =alphabets_in_pass+numbers_in_pass+symbols_in_pass

#Suffling the letters of the password
password_as_list=list(password)
random.shuffle(password_as_list)
jumbledpassword=""
for i in password_as_list:
    jumbledpassword+=i

print(f"Your password is: {jumbledpassword}")
