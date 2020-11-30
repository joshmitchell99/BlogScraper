# import requests
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(open('articles.html','r'), 'html.parser')
#
# text = ""
#
# def print_font(str):
#     print(str)
#
# for link in soup.find_all('a')[1:]:
#
#
#
#     print(link.get('href'))
#
#     page = requests.get("http://paulgraham.com/" + link.get('href'))
#     soup1 = BeautifulSoup(page.text, 'html.parser')
#     soup1.prettify()
#
#     table = soup1.find('table', border=0, cellspacing=0, width=435)
#     font = table.find('font', size=2)
#     print_font(font)
#
#     # for text in all_text:
#     #     print(text.text)
#
#     #text += soup1.get_text()
#
#     break
#
# #with open('saved_text.txt', 'w') as text_file:
# #    text_file.write(text)
# print("DONE!!!")














import requests
from bs4 import BeautifulSoup
import re
import time
import random

soup = BeautifulSoup(open('articles.html','r'), 'html.parser')

text = ""

for link in soup.find_all('a')[1:]:



    #print(link.get('href'))

    page = requests.get("http://paulgraham.com/" + link.get('href'))
    soup1 = BeautifulSoup(page.text, 'html.parser')
    soup1.prettify()

    i = 0

    soup_text = soup1.text
    soup_text.replace('\n', ' ')

    soup_text = soup_text.replace('Want to start a startup?', ' ', 1)
    soup_text = soup_text.replace('Get funded by', ' ', 1)
    soup_text = soup_text.replace('Y Combinator.', ' ', 1)


    text += '<h2 class="chapter">'
    for word in soup_text.split():
        #print(word)
        if i < 30 and word[0:3].isdigit():
            text += word[:4] + "</h2> \n\n" + word[4:] + ' '
        else:
            text += word + " "
        i += 1

    text += '\n\n\n\n\n\n\n\n\n\n\n'
    print('one done...')

    # if random.randint(0,5) == 5:
    #      break

with open('saved_text.html', 'w') as text_file:
    text_file.write(text)
print("DONE!!!")
