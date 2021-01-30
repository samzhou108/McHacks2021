import requests
from bs4 import BeautifulSoup



def read_url(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    blacklist2 = ['style', 'script', 'head', 'title', 'meta', '[document]',
                  'header', 'html', 'noscript', 'input', 'footer']


    for t in text:
        if t.parent.name not in blacklist2:
            output += '{} '.format(t)

    good_text = str(output)
    good_text = good_text.split("\n")
    good_text = [s for s in good_text if s != ' ']
    good_text = ",".join(good_text)

    return good_text

url = 'https://www.aljazeera.com/news/2020/9/20/coronavirus-all-you-need-to-know-in-under-500-words'
good_text = read_url(url)
print(good_text)