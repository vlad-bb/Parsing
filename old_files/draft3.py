# while True:
#     age = input("How old are you? ")
#     try:
#         age = int(age)
#         if age >= 18:
#             print("Access allowed")
#             break
#         else:
#             print('Access denied')
#             break
#     except ValueError:
#         print(f'{age} is not a number. Please write number!')
#     finally:
#         print('-' * 30)

# some = set()
# for _ in range(10):
#     i = 'Title'
#     some.add(i)
# print(some)
import requests
from bs4 import BeautifulSoup

url = 'https://ottawa.bibliocommons.com/explore/bestsellers/5925_new_york_times'
html_doc = requests.get(url)

file = "old_files/example.html"
with open(file, "w") as fh:
    fh.write(html_doc.text)
with open(file) as fr:
    response = fr.read()

soup = BeautifulSoup(response, 'html.parser')
# print(soup)
books = soup.find('div', class_='cp_bib_list clearfix').find_all('div', class_='col-xs-12 list_item_outer clearfix')

for book in books:
    print(book.find('span', class_="title").text)
    print('-'*60)
