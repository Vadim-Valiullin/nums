from abc import ABC

class Storage(ABC):


    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity


    def add(self, product: str, quantity: int):
        if product in self.items:
            self._items[product] += quantity
        else:
            self._items[product] = quantity
        """ увеличивает запас items """


    def remove(self, product: str, quantity: int):
        if quantity < self._items[product]:
            self._items[product] -= quantity
        """ уменьшает запас items """


    def get_free_space(self):
        """ вернуть количество свободных мест """
        return self._capacity


    def get_items(self):
        return self._items
        """ возвращает сожержание склада в словаре {товар: количество}"""



    def get_unique_items_count():
        return  len(self._items)
        """ возвращает количество уникальных товаров """


class Store(Storage):


            """ В нем хранится любое количество любых товаров.
    Store не может быть заполнен если свободное место закончилось """


def add(self, product: str, quantity: int):
    if self.get_free_space >= quantity:
        super().add(product, quantity)
        return True
    return False
""" увеличивает запас items с учетом лимита capacity """


def remove(self, product: str, quantity: int):
    if quantity <= self._items[product] and product in self.get_items():
        super().remove(product, quantity)
        True
    False
    """ уменьшает запас items но не ниже 0 """


Class Shop():


    def add(self, product: str, quantity: int):
        if self.get_free_space >= quantity:
            super().add(product, quantity)
            return True
        return False
    """ увеличивает запас items с учетом лимита capacity """


    def remove(self, product: str, quantity: int):
        if quantity <= self._items[product] and product in self.get_items():
            super().remove(product, quantity)
            True
        False
        """ уменьшает запас items но не ниже 0 """


class Request:
    def __init__(self, fromm: str, to: str, amount: int, product: str):
        self.fromm = fromm
        self.to = to
        self.product = product
        self.amount = amount


    def __repr__(self, fromm: str, to: str, amount: int, product: str):
        return  (f'Доставить {self.amount} {self.product} из {self.take_from} в {self.to}')








