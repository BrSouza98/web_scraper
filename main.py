#First, you need to import our class WebScraper
from WebScraper import WebScraper

#Now, create an new Object's WebCraper
futebol_scraper = WebScraper

#Define your url were the datas will be mining
futebol_scraper.setUrl(futebol_scraper, 'https://www.Globo.com/')

#you can create an list with your self keywords to find what do you need
futebol_scraper.setKeywords(futebol_scraper, ['São Paulo', 'Palmeiras', 'Corinthians', 'Santos', 'Campeonato Paulista'])

#If you need an text file withi the links Scraped, this function will made it to you!!
futebol_scraper.save_links(futebol_scraper, 'Relatório Futebol - Uol')

