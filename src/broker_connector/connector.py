from dhanhq import dhanhq


class connector():
    def __init__(self, client_id, order_key, data_key) -> None:
        self.client_id = client_id
        self.order_key = order_key
        self.data_key = data_key

    def data_api_connect(self):
        dhan_data = dhanhq(self.client_id, self.data_key)
        return dhan_data

    def order_api_connect(self):
        dhan_order = dhanhq(self.client_id, self.order_key)
        return dhan_order
