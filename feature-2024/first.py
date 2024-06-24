class Counter:
    def __init__(self, limit=100) -> None:
        self.counter = 0
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter <= self.limit:
            return self.counter
        raise StopIteration
        
    
