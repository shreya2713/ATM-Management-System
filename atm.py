import time
import datetime
import pyttsx3
import os
import getpass
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.say("Hi Sir")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning. Please insert your card.")
    elif hour < 18:
        speak("Good afternoon. Please insert your card.")
    else:
        speak("Good evening. Please insert your card.")
    
    #for card processing
    time.sleep(3)

    password = 1234
    attempts = 3

    while attempts > 0:
        #taking atm pin from user
        speak("Please enter your ATM pin:")
        pin = getpass.getpass(prompt="Enter your ATM pin: ")

        #checking pin is valid or not 
        if pin == str(password):
            #user account balance
            balance = 5000

            #loop will run until user gets free 
            while True:

                #Showing  info to user
                speak(""" 
                    1 = balance
                    2 = withdraw balance
                    3 = deposit balance
                    4 = exit
                    """)

                try:    
                    #taking an option from user
                    option = int(input("Please enter your choice: "))
                except:
                    speak("Please enter a valid option")
                
                #for option 1        
                if option == 1:
                    speak(f"Your current balance is {balance}")
                                     
                if option == 2:
                    speak("Please enter the amount you want to withdraw:")
                    withdraw_amount = int(input("Please enter withdraw_amount: "))
                    if withdraw_amount >= balance:
                        speak("Insufficient balance.")
                        continue
                    if withdraw_amount < (balance - 1000):
                        speak("You cannot withdraw the amount less than deposit amount by 1000.")
                        continue
                    balance = balance - withdraw_amount
                    speak(f"{withdraw_amount} is debited from your account:")
                    speak(f"Your updated balance is {balance}.")
                
                if option == 3:
                    speak("Please enter the amount you want to deposit:")
                    deposit_amount = int(input("Please enter deposit_amount: "))
                    balance = balance + deposit_amount
                    speak(f"{deposit_amount} is credited to your account:")
                    speak(f"Your updated balance is: {balance}.")

                if option == 4:
                    break
            break
        else:
            attempts -= 1
            if attempts > 0:
                speak(f"Wrong pin. Please try again! You have {attempts} attempts left.")
            else:
                speak("Your pin is blocked. Please contact your bank for assistance.")
                break