import datetime 
from dataclasses import dataclass, field

@dataclass
class Config:
    """Class for keeping track of an item in inventory."""

    TIMEZONE_OFFSET = 5.50  # +5:30 Indian Time # Pacific Standard Time (UTC−08:00)
    tzinfo = datetime.timezone(datetime.timedelta(hours=TIMEZONE_OFFSET))

    ENERGY_TYPES = [
        'Biomass',
        'Geothermal',
        'Hydro',
        'Nuclear',
        'Solar',
        'Waste',
        'Wave and Tidal',
        'Wind',
    ]

    path_nuclear_csv = 'data/nuclear_data/nuclear_data.csv'
    path_energy_csv = 'data/energy_data/energy_data.csv'
    

    rules_cols = ['Daily Recovery', 'Daily New Cases', 'Daily Deaths', 'Daily Test', 'Daily Active Cases']
    
    # RULE_MAP = {
    #     'Total': 'total',
    #     'Data per 10,00,000': 'percentage',
    # }
    # default factory field
    # RULE_MAP_DICT: dict = field(default_factory={
    #     'Total': 'total',
    #     'Data per 10,00,000': 'percentage',
    # })
