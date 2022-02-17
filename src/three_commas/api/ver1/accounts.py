from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasError
from typing import Tuple


wrapper = Py3CW('', '')


def post_transfer():
    """
    /ver1/accounts/transfer
    Transfer coins between accounts (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='transfer',
    )
    return ThreeCommasError(error), data


def get_transfer_history():
    """
    /ver1/accounts/transfer_history
    Transfers history (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='transfer_history',
    )
    return ThreeCommasError(error), data


def get_transfer_data():
    """
    /ver1/accounts/transfer_data
    Data for transfer between accounts (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='transfer_data',
    )
    return ThreeCommasError(error), data


def post_new():
    """
    /ver1/accounts/new
    Add exchange account  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='new',
    )
    return ThreeCommasError(error), data


def post_update():
    """
    /ver1/accounts/update
    Edit exchange account

    """
    error, data = wrapper.request(
        entity='accounts',
        action='update',
    )
    return ThreeCommasError(error), data


def get():
    """
    /ver1/accounts
    User connected exchanges(and EthereumWallet) list (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='',
    )
    return ThreeCommasError(error), data


def get_market_list():
    """
    /ver1/accounts/market_list
    Supported markets list (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='market_list',
    )
    return ThreeCommasError(error), data


def get_market_pairs():
    """
    /ver1/accounts/market_pairs
    All market pairs (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='market_pairs',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_currency_rates_with_leverage_data():
    """
    /ver1/accounts/currency_rates_with_leverage_data
    Currency rates and limits with leverage data (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
    )
    return ThreeCommasError(error), data
'''


def get_currency_rates():
    """
    /ver1/accounts/currency_rates
    Currency rates and limits (Permission: NONE, Security: NONE)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='currency_rates',
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_deposit_data_by_id(account_id):
    """
    /ver1/accounts/{account_id}/deposit_data
    User Deposit Data (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


def get_networks_info_by_id(account_id):
    """
    /ver1/accounts/{account_id}/networks_info
    Deposit/withdraw networks info (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='networks_info',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_convert_dust_to_bnb_by_id(account_id):
    """
    /ver1/accounts/{account_id}/convert_dust_to_bnb
    Convert dust coins to BNB (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='convert_dust_to_bnb',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def get_active_trading_entities_by_id(account_id):
    """
    /ver1/accounts/{account_id}/active_trading_entities
    Active trade entities (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='active_trading_entities',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_sell_all_to_usd_by_id(account_id):
    """
    /ver1/accounts/{account_id}/sell_all_to_usd
    Sell all to USD  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='sell_all_to_usd',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_sell_all_to_btc_by_id(account_id):
    """
    /ver1/accounts/{account_id}/sell_all_to_btc
    Sell all to BTC  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='sell_all_to_btc',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def get_balance_chart_data_by_id(account_id):
    """
    /ver1/accounts/{account_id}/balance_chart_data
    balance history data (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='balance_chart_data',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_load_balances_by_id(account_id):
    """
    /ver1/accounts/{account_id}/load_balances
    Load balances for specified exchange  (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='load_balances',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_rename_by_id(account_id):
    """
    /ver1/accounts/{account_id}/rename
    Rename exchange connection  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='rename',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_pie_chart_data_by_id(account_id):
    """
    /ver1/accounts/{account_id}/pie_chart_data
    Information about all user balances on specified exchange in pretty for pie chart format (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='pie_chart_data',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_account_table_data_by_id(account_id):
    """
    /ver1/accounts/{account_id}/account_table_data
    Information about all user balances on specified exchange  (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='account_table_data',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


def post_remove_by_id(account_id):
    """
    /ver1/accounts/{account_id}/remove
    Remove exchange connection  (Permission: ACCOUNTS_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='remove',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def get_leverage_data_by_id(account_id):
    """
    /ver1/accounts/{account_id}/leverage_data
    Information about account leverage (Permission: ACCOUNTS_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='accounts',
        action='<py3cw_action>',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data
'''


def get_by_id(account_id):
    """
    /ver1/accounts/{account_id}
    Single Account Info (Permission: ACCOUNTS_READ, Security: SIGNED)
You can send 'summary' instead of {account_id} to get summary account info

    """
    error, data = wrapper.request(
        entity='accounts',
        action='account_info',
        action_id=str(account_id),
    )
    return ThreeCommasError(error), data


