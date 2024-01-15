from manage_order import fun_limits, open_positions, exit_position, new_position


class OrderExecution:
    def __init__(self, my_acc):
        self.my_acc = my_acc
        self.sell_qty = 15
        self.position_type = "SHORT"

    def execute_trade(self, security_id):
        self.security_id = security_id
        self.funds = fun_limits(self.my_acc)
        print("funds available: ", self.funds)
        securityId, qty, positionType = open_positions(self.my_acc)
        if securityId != '0' and securityId != '-1':
            status, orderId = exit_position(self.my_acc, securityId, qty, positionType )
            if status == 'success':
                print(f"Success (Existing Position): {orderId}")
            else:
                print(f"Failed (Existing Position) with reason: {orderId}")

        elif securityId == '0':
            print("Currently no open position")
        else:
            print(f"Failed with reason: {self.positionType}")
        status, orderId = new_position(self.my_acc, self.security_id, self.sell_qty, self.position_type)
        if status == 'success':
            print(f"Success (New Position): {orderId}")
        else:
            print(f"Failed (New Position) with reason: {orderId}")


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