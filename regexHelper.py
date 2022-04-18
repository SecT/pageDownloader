#Wrapper for basic regex operations to be used by other projects
#version 1.0

import re

class RegexHelper:
    def __init__(self):
        pass

    def generateSingleMatch(pattern, content):  # static method
        result = re.search(pattern, content)

        if result is not None:
            match = result.group()

            return match
        else:
            return False

    def generateMultipleMatches(pattern, content):
        result = re.findall(pattern, content)

        if len(result) > 0:
            matches = result

            return matches
        else:
            return False
