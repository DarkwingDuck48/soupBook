import re
import os


def checkpath(path):
    if not os.path.isdir(path):
        print("This directory doesn't exist.")
        return False
    else:
        return True


def checkfilename(files):
    filenames = files.split(",")
    errors = []
    pattern = r"\w*\.\w\w\w"
    for file in filenames:
        if re.match(pattern, file) is None:
            errors.append(file)
    if len(errors) != 0:
        print("You have {} mistakes in your filenames: ".format(len(errors)))
        print(",".join("{}".format(error) for error in errors))
        return False
    else:
        print("Good files. Start work.")
        return True
