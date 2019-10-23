class UtilCountry:
    def maker_data_graph(self, data_top):
        """
            Método responsável por preparar o dados para serem plotados no gráfico
        :param data_top: dados com os países e a quantidade de vagas
        :return: lista de países e valores
        """

        countries = [country for country in data_top]
        values = [value for value in data_top.values()]

        return countries, values

    def preprocess_pais(self, local):
        """
            Método responsável por identificar apenas o país da vaga
        :param local: localização da vaga
        :return: país da vaga
        """

        location_split = local.split(', ')
        country = location_split[len(location_split) - 1]

        return country
