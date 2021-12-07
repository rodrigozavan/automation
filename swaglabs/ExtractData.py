from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ExtractData:
    def __init__(self):
        pass

    def get_html(self, driver):
        try:
            html = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))
            html = str(html.get_attribute('innerHTML'))
            parser = BeautifulSoup(html, 'html.parser')
            return parser
        except:
            return {'error': True, 'data': 'Erro ao extrair html'}

    def filter_html(self, parser):
        try:
            items = parser.find_all('div', {'class': 'inventory_item'})
            dicts = []
            for item in items:
                name = item.find('div', {'class': 'inventory_item_name'}).text
                desc = item.find('div', {'class': 'inventory_item_desc'}).text
                price = item.find('div', {'class': 'inventory_item_price'}).text
                link_img = 'https://www.saucedemo.com' + str(item.find('img', {'class': 'inventory_item_img'}).attrs['src'])
                price = str(price).replace('$', '')
                data = {'name': name, 'description': desc, 'price': price, 'link_img': link_img}
                dicts.append(data)
            return dicts
        except:
            return {'error': True, 'data': 'Erro ao extrair dados do html.'}
