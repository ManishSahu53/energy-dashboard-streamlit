from datetime import datetime 
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

    # RULE_MAP = {
    #     'Total': 'total',
    #     'Data per 10,00,000': 'percentage',
    # }
    # default factory field
    # RULE_MAP_DICT: dict = field(default_factory={
    #     'Total': 'total',
    #     'Data per 10,00,000': 'percentage',
    # })
