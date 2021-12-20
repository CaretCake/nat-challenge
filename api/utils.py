from decimal import Decimal

def use_coin(coin_value: Decimal, dollar_amount: Decimal) -> bool:
    return coin_value.compare(dollar_amount) < 1