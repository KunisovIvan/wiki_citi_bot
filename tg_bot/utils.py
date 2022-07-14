from urllib.parse import unquote

from lxml import etree
import requests
from bs4 import BeautifulSoup
from lxml.builder import unicode

from tg_bot.models import Locality, TypeOfLocality

base_url = 'https://ru.wikipedia.org/wiki'
base_xpath = '//div[@class="mw-parser-output"]'


def save_locality(table: int, elem):
    old_locality_dict = {l.title: l for l in Locality.objects.all()}

    to_create = []
    to_update = []

    row_count = len(elem.xpath(f'{base_xpath}//table[{table}]/tbody/tr'))
    for n in range(2, row_count + 1):
        link = elem.xpath(
            f'{base_xpath}/table[{table}]/tbody/tr[{n}]/td[2]/a'
        )
        if link:
            link = link[0]
            title = link.text
            href = base_url + unquote(link.attrib['href'])[5:]
            population = elem.xpath(
                f'{base_xpath}/table[{table}]/tbody/tr[{n}]/td[5]/text()[1]'
            )
            population = int(unicode(population[0]).replace(u'\xa0', u''))

            if title not in old_locality_dict:
                to_create.append(
                    Locality(title=title, href=href, population=population,
                             type=TypeOfLocality.citi
                             if table == 1 else TypeOfLocality.pgt)
                )
            else:
                old_l = old_locality_dict[title]
                old_l.href = href
                old_l.population = population
                old_l.type = (TypeOfLocality.citi
                              if table == 1 else TypeOfLocality.pgt)
                to_update.append(old_l)

    Locality.objects.bulk_create(to_create)
    Locality.objects.bulk_update(
        to_update, fields=['href', 'population', 'type']
    )


def parse_wiki_page():
    url = f'{base_url}/Городские_населённые_пункты_Московской_области'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    elem = etree.HTML(str(soup))
    save_locality(1, elem)
    save_locality(2, elem)
