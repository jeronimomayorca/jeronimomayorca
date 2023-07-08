### Hi there 👋
#!/usr/bin/python
# -*- coding: utf-8 -*-

from skills import codding
from utils import tools

class SoftwareDeveloper:

    def __init__(self):
        self.name = "Jeronimo Mayorca Arias"
        self.role = "Software Developer"
        self.language_spoken = ["es_CO", "en_US"]
        self.code = [codding.Python, codding.Javascript, codding.Php, codding.Java, codding.VTL, codding.front,]
        self.tools = [tools.Angular, tools.Bootstrap]
        self.interests = ["Learn", "Programming", "Tech", "Best practices"]

    def say_hi(self):
        print("Thanks for reading this, hope you find some of my work interesting.")


me = SoftwareEngineer()
me.say_hi()
