import requests
from bs4 import BeautifulSoup



url = 'https://books.toscrape.com/'

# The url for each page is generated appending this to the url
added_url_per_page = 'catalogue/page-{}.html'

response = requests.get(url)
if response.status_code == 200:
    html = response.text # to get the text
    parsed_html = BeautifulSoup(response.content, "html.parser")

    pager_footer = parsed_html.find('ul', class_='pager')
    n_pages = int(pager_footer.find('li', class_='current').text.replace('Page 1 of ', ''))

    n_results = parsed_html.find('form', class_='form_horizontal').find('strong').text
    print(n_results)

    for i in range(1, n_pages + 1):
        page_url = (url + added_url_per_page).format(i)

