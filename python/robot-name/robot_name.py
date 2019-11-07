from random import choices, seed
from string import ascii_uppercase, digits

class Robot(object):
    """A very loyal robot."""
    
    name: str
    all_robot_names = []

    def __init__(self):
        self.__set_name()

    def __set_name(self):
        seed()
        self.name = "".join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
        self.__verify_name()

    def __verify_name(self):
        if self.name in Robot.all_robot_names:
            self.reset() # reset if name is already taken
        else:
            Robot.all_robot_names.append(self.name) # if we get past that, record

    def reset(self):
        self.__set_name()
