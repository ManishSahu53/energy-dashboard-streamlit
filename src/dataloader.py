import numpy as np
import pandas as pd

class NuclearDataLoader:
    def __init__(self, path_csv) -> None:
        self.path_csv = path_csv
        self.cols = [
                    'powerplant',
                    'unit',
                    'country',
                    'latitude',
                    'longitude',
                    'grosspower',
                    'type',
                    'status'
                    ]
        

    def load_dataset(self):
        self.data = pd.read_csv(self.path_csv, usecols=self.cols)
        return self.data

    def filter_by_country(self, country):
        return self.data[self.data.country == country]

    def filter_by_type(self, type):
        return self.data[self.data.type == type]

    def filter_by_status(self, status):
        return self.data[self.data.status == status]
    

class EnergyDataLoader:
    def __init__(self, path_csv) -> None:
        self.path_csv = path_csv
        self.cols = [
                    'country',
                    'country_long',
                    'name',
                    'capacity_mw',
                    'latitude',
                    'longitude',
                    'primary_fuel'
                ]

    def load_dataset(self):
        self.data = pd.read_csv(self.path_csv, usecols=self.cols)
        return self.data

    def filter_by_country(self, country):
        return self.data[self.data.country_long == country]

    def filter_by_fuel(self, fuel):
        return self.data[self.data.primary_fuel == fuel]

   
