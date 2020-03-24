import requests
import json
import os
from time import sleep

gcountry = 'Russia'
def clearscreen():
    if os.name == "nt":
        os.system('@echo off')
        os.system('cls')
    elif os.name == "posix":
        os.system('clear')

def worldstat():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"
    headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "c9701bc214msh9e26d3823d575f6p1d5fdcjsne5bad4667b25"
        }
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)
def countrystat():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"
    headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "c9701bc214msh9e26d3823d575f6p1d5fdcjsne5bad4667b25"
        }
    response = requests.request("GET", url, headers=headers)
    res = json.loads(response.text)
    re = res['countries_stat']
    for c in re:
        if c['country_name'] == gcountry:
            return "\nСтатистика по стране: {} \nВсего случаев: {} \nВсего смертей: {} \nВсего выздоровеших: {} \nНовых случаев: {} \nНовых смертей: {} \nАктивных зараженных: {} \nЗараженных на 1 миллион населения: {} \n".format(c['country_name'], c['cases'], c['deaths'], c['total_recovered'], c['new_cases'], c['new_deaths'], c['active_cases'], c['total_cases_per_1m_population'])
    return "Страна не найдена"
if __name__ == "__main__":
    clearscreen()
    while 1:
        stat = worldstat()
        statcountry = countrystat()
        clearscreen()
        print("\nВсего случаев: {} \nВсего смертей: {} \nВсего вылечившихся: {} \nНовых случаев за сегодня: {} \nНовых смертей сегодня: {} \nАктуально на: {} \n".format(stat['total_cases'],stat['total_deaths'], stat['total_recovered'], stat['new_cases'], stat['new_deaths'], stat['statistic_taken_at']))
        print(statcountry)
        sleep(2)
