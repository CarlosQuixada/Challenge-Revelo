import pandas as pd
import plotly.graph_objs as go


class UtilCountry:
    def maker_data_graph(self, data_top):
        """
            Método responsável por preparar o dados para serem plotados no gráfico
        :param data_top: dados com os países e a quantidade de vagas
        :return: lista de países e valores
        """

        countries = [country for country in data_top]
        values = [value for value in data_top.values()]
        latitudes, longitudes = self.get_countries_coordinates(countries)

        data_countries = pd.DataFrame({
            "country": countries,
            "vacancy": values,
            "latitude": latitudes,
            "longitude": longitudes
        })

        trace = go.Scattergeo(locationmode='ISO-3', lon=data_countries['longitude'], lat=data_countries['latitude'],
                              text=data_countries['country'] + ' - N° Vagas: ' + data_countries['vacancy'].astype(str),
                              marker=dict(size=data_countries['vacancy'] * 3, color='#e74c3c',
                                          line={'width': 0.8, 'color': '#2c3e50'}, sizemode='area'))

        data = [trace]

        layout = go.Layout(title='<b>Distribuição de vagas do Google pelo mundo</b>',
                           titlefont={'family': 'Arial', 'size': 24},
                           geo={'scope': 'world', 'projection': {'type': 'equirectangular', 'scale': 1.1},
                                'showland': True, 'landcolor': '#2ecc71', 'showlakes': True, 'lakecolor': '#3498db',
                                'subunitwidth': 2, 'subunitcolor': "rgb(255, 255, 255)"})

        return data, layout

    def get_countries_coordinates(self, countries):
        """
            Método responsável por obter latitude e longitude dos países
        :param countries: lista de países
        :return: lista de latitudes e longitudes
        """

        countries_coordinates = pd.read_csv('./country/country-capitals.csv')

        latitudes = []
        longitudes = []

        for country in countries:
            data_countries_filters = countries_coordinates[countries_coordinates['Name'] == country]

            latitudes.append(list(data_countries_filters['Latitude'])[0])
            longitudes.append(list(data_countries_filters['Longitude'])[0])

        return latitudes, longitudes

    def validate_transform(self, country):
        country_split = country.split(" - ")
        if len(country_split) > 1:
            country = country_split[len(country_split) - 1]

        if country == "Hong Kong":
            country = "China"

        if country == "Czechia":
            country = "Czech Republic"

        if country == "USA":
            country = "United States"

        return country

    def preprocess_pais(self, local):
        """
            Método responsável por identificar apenas o país da vaga
        :param local: localização da vaga
        :return: país da vaga
        """

        location_split = local.split(', ')
        country = location_split[len(location_split) - 1]

        country = self.validate_transform(country)

        return country
