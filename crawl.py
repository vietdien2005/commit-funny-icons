from bs4 import BeautifulSoup
import requests
import os

def crawl():
    page = 41
    data = []
    num = 1
    for x in xrange(1, page):
        link = 'http://dongerlist.com/page/' + str(x)
        print(link)
        body = requests.get(link)
        obj_save = {'icon': ''}
        html = BeautifulSoup(body.text, "html.parser")
        icons = html.find_all('textarea', {'class': 'donger'})
        for i in icons:
            # print(i.text.strip())
            obj_save['icon'] = i.text.strip()
            data.append(obj_save)
            with open('icons/' + str(num) + '.txt','w') as file:
                print >> file, i.text.encode('utf-8').strip()
                num+=1
        # print(obj_save)
    return data

if __name__ == '__main__':
    if not os.path.isdir("icons"):
        os.makedirs("icons")
    crawl()
