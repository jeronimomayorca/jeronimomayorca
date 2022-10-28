from skills import codding
from utils import tools

class SoftwareDeveloper:

    def __init__(self):
        self.name = "Jeronimo Mayorca Arias"
        self.role = "Student"
        self.language_spoken = ["Spanish", "English"]
        self.code = [codding.Python, codding.HTML, codding.others]
        self.tools = [tools.Angular, tools.Chalice]
        self.interests = ["Learn", "Programming", "Tech", "Best practices", "AWS"]

    def say_hi(self):
        print("Thanks for dropping by, hope you find some of my work interesting.")


me = SoftwareEngineer()
me.say_hi()
