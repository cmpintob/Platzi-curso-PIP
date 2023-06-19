def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

#funcion de mi solucion al reto de poblacion historica
def historical_country_population(country_dict_list):
  h_population = {}
  validacion = True
  while validacion == True:    
    country = str.capitalize(input('Escribe el pais del cual deseas conocer información historica de su población: '))    
    for element in country_dict_list:
      if element['Country/Territory'] == country:
        for key in element.keys():        
          if any(char.isdigit() for char in key) == True:               
            new_key = ''.join(char for char in key if char.isdigit() == True)
            if len(new_key) > 3:
              h_population[str(new_key)] = int(element[key])          
        validacion = False        
    if validacion == True:
      print('su pais no se encuentra en la base de datos, por favor, intente nuevamente')
  labels = h_population.keys() 
  values = h_population.values()
  return labels, values

#funcion segundo reto para obtener porcentajes de poblacion mundial
def world_population_p(data):
  data_v2 = data.copy()
  #Country/Territory
  #World Population Percentage
  countries = [country['Country/Territory'] for country in data_v2]  
  wpp = [float(worldpp['World Population Percentage']) for worldpp in data_v2]
  
  return countries, wpp  
  
  