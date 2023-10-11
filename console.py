#!/usr/bin/python3
"""Module for the console that contains entry point of command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage


class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Place": Place,
              "Review": Review, "Amenity": Amenity}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # prompt for imput

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True  # exits the interpreter loop

    def do_EOF(self, args):
        """EOF to exit the program"""
        return True  # exits the interpreter loop

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, args):
        """Creates a new instance of the class, saves it and prints the id"""
        # split args to get command and class name
        argv = args.split()
        if not argv:
            print("** class name missing **")
            return
        class_name = argv[0]  # get class name
        if class_name not in class_dict:
            # checks if class name exists
            print("** class doesn't exist **")
            return
        instance_class = class_dict[class_name]
        new_instance = instance_class()
        new_instance.save
        storage.save()
        print(new_instance.id)
        return

    def do_show(self, args):
        """Prints string rep of an instance based on class name and id"""
        # splits args to get class name and id
        argv = args.split()

        if not argv:
            print("** class name missing **")
            return
        class_name = argv[0]  # get class name
        if class_name not in class_dict:
            print(class_name)
            print("** class does not exist **")
            return
        if len(argv) < 2:
            print("** instance id missing **")
            return
        instance_id = argv[1]  # get id
        instance_key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
        if instance_key in all_objects:
            instance = all_objects[instance_key]
            print(instance)
            return
        else:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        argv = args.split()
        if not argv:
            print("** class name missing **")
            return
        class_name = argv[0]  # get class name
        if class_name not in class_dict:
            print(class_name)
            print("** class does not exist **")
            return
        if len(argv) < 2:
            print("** instance id missing **")
            return
        instance_id = argv[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            # checks if key is in storage dictionary
            print("** no instance found **")
            return
        # delete the key
        del storage.all()[instance_key]
        # save
        storage.save()

    def do_all(self, args):
        """Prints all string reps of instances based on class name"""
        argv = args.split()
        if not argv:
            print("** class name missing **")
            return
        class_name = argv[0]

        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
        all_instances = []

        for key, value in storage.all().items():
            if key.split('.')[0] == class_name:
                all_instances.append(str(value))
        print(all_instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        argv = args.split()
    
        if not argv:
            print("** class name missing **")
            return
        class_name = argv[0]  # Get class name
        if class_name not in class_dict:
            print("** class doesn't exist **")
            return
    
        if len(argv) < 2:
            print("** instance id missing **")
            return
        instance_id = argv[1]  # Get instance id
        instance_key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()
    
        if instance_key not in all_objects:
            print("** no instance found **")
            return
    
        if len(argv) < 3:
            print("** attribute name missing **")
            return
        attribute_name = argv[2]  # Get attribute name
    
        if len(argv) < 4:
            print("** value missing **")
            return
        attribute_value = argv[3]  # Get attribute value
        # Check if the attribute can be updated (string, integer, float)
        instance = all_objects[instance_key]
        attribute_type = type(getattr(instance, attribute_name, None))
    
        if attribute_type in [str, int, float]:
            # Cast the attribute value to the correct type
            if attribute_type == int:
                attribute_value = int(attribute_value)
            elif attribute_type == float:
                attribute_value = float(attribute_value)
            # Update the attribute
            setattr(instance, attribute_name, attribute_value)
            instance.save()
            storage.save()
        else:
            print("** cannot update attribute **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()  # starts the interpreter loop
