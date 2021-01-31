# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup


# def enter_info():

value = input("Please enter your question:\n")


# extract keywords

payload = {'term': value, 'format': 'abstract', 'size': '10'}

response = requests.get("https://pubmed.ncbi.nlm.nih.gov/", params=payload)
# print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

#for script in soup(["script", "style", ""]):
#    script.extract()

#output = soup.prettify()
#print(output)
counter=0

total_results = soup.find(class_='value')
titles_blocks = soup.find_all("h1", class_="heading-title")
abstracts = soup.find_all(class_="abstract-content selected")
# print(abstracts)
for abstr in abstracts:
    # print(abstr.get_text(strip=True))
    result = abstr.get_text(strip=True).partition("Conclusion") [2]
    # print(result)
    result2 = abstr.get_text(strip=True).partition("conclusion")[2]
    # print(result2)


for titles in titles_blocks:
    lines = titles.get_text().strip()
    counter += 1
    if counter%2 != 0:
        continue
    print(lines)

print("Total Number of Research Articles: " + total_results.get_text())

counter = int(counter/2)
# print(counter)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('image.jpg')
imgplot = plt.imshow(img)
plt.show()

# access database
# search for keywords

# link to new article
# then analyze article (maybe)

# scrape article/abstracts
# find and return key info


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
