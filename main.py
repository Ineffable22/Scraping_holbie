#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from correo import username, password
from sys import argv

def main():
    user = "Ineffable22/"
    git = "https://github.com/" + user
    url = 'https://intranet.hbtn.io/auth/sign_in'
    num = argv[1]
    with requests.Session() as session:
        txt = session.get(url)
        soup = BeautifulSoup(txt.text, 'html.parser')
        code = soup.select('form > input[name="authenticity_token"]')[0].get('value')
        check = {
            'user[login]': username,
            'user[password]': password,
            'commit': 'submit',
            'authenticity_token': code,
        }
        re_1 = session.post(url, data=check)
        new_url = "https://intranet.hbtn.io/projects/{}".format(num)
        # guarda en index la página principal
        with open("index.html", "w") as fo:
            fo.write(re_1.text)
        # guarda en project el proyecto actual
        re_2 = session.get(new_url)
        with open("project.html", "w") as fo:
            fo.write(re_2.text)
 #       print("nueva pagina -> " + new_url)
        soup = BeautifulSoup(re_2.text, 'html.parser')
        directory = soup.select('div.list-group-item>ul>li>code:nth-child(1)')
        directory = directory[0].get_text()
#        print("directory -> ", directory)
        tittle = soup.select('div>h1.gap')
        File = soup.select('div.list-group-item>ul>li:nth-child(3)')
#        print("title")
        tittle = tittle[0].get_text()
#        print(tittle)
#        print("File")


        with open("README.md", "w") as fo:
            Files = ""
            fo.write("# " + tittle + "\n\n" + "## Description:\n\n## Files\n\n")
            tittle = tittle.replace(" ", "")
            tittle = tittle.replace(".", "-")
            tittle = tittle.replace(",", "_")
            tittle = tittle.lower()
            for i in File:
                line = i.get_text()[6:]
                if "," in line:
                    lines = line.split()
#                    lines = lines.repace
                    for j in lines:
                        url_git = git + directory + "/blob/main/" + tittle + "/" + j
                        fo.write("### [" + j  + "](" + url_git + ")" +"\n\n")
                else:
                    url_git = git + directory + "/blob/main/" + tittle + "/" + line
                    fo.write("### [" + line  + "](" + url_git + ")" +"\n\n")
            print(Files)
        fo.close()




if __name__ == '__main__':
    main()
