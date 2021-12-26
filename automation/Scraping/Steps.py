from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utils.Waits import Waits
from models import ScrapingModel


class Steps:
    def __init__(self):
        self._wait = Waits.Wait()
        self.db_scraping = ScrapingModel.ScrapingBot()

    def get_max_pages(self, driver):
        element = ('class name', 'last')
        last_page = self._wait.wait_by_presence(driver, element, 10)
        if not last_page:
            return {'error': True, 'type': 'Elemento max page não encontrado'}

        try:
            href = last_page.find_element(By.TAG_NAME, 'a').get_attribute('href')
            maxpage = str(href).split('page')[1]
            maxpage = int(maxpage.replace('=', ''))
        except:
            return {'error': True, 'type': 'Erro ao coletar max page'}

        return maxpage

    def get_info(self, driver):
        element = ('class name', 'responsive-table')
        table = self._wait.wait_by_presence(driver, element, 10)
        if not table:
            return {'error': True, 'type': 'Erro ao encontrat tabela'}

        try:
            html = table.get_attribute('innerHTML')
            soap = BeautifulSoup(html, 'html.parser')
            trs = soap.findAll('tr')
            for tr in trs:
                tds = tr.findAll('td')
                if not tds:
                    continue
                else:
                    data = {
                        'primeiro_nome': tds[0].text,
                        'ultimo_nome': tds[1].text,
                        'email': tds[2].text,
                        'universidade': tds[3].text,
                        'sexo': tds[4].text,
                        'profissao': tds[5].text,
                        'idade': tds[6].text,
                        'endereco': tds[7].text,
                    }
                    self.db_scraping.create(data)
            return True
        except:
            return {'error': True, 'type': 'Erro ao coletar dados.'}
