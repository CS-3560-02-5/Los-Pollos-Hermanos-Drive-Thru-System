
import uuid
from itertools import cycle
class Order:
    queue = cycle(range(1, 200))

    def __init__(self, name: str, *, order_id=uuid.uuid1().hex, status='s'):
        self.name = name
        self.order_id = order_id
        self.queue_number = next(self.queue)
        self.status = status

    def prepare(self):
        self.status = 'p'
        pass

    def complete(self):
        self.status = "c"
        pass

    def cancel(self):
        self.status = 'x'
        pass
