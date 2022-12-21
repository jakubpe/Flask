from bs4 import BeautifulSoup
import requests
QUOTES_URL = 'https://parade.com/1219723/alexandra-hurtado/thanos-quotes/'


def get_quotes():
    """prints thanos quotes"""
    response = requests.get(url=QUOTES_URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    findings = soup.find_all(class_='m-detail--body')
    all_p = findings[0].find_all_next('p')
    # print(all_p)
    for p in all_p:
        quote = p.text
        quote.replace('<p>', '')
        quote.replace('</p>', '')
        print(quote)

