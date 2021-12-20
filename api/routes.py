import re
from api.utils import use_coin, get_num_of_coin
from flask import Flask, request, jsonify
from decimal import Decimal, getcontext
from api.constants import HALF_DOLLAR, QUARTER, DIME, NICKEL, PENNY

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/coins', methods=['GET'])
def coins():
    if 'dollaramount' in request.args:
        dollar_amount = '0' + str(request.args['dollaramount'].strip())
    else:
        return "Error: no dollar amount provided. Please specify a dollar amount."

    if re.search(r"^\d*\.?\d{0,2}$", dollar_amount) is None:
        return jsonify({'error': 'Invalid dollar amount.'}), 400
    
    optimal_coins = {
        'silver-dollar': 0,
        'half-dollar': 0,
        'quarter': 0,
        'dime': 0,
        'nickel': 0,
        'penny': 0
    }

    split_amount = dollar_amount.split('.')
    optimal_coins['silver-dollar'] = int(split_amount[0])
    dollar_amount = Decimal('.' + split_amount[1])

    getcontext().prec = 2
    if use_coin(HALF_DOLLAR, dollar_amount):
        num_of_coins = get_num_of_coin(HALF_DOLLAR, dollar_amount)
        dollar_amount = dollar_amount - (HALF_DOLLAR * num_of_coins)
        optimal_coins['half-dollar'] = int(optimal_coins.get('half-dollar') + num_of_coins)
    if use_coin(QUARTER, dollar_amount):
        num_of_coins = get_num_of_coin(QUARTER, dollar_amount)
        dollar_amount = dollar_amount - (QUARTER * num_of_coins)
        optimal_coins['quarter'] = int(optimal_coins.get('quarter') + num_of_coins)
    if use_coin(DIME, dollar_amount):
        num_of_coins = get_num_of_coin(DIME, dollar_amount)
        dollar_amount = dollar_amount - (DIME * num_of_coins)
        optimal_coins['dime'] = int(optimal_coins.get('dime') + num_of_coins)
    if use_coin(NICKEL, dollar_amount):
        num_of_coins = get_num_of_coin(NICKEL, dollar_amount)
        dollar_amount = dollar_amount - (NICKEL * num_of_coins)
        optimal_coins['nickel'] = int(optimal_coins.get('nickel') + num_of_coins)
    if use_coin(PENNY, dollar_amount):
        num_of_coins = get_num_of_coin(PENNY, dollar_amount)
        optimal_coins['penny'] = int(num_of_coins)
        dollar_amount = 0


    return jsonify(optimal_coins)

if __name__ == '__main__':
    app.run(debug=True)