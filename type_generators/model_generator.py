from typing import List, Union
import datetime
import json
from enum import Enum

# from src.three_commas.model.models import BotEvent
# from src.three_commas.model.generated_models import Deal
# from src.three_commas.model.generated_enums import DealStatus, MarketCode
# from src.three_commas.model.other_enums import AbstractStringEnum

INDENT = '    '


class ThreeCommasJsonProperty:
    def __init__(self, name: str, initial_type: type, parsed_type: Union[type, str] = None):
        self.name = name
        self.initial_type = initial_type
        self.parsed_type = parsed_type


class ThreeCommasModelClass:
    def __init__(self, name: str, properties: List[ThreeCommasJsonProperty]):
        self.name = name
        self.properties = properties





tc_generated_classes = [
    ThreeCommasModelClass(name='Deal',
                          properties=[
                              ThreeCommasJsonProperty('id', int),
                              ThreeCommasJsonProperty('type', str),
                              ThreeCommasJsonProperty('bot_id', int),
                              ThreeCommasJsonProperty('max_safety_orders', int),
                              ThreeCommasJsonProperty('deal_has_error', bool),
                              # ThreeCommasJsonProperty('from_currency_id', int),  # TODO check if could be float
                              # ThreeCommasJsonProperty('to_currency_id', int),  # TODO check if could be float
                              ThreeCommasJsonProperty('account_id', int),
                              ThreeCommasJsonProperty('active_safety_orders_count', int),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('updated_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('closed_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('finished?', bool),
                              ThreeCommasJsonProperty('current_active_safety_orders_count', int),
                              ThreeCommasJsonProperty('current_active_safety_orders', int),
                              ThreeCommasJsonProperty('completed_safety_orders_count', int),
                              ThreeCommasJsonProperty('completed_manual_safety_orders_count', int),
                              ThreeCommasJsonProperty('cancellable?', bool),
                              ThreeCommasJsonProperty('panic_sellable?', bool),
                              ThreeCommasJsonProperty('trailing_enabled', bool),
                              ThreeCommasJsonProperty('tsl_enabled', bool),
                              ThreeCommasJsonProperty('stop_loss_timeout_enabled', bool),
                              ThreeCommasJsonProperty('stop_loss_timeout_in_seconds', int),
                              ThreeCommasJsonProperty('active_manual_safety_orders', int),
                              ThreeCommasJsonProperty('pair', str),
                              ThreeCommasJsonProperty('status', str, 'DealStatus'),  # could be enum DealStatus
                              ThreeCommasJsonProperty('localized_status', str),
                              ThreeCommasJsonProperty('take_profit', str, float),
                              ThreeCommasJsonProperty('base_order_volume', str, float),
                              ThreeCommasJsonProperty('safety_order_volume', str, float),
                              ThreeCommasJsonProperty('safety_order_step_percentage', str, float),
                              ThreeCommasJsonProperty('leverage_type', str),
                              # ThreeCommasJsonProperty('leverage_custom_value', NoneType), TODO
                              ThreeCommasJsonProperty('bought_amount', str, float),
                              ThreeCommasJsonProperty('bought_volume', str, float),
                              ThreeCommasJsonProperty('bought_average_price', str, float),
                              ThreeCommasJsonProperty('base_order_average_price', str, float),
                              ThreeCommasJsonProperty('sold_amount', str, float),
                              ThreeCommasJsonProperty('sold_volume', str, float),
                              ThreeCommasJsonProperty('sold_average_price', str, float),
                              ThreeCommasJsonProperty('take_profit_type', str),
                              ThreeCommasJsonProperty('final_profit', str, float),
                              ThreeCommasJsonProperty('martingale_coefficient', str, float),
                              ThreeCommasJsonProperty('martingale_volume_coefficient', str, float),
                              ThreeCommasJsonProperty('martingale_step_coefficient', str, float),
                              ThreeCommasJsonProperty('stop_loss_percentage', str, float),
                              # ThreeCommasJsonProperty('error_message', NoneType), TODO
                              ThreeCommasJsonProperty('profit_currency', str),
                              ThreeCommasJsonProperty('stop_loss_type', str),
                              ThreeCommasJsonProperty('safety_order_volume_type', str),
                              ThreeCommasJsonProperty('base_order_volume_type', str),
                              ThreeCommasJsonProperty('from_currency', str),
                              ThreeCommasJsonProperty('to_currency', str),
                              ThreeCommasJsonProperty('current_price', str, float),
                              ThreeCommasJsonProperty('take_profit_price', str, float),
                              # ThreeCommasJsonProperty('stop_loss_price', NoneType), TODO
                              ThreeCommasJsonProperty('final_profit_percentage', str, float),
                              ThreeCommasJsonProperty('actual_profit_percentage', str, float),
                              ThreeCommasJsonProperty('bot_name', str),
                              ThreeCommasJsonProperty('account_name', str),
                              ThreeCommasJsonProperty('usd_final_profit', str, float),
                              ThreeCommasJsonProperty('actual_profit', str, float),
                              ThreeCommasJsonProperty('actual_usd_profit', str, float),
                              # ThreeCommasJsonProperty('failed_message', NoneType),  TODO
                              ThreeCommasJsonProperty('reserved_base_coin', str, float),
                              ThreeCommasJsonProperty('reserved_second_coin', str, float),
                              ThreeCommasJsonProperty('trailing_deviation', str, float),
                              ThreeCommasJsonProperty('trailing_max_price', str, float),
                              # ThreeCommasJsonProperty('tsl_max_price', NoneType), TODO
                              ThreeCommasJsonProperty('strategy', str),
                              ThreeCommasJsonProperty('reserved_quote_funds', str, float),
                              # ThreeCommasJsonProperty('reserved_base_funds', int), # TODO could be float
                              ThreeCommasJsonProperty('buy_steps', 'List[dict]'),
                              ThreeCommasJsonProperty('bot_events', List[dict], 'List[BotEvent]'),
                          ]),
    ThreeCommasModelClass(name='Bot',
                          properties=[
                              ThreeCommasJsonProperty('id', int),
                              ThreeCommasJsonProperty('account_id', int),
                              ThreeCommasJsonProperty('is_enabled', bool),
                              ThreeCommasJsonProperty('max_safety_orders', int),
                              ThreeCommasJsonProperty('active_safety_orders_count', int),
                              ThreeCommasJsonProperty('pairs', List[str]),
                              ThreeCommasJsonProperty('strategy_list', List[dict]),
                              ThreeCommasJsonProperty('max_active_deals', int),
                              ThreeCommasJsonProperty('active_deals_count', int),
                              ThreeCommasJsonProperty('deletable?', bool),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('updated_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('trailing_enabled', bool),
                              ThreeCommasJsonProperty('tsl_enabled', bool),
                              ThreeCommasJsonProperty('deal_start_delay_seconds', int),
                              ThreeCommasJsonProperty('stop_loss_timeout_enabled', bool),
                              ThreeCommasJsonProperty('stop_loss_timeout_in_seconds', int),
                              # ThreeCommasJsonProperty('disable_after_deals_count', ), TODO probably int
                              # ThreeCommasJsonProperty('deals_counter', ), TODO probably int
                              ThreeCommasJsonProperty('allowed_deals_on_same_pair', int),
                              ThreeCommasJsonProperty('easy_form_supported', bool),
                              # ThreeCommasJsonProperty('close_deals_timeout', ), TODO probably int
                              ThreeCommasJsonProperty('url_secret', str),
                              ThreeCommasJsonProperty('name', str),
                              ThreeCommasJsonProperty('take_profit', str, float),
                              ThreeCommasJsonProperty('base_order_volume', str, float),
                              ThreeCommasJsonProperty('safety_order_volume', str, float),
                              ThreeCommasJsonProperty('safety_order_step_percentage', str, float),
                              ThreeCommasJsonProperty('take_profit_type', str),
                              ThreeCommasJsonProperty('type', str),
                              ThreeCommasJsonProperty('martingale_volume_coefficient', str, float),
                              ThreeCommasJsonProperty('martingale_step_coefficient', str, float),
                              ThreeCommasJsonProperty('stop_loss_percentage', str, float),
                              # ThreeCommasJsonProperty('cooldown', str, ), # TODO probably parsed into int, could be float
                              ThreeCommasJsonProperty('btc_price_limit', str, float),
                              ThreeCommasJsonProperty('strategy', str),
                              ThreeCommasJsonProperty('min_volume_btc_24h', str, float),
                              ThreeCommasJsonProperty('profit_currency', str),
                              # ThreeCommasJsonProperty('min_price', ), TODO probably float
                              # ThreeCommasJsonProperty('max_price', ), TODO probably float
                              ThreeCommasJsonProperty('stop_loss_type', str),
                              ThreeCommasJsonProperty('safety_order_volume_type', str),
                              ThreeCommasJsonProperty('base_order_volume_type', str),
                              ThreeCommasJsonProperty('account_name', str),
                              ThreeCommasJsonProperty('trailing_deviation', str, float),
                              ThreeCommasJsonProperty('finished_deals_profit_usd', str, float),
                              ThreeCommasJsonProperty('finished_deals_count', str, int),
                              ThreeCommasJsonProperty('leverage_type', str),
                              # ThreeCommasJsonProperty('leverage_custom_value', ),  TODO probably str
                              ThreeCommasJsonProperty('start_order_type', str),
                              ThreeCommasJsonProperty('active_deals_usd_profit', str, float),
                              ThreeCommasJsonProperty('active_deals', List[dict], 'List[Deal]'),
                              # TODO probably complex type
                              ThreeCommasJsonProperty('bot_events', List[dict], 'List[BotEvent]'),
                          ]),
    ThreeCommasModelClass(name='DealMarketOrder',
                          properties=[
                              ThreeCommasJsonProperty('order_id', str, int),
                              ThreeCommasJsonProperty('order_type', str),
                              ThreeCommasJsonProperty('deal_order_type', str),
                              ThreeCommasJsonProperty('cancellable', bool),
                              ThreeCommasJsonProperty('status_string', str),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('updated_at', str, datetime.datetime),

                              ThreeCommasJsonProperty('quantity', str, float),
                              ThreeCommasJsonProperty('quantity_remaining', str, float),
                              ThreeCommasJsonProperty('total', str, float),
                              ThreeCommasJsonProperty('rate', str, float),
                              ThreeCommasJsonProperty('average_price', str, float),
                          ]),
    ThreeCommasModelClass(name='PieChartDataElement',
                          properties=[
                              ThreeCommasJsonProperty('code', str),
                              ThreeCommasJsonProperty('coinmarketcapid', str, int),  # probably int
                              ThreeCommasJsonProperty('name', str),
                              ThreeCommasJsonProperty('y', float),
                              ThreeCommasJsonProperty('percentage', float),
                              ThreeCommasJsonProperty('amount', float),
                              ThreeCommasJsonProperty('btc_value', str, float),
                              ThreeCommasJsonProperty('usd_value', str, float),
                              ThreeCommasJsonProperty('account_id', int),
                          ]),
    ThreeCommasModelClass(name='Account',
                          properties=[
                              ThreeCommasJsonProperty('id', int),
                              ThreeCommasJsonProperty('auto_balance_period', int),
                              # ThreeCommasJsonProperty('auto_balance_portfolio_id', NoneType),
                              # ThreeCommasJsonProperty('auto_balance_portfolio', NoneType),
                              # ThreeCommasJsonProperty('auto_balance_currency_change_limit', NoneType),
                              ThreeCommasJsonProperty('autobalance_enabled', bool),
                              ThreeCommasJsonProperty('hedge_mode_available', bool),
                              ThreeCommasJsonProperty('hedge_mode_enabled', bool),
                              ThreeCommasJsonProperty('is_locked', bool),
                              ThreeCommasJsonProperty('smart_trading_supported', bool),
                              ThreeCommasJsonProperty('smart_selling_supported', bool),
                              # ThreeCommasJsonProperty('available_for_trading', dict), # TODO
                              ThreeCommasJsonProperty('stats_supported', bool),
                              ThreeCommasJsonProperty('trading_supported', bool),
                              ThreeCommasJsonProperty('market_buy_supported', bool),
                              ThreeCommasJsonProperty('market_sell_supported', bool),
                              ThreeCommasJsonProperty('conditional_buy_supported', bool),
                              ThreeCommasJsonProperty('bots_allowed', bool),
                              ThreeCommasJsonProperty('bots_ttp_allowed', bool),
                              ThreeCommasJsonProperty('bots_tsl_allowed', bool),
                              ThreeCommasJsonProperty('gordon_bots_available', bool),
                              ThreeCommasJsonProperty('multi_bots_allowed', bool),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('updated_at', str, datetime.datetime),
                              # ThreeCommasJsonProperty('last_auto_balance', NoneType),
                              ThreeCommasJsonProperty('fast_convert_available', bool),
                              ThreeCommasJsonProperty('grid_bots_allowed', bool),
                              ThreeCommasJsonProperty('api_key_invalid', bool),
                              ThreeCommasJsonProperty('nomics_id', str),
                              ThreeCommasJsonProperty('market_icon', str),
                              ThreeCommasJsonProperty('deposit_enabled', bool),
                              ThreeCommasJsonProperty('supported_market_types', List[str]),
                              ThreeCommasJsonProperty('api_key', str),
                              ThreeCommasJsonProperty('name', str),
                              # ThreeCommasJsonProperty('auto_balance_method', NoneType),
                              # ThreeCommasJsonProperty('auto_balance_error', NoneType),
                              # ThreeCommasJsonProperty('customer_id', NoneType),
                              # ThreeCommasJsonProperty('subaccount_name', NoneType),
                              # ThreeCommasJsonProperty('lock_reason', NoneType),
                              ThreeCommasJsonProperty('btc_amount', str, float),
                              ThreeCommasJsonProperty('usd_amount', str, float),
                              ThreeCommasJsonProperty('day_profit_btc', str, float),
                              ThreeCommasJsonProperty('day_profit_usd', str, float),
                              ThreeCommasJsonProperty('day_profit_btc_percentage', str, float),
                              ThreeCommasJsonProperty('day_profit_usd_percentage', str, float),
                              ThreeCommasJsonProperty('btc_profit', str, float),
                              ThreeCommasJsonProperty('usd_profit', str, float),
                              ThreeCommasJsonProperty('usd_profit_percentage', str, float),
                              ThreeCommasJsonProperty('btc_profit_percentage', str, float),
                              ThreeCommasJsonProperty('total_btc_profit', str, float),
                              ThreeCommasJsonProperty('total_usd_profit', str, float),
                              ThreeCommasJsonProperty('pretty_display_type', str),
                              ThreeCommasJsonProperty('exchange_name', str),
                              ThreeCommasJsonProperty('market_code', str, 'AccountMarketCode'),
                          ]),
    ThreeCommasModelClass(name='PairsBlackList',
                          properties=[
                              ThreeCommasJsonProperty('pairs', List[str]),
                          ]),
    ThreeCommasModelClass(name='SmartTradeV2Entity',
                          properties=[
                              ThreeCommasJsonProperty('id', int),
                              ThreeCommasJsonProperty('version', int),
                              ThreeCommasJsonProperty('account', dict),
                              ThreeCommasJsonProperty('pair', str),
                              ThreeCommasJsonProperty('instant', bool),
                              ThreeCommasJsonProperty('status', dict),
                              ThreeCommasJsonProperty('leverage', dict),
                              ThreeCommasJsonProperty('position', dict),
                              ThreeCommasJsonProperty('take_profit', dict),
                              ThreeCommasJsonProperty('stop_loss', dict),
                              ThreeCommasJsonProperty('reduce_funds', dict),
                              ThreeCommasJsonProperty('market_close', dict),
                              ThreeCommasJsonProperty('note', str),
                              # ThreeCommasJsonProperty('note_raw', NoneType),
                              ThreeCommasJsonProperty('skip_enter_step', bool),
                              ThreeCommasJsonProperty('data', dict),
                              ThreeCommasJsonProperty('profit', dict),
                              ThreeCommasJsonProperty('margin', dict),
                              ThreeCommasJsonProperty('is_position_not_filled', bool),
                          ]),
    ThreeCommasModelClass(name='SmartTradeV2Trade',
                          properties=[
                              ThreeCommasJsonProperty('id', int),
                              ThreeCommasJsonProperty('average_price', str, float),
                              ThreeCommasJsonProperty('follow_price_type', str),
                              ThreeCommasJsonProperty('initial_amount', str, float),
                              ThreeCommasJsonProperty('initial_total', str, float),
                              # ThreeCommasJsonProperty('order_price', NoneType),
                              ThreeCommasJsonProperty('order_side', str),
                              ThreeCommasJsonProperty('order_type', str),
                              ThreeCommasJsonProperty('pair', str),
                              # ThreeCommasJsonProperty('position_percentage', NoneType),
                              ThreeCommasJsonProperty('realised_amount', str, float),
                              ThreeCommasJsonProperty('realised_total', str, float),
                              ThreeCommasJsonProperty('status', str),
                              # ThreeCommasJsonProperty('take_profit_percentage', NoneType),
                              ThreeCommasJsonProperty('trade_purpose', str),
                              # ThreeCommasJsonProperty('trail_percentage', NoneType),
                              # ThreeCommasJsonProperty('trail_value', NoneType),
                              ThreeCommasJsonProperty('trailing_enabled', bool),
                              # ThreeCommasJsonProperty('trailing_last_price', NoneType),
                              # ThreeCommasJsonProperty('trailing_last_price_updated_at', NoneType),
                              # ThreeCommasJsonProperty('trigger_condition', NoneType),
                              # ThreeCommasJsonProperty('trigger_price', NoneType),
                              # ThreeCommasJsonProperty('trigger_price_percentage', NoneType),
                              ThreeCommasJsonProperty('trigger_type', str),
                              ThreeCommasJsonProperty('created_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('updated_at', str, datetime.datetime),
                              ThreeCommasJsonProperty('realised_percentage', str, float),
                              ThreeCommasJsonProperty('initial_price', str, float),
                              ThreeCommasJsonProperty('realised_price', str, float),
                              ThreeCommasJsonProperty('cancelable', bool),
                              ThreeCommasJsonProperty('force_processable', bool),
                          ]),
    ThreeCommasModelClass(name='BalanceChartDataElement',
                          properties=[
                              ThreeCommasJsonProperty('date', int),
                              ThreeCommasJsonProperty('usd', float),
                              ThreeCommasJsonProperty('btc', float),
                              ThreeCommasJsonProperty('btc_deposit_amount', float),
                              ThreeCommasJsonProperty('usd_deposit_amount', float),
                          ]),
]


def generate_models():
    with open('../src/three_commas/model/generated_models.py', 'w') as f:
        file_buffer = list()
        # imports
        file_buffer.append('from typing import List, Union')
        file_buffer.append('import datetime')
        file_buffer.append('from .models import * #OfDictClass, ThreeCommasParser, BotEvent')
        file_buffer.append('from .generated_enums import * #DealStatus, AccountMarketCode')
        file_buffer.append('from . import other_enums')

        for tc_gen_class in tc_generated_classes:
            file_buffer.append('')
            file_buffer.append('')
            file_buffer.append(f'class {tc_gen_class.name}(OfDictClass):')

            for prop in tc_gen_class.properties:
                file_buffer.extend(create_getter(prop))
                file_buffer.extend(create_setter(prop))
                # if is_abstract_three_commas_enum_class(prop.initial_type):
                #    file_buffer.extend(create_enum_boolean_methods(prop))

        file_buffer.append('')

        generated_code = '\n'.join(file_buffer)
        f.write(generated_code)


def create_enum_boolean_methods(prop: ThreeCommasJsonProperty):
    # Deprecated
    file_buffer = list()
    property_name = prop.name
    enum_type = prop.initial_type

    for et in enum_type._list_values():
        file_buffer.append('')
        file_buffer.append(f"{INDENT}def is_{property_name}_{et}(self) -> bool:")
        file_buffer.append(f"{INDENT * 2}return self.get('{property_name}') == '{et}'")

    return file_buffer


def create_getter(prop: ThreeCommasJsonProperty):
    file_buffer = list()
    property_name = prop.name
    initial_type_name_str = get_type_name_string(prop.initial_type)
    parsed_type_name_str = get_type_name_string(prop.parsed_type)

    getter_name = create_getter_function_name(prop)

    return_type = f'Union[{initial_type_name_str}, {parsed_type_name_str}]' if prop.parsed_type else initial_type_name_str

    file_buffer.append('')
    if prop.parsed_type is not None:
        if prop.parsed_type is datetime.datetime:
            file_buffer.append(f"{INDENT}@ThreeCommasParser.parsed_timestamp")
        elif prop.parsed_type in (int, float) or is_abstract_three_commas_enum_class(prop.parsed_type):
            file_buffer.append(f"{INDENT}@ThreeCommasParser.parsed({parsed_type_name_str})")
        else:
            file_buffer.append(f"{INDENT}@ThreeCommasParser.lazy_parsed({parsed_type_name_str})")
    file_buffer.append(f"{INDENT}def {getter_name}(self) -> {return_type}:")
    file_buffer.append(f"{INDENT * 2}return self.get('{property_name}')")

    return file_buffer


def create_getter_function_name(prop):
    property_variable = prop.name.replace('?', '')  # handles properties like 'deletable?'
    if prop.initial_type is bool:
        function_name = property_variable if property_variable.startswith('is_') else f'is_{property_variable}'
        function_name = function_name.replace('?', '')
    else:
        function_name = f'get_{property_variable}'
    return function_name


def create_setter_function_name(prop):
    property_variable = prop.name.replace('?', '')  # handles properties like 'deletable?'
    return f'set_{property_variable}'


def create_setter(prop: ThreeCommasJsonProperty):
    file_buffer = list()
    property_name = prop.name
    property_variable = property_name.replace('?', '')
    initial_type_name_str = get_type_name_string(prop.initial_type)
    parsed_type_name_str = get_type_name_string(prop.parsed_type)

    union_setter_condition = not is_typing_module_type(prop.initial_type) \
                             and is_abstract_three_commas_enum_class(prop.parsed_type)
    if union_setter_condition or is_primitive_type(prop.parsed_type):
        attribute_types = f'Union[{initial_type_name_str}, {parsed_type_name_str}]'
    else:
        attribute_types = initial_type_name_str

    setter_name = create_setter_function_name(prop)

    file_buffer.append('')
    file_buffer.append(f'{INDENT}def {setter_name}(self, {property_variable}: {attribute_types}):')
    file_buffer.append(f"{INDENT * 2}self['{property_name}'] = {property_variable}")

    return file_buffer


def get_type_name_string(t: Union[type, str]) -> str:
    if t is None:
        return None
    if isinstance(t, str):
        return t
    if t is dict:
        return 'dict'

    if is_primitive_type(t):
        return t.__name__

    if t is datetime.datetime:
        return 'datetime.datetime'

    if is_typing_module_type(t):
        s = str(t).replace('typing.', '')
        inner_type_pure_name = s.split('[')[1].split(']')[0].split('.')[-1]
        return f'List[{inner_type_pure_name}]'
        # return str(t).replace('typing.', '')

    if is_abstract_three_commas_enum_class(t):
        return t.__name__

    return t.__name__.split('.')  # str(t).split('.')[-1].replace('>', '').replace("'", '')


def is_typing_module_type(t) -> bool:
    if t is None:
        return False
    return 'typing' in str(type(t))


def is_primitive_type(t) -> bool:
    if t is None:
        return False
    return t in {int, float, str, bool}


def is_abstract_three_commas_enum_class(t) -> bool:
    if t is None:
        return False
    return str(t) in {'AccountMarketCode', 'DealStatus'}
    # return not is_typing_module_type(t) and not isinstance(t, str) and issubclass(t, AbstractStringEnum)
    # return not is_typing_module_type(t) and issubclass(t, AbstractStringEnum)


def generate_json_properties():
    def is_int(s: str):
        if s.startswith('-'):
            s = s[1:]
        return s.isnumeric()

    def is_float(s: str):
        if s.startswith('-'):
            s = s[1:]
        return '.' in s and s.replace('.', '', 1).isdigit()

    with open('../test/sample_data/accounts/paper_account.json') as f:
        d: dict = json.loads(f.read())
        for k, v in d.items():
            t_str = type(v).__name__
            parsed_t = None
            if isinstance(v, str) and is_int(v):
                parsed_t = 'int'
            if isinstance(v, str) and is_float(v):
                parsed_t = 'float'

            if parsed_t:
                print(f"ThreeCommasJsonProperty('{k}', {t_str}, {parsed_t}),")
            else:
                print(f"ThreeCommasJsonProperty('{k}', {t_str}),")


if __name__ == '__main__':
    generate_models()
    # generate_json_properties()
