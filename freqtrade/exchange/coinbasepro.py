""" Coinbasepro exchange subclass """
import logging
from typing import Dict

import ccxt

from freqtrade import (DependencyException, InvalidOrderException,
                       OperationalException, TemporaryError)
from freqtrade.exchange import Exchange

logger = logging.getLogger(__name__)


class Coinbasepro(Exchange):

    _ft_has: Dict = {
        "ohlcv_candle_limit": 300,
    }

