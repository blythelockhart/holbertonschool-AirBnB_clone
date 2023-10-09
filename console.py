#!/usr/bin/python3
"""Module for the console that contains entry point of command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # prompt for imput

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True  # exits the interpreter loop

    def do_EOF(self, args):
        """EOF to exit the program"""
        return True # exits the interpreter loop

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()  # starts the interpreter loop
