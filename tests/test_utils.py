# test_utils.py
from api.routes import app
from api.utils import use_coin
from decimal import Decimal
from flask import json

def test_use_coin():        
    half_dollar = Decimal('.50')

    assert use_coin(half_dollar, Decimal('.99')) == True
    assert use_coin(half_dollar, Decimal('.51')) == True
    assert use_coin(half_dollar, Decimal('.5')) == True
    assert use_coin(half_dollar, Decimal('.49')) == False
