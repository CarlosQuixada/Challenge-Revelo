import pandas as pd
from descrever import Descrever

data_job = pd.read_excel("job_skills.xlsx", sheet_name='job_skills')

# Visualização da Amostra dos Dados
##print(data_job.head().to_string())

# Identificar se existe dados faltantes
##print(data_job.isnull().sum())

# Identificar todas as localizações
desc = Descrever(data_job)

# Top paises
data_top = desc.top_pais()
##print(data_top.sort_values('Quantidade', ascending=False))

# Quantidade no Brazil
data = data_top[data_top['Pais'] == "Brazil"]
print(data['Quantidade'].values[0])
