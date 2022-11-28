import random,ctypes
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
def NewPassword(lengh):
	password = "" 
	for i in range(int(lengh)):
		char1 = random.choice(chars)
		password = password + char1
	return password

def MassCreatePasswords(amout, lengh):
	pswds = []
	for i in range(int(amout)):	
		psw1=NewPassword(lengh)
		pswds.append(psw1)
	return pswds

def Logo():
	print("""
  ___                              _    ___                       _           
 | _ \__ _ _______ __ _____ _ _ __| |  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_| \__,_/__/__/\_/\_/\___/_| \__,_|  \___\___|_||_\___|_| \__,_|\__\___/_|  
                                                                              """)
	print("\t\t\t\t Made by github.com/x47base\n\n")

def Programm():
	ctypes.windll.kernel32.SetConsoleTitleW("Password Generator | Made by DbomDev")
	Logo()
	print("Welcome to the Password Generator. How may we help you today? ")
	print("\n Options: 1 - Generart Password\n\t  2 - Mass Generate Passwods\n\t  3 - Set Characters")
	choice = int(input("\nTool > "))
	if choice == 1:
		lengh = input("\nLengh > ")
		mypass = NewPassword(lengh)
		print(f'\nYour Generated Password is: \n{mypass}')
		print("\n########\tJob Done!\t########\n\n\n")
	elif choice == 2:
		amount = input("\nAmount > ")
		lengh = input("\nLengh > ")
		mypasses = MassCreatePasswords(amount, lengh)
		print(f'\nYour Generated Passwords are:')
		for i in mypasses:
			print(i)
		print("\n#########\tJob Done!\t#########\n\n\n")
Programm()
