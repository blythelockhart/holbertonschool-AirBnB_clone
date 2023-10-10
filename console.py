#!/usr/bin/python3
"""Module for the console that contains entry point of command interpreter"""


import cmd
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        # split args to get command and class name
        class_name = args.split()
        if not class_name:
            print("** class name missing **")
            return
        if class_name != ['BaseModel']:
            # atm, if class name is not BaseModel, it doesn't exist
            # will need to be changed when other classes are implemented
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save
        print(new_instance.id)
        return

    def do_show(self, args):
        """Prints string rep of an instance based on class name and id"""
        # splits args to get class name and id
        argv = args.split()

        if not argv:
            print("** class name missing **")
            return
        class_name = argv[0] # get class name
        if class_name != 'BaseModel':
            # atm, if class name is not BaseModel, it doesn't exist
            # will need to be changed when other classes are implemented
            print(class_name)
            print("** class does not exist **")
            return
        if len(argv) < 2:
            print("** instance id missing **")
            return
        instance_id = argv[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
        if instance_key in all_objects:
            instance = all_objects[instance_key]
            print(instance)
            return
        else:
            print("** no instance found **")
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()  # starts the interpreter loop
