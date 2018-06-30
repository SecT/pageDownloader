import re

class RegexHelper:
    def __init__(self):
        pass

    def generateSingleMatch( pattern, content):  #static method
        result = re.search(pattern, content)

        if result is not None:
            match = result.group()

            return match
        else:
            return False