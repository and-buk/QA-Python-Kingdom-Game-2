from __future__ import annotations
import random
from abc import ABC, abstractmethod
from typing import Any, Union


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    абстрактные классы игровых предметов.
    """

    @abstractmethod
    def create_standart_item(self) -> Union[Sword, Bow, SpellBook, Arrow, Apple, Totem]:
        """Метод для создания стандартного игрового предмета."""
        pass

    @abstractmethod
    def create_unique_item(self) -> Union[UniqueSword, UniqueBow, UniqueSpellBook]:
        """Метод для создания улучшенного игрового предмета."""
        pass


class SwordFactory(AbstractFactory):
    """Фабрика по производству мечей."""

    def __init__(self) -> None:
        self.standart_damage_rate = random.randint(5, 20)
        self.improved_damage_rate = random.randint(20, 40)

    def create_standart_item(self) -> Sword:
        """Метод для создания стандартного меча."""
        return Sword(self.standart_damage_rate)

    def create_unique_item(self) -> UniqueSword:
        """Метод для создания улучшенного меча."""
        return UniqueSword(self.improved_damage_rate)


class BowFactory(AbstractFactory):
    """Фабрика по производству луков."""

    def __init__(self) -> None:
        self.standart_damage_rate = random.randint(5, 20)
        self.improved_damage_rate = random.randint(20, 40)

    def create_standart_item(self) -> Bow:
        """Метод для создания стандартного лука."""
        return Bow(self.standart_damage_rate)

    def create_unique_item(self) -> UniqueBow:
        """Метод для создания уникального лука."""
        return UniqueBow(self.improved_damage_rate)


class ArrowFactory(AbstractFactory):
    """Фабрика по производству стрел."""

    def create_standart_item(self) -> Arrow:
        """Метод для стандартных стрел для лука."""
        return Arrow()

    def create_unique_item(self) -> Any:
        """Метод для уникальных стрел для лука."""
        pass


class MagicLibrary(AbstractFactory):
    """Волшебная библиотека в которой можно найти различные книги с заклинанями."""

    def __init__(self) -> None:
        self.standart_damage_rate: int = random.randint(5, 20)
        self.improved_damage_rate: int = random.randint(20, 40)

    def create_standart_item(self) -> SpellBook:
        """Метод для создания стандартной книги с заклинаниями."""
        return SpellBook(self.standart_damage_rate)

    def create_unique_item(self) -> UniqueSpellBook:
        """Метод для создания уникальной книги с заклинаниями."""
        return UniqueSpellBook(self.improved_damage_rate)


class MagicTree(AbstractFactory):
    """Волшебное дерево с целебными яблоками."""

    def __init__(self) -> None:
        self.healing_power: int = random.randint(3, 10)

    def create_standart_item(self) -> Apple:
        """Метод для создания целебного яблока."""
        return Apple(self.healing_power)

    def create_unique_item(self) -> Any:
        """Метод для создания уникального по своим свойствам целебного яблока."""
        pass


class MysteriousPlace(AbstractFactory):
    """Фабрика по производству тотемов."""

    def create_standart_item(self) -> Totem:
        """Метод для создания стандартного тотема."""
        return Totem()

    def create_unique_item(self) -> Any:
        """Метод для создания уникального по своим свойствам тотема."""
        pass


class AbstractSword(ABC):
    """Базовый интерфейс абстрактного класса "Меч"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        pass


class AbstractUniqueSword(ABC):
    """Базовый интерфейс абстрактного класса "Уникальный меч"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        pass


class AbstractBow(ABC):
    """Базовый интерфейс абстрактного класса "Лук"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        pass


class AbstractUniqueBow(ABC):
    """Базовый интерфейс абстрактного класса "Уникальный лук"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        pass


class AbstractArrow(ABC):
    """Базовый интерфейс абстрактного класса "Стрелы"."""

    pass


class AbstractSpellBook(ABC):
    """Базовый интерфейс абстрактного класса "Книга заклинаний"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        pass


class AbstractUniqueSpellBook(ABC):
    """Базовый интерфейс абстрактного класса "Уникальная книга заклинаний"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        pass


class AbstractApple(ABC):
    """Базовый интерфейс абстрактного предмета "Яблоко"."""

    @abstractmethod
    def get_hp_info(self) -> int:
        pass


class AbstractTotem(ABC):
    """Базовый интерфейс абстрактного предмета "Тотем"."""

    pass


class Sword(AbstractSword):
    """Класс обьекта для создания стандартного меча."""

    def __init__(self, damage_rate: int) -> None:
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Меч"


class UniqueSword(AbstractUniqueSword):
    """Класс обьекта для создания уникального меча."""

    def __init__(self, damage_rate: int) -> None:
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Меч"


class Bow(AbstractBow):
    """Класс обьекта для создания лука."""

    def __init__(self, damage_rate: int) -> None:
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Лук"


class UniqueBow(AbstractUniqueBow):
    """Класс обьекта для создания уникального лука."""

    def __init__(self, damage_rate: int) -> None:
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Лук"


class Arrow(AbstractArrow):
    """Класс обьекта для создания стрел."""

    def __init__(self) -> None:
        self.damage_rate: int = 0

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Стрелы"


class SpellBook(AbstractSpellBook):
    """Класс обьекта для создания книги заклинаний."""

    def __init__(self, damage_rate: int) -> None:
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Книга заклинаний"


class UniqueSpellBook(AbstractUniqueSpellBook):
    """Класс обьекта для создания уникальной книги заклинаний."""

    def __init__(self, damage_rate: int) -> None:
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        return self.damage_rate

    def __str__(self) -> str:
        return "Книга заклинаний"


class Apple(AbstractApple):
    """Класс обьекта для создания целебного яблока."""

    def __init__(self, healing_power: int) -> None:
        self.healing_power = healing_power

    def get_hp_info(self) -> int:
        return self.healing_power

    def __str__(self) -> str:
        return f"Вы нашли яблоко здоровья! +{self.healing_power} к здоровью героя."


class Totem(AbstractTotem):
    """Класс обьекта для создания тотема сохранений."""

    @staticmethod
    def get_damage_info() -> str:
        return "Воскрешение"

    def __str__(self) -> str:
        return "Тотем"
