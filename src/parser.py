import requests
import json
from abc import ABC, abstractmethod
import os
from config import ROOT_DIR

class Parser(ABC):
    """
    Абстрактный класс для создания парсера
    """

    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API Headhunter
    родительский класс - Parser
    фильтрует по региону Россия
    """

    def __init__(self, keyword):
        self.url = "https://api.hh.ru/vacancies"
        self._headers = {'User-Agent':'HH-User-Agent'}
        self._params = {'text': keyword, 'page':0, 'per_page':50, 'area': 113,
                        'employer_id': (6093775,15478,10711119,9418714,41144,733,1740,67611,78638)}
        self.vacancies = []
        self.filepath = os.path.join(ROOT_DIR, 'data', 'vacancies.json')
        super().__init__()


    def load_vacancies(self, *args, **kwargs):
        """
        Функция загрузки вакансии с сайта по ключевыму слову
        :return:
        """

        response = requests.get(self.url, headers=self._headers, params=self._params)
        response_info = response.json()
        total_pages = response_info['pages']
        while self._params['page'] < total_pages:
            response = requests.get(self.url, headers=self._headers, params=self._params)
            vacancies = response.json()['items']
            #vacancies = response.json()
            self.vacancies.extend(vacancies)
            self._params['page'] += 1
            return vacancies

    def Save_File(self, data):
        """
        сохраняет файл с вакансиями
        """
        FILEPATH = self.filepath
        with open(FILEPATH, "w", encoding="utf-8") as datafile:
            json.dump(data, datafile,  ensure_ascii=False, indent=4)

    def Convert_To_CSV(self):
        pass

    def Create_SQL_database(self):
        pass

    @property
    def connect(self):
        return requests.get(self.url).status_code

if __name__ == '__main__':
    Vac = HH('Python')
    print(Vac.load_vacancies())
    Vac.save_file(Vac.load_vacancies())
