import os,stat
from bs4 import BeautifulSoup
import re


pattern_bg = "white.gif"
pattern_book = "turnbook.gif"
path_work = "D:\Документы\Книга_Геодезия_Дьяков\Example"
workdir = os.listdir(path_work)
for direct in workdir:
    if os.path.isfile(path_work+"\\"+direct):
        path_to_file = path_work+"\\"+direct
        if os.access(path_to_file,os.R_OK):
            os.chmod(path_to_file, stat.S_IRWXU)
        file = open(path_to_file, "r+", encoding='windows-1251')
        soup = BeautifulSoup(file, "lxml", from_encoding="windows-1251")
        links = soup.find_all("a")
        images = soup.find_all("img")
        print(path_to_file)
#        for link in links:
#            if re.match(pattern,link['href']):
#                link['href'] = 'Files/background/white.gif'
        for image in images:
            if image['src'].endswith(pattern_book):
                image['src'] = "Files/book/turnbook.gif"
            print(image['src'])
        print(type(soup.prettify()))
        file2 = open(path_to_file, "w+", encoding='utf-8')
        file2.write(soup.prettify())
        file2.close()

