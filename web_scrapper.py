from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

page_html = urlopen("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en").read()
soup = BeautifulSoup(page_html, "html.parser")
relevance_list = ['internal security', 'constitution', 'state', 'states', 'Coronavirus', 'Police', 'Government', 'govt',
                  'India', 'Lok Sabha', 'NASA', 'RBI', ]
irrelevant_list = ['cricket', 'T20 World Cup', 'semifinals', 'finals', 'bollywood', 'hollywood', 'movie',
                   'review', 'Tennis', 'sports', 'IPL']

csv_file = open('news_excel.csv', "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'links'])
container_counter = 0


def check_relevency(headline, rel_list, irr_list):
    for x in rel_list:
        if headline.__contains__(x):
            for y in irr_list:
                if not headline.__contains__(y):
                    return True

        else:
            x = x.lower()
            if headline.__contains__(x):
                for y in irr_list:
                    y = y.lower()
                    if not headline.__contains__(y):
                        return True


for container in soup.find_all("div", class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf"):
    container_counter = container_counter + 1
    print(container_counter)
    print()
    for article in container.find_all("article"):
        headline = article.find("a", class_="DY5T1d").text
        if check_relevency(headline, relevance_list, irrelevant_list):
            link = article['jslog'].split()[1][2:]
            csv_writer.writerow([headline, link])
