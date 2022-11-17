
from datetime import datetime

class Order:
    def __init__(self, name: str, id: int, time_in):
        name = name
        id = id
        time_in = datetime.now()
        print(type(time_in))
        time_out = None
        status = "entered"

    def prepare(self):
        status = "prepared"
        pass

    def complete(self):
        time_out = datetime.now()
        status = "completed"
        pass

    def edit(self):
        pass

    def cancel():
        pass
