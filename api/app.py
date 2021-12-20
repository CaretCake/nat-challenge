import decimal
import flask
from flask import request, jsonify
from decimal import Decimal, FloatOperation, getcontext
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/coins', methods=['GET'])
def coins():
    if 'dollaramount' in request.args:
        dollar_amount = Decimal(request.args['dollaramount'])
    else:
        return "Error: no dollar amount provided. Please specify a dollar amount."

    if dollar_amount < 0:
        return "Error: dollar amount cannot be negative."
    
    optimal_coins = {
        'silver-dollar': 0,
        'half-dollar': 0,
        'quarter': 0,
        'dime': 0,
        'nickel': 0,
        'penny': 0
    }

    silver_dollar = Decimal('1')
    half_dollar = Decimal('.50')
    quarter = Decimal('.25')
    dime = Decimal('.10')
    nickel = Decimal('.05')
    penny = Decimal('.01')

    getcontext().prec = 2
    while dollar_amount > 0:
        if silver_dollar.compare(dollar_amount) < 1:
            dollar_amount = dollar_amount - silver_dollar
            optimal_coins['silver-dollar'] = optimal_coins.get('silver-dollar') + 1
        elif half_dollar.compare(dollar_amount) < 1:
            dollar_amount = dollar_amount - half_dollar
            optimal_coins['half-dollar'] = optimal_coins.get('half-dollar') + 1
        elif quarter.compare(dollar_amount) < 1:
            dollar_amount = dollar_amount - quarter
            optimal_coins['quarter'] = optimal_coins.get('quarter') + 1
        elif dime.compare(dollar_amount) < 1:
            dollar_amount = dollar_amount - dime
            optimal_coins['dime'] = optimal_coins.get('dime') + 1
        elif nickel.compare(dollar_amount) < 1:
            dollar_amount = dollar_amount - nickel
            optimal_coins['nickel'] = optimal_coins.get('nickel') + 1
        elif penny.compare(dollar_amount) < 1:
            optimal_coins['penny'] = int(Decimal(dollar_amount) / Decimal(0.01))
            dollar_amount = 0
            


    

    #print(optimal_coins)

    return jsonify(optimal_coins)

if __name__ == '__main__':
    app.run(debug=True)