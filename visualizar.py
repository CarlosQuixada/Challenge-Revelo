import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py
from wordcloud import WordCloud

from country.country import Country
from country.util_country import UtilCountry
from minimum_qualifications.minimum_qualifications import MinimunQualification
from minimum_qualifications.minimum_qualifications import UtilMinimumQualification
from skills.skill import Skill
from skills.util_skill import UtilSkill

py.init_notebook_mode(connected=True)

jobs_google = pd.read_excel("job_skills.xlsx", sheet_name='job_skills')
jobs_google.dropna(axis=0, how='any', inplace=True)

################ Q1 ###################

country = Country(jobs_google)
util_country = UtilCountry()

vacancies_by_country = country.count_vacancies_by_country()
country, values = util_country.maker_data_graph(vacancies_by_country)

trace1 = go.Bar(x=country,
                y=values)
data = [trace1]
py.iplot(data)

################ Q2 ###################
print(vacancies_by_country['Brazil'])

################ Q3 ###################

minimum_qualifications = MinimunQualification(jobs_google)
util_minimum_qualification = UtilMinimumQualification()

top_minimum_qualifications = minimum_qualifications.minimum_qualifications_identifier()

text_minimum_qualifications = util_minimum_qualification.maker_data_graph(top_minimum_qualifications)

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      min_font_size=10).generate(text_minimum_qualifications)

plt.figure(figsize=(8, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()

################ Q4 ###################

skill = Skill(jobs_google)
util_skill = UtilSkill()

skills_ti = skill.skill_identifier()

skills, values = util_skill.maker_data_graph_bar(skills_ti)

trace1 = go.Bar(x=skills,
                y=values)
data = [trace1]
py.iplot(data)
