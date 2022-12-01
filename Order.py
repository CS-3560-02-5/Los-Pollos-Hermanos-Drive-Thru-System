import uuid
from itertools import cycle


class Order:
    queue = cycle(range(1, 200))

    def __init__(self, customer_name: str, *, order_id=uuid.uuid1().hex, order_status='s', queue_num=-1):
        self.customer_name = customer_name
        self.order_id = order_id
        self.queue_num = next(self.queue)
        self.order_status = order_status

    def getQueue(self):
        return self.queue_num
    def prepare(self):
        self.order_status = 'p'
        pass

    def complete(self):
        self.order_status = "c"
        pass

    def cancel(self):
        self.order_status = 'x'
        pass
