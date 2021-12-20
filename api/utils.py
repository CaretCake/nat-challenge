from decimal import Decimal, getcontext

def use_coin(coin_value: Decimal, dollar_amount: Decimal) -> bool:
    """
    Returns True or False depending on if given coin value "fits" given dollar amount.

        Parameters:
            coin_value (Decimal): A decimal representing the given coin's value
            dollar_amount (Decimal): A decimal representing the dollar amount remaining

        Returns:
            True if coin_value <= dollar_amount, False otherwise
    """
    return coin_value.compare(dollar_amount) < 1

def get_num_of_coin(coin_value: Decimal, dollar_amount: Decimal) -> int:
    """
    Returns number of coins of given value that "fit" in given dollar amount.

        Parameters:
            coin_value (Decimal): A decimal representing the given coin's value
            dollar_amount (Decimal): A decimal representing the dollar amount remaining

        Returns:
            num_of_coins (Decimal): integer value representing number of coins that "fit" given dollar_amount
    """
    getcontext().prec = 100
    num_of_coins = dollar_amount // coin_value
    getcontext().prec = 2
    return num_of_coins