from dataclasses import dataclass, field


@dataclass
class Config:
    """Class for keeping track of an item in inventory."""
    quantity_on_hand: int = 0

    UNIT: int = 1000000
    POPULATION: int = 1336459178
    # +5:30 Indian Time # Pacific Standard Time (UTC−08:00)
    TIMEZONE_OFFSET: float = 5.50

    # RULE_MAP = {
    #     'Total': 'total',
    #     'Data per 10,00,000': 'percentage',
    # }
    # default factory field
    # RULE_MAP_DICT: dict = field(default_factory={
    #     'Total': 'total',
    #     'Data per 10,00,000': 'percentage',
    # })
