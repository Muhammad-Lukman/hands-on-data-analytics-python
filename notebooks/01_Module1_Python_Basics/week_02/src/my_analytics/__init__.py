'''
__init__.py file is a Public API for the my_analytics package.
Importing from the package directly exposes these names:

    from src.my_analytics import mean, median, mode, minmax, zscore
    
'''

from .central_tendency import mean, median, mode
from .scaling import minmax, zscore
from .dispersion import variance, std, IQR, CV

__version__ = "1.0.0"
__author__  = "Muhammad Luqman"
__all__     = ["mean", "median", "mode", "minmax", "zscore"]