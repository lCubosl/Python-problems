# 901. Online stock span
# monotonic
class StockSpanner():
  def __init__(self):
    self.stack = []

  def next(self, price):
    span = 1
    while self.stack and self.stack[-1][0] <= price:
      span += self.stack[-1][1]
      self.stack.pop()
    self.stack.append([price, span])
    
    return self.stack[-1][1]

stockSpanner = StockSpanner()
print(stockSpanner.next(100)) # return 1
print(stockSpanner.next(80))  # return 1
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(70))  # return 2
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(75))  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(85))  # return 6