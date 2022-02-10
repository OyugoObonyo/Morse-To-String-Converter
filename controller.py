"""
Module with the class that handles the encoding and decoding functionalities
"""
from data import CHARACTERS as chs


class Controller:
    """
    A class that handles the user input
    """
    def encode(self, string):
        """
        Method that converts string to morse code
        """
        conversion = ""
        for ch in string:
            for key in chs:
                if key == ch:
                    print(ch)
                    print(key)
                    print(chs[key])
                    conversion += chs[key]
                    
        print(f"{string} succesfully converted to morse")
        print(f"Morse code: {conversion}")

    def decode(self, morse_code):
        """
        Method that converts morse code to string
        """
        pass