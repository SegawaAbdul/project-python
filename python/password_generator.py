import secrets as se
import string  as st

def core(length=10, ucase=False,num=False,sp_ch=False):
    alphabet = st.ascii_lowercase
    if ucase:
        alphabet += st.ascii_uppercase
    if num:
        alphabet += st.digits
    if sp_ch:
        alphabet += st.punctuation
    
    # Ensure password meets complexity requirements
    password = ''
    if not ucase:
        password += se.choice(st.ascii_uppercase)
    if not num:
        password += se.choice(st.digits)
    if not sp_ch:
        password += se.choice(st.punctuation)
    
    # Fill rest of password with random characters
    for _ in range(length - len(password)):
        password += se.choice(alphabet)
    
    # Shuffle the password to avoid the first characters always being in the same character set
    password_list = list(password)
    se.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    
    return password
def cache(password, length):
    with open("password_log.txt","a") as ft:
        ft.write(f"Password: {password}\n")
        ft.write(f"Length: {length}\n\n")
        

def main():
    while True:
        print("Password Generator")
        print("------------------")
        
        while True:
            try:
                
                length = int(input(f"Enter password length (): "))
            
                if 8 <= length <= 50:
                    break
                else:
                    print("Please enter a value greater than that or less than that !!!")
            except ValueError:
                print("Invalid input. Please enter a number.")

        ucase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        num = input("Include numbers? (y/n): ").lower() == 'y'
        sp_ch = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = core(length, ucase, num, sp_ch)
        print("\nGenerated Password:")
        print("__'",password,"'____")
        cache(password,length)

        con = input("\n\nDo you want to generate another password? (yes/no):\nEnter 'yes' or 'y' -> continue\n\t'no' or 'n' -> Quit\n -").lower()

        if con == 'yes' or con == 'y':
            print("Continuing...")
        elif con == 'no' or con == 'n':
            print("Thank you for using the password Generator")
            break  
if __name__ == "__main__":
    main()
