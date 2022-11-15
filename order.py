
import pyodbc

class Order:
    def __init__(self, name: str, order_id: int, queue_number: int):
        name = name
        order_id = order_id  # PK
        queue_number = queue_number
        status = 's'

    def prepare(self):
        status = 'p'
        pass

    def complete(self):
        status = "c"
        pass

    def cancel(self):
        status = 'x'
        pass

    def edit_add(self, menu_id: int):
        pass

    def edit_remove(self, menu_id: int):
        pass
