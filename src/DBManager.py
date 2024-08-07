import psycopg2

class DBManager:
    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании.
        :return:
        """
        pass


    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        :return:
        """
        pass


    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям
        """
        pass


    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        :return:
        """
        pass


    def get_vacancies_with_keyword(self):
        """
        получает список всех вакансий,
        в названии которых содержатся переданные в метод слова, например python
        :return:
        """
        pass