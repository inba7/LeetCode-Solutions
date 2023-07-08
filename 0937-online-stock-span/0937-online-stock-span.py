class StockSpanner(object):
    from collections import OrderedDict
    def __init__(self):
        self.stack = []
    def next(self, price):
        days_total = 0
        while self.stack and self.stack[-1][0] <= price:
            days_total += self.stack.pop()[1]
        self.stack.append([price, days_total + 1])
        return days_total + 1