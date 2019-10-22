import pandas as pd


class Descrever:
    def __init__(self, data_job):
        self.data_job = data_job
        self.data_job['Pais'] = self.data_job['Location'].apply(self.__preprocess_pais)

    def __preprocess_pais(self, local):
        info_local = local.split(', ')
        pais = info_local[len(info_local) - 1]

        return pais

    def identificador_pais(self, local):
        data_location = self.data_job[self.data_job['Pais'] == local]

        data_frame = pd.DataFrame({
            'Pais': [data_location['Pais'].values[0]],
            'Quantidade': [len(data_location)]
        })

        return data_frame

    def top_pais(self):
        list_paises = sorted(set(self.data_job['Pais'].values))

        data_result = []
        for local in list_paises:
            data_new = self.identificador_pais(local)

            if len(data_result) == 0:
                data_result = data_new

            else:
                data_result = pd.concat([data_result, data_new])

        return data_result
