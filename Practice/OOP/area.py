class Area:
    long: float
    width: float
    area: float

    def __init__(self, l, w) -> None:
        self.long = l
        self.width = w

    def calArea(self):
        self.area = self.long * self.width