import os, stat
from bs4 import BeautifulSoup


path_work = "D:\Документы\Книга_Геодезия_Дьяков"
workdir = [direct for direct in os.listdir(path_work) if os.path.isfile(path_work+"\\"+direct)]
print(workdir)
for direct in workdir:
    path_to_file = path_work+"\\"+direct
    if os.access(path_to_file, os.R_OK):
        os.chmod(path_to_file, stat.S_IRWXU)
    file = open(path_to_file, "r+", encoding='windows-1251')
    soup = BeautifulSoup(file, "lxml", from_encoding="windows-1251")
    links = soup.find_all("a")
    images = soup.find_all("img")
    print("----------------------------------------------------------------------------------------------------------")
    print("Изменяемый файл - ", path_to_file)
    for link in links:
        if link.string == "Об авторах" and link['href'] != "0002_Об_авторах.htm":
            link['href'] = "0002_Об_авторах.htm"
        elif link.string == "Содержание" and link['href'] != "0003_Содержание.htm":
            link['href'] = "0003_Содержание.htm"
        elif str(link.string).startswith("Предыдущий раздел") or str(link.string).startswith("Следующий раздел"):
            if str(link.string).startswith("Предыдущий раздел"):
                print("This is previous file for {1} is {0}".format(workdir[workdir.index(direct)-1], direct))
                link['href'] = workdir[workdir.index(direct)-1]
            elif str(link.string).startswith("Следующий раздел"):
                if workdir.index(direct) + 1 < len(workdir):
                    print("This is next file for {1} is {0}".format(workdir[workdir.index(direct) + 1], direct))
                    link['href'] = workdir[workdir.index(direct) + 1]
                else:
                    print("Files finish.")
                    link['href'] = workdir[0]
        print(link)
    print("----------------------------------------------------------------------------------------------------------")
    for image in images:
        if image['src'].endswith("turnbook.gif"):
            image['src'] = "Files/book/turnbook.gif"
        elif image['src'].endswith('left.gif'):
            image['src'] = "Files/hand/left.gif"
        elif image['src'].endswith('right.gif'):
            image['src'] = "Files/hand/right.gif"
        else:
            folder = direct.split(".")
            filename = image['src'].split("/")
            image['src'] = "Files/pages/"+folder[0][14:].strip()+"/"+filename[-1].strip()
    file2 = open(path_to_file, "w+", encoding='utf-8')
    file2.write(soup.prettify())
    file2.close()

