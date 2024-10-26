"""
Author: <Chuanyu> (skewcy@gmail.com)
__init__.py (c) 2024
Desc: description
Created:  2024-09-15T01:53:29.530Z
"""

from .operator import match_table as operator_match_table
from .motion import match_table as motion_match_table
from typing import Dict, Callable

match_table: Dict[str, Callable] = {**operator_match_table, **motion_match_table}
