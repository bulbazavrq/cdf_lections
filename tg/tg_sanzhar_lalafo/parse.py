from bs4 import BeautifulSoup
import requests
import csv

url_ = 'https://lalafo.kg/'

def parsing_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    container = soup.find('div', class_ = 'business-profile-feed__container')
    inner_container = container.find('article', class_ = 'adTile-wrap')
    products =  container.find_all('article', class_ = 'adTile-wrap')
    result = []
    # for product in products:
    #     description = product.find('a', class_ = 'adTile-mainInfo').find('div', class_ = 'adTile-title__wrap').find('span', class_ = 'adTile-title').text
    #     price = product.find('a', class_ = 'adTile-mainInfo').find('p').text
    #     img = product.find('a', class_ = 'adTile-mainInfo').find('div', class_ = 'adTile-image').find('picture').find('img').get('src')
    #     data = {'description': description, 'price': price, 'img': img}
    #     result.append(data)
    #     write_to_csv(result)


def write_to_csv(data:list):
    with open('notnik.xls', 'w') as f:
        c = 1
        fieldnames = ['№', 'description', 'price', 'image']
        writer = csv.DictWriter(f, fieldnames)
        writer.writerow({
            '№': '№',
            'description': 'Description:',
            'price': 'Price:',
            'image': 'Image Url:'
        })
        for i in data:
            writer.writerow({
                '№': c,
                'description': i['description'],
                'price': i['price'],
                'image': i['img']
            })
            c += 1


parsing_data(url_)
