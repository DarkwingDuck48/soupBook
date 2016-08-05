import os
import stat
import checks

class DeleteByMask:
    def __init__(self, path, todelete):
        """

        :param path: путь к целевой директории
        :param todelete: имена файлов с расширениями для удаления
        """
        self.todelete = todelete
        # Проверка имени файла на соответствие образцу - имяфайла.расширение
        if checks.checkfilename(self.todelete) != "0":
            raise Exception("You have {} wrong filenames".format(len(checks.checkfilename(self.todelete))))
        else:
            print("Filenames is valid")
        self.path = path
        if not(checks.checkpath(self.path)):
            raise Exception("This directory doesn't exist! Check it!")
        self.withchange = 0
        self.withoutchange = 0
        self.error_permission = 0
        self.error_notadirectory = 0

    def deletefiles(self):
        """
        Функция удаления файлов в каталоге по введеному пути и с введенными именами
        :return: True по окончанию действия
        """
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
        return True

    def cleandir(self):
        """
        Очищает выбранную директорию от пустых папок
        :return: True по окончанию действия
        """
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
        return True


if __name__ == "__main__":
    path = input("Type path to directory - ")
    while not checks.checkpath(path):
        path = input("Type path to directory - ")

    filenames = input("Type filenames which you want to delete (exm: filename.exe)\n")
    while not checks.checkfilename(filenames):
        filenames = input("Type filenames which you want to delete (exm: filename.exe)\n")
