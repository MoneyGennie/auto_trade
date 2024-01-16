from .manage_order import fun_limits, open_positions, exit_position, new_position


class OrderExecution:
    def __init__(self, my_acc):
        self.my_acc = my_acc
        self.sell_qty = 15
        self.position_type = "LONG"

    def execute_trade(self, security_id):
        self.security_id = str(security_id)
        print(self.security_id)
        print(type(self.security_id))
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
        securityId, qty, positionType = open_positions(self.my_acc)
        if securityId != '0' and securityId != '-1':
            print(f"Current Position detils: Security ID {securityId}, Quantity {qty}, Position Type {positionType}")
        else:
            print("Currently No Open Position")

        print("Holding position")