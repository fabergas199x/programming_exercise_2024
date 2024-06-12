def get_price_of_operator(operator_price_dict: dict[str: float], phone_number: str) -> float:
    price = None
    # For loop to get prefix of phone_number from longest to shortest
    for i in range(len(phone_number)):
        # If we can get price with longer prefix, assign the variable price to the get value and break the loop
        if operator_price_dict.get(phone_number[0:len(phone_number)-i]):
            price = operator_price_dict.get(phone_number[0:len(phone_number)-i])
            break
    return price


def get_cheapest_operator(operator_prices: dict[str, dict[str: float]], phone_number: str) -> dict[str: float]:
    cheapest_operator = None
    cheapest_price = None
    # For loop all operators in list
    for key in operator_prices:
        # Get price of an operator
        price = get_price_of_operator(operator_prices.get(key), phone_number)
        # compare with current cheapest price
        if price and (not cheapest_price or price < cheapest_price):
            cheapest_price = price
            cheapest_operator = key
    # If we can find valid price return as dict
    if cheapest_operator:
        return {cheapest_operator: cheapest_price}
    # Else we return none value
    else:
        return None
