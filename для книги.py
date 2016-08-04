import os
import stat
import re
import checks

class DeleteByMask:
    def __init__(self, path, todelete):
        self.todelete = todelete
        self.path = path
        self.withchange = 0
        self.withoutchange = 0
        self.error_permission = 0
        self.error_notadirectory = 0

    def deletefiles(self):
        workdir = os.listdir(self.path)
        for direct in workdir:
            path_2 = self.path + '\\' + direct
            if os.path.isdir(path_2):
                try:
                    new_direct = os.listdir(path_2)
                except NotADirectoryError:
                    self.error_notadirectory += 1
                    continue
                for file in new_direct:
                    if file in self.todelete:
                        try:
                            if os.access(path_2 + '\\' + file, os.R_OK):
                                os.chmod(path_2 + '\\' + file, stat.S_IRWXU)
                                os.remove(path_2 + '\\' + file)
                                self.withchange += 1
                                print("I'm change rights and delete {}".format(file))
                            else:
                                os.remove(path_2 + '\\' + file)
                                self.withoutchange += 1
                                print("I'm delete {}".format(file))
                        except PermissionError:
                            self.error_permission += 1
                            print('No access to file ' + path_2 + '\\' + file)
                            continue

    def cleandir(self):
        workdir = os.listdir(self.path)
        for direct in workdir:
            path_2 = self.path + '\\' + direct
            if os.path.isdir(path_2):
                try:
                    path_2 = path + "\\" + direct
                    os.chmod(path_2, stat.S_IRWXU)
                    new_direct = os.listdir(path_2)
                    if not new_direct:
                        os.rmdir(path_2)
                        print("Remove " + path_2)
                except NotADirectoryError:
                    continue

# Hi
if __name__ == "__main__":
    path = input("Type path to directory - ")
    while not checks.checkpath(path):
        path = input("Type path to directory - ")

    filenames = input("Type filenames which you want to delete (exm: filename.exe)\n")
    while not checks.checkfilename(filenames):
        filenames = input("Type filenames which you want to delete (exm: filename.exe)\n")
