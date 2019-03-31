'''
Made by Gritchin Oleg

Parser of 6pm.com

Part of sales bot for telegram
Hisname is @DiscountNotificator_bot

github: github.com/oleggr/6pm_parser
telegram: t.me/grit4in
'''


import datetime
import urllib.request
from bs4 import BeautifulSoup


URL = 'https://www.6pm.com/null/.zso?s=percentOff/desc/'
#eplyes = []


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_html_from_file(filename='6pm.html'):

    with open (filename, 'r') as f:
        html = f.read()

    return html


def parse(html):

    replyes = []

    soup = BeautifulSoup(html, features="html.parser")

    #print(soup)

    sales_page = soup.find('div', class_ = '_3a_mTsgKrQ')

    articles = sales_page.find_all('article')

    for article in articles:

        current_price = float(article.find('span', class_='_3g-jZuDv10 A3nFJo4_bv').text.split('$')[1])
        standart_price = float(article.find('span', class_='_2GD3fhboDf').text.split('$')[1])
        discount = 100 - round((current_price / standart_price) * 100, 2)
        link = 'https://www.6pm.com' + article.a.get('href')
        # name1 = article.find('p', class_ = '_1HOLv').span.text
        name = '*' + article.find('p', class_ = 'tvGtN07acv').span.text \
                + '*\n_' \
                + article.find('p', class_ = '_3J_2hAUBnw').text + '_'

        if discount > 87.0:
            message = name + '\n' \
                    + 'Price now: ' + str(current_price) + '\n' \
                    + 'Standart price: ' + str(standart_price) + '\n' \
                    + 'Discount: *' + str(discount) + '*\n' \
                    + '[link to 6pm](' + link + ')' + '\n\n'

            #return message
            replyes.append(message)


        # print()
        # # print('name1: ' + name1)
        # print('name: ' + name)
        # print('\ncurrent_price: ' + str(current_price))
        # print('\nstandart_price: ' + str(standart_price))
        # print('\ndiscount: ' + str(discount) + '%')

        # print()
        # print('=======================')

    return replyes


#if __name__ == '__main__':
#    print(parse(get_html_from_file()))
