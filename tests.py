"""
Module that tests our application's functionality
"""
from lib2to3.pygram import Symbols
import string
import unittest
from controller import Controller


class ControllerTestCase(unittest.TestCase):
    """
    Test the controller class
    """
    def setUp(self) -> None:
        self.control = Controller()

    def test_word_to_morse(self):
        string = "BRUNO"
        expected_output = "-... .-. ..- -. ---"
        self.assertEqual(self.control.encode(string), expected_output)

    def test_morse_to_word(self):
        morse = "-... .-. ..- -. ---"
        expected_output = "BRUNO"
        self.assertEqual(self.control.decode(morse), expected_output)

    def test_words_to_morse(self):
        words = "BRUNO IS TESTING"
        expected_output = "-... .-. ..- -. --- / .. ... / - . ... - .. -. --."
        self.assertEqual(self.control.encode(words), expected_output)

    def test_morse_to_words(self):
        morse = "-... .-. ..- -. --- / .. ... / - . ... - .. -. --."
        expected_output = "BRUNO IS TESTING"
        self.assertEqual(self.control.decode(morse), expected_output)

    def test_morse_to_numbers(self):
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(self.control.decode(morse), expected_output)

    def test_symbols_to_morse(self):
        symbols = "&'@)(:,=!.-+\"?/"
        expected_output = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        self.assertEqual(self.control.encode(symbols), expected_output)

    def test_morse_to_symbols(self):
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        expected_output = "&'@)(:,=!.-+\"?/"
        self.assertEqual(self.control.decode(morse), expected_output)

if __name__ == "__main__":
    unittest.main()
