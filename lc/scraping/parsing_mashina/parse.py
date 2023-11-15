from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.mashina.kg/search/all/'

def parsing_data():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_ = 'table-view-list')
    cars = container.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_ ='name').text.strip()
        img = car.find('img', class_='lazy-image').get('data-src')
        price = car.find('div', class_='block price').find('p').find('strong').text
        desc = ''.join(car.find('div', class_='item-info-wrapper').text.split())
        data = {'title': name, 'desc': desc, 'price': price, 'img': img}
        result.append(data)
    write_to_csv(result)


def write_to_csv(data:list):
    with open('cars.csv', 'w') as file:
        count = 1
        fieldnames = ['№', 'name', 'desc', 'price', 'image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'name': 'Name:',
            'desc': 'Description:',
            'price': 'Price:',
            'image': 'Image Url:',
        })
        for car in data:
            writer.writerow({
            '№': count,
            'name': car['title'],
            'desc': car['desc'],
            'price': car['price'],
            'image': car['img'],
        })                       
            count += 1

parsing_data()