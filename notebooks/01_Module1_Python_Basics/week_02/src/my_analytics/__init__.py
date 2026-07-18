'''
__init__.py file is a Public API for the my_analytics package.
Importing from the package directly exposes these names:

    from src.my_analytics import mean, median, mode, minmax, zscore

    Without these imports in __init__.py, your users have to type long, deep paths to access our functions. Including them creates a clean Public API.

This will FAIL if __init__.py is blank:
from my_analytics import mean 

# Users are forced to do this instead:
from my_analytics.central_tendency import mean
from my_analytics.scaling import minmax
    
'''

from .central_tendency import mean, median, mode
from .scaling import minmax, zscore
from .dispersion import variance, std, IQR, CV



__version__ = "1.0.0"
__author__  = "Muhammad Luqman"
__all__     = ["mean", "median", "mode", "minmax", "zscore"]#,"variance","std","IQR","CV"]