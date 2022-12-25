import random
import string
import pyperclip
import time

plength = int(input("How long would you like your password to be?"))



def rp(length):
    result_str = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+.`~') for i in range(length)))
    print(result_str)
    ctc = (input("Would you like to copy this password to clipboard? (Y/N)"))
    if ctc == "Y":
        pyperclip.copy(result_str)
        print("success!")
        time.sleep(1)
    if ctc == "y":
        pyperclip.copy(result_str)
        print("success!")
        time.sleep(1)
    if ctc =="N":
        print("Ok!")
        time.sleep(1)
    if ctc =="n":
        print("Ok!")
        time.sleep(1)
    save = (input("Would you like to save this to the database?(Y/N)"))
    if save == "N":
        exit()
    if save == "n":
        exit()
    name = (input("And what is the name of the platform this password is for?"))
    user = (input("And what is your username/email for this website?"))
    if save == "Y":
        lines = [name, result_str]
        with open("Passwords.txt", "a") as file:
         file.write('\n')
         file.write('\n')
         file.write(name)
         file.write('\n')
         file.write(user)
         file.write('\n')
         file.write(result_str)
        
        print('Success!')
        time.sleep(1)
        pass
    if save == "y":
        lines = [name, result_str]
        with open("Passwords.txt", "a") as file:
         file.write('\n')
         file.write('\n')
         file.write(name)
         file.write('\n')
         file.write(user)
         file.write('\n')
         file.write(result_str)
         print('Success!')
         time.sleep(1)
         pass

    

   
    



rp(plength)

while True:
    redo = input("Would you like to generate another password? (Y/N) ")
    result_str = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-=+') for i in range(rplength)))



    if redo == "Y":
        rplength = int(input("How long would you like your password to be?"))
        rp(rplength)


    if redo == "y":
        rplength = int(input("How long would you like your password to be?"))
        rp(rplength)

    if redo == "N":
        print("Ok! Closing...")
        time.sleep(3)
        break


    if redo == "n":
        print("Ok! Closing...")
        time.sleep(3)
        break
    save = (input("Would you like to save this to the database?(Y/N)"))
    if save == "N":
        exit()
    if save == "n":
        exit()
    name = (input("And what is the name of the platform this password is for?"))
    if save == "Y":
        lines = [name, result_str]
        with open("Passwords.txt", "a") as file:
         file.write('\n')
         file.write('\n')
         file.write('\n')
         file.write('\n'.join(lines))
         break
    if save == "y":
        lines = [name, result_str]
        with open("Passwords.txt", "a") as file:
         file.write('\n')
         file.write('\n')
         file.write('\n')
         file.write('\n'.join(lines))
         break