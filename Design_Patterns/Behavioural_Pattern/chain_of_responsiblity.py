'''
Intent: Chain of responsibility is a behavioural design pattern that lets you pass requests along a chain of handlers
until one of them handles request.

Analogy : Call center -> Robot -> technician -> engineer
Url: https://refactoring.guru/design-patterns/chain-of-responsibility/python/example
'''

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional

"""
The handler interface declares a method for building the chain of handlers. It also declares a method for executing 
a request.
"""


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


"""
The default chaining behaviour can be implemented inside a base handler class.
"""


class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


"""
All Concerete Handlers either handle a request or pass it to the next handler in the chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler):
    "The client code is usually suited to work with a single handler ,it is not aware that handler is part of chain"

    for food in ["Nut", "Banana", "Coffee"]:
        print(f"\nClient: Who wants a {food}")
        result = handler.handle(food)
        if result:
            print(f"{result}", end="")
        else:
            print(f"{food} was left untouched.", end="")


if __name__ == '__main__':
    monkey = MonkeyHandler()
    dog = DogHandler()
    squirrel = SquirrelHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print()
    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
