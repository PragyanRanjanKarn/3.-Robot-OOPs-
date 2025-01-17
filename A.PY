class Robot:
    type = "machine"  # Class Variable: Common Variable for the class

    def __init__(self, name, model_year):
        self.name = name  # Instance Variable: specific to the object
        self.model_year = model_year  # Instance Variable: specific to the object

    def speak(self, message):
        return self.name + " says, '" + message + "'"

    def move(self):
        return self.name + " is now moving."

# Creating objects of the Robot class
robot1 = Robot("Robo", 2022)
robot2 = Robot("Mobo", 2023)

# Displaying details of each robot
print(robot1.name, "is a", robot1.type, "from the year", robot1.model_year)
print(robot2.name, "is a", robot2.type, "from the year", robot2.model_year)

# Robots performing actions
print(robot1.speak("Hello, humans!!"))
print(robot1.move())
print(robot2.speak("Have a good day!!"))
print(robot2.move())
