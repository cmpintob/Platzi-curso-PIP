import utils
import read_csv
import charts
import pandas as pd

def run():
  
#Solucion reto poblacion historica por pais seleccionable
  '''data = read_csv.read_csv('./app/data.csv')
  labels, values = utils.historical_country_population(data)
  charts.generate_bar_chart(labels, values)'''
#Solucion reto columna de poblacion
  '''
  data = read_csv.read_csv('./data.csv')
  countries, percentages = utils.world_population_p(data)  
  charts.generate_pie_chart(countries, percentages)'''

#Soluciones del profe
  
  '''data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)'''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages) 

  data = read_csv.read_csv('data.csv')  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  

if __name__ == '__main__':
  run()