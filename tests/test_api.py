# test_api.py
from api.routes import app
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

def test_optimal_coins_whole_dollar():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '5'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 5
    assert data.get('half-dollar') == 0
    assert data.get('quarter') == 0
    assert data.get('dime') == 0
    assert data.get('nickel') == 0
    assert data.get('penny') == 0

def test_optimal_coins_one():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '.99'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 0
    assert data.get('half-dollar') == 1
    assert data.get('quarter') == 1
    assert data.get('dime') == 2
    assert data.get('nickel') == 0
    assert data.get('penny') == 4

def test_optimal_coins_two():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '1.56'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 1
    assert data.get('half-dollar') == 1
    assert data.get('quarter') == 0
    assert data.get('dime') == 0
    assert data.get('nickel') == 1
    assert data.get('penny') == 1

def test_optimal_coins_three():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '12.85'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 12
    assert data.get('half-dollar') == 1
    assert data.get('quarter') == 1
    assert data.get('dime') == 1
    assert data.get('nickel') == 0
    assert data.get('penny') == 0

def test_optimal_coins_zero():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '0.0'}
    )

    data = json.loads(response.get_data(as_text=True))
    
    assert response.status_code == 200
    assert data.get('silver-dollar') == 0
    assert data.get('half-dollar') == 0
    assert data.get('quarter') == 0
    assert data.get('dime') == 0
    assert data.get('nickel') == 0
    assert data.get('penny') == 0

def test_optimal_coins_invalid():        
    response = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '3blah3.45'}
    )
    response_two = app.test_client().get(
        '/api/v1/coins',
        query_string={'dollaramount': '3.444444'}
    )
    
    assert response.status_code == 400
    assert response_two.status_code == 400