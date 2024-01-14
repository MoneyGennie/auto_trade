import time


class OrderExecution:
    def __init__(self, my_acc):
        self.my_acc = my_acc
        self.sell_qty = 15
        

    def execute_call(self, security_id):
        response = self.my_acc.get_positions()
        self.my_pos = response['data']
        if len(self.my_pos) != 0:
            exit_order_response = self.my_acc.place_order(
                tag='',
                transaction_type=self.my_acc.BUY,
                exchange_segment=self.my_acc.FNO,
                product_type=self.my_acc.CNC,
                order_type=self.my_acc.MARKET,
                validity='DAY',
                security_id=self.my_pos['securityId'],
                quantity=self.my_pos['sellQty'],
                disclosed_quantity=0,
                price=0,
                trigger_price=0,
                after_market_order=False,
                amo_time='OPEN',
                bo_profit_value=0,
                bo_stop_loss_Value=0,
                drv_expiry_date=None,
                drv_options_type=None,
                drv_strike_price=None    
            )
            order_id = exit_order_response['data']['orderId']
            order_status = exit_order_response['data']['orderStatus']
            while order_status != "TRADED":
                response = self.my_acc.get_order_by_id(order_id)
                order_status = response['data']['orderStatus']
                print('Exit Order status: ', order_status)
                time.sleep(0.5)
            print('Exit Order status: ', order_status)

            new_order_response = self.my_acc.place_order(
                    tag='',
                    transaction_type=self.my_acc.SELL,
                    exchange_segment=self.my_acc.FNO,
                    product_type=self.my_acc.CNC,
                    order_type=self.my_acc.MARKET,
                    validity='DAY',
                    security_id = security_id,
                    quantity=self.sell_qty,
                    disclosed_quantity=0,
                    price=0,
                    trigger_price=0,
                    after_market_order=False,
                    amo_time='OPEN',
                    bo_profit_value=0,
                    bo_stop_loss_Value=0,
                    drv_expiry_date=None,
                    drv_options_type=None,
                    drv_strike_price=None    
                )
            order_id = new_order_response['data']['orderId']
            order_status = new_order_response['data']['orderStatus']
            while order_status != "TRADED":
                response = self.my_acc.get_order_by_id(order_id)
                order_status = response['data']['orderStatus']
                print('New entry status: ', order_status)
                time.sleep(0.5)
            print('New entry status: ', order_status)

        else:
            new_order_response = self.my_acc.place_order(
                    tag='',
                    transaction_type=self.my_acc.SELL,
                    exchange_segment=self.my_acc.FNO,
                    product_type=self.my_acc.CNC,
                    order_type=self.my_acc.MARKET,
                    validity='DAY',
                    security_id = security_id,
                    quantity=self.sell_qty,
                    disclosed_quantity=0,
                    price=0,
                    trigger_price=0,
                    after_market_order=False,
                    amo_time='OPEN',
                    bo_profit_value=0,
                    bo_stop_loss_Value=0,
                    drv_expiry_date=None,
                    drv_options_type=None,
                    drv_strike_price=None    
                )
            order_id = new_order_response['data']['orderId']
            order_status = new_order_response['data']['orderStatus']
            while order_status != "TRADED":
                response = self.my_acc.get_order_by_id(order_id)
                order_status = response['data']['orderStatus']
                print('New entry status: ', order_status)
                time.sleep(0.5)
            print('New entry status: ', order_status)
            


        
            
    
    def execute_put(self):
        # Add your logic for executing a "PUT" order
        print("Executing PUT order")

    def execute_hold(self):
        # Add your logic for executing a "hold" order
        self.my_pos = self.my_acc.get_positions()
        if len(self.my_pos['data']) != 0:
            print("Current Position detils:")
            for item in self.my_pos:
                print(f"Trading Symbol: {item['tradingSymbol']}")
                print(f"Position Type: {item['positionType']}")
                print(f"Realized Profit: {item['realizedProfit']}")
                print(f"Unrealized Profit: {item['unrealizedProfit']}")
                print()
        else:
            print("Currently No Open Position")

        print("Holding position")