# temporary storage for historic data
class DataStore:
    def __init__(self) -> None:
        self.historic_df = None

    def store_historic_data(self, historic_df):
        self.historic_df = historic_df


_data_store = {}


def get_data_store(symbol):
    data_store = _data_store.get(symbol, None)
    if (data_store):
        return data_store
    _data_store[symbol] = DataStore()
    return _data_store[symbol]


def release_data_store(symbol):
    data_store = _data_store.get(symbol, None)
    if data_store:
        _data_store[symbol] = None
