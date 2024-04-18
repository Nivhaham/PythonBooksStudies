import webbrowser
import requests
from bs4 import BeautifulSoup
import sys

'''
This module is responsible for taking users keywords
runs a query in google and fetch all the links.
'''


def main():
    buildingUrlPath = ''
    for index, arg in enumerate(sys.argv[1:], start=1):
        buildingUrlPath = buildingUrlPath + arg + '+'
    buildingUrlPath = buildingUrlPath[:-1]
    url = f"https://www.google.com/search?q={buildingUrlPath}"
    response = requests.get(url)

    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    search_result_links = soup.find_all("a", href=True)
    webbrowser.open(url)
    print(search_result_links)


if __name__ == '__main__':
    main()
