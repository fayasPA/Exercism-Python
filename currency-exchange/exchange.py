"""
This module is used to calculate the exchange value of one currency to another.
"""
def exchange_money(budget, exchange_rate):
    """
    This function returns exchanged value of the foreign currency you can recieve
    according to the exchange_rate given.
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget/exchange_rate


def get_change(budget, exchanging_value):
    """
    This function returns the remaining money from the budget after exchanging
    according to the exchanging_value.
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    This function returns the total value of bills we recieved according to the
    number_of_bills we have.
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination*number_of_bills


def get_number_of_bills(budget, denomination):
    """
    This function returns the total no. of bills that you will recieve
    according to the budget.
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget//denomination


def get_leftover_of_bills(budget, denomination):
    """
    This function returns the amount of leftover bills booth get
    to keep after the exchange.
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    return budget - get_number_of_bills(budget, denomination)*denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function returns the maximum value after exchange considering the spread.
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    total_exchange_rate = exchange_rate + exchange_rate*(spread/100)
    return get_number_of_bills(exchange_money(budget, total_exchange_rate), denomination)*denomination
