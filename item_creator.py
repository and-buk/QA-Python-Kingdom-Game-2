from __future__ import annotations

import random
from abc import ABC, abstractmethod
from typing import Any, Union


class AbstractFactory(ABC):
    """Интерфейс Абстрактной Фабрики игровых предметов.

    Определяет набор методов для создания игровых предметов стандартных
    или уникальных по своим свойствам и характеристикам.
    """

    @abstractmethod
    def create_standart_item(self) -> Union[Sword, Bow, SpellBook, Arrow, Apple, Totem]:
        """Базовый метод для создания игрового предмета со стандартными свойствами и характеристиками."""
        pass

    @abstractmethod
    def create_unique_item(self) -> Union[UniqueSword, UniqueBow, UniqueSpellBook]:
        """Базовый метод для создания игрового предмета со стандартными свойствами и характеристиками."""
        pass


class SwordFactory(AbstractFactory):
    """Фабрика по производству оружия класса «Меч»."""

    def __init__(self) -> None:
        """Конструктор параметров выпускаемых на фабрике мечей."""
        self.standart_damage_rate = random.randint(5, 20)
        self.improved_damage_rate = random.randint(20, 40)

    def create_standart_item(self) -> Sword:
        """Базовый метод для выпуска стандартных мечей."""
        return Sword(self.standart_damage_rate)

    def create_unique_item(self) -> UniqueSword:
        """Базовый метод для выпуска уникальных мечей."""
        return UniqueSword(self.improved_damage_rate)


class BowFactory(AbstractFactory):
    """Фабрика по производству оружия класса «Лук»."""

    def __init__(self) -> None:
        """Конструктор параметров выпускаемых на фабрике луков."""
        self.standart_damage_rate = random.randint(5, 20)
        self.improved_damage_rate = random.randint(20, 40)

    def create_standart_item(self) -> Bow:
        """Базовый метод для выпуска стандартных луков."""
        return Bow(self.standart_damage_rate)

    def create_unique_item(self) -> UniqueBow:
        """Базовый метод для выпуска уникальных луков."""
        return UniqueBow(self.improved_damage_rate)


class ArrowFactory(AbstractFactory):
    """Фабрика по производству боеприпасов класса «Стрелы»."""

    def create_standart_item(self) -> Arrow:
        """Базовый метод для выпуска стандартных стрел."""
        return Arrow()

    def create_unique_item(self) -> Any:
        """Базовый метод для выпуска уникальных стрел."""
        pass


class MagicAcademy(AbstractFactory):
    """Академия, выпускающая рукописи класса «Книга заклинаний»."""

    def __init__(self) -> None:
        """Конструктор параметров, выпускаемых в академии книг."""
        self.standart_damage_rate: int = random.randint(5, 20)
        self.improved_damage_rate: int = random.randint(20, 40)

    def create_standart_item(self) -> SpellBook:
        """Базовый метод для выпуска стандартных книг с заклинаниямию."""
        return SpellBook(self.standart_damage_rate)

    def create_unique_item(self) -> UniqueSpellBook:
        """Базовый метод для выпуска уникальных книг с заклинаниямию."""
        return UniqueSpellBook(self.improved_damage_rate)


class AppleTree(AbstractFactory):
    """Яблоня с целебными плодами."""

    def __init__(self) -> None:
        """Конструктор параметров яблони."""
        self.healing_power: int = random.randint(3, 15)

    def create_standart_item(self) -> Apple:
        """Базовый метод создания яблока."""
        return Apple(self.healing_power)

    def create_unique_item(self) -> Any:
        """Метод для создания уникального по своим свойствам целебного яблока."""
        pass


class MysteriousPlace(AbstractFactory):
    """Место где из ниоткуда возникают различные волшебные предметы, например, класса «Тотем»."""

    def create_standart_item(self) -> Totem:
        """Из ниоткуда возникает стандартный волшебный тотем."""
        return Totem()

    def create_unique_item(self) -> Any:
        """Из ниоткуда возникает уникальный волшебный тотем."""
        pass


class AbstractSword(ABC):
    """Базовый класс объекта-оружия "Меч"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractUniqueSword(ABC):
    """Базовый класс объекта-оружия "Уникальный меч"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractBow(ABC):
    """Базовый класс объекта-оружия "Лук"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractUniqueBow(ABC):
    """Базовый класс объекта-оружия "Уникальный лук"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractArrow(ABC):
    """Базовый класс объекта-боеприпаса "Стрелы"."""

    pass


class AbstractSpellBook(ABC):
    """Базовый класс объекта-рукописи "Книга заклинаний"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractUniqueSpellBook(ABC):
    """Базовый класс объекта-рукописи "Уникальная книга заклинаний"."""

    @abstractmethod
    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractApple(ABC):
    """Базовый класс объекта-плода "Яблоко"."""

    @abstractmethod
    def get_hp_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        pass


class AbstractTotem(ABC):
    """Базовый класс волшебного объекта "Тотем"."""

    pass


class Sword(AbstractSword):
    """Класс обьекта для создания стандартного меча."""

    def __init__(self, damage_rate: int) -> None:
        """Конструктор параметров."""
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится оружие."""
        return "МЕЧ"


class UniqueSword(AbstractUniqueSword):
    """Класс обьекта для создания уникального меча."""

    def __init__(self, damage_rate: int) -> None:
        """Конструктор параметров."""
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится оружие."""
        return "МЕЧ"


class Bow(AbstractBow):
    """Класс обьекта для создания лука."""

    def __init__(self, damage_rate: int) -> None:
        """Конструктор параметров."""
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится оружие."""
        return "ЛУК"


class UniqueBow(AbstractUniqueBow):
    """Класс обьекта для создания уникального лука."""

    def __init__(self, damage_rate: int) -> None:
        """Конструктор параметров."""
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится оружие."""
        return "ЛУК"


class Arrow(AbstractArrow):
    """Класс обьекта для создания стрел."""

    def __init__(self) -> None:
        """Конструктор параметров."""
        self.damage_rate: int = 0

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится боеприпас."""
        return "СТРЕЛЫ"


class SpellBook(AbstractSpellBook):
    """Класс обьекта для создания книги заклинаний."""

    def __init__(self, damage_rate: int) -> None:
        """Конструктор параметров."""
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится рукопись."""
        return "КНИГА ЗАКЛИНАНИЙ"


class UniqueSpellBook(AbstractUniqueSpellBook):
    """Класс обьекта для создания уникальной книги заклинаний."""

    def __init__(self, damage_rate: int) -> None:
        """Конструктор параметров."""
        self.damage_rate = damage_rate

    def get_damage_info(self) -> int:
        """Получаем информацию о силе атаки предмета."""
        return self.damage_rate

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится рукопись."""
        return "КНИГА ЗАКЛИНАНИЙ"


class Apple(AbstractApple):
    """Класс обьекта для создания целебного яблока."""

    def __init__(self, healing_power: int) -> None:
        """Конструктор параметров."""
        self.healing_power = healing_power

    def get_hp_info(self) -> int:
        """Получаем информацию о целебной силе яблока."""
        return self.healing_power

    def __str__(self) -> str:
        """Получаем значение целительной силы яблока."""
        return f"Вы нашли яблоко здоровья! +{self.healing_power} к здоровью героя."


class Totem(AbstractTotem):
    """Класс обьекта для создания тотема сохранений."""

    @staticmethod
    def get_damage_info() -> str:
        """Получаем информацию о свойствах волшебного предмета."""
        return "Воскрешение"

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится волшебный предмет."""
        return "ТОТЕМ"
