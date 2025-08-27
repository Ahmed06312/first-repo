<<<<<<< HEAD
class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

  def get_price(self, item):
    return self.menu.get(item.lower())

  def add_item(self, item, price):
=======
class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

  def get_price(self, item):
    return self.menu.get(item.lower())

  def add_item(self, item, price):
>>>>>>> 9da8d046e45ae3d94f7d64fce2fdae6a7cae459b
    self.menu[item.lower()] = price