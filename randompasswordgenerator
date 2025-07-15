import random 
import string 

def generate_password(length,use_letters,use_symbols,use_numbers):
    character_pool = ""

    if use_letters:
        character_pool+= string.ascii_letters

    if use_symbols:
        character_pool+= string.punctuation

    if use_numbers:
        character_pool+= string.digits

    if not character_pool:
        return "Error: no character types selected"
     
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def get_boolean_input(message):
    while True:
     choice = input(message + "(y/n):").lower()
     if choice == 'y':
         return True
     if choice == 'n':
         return False
     else:
         print("enter is form of yes or no")

def main():
    print("RANDOM PASSWORD GENERATOR")

    try:
        length = int(input("enter your password length: "))
        if length <=0:
            print("enter length in positive number")
            return
        
        use_letters = get_boolean_input("include letters?")
        use_symbols = get_boolean_input("include symbols?")
        use_numbers = get_boolean_input("include numbers?")
        
        password = generate_password(length,use_letters,use_numbers,use_symbols)
        print(f"your password is:\n {password}")

    except ValueError:
        print("please enter valid value for length")

if __name__ == "__main__":
    main()
    
