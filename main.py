import requests
from bs4 import BeautifulSoup
import re
import time
import random

soup = BeautifulSoup(open('naval.html','r'), 'html.parser')

text = ""

dates = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
def contains_date(line):
    for date in dates:
        if date in line:
            return True
    return False

def beautify_and_save(text):
    print('beautifying...')
    text = text.replace('.', '. ')
    text = text.replace('.  ', '. ')
    print('saving...')
    with open('saved_text.html', 'w') as text_file:
        text_file.write(text)

for link in soup.find_all('a')[13:-19]:

    #print(link.get('href'))

    page = requests.get(link.get('href'))
    soup1 = BeautifulSoup(page.text, 'html.parser')
    soup1.prettify()

    soup_text = soup1.text
    soup_text.replace('\n', ' ')
    #print(soup_text)



    date_passed = False
    date_was_last_line = False
    for line in soup_text.splitlines():
        line = line.strip('\n')

        if "Subscribe to Naval" in line:
            break

        if date_was_last_line == True and len(line) != 0:
            text += '<h2 class="chapter">' + line + '</h2>' + '\n\n\n\n'
            date_was_last_line = False
            continue

        if date_passed == False and contains_date(line) == True:
            date_passed = True
            date_was_last_line = True
            text
        if date_passed == False:
            continue

        text += line

    text += '\n\n\n\n\n\n\n\n\n\n\n'
    print('one done...')

    #if random.randint(0,50) == 5:
    #break

beautify_and_save(text)

print("DONE!!!")
