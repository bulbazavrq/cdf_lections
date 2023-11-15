from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.mashina.kg/search/all'
url_test = 'https://www.mashina.kg/details/toyota-land-cruiser-65267c4b2ba2b533629501'

def parsing_data(car_url):
    response = requests.get(car_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_ = 'main-info clr')

    name = soup.find('div', class_ = 'head-wrapper-main').find('h1').text
    price = soup.find('div', class_ = 'price-dollar').text

    preview_desc = container.find_all('div', class_ = 'right-side')
    preview_desc = preview_desc[-1].find_all('div')
    preview_desc_ls = []
    for p in preview_desc[:2:]:
        preview_desc_ls.append(p.text)
    desc = ''.join(preview_desc_ls).strip()

    fotorama_ls = []
    fotorama = container.find('div', class_ = 'fotorama').find_all('a')
    for img in fotorama:
        fotorama_ls.append(img.get('data-full'))

    car = {
        'name': name,
        'price': price,
        'desc': desc,
        'img': fotorama_ls}
    return car



def get_cars(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', class_ = 'table-view-list')

    cars = container.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        result.append(parsing_data('https://www.mashina.kg'+car.find('a').get('href')))

    write_to_csv(result)

################################################################

def write_to_csv(data:list):
    with open('detail_cars.csv', 'w') as file:
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
            'name': car['name'],
            'desc': car['desc'],
            'price': car['price'],
            'image': ''.join(x+'\n' for x in car['img']),
        })                       
            count += 1

get_cars(url)






















