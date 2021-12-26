from bs4 import BeautifulSoup
from utils.Waits import Waits


class ExtractData:
    def __init__(self):
        self._waits = Waits.Wait()

    def get_html(self, driver):
        try:

            html = self._waits.wait_by_presence(driver=driver, time=10, name_element=('class name', 'inventory_list'))
            html = str(html.get_attribute('innerHTML'))
            parser = BeautifulSoup(html, 'html.parser')

            if not html or not parser:
                return {'error': True, 'data': 'Erro ao extrair dados do html.', 'type': f'Elemento não encontrado',
                        'method': 'get_html'}
            else:
                return parser

        except Exception as e:
            return {'error': True, 'data': 'Erro ao extrair dados do html.', 'type': f'{e}', 'method': 'get_html'}

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
        except Exception as e:
            return {'error': True, 'data': 'Erro ao extrair dados do html.', 'type': f'{e}', 'method': 'filter_html'}
