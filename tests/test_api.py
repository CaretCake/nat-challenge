# test_test.py
from api.app import app
from flask import json

def test_optimal_coins_one_each_coin():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '1.91'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 1
    assert data.get('half-dollar') == 1
    assert data.get('quarter') == 1
    assert data.get('dime') == 1
    assert data.get('nickel') == 1
    assert data.get('penny') == 1

def test_optimal_coins_zero():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '0'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 0
    assert data.get('half-dollar') == 0
    assert data.get('quarter') == 0
    assert data.get('dime') == 0
    assert data.get('nickel') == 0
    assert data.get('penny') == 0