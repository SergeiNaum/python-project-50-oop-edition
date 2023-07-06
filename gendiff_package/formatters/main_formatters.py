from abc import ABC, abstractmethod
from colorama import Fore, Style

class Formatter(ABC):
    """Абстрактный класс форматирования (base class)"""

    RED = Fore.RED
    GREEN = Fore.GREEN
    WHITE = Fore.LIGHTWHITE_EX
    RESET = Style.RESET_ALL

    @classmethod
    @abstractmethod
    def to_string(cls, value, depth: int):
        pass

    @classmethod
    @abstractmethod
    def iter_(cls, node: dict, path=""):
        pass

    @classmethod
    def format_(cls, node: dict):
        return cls.iter_(node)

    @classmethod
    def colored_string(cls, value, color):
        return f"{color}{value}{cls.RESET}"

    @classmethod
    def colored_formated_str(cls, item, depth):
        return f"{cls.WHITE}{cls.to_string(item, depth)}{cls.RESET}"
