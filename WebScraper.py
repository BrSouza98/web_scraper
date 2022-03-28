import datetime
import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self):

        self.url = ''

        self.keywords = ['']



    def getUrl(self):
        return getattr(self, 'url')

    def setUrl(self, url):
        return setattr(self, 'url', url)

    def getKeywords(self):
        return getattr(self, 'keywords')

    def setKeywords(self, keywords=['']):
        return setattr(self, 'keywords', keywords)

    def addKeyword(self, keyword=['']):
        return self.keywords.append(keyword)

    def find_links_by_keywords(self):
        soup = BeautifulSoup(requests.get(self.getUrl(self)).content, 'html.parser')
        tags_a = soup.findAll('a')
        links_list = []
        for keyword in self.getKeywords(self):
            for tag_a in tags_a:
                if keyword.upper() in tag_a.text.upper():
                    links_list.append(tag_a['href'])


        return links_list

    def save_links(self, file_name='data' ):
        file_record = open(f'{file_name}.txt', 'a')
        file_record.write(f'Links salvos do site: {self.getUrl(self)} \n ############################# \n')
        links = self.find_links_by_keywords(self)

        for link in links:
            file_record.write(f'Link para notícia salva: {link}')
            file_record.write(f'\n')

        today = datetime.datetime.now()
        file_record.write(f' ####################### \n')
        file_record.write(f'Relatório gerado as {today.hour}:{today.minute}:{today.second} do dia {today.day}/{today.month}/{today.year} ')
        return
