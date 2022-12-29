import numpy as np
import pandas as pd
import config
import streamlit as st

class NuclearDataLoader:
    def __init__(self, path_csv) -> None:
        self.config = config.Config()
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

    def get_total_capacity(self):
        power = np.sum(self.data.grosspower.values)
        return power

class EnergyDataLoader:
    def __init__(self, path_csv) -> None:
        self.path_csv = path_csv
        self.config = config.Config()

        self.cols = [
                    'country',
                    'country_long',
                    'name',
                    'capacity_mw',
                    'latitude',
                    'longitude',
                    'primary_fuel'
                ]

    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def load_dataset(self):
        self.data = pd.read_csv(self.path_csv, usecols=self.cols)
        self.data['filter'] = self.data.primary_fuel.apply(lambda x: x in self.config.ENERGY_TYPES)
        self.data = self.data[self.data['filter'] == True]

        self.data['map_size'] = self.data['capacity_mw']/50
        return self.data

    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def filter_by_country(self, country):
        return self.data[self.data.country_long == country]

    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def filter_by_fuel(self, fuel):
        return self.data[self.data.primary_fuel == fuel]

    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def get_total_capacity(self):
        power = np.sum(self.data.capacity_mw.values)
        return power

    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def get_specific_energy_capacity(self, energy_type='Nuclear'):
        temp_data = self.data[self.data.primary_fuel == energy_type]
        power = np.sum(temp_data.capacity_mw.values)
        return power

    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def get_energy_capacity_fuel_wise(self):
        fuel_capacity_counter = self.data.groupby('primary_fuel').sum()['capacity_mw'].reset_index()
        return fuel_capacity_counter


    # @st.cache(ttl=60*60*24, allow_output_mutation=True)
    def get_top_12_country_energy_capacity_fuel_wise(self, energy_type='Nuclear'):
        temp_data = self.data[self.data.primary_fuel == energy_type]
        power = temp_data.groupby('country_long').sum('capacity_mw').sort_values('capacity_mw', ascending=False)['capacity_mw'][:12].reset_index()
        return power

    def get_average_plant_size_fuel_size(self):
        fuel_capacity_counter = self.data.groupby('primary_fuel').mean()['capacity_mw'].reset_index()
        return fuel_capacity_counter
