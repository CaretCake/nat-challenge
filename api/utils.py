from decimal import Decimal

def use_coin(coin_value: Decimal, dollar_amount: Decimal) -> bool:
    """
    Returns True or False depending on if given coin value should be used with dollar amount.

        Parameters:
            coin_value (Decimal): A decimal representing the given coin's value
            dollar_amount (Decimal): A decimal representing the dollar amount remaining

        Returns:
            True if coin_value <= dollar_amount, False otherwise
    """
    return coin_value.compare(dollar_amount) < 1