import os
from bs4 import BeautifulSoup

# path_to_file = "D:\Документы\Книга_Геодезия_Дьяков"+"\\"+"0003_Содержание.htm"
path_work = "D:\Документы\Книга_Геодезия_Дьяков"
work_directory = [direct for direct in os.listdir(path_work) if os.path.isfile(path_work + "\\" + direct)]
for file in work_directory:
    path_to_file = path_work + "\\" + file
    with open(path_to_file, "r", encoding='utf-8') as f:
        soup = BeautifulSoup(f, "lxml", from_encoding='utf-8')
    links = soup.find_all("a")
    images = soup.find_all("img")
    i = 0
    x = 0
    error_links = []
    error_images = []
    print("-----------------------------------------------------------")
    print("Checking links in file {}...".format(path_to_file))
    for link in links:
        check_path = "D:\Документы\Книга_Геодезия_Дьяков" + "\\" + link["href"]
        if not (os.path.isfile(check_path)):
            i += 1
            error_links.append(link["href"])
    print("Checking images in file {} ...".format(path_to_file))
    for image in images:
        check_path = "D:\Документы\Книга_Геодезия_Дьяков" + "\\" + image["src"]
        if not(os.path.isfile(check_path)):
            x += 1
            error_images.append(image["src"])
    if i != 0:
        #n = input("File {} has bad links. Print them? y/n".format(file))
        #if n.lower() == "y":
        print("Errors in links: ")
        for j in range(1, len(error_links)):
            print(j, error_links[j])
    if x != 0:
        #n = input("File {} has bad links. Print them? y/n".format(file))
        #if n.lower() == "y":
        print("Errors in images: ")
        for j in range(1, len(error_images)):
            print(j, error_images[j])