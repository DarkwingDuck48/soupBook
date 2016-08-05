import re
import os


def checkpath(path):
    if not os.path.isdir(path):
        return False
    else:
        return True


def checkfilename(files):
    filenames = files.split(",")
    errors = []
    pattern_full = r"\w*\.\w\w\w"
    pattern_after_dot = re.compile("\.\w\w\w$")
    pattern_before_dot = re.compile('^\w*')
    for file in filenames:
        if re.match(pattern_full, file) is None:
            errors.append(file)
    if len(errors) != 0:
        #print("You have {} mistakes in your filenames: ".format(len(errors)))
        #print(",".join("{}".format(error) for error in errors))
        return errors
    else:
        return "0"