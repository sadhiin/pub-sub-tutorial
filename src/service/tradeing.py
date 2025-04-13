class SimpleTradingStrategy:
   def __init__(self, threshold):
       self.threshold = threshold

   def process_event(self, event):
       if event.price < self.threshold:
           print(f"Buying {event.symbol} at {event.price}")

strategy = SimpleTradingStrategy(threshold=150)

for message in consumer:
   event = message.value
   strategy.process_event(event)