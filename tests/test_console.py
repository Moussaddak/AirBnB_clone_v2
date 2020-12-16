import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):

    def test_create_not_exist(self):
        with patch('sys.stdout', new=StringIO()) as testOutput:
            HBNBCommand().onecmd("create fake_state")
        output = testOutput.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_no_exist(self):
        with patch('sys.stdout', new=StringIO()) as testOutput:
            HBNBCommand().onecmd("create")
        output = testOutput.getvalue().strip()
        self.assertEqual(output, "** class name missing **")


if __name__ == '__main__':
    unittest.main()
