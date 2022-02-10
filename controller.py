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
                    conversion += chs[key]
            conversion += " "

        # remove the final blank line
        conversion = conversion.rstrip()
        print(f"Morse code: {conversion}")
        return conversion

    def decode(self, morse_code):
        """
        Method that converts morse code to string
        """
        morse_code = morse_code.split(" ")
        conversion = ""
        for ch in morse_code:
            for key in chs:
                if chs[key] == ch:
                    conversion += key

        print(f"String: {conversion}")
        return conversion
