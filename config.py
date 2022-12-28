from dataclasses import dataclass, field


@dataclass
class Config:
    """Class for keeping track of an item in inventory."""

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
