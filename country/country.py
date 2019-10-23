from collections import Counter

from country.util_country import UtilCountry


class Country:
    def __init__(self, data_job):
        self.data_job = data_job
        self.util_country = UtilCountry()
        self.data_job['Country'] = self.data_job['Location'].apply(self.util_country.preprocess_pais)

    def count_vacancies_by_country(self):
        """
            Método responsável por fazer a contagem de vagas por países
        :return: lista de número de vagas por país
        """

        list_countries = self.data_job['Country'].values

        counts_countries = Counter(list_countries)
        count_vacancies = dict(counts_countries.most_common())

        return count_vacancies
