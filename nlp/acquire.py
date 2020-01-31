


def get_article_text():
    from requests import get
    from bs4 import BeautifulSoup
    import os
    from os import path
    url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    headers = {'User-Agent': 'Codeup Ada Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text,features="lxml")
    article = soup.find('div', class_='mk-single-content')

    with open('article.txt', 'w') as f:
        f.write(article.text)

    return article.text

