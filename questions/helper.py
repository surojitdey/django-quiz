import requests
import random

class Quiz:
    def __init__(self):
        self.api = "https://countriesnow.space/api/v0.1/countries/capital"
        self.data = requests.get(self.api).json()["data"]
        self.data = [i for i in self.data if i["name"] !="" and i["capital"] !=""]

    def get_random_country_name(self):
        country = random.choice([i["name"] for i in self.data])
        options = self.get_random_options(country)
        random.shuffle(options)
        return country, options
    
    def get_random_options(self, country):
        capital_list = [i["capital"] for i in self.data]
        option_list = []
        option_list.append(self.get_correct_capital(country))
        while True:
            if len(option_list)==4:
                break
            option = random.choice(capital_list)
            if option not in option_list:
                option_list.append(option)
        return option_list

    def get_correct_capital(self, country):
        filtered_list = [d for d in self.data if d["name"]==country]
        return filtered_list[0]["capital"]