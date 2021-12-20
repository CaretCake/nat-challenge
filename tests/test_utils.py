# test_utils.py
from api.routes import app
from api.utils import use_coin, get_num_of_coin
from api.constants import HALF_DOLLAR, QUARTER, DIME, NICKEL, PENNY
from decimal import Decimal
from flask import json

def test_use_coin():
    assert use_coin(HALF_DOLLAR, Decimal('.99')) == True
    assert use_coin(HALF_DOLLAR, Decimal('.51')) == True
    assert use_coin(HALF_DOLLAR, Decimal('.5')) == True
    assert use_coin(HALF_DOLLAR, Decimal('.49')) == False

def test_get_num_of_coin():
    assert get_num_of_coin(HALF_DOLLAR, Decimal('54.5')) == 109
    assert get_num_of_coin(HALF_DOLLAR, Decimal('0.24')) == 0
    assert get_num_of_coin(PENNY, Decimal('100')) == 10000