"""
Module containing the program's main logic
"""
from controller import Controller

print(
   """
 _____                              _          
|     |___ ___ ___ ___    ___ ___ _| |___      
| | | | . |  _|_ -| -_|  |  _| . | . | -_|     
|_|_|_|___|_| |___|___|  |___|___|___|___|     
                                   _           
           ___ ___ ___ _ _ ___ ___| |_ ___ ___ 
          |  _| . |   | | | -_|  _|  _| -_|  _|
          |___|___|_|_|\_/|___|_| |_| |___|_|  
                                               
   """
)
proceed = True
while proceed:
    res = input("Enter 1 if you'd like to convert a string to morsecode or 2 if you'd like to convert morsecode to string: ")
    if res == "1":
        string = input("Enter string you'd like to convert: ").upper()
        action = Controller()
        action.encode(string)
    elif res == "2":
        morse = input("Enter morse code you'd like to decode: ")
        action = Controller()
        action.decode(morse)
    else:
        print("Program only accepts either 1 or 2 as input")
        break
    next_step = input("Enter 1 if you'd like to convert again or 2 if you'd like to exit: ")
    if next_step == "1":
        continue
    elif next_step == "2":
        print("Thank you for using our converter")
        proceed = False
    else:
        print("Program only accepts either 1 or 2 as input")
        break
