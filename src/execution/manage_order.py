import time


def fun_limits(order_dhan):
    funds = order_dhan.get_fund_limits()
    if funds['status'] == 'success':
        return funds['availabelBalance']
    else:
        return f"Error reading funds: {funds['remarks']}"
    

def all_positions(order_dhan):
    response = order_dhan.get_positions()
    print(response)
    print(response['data'])


def open_positions(order_dhan):
    response = order_dhan.get_positions()
    if response['status'] == 'success':
        if len(response['data']) > 0:
            positions = response['data']
            return positions['securityId'], positions['sellQty'], positions['positionType']
        else:
            return '0', 0, 0
    else:
        return '-1', 0, response['remarks']

def new_position(order_dhan, securityId, Qty, positionType):
    if positionType == "SHORT":
        response = order_dhan.place_order(
            transaction_type=order_dhan.SELL,
            exchange_segment=order_dhan.FNO,
            product_type=order_dhan.MARGIN,
            order_type=order_dhan.MARKET,
            validity='DAY',
            security_id = securityId,
            quantity=Qty,
            price=0.0,
        )
    else:
        response = order_dhan.place_order(
            transaction_type=order_dhan.BUY,
            exchange_segment=order_dhan.FNO,
            product_type=order_dhan.MARGIN,
            order_type=order_dhan.MARKET,
            validity='DAY',
            security_id = securityId,
            quantity=Qty,
            price=0.0,
        )
    if response['status'] == 'success':
        order = response['data']
        orderId = order['orderId']
        for _ in range(6):
            if order['orderStatus'] != 'TRADED ':
                time.sleep(0.5)    
                order = order_dhan.get_order_by_id(orderId)
                if order['status'] == 'success':
                    order = order['data']
                else:
                    return "failed", order['remarks']
            else:
                return 'success', order['orderId']
    else:
        return "failed", order['remarks']
    


def exit_position(order_dhan, securityId, Qty, positionType):
    if positionType == "SHORT":
        response = order_dhan.place_order(
            transaction_type=order_dhan.BUY,
            exchange_segment=order_dhan.FNO,
            product_type=order_dhan.MARGIN,
            order_type=order_dhan.MARKET,
            validity='DAY',
            security_id = securityId,
            quantity=Qty,
            price=0.0,
        )
    else:
        response = order_dhan.place_order(
            transaction_type=order_dhan.SELL,
            exchange_segment=order_dhan.FNO,
            product_type=order_dhan.MARGIN,
            order_type=order_dhan.MARKET,
            validity='DAY',
            security_id = securityId,
            quantity=Qty,
            price=0.0,
        )
    if response['status'] == 'success':
        order = response['data']
        orderId = order['orderId']
        for _ in range(6):
            if order['orderStatus'] != 'TRADED ':
                time.sleep(0.5)    
                order = order_dhan.get_order_by_id(orderId)
                if order['status'] == 'success':
                    order = order['data']
                else:
                    return "failed", order['remarks']
            else:
                return 'success', order['orderId']
    else:
        return "failed", order['remarks']
    
