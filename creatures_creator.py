from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Union, Tuple

from numpy.random import choice


class AbstractFactory(ABC):
    """Интерфейс Абстрактной Фабрики воинов, специализирующихся на различном оружии."""

    @abstractmethod
    def create_swordsman(self) -> Union[MonsterSwordsman, HumanSwordsman]:
        """Базовый метод, создающий класс воинов 'Мечник'."""
        pass

    @abstractmethod
    def create_archer(self) -> Union[MonsterArcher, HumanArcher]:
        """Базовый метод, создающий класс воинов 'Лучник'."""
        pass

    @abstractmethod
    def create_wizard(self) -> Union[MonsterWizard, HumanWizard]:
        """Базовый метод, создающий класс воинов 'Маг'."""
        pass


class MonsterFactory(AbstractFactory):
    """Фабрика монстров - войнов."""

    def __init__(self, initial_monster_hp: int, initial_monster_attack: int) -> None:
        """Конструктор параметров монстров-воинов."""
        self.health = initial_monster_hp
        self.attack_value = initial_monster_attack

    def create_swordsman(self) -> MonsterSwordsman:
        """Создаём Мечника."""
        return MonsterSwordsman(self.health, self.attack_value)

    def create_archer(self) -> MonsterArcher:
        """Создаём Лучника."""
        return MonsterArcher(self.health, self.attack_value)

    def create_wizard(self) -> MonsterWizard:
        """Создаём Мага."""
        return MonsterWizard(self.health, self.attack_value)


class HumanFactory(AbstractFactory):
    """Фабрика людей - войнов."""

    def __init__(self, initial_hp: int, initial_attack_value: int) -> None:
        """Конструктор параметров людей-воинов."""
        self.health = initial_hp
        self.attack_value = initial_attack_value

    def create_swordsman(self) -> HumanSwordsman:
        """Создаём Мечника."""
        return HumanSwordsman(self.health, self.attack_value)

    def create_archer(self) -> HumanArcher:
        """Создаём Лучника."""
        return HumanArcher(self.health, self.attack_value)

    def create_wizard(self) -> HumanWizard:
        """Создаём Мага."""
        return HumanWizard(self.health, self.attack_value)


class AbstractSwordsman(ABC):
    """Базовый интерфейс абстрактного класса "Мечник"."""

    @abstractmethod
    def get_health_info(self) -> int:
        """Базовый метод, вызов которого, возвращает текущей уровень жизни Мечника."""
        pass

    @abstractmethod
    def get_attack_info(self) -> int:
        """Базовый метод, вызов которого, возвращает текущее значение силы атаки Мечника."""
        pass


class AbstractArcher(ABC):
    """Базовый интерфейс абстрактного класса "Лучник"."""

    @abstractmethod
    def get_health_info(self) -> int:
        """Базовый метод, вызов которого, возвращает текущей уровень жизни Лучника."""
        pass

    @abstractmethod
    def get_attack_info(self) -> int:
        """Базовый метод, вызов которого, возвращает текущее значение силы атаки Лучника."""
        pass


class AbstractWizard(ABC):
    """Базовый интерфейс абстрактного класса "Маг"."""

    @abstractmethod
    def get_health_info(self) -> int:
        """Базовый метод, вызов которого, возвращает текущей уровень жизни Мага."""
        pass

    @abstractmethod
    def get_attack_info(self) -> int:
        """Базовый метод, вызов которого, возвращает текущее значение силы атаки Мага."""
        pass


class MonsterSwordsman(AbstractSwordsman):
    """Класс для представления монстра-мечника."""

    def __init__(self, hp: int, attack_value: int) -> None:
        """Конструктор параметров монстра-мечника."""
        self.health = hp
        self.attack_value = attack_value

    def get_health_info(self) -> int:
        """Получаем текущее значение уровня жизни монстра-мечника."""
        return self.health

    def get_attack_info(self) -> int:
        """Получаем текущее значение силы атаки монстра-мечника."""
        return self.attack_value

    def get_attack(self, human: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> int:
        """Атакуем противника. Получаем новое значение уровня жизни монстра-мечника после атаки."""
        self.health = self.health - human.get_attack_info()
        return self.health

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится воин."""
        return "Мечник"


class MonsterArcher(AbstractArcher):
    """Класс для представления монстра-лучника."""

    def __init__(self, hp: int, attack_value: int) -> None:
        """Конструктор параметров монстра-лучника."""
        self.health = hp
        self.attack_value = attack_value

    def get_health_info(self) -> int:
        """Получаем текущее значение уровня жизни монстра-лучника."""
        return self.health

    def get_attack_info(self) -> int:
        """Получаем текущее значение силы атаки монстра-лучника."""
        return self.attack_value

    def get_attack(self, human: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> int:
        """Атакуем противника. Получаем новое значение уровня жизни монстра-лучника после атаки."""
        self.health = self.health - human.get_attack_info()
        return self.health

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится воин."""
        return "Лучник"


class MonsterWizard(AbstractWizard):
    """Класс для представления монстра-мага."""

    def __init__(self, hp: int, attack_value: int) -> None:
        """Конструктор параметров монстра-мага."""
        self.health = hp
        self.attack_value = attack_value

    def get_health_info(self) -> int:
        """Получаем текущее значение уровня жизни монстра-мага."""
        return self.health

    def get_attack_info(self) -> int:
        """Получаем текущее значение силы атаки монстра-мага."""
        return self.attack_value

    def get_attack(self, human: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> int:
        """Атакуем противника. Получаем новое значение уровня жизни монстра-мага после атаки."""
        self.health = self.health - human.get_attack_info()
        return self.health

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится воин."""
        return "Маг"


class HumanSwordsman(AbstractSwordsman):
    """Класс для представления человека-мечника."""

    def __init__(self, hp: int, attack_value: int):
        """Конструктор параметров человека-мечника."""
        self._health = hp
        self._attack_value = attack_value
        self._weapon: Union[None, str] = None
        self._bag: List[Any] = []

    def get_health_info(self) -> int:
        """Получаем текущее значение уровня жизни."""
        return self._health

    def get_attack_info(self) -> int:
        """Получаем текущее значение силы атаки."""
        return self._attack_value

    def get_weapon_info(self) -> Any[str]:
        """Получаем информацию о наименовании текущего оружия."""
        return self._weapon

    def add_item_to_bag(self, item: Any, initial_weapon: bool = False) -> None:
        """Добавляем предметы в инвентарь. Обновляем информацию о предметах в инвентаре."""
        if initial_weapon:
            self._weapon = item.__str__()
            self._attack_value = item.get_damage_info()

        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            self._bag.append(item)
        elif item_index is not None and item.__str__() == self._weapon:
            self._bag[item_index] = item
            self._attack_value = item.get_damage_info()
        else:
            self._bag[item_index] = item

    def remove_item_from_bag(self, item: Union[Any]) -> None:
        """Удаляем предметы из инвентаря."""
        item_index = next(
            i for i, x in enumerate(self._bag) if isinstance(x, type(item))
        )
        del self._bag[item_index]

    def show_bag(self) -> List[str]:
        """Представляем предметы инвентаря списком их наименований."""
        return [f"{item.__str__()}: {item.get_damage_info()}" for item in self._bag]

    def check_item_in_bag(self, item: Any) -> bool:
        """Проверяем наличие предмета в инвентаре."""
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            return False
        else:
            return True

    @staticmethod
    def __check_completeness(npc_bag: list) -> list:
        """Проверяем инвентарь воина на наличие боеприпасов и оружия их использующего.

        При успешной проверки возвращаем список доступного для использования оружия.
        В список не включаются не боевые предметы.

        """
        if not any(item.__str__() == "ЛУК" for item in npc_bag) or not any(
            item.__str__() == "СТРЕЛЫ" for item in npc_bag
        ):
            return [
                item
                for item in npc_bag
                if item.__str__() != "ЛУК"
                and item.__str__() != "СТРЕЛЫ"
                and item.__str__() != "ТОТЕМ"
            ]
        else:
            return [
                item
                for item in npc_bag
                if item.__str__() != "СТРЕЛЫ" and item.__str__() != "ТОТЕМ"
            ]

    def select_weapon(self) -> None:
        """Из имеющегося в инвентаре оружия выбираем доступное для атаки."""
        while True:
            try:
                npc_bag_for_select = self.__check_completeness(self._bag)
                readable_bag = [
                    f"{n + 1} - {item.__str__()}: {item.get_damage_info()}"
                    for n, item in enumerate(npc_bag_for_select)
                ]
                request = "Выберете оружие: "
                for _ in range(len(readable_bag)):
                    request = request + "{}. "
                decision = int(input(request.format(*readable_bag)))
                if decision > 3 or decision < 1:
                    raise ValueError()
                self._attack_value = npc_bag_for_select[decision - 1].get_damage_info()
                self._weapon = npc_bag_for_select[decision - 1].__str__()
            except ValueError:
                print("Неккоректный ввод! Повторите!")
            else:
                break
        return

    def increase_health(self, hp: int) -> None:
        """Увеличиваем уровень здоровья на заданное значение."""
        self._health = self._health + hp

    def get_attack(
        self, monster: Union[MonsterSwordsman, MonsterArcher, MonsterWizard]
    ) -> None:
        """Атакуем противника.

        Можем увернуться от его встречной атаки, если противник Мечник.
        Получаем новое значение уровня жизни после атаки.

        """
        if type(self).__mro__[1] == type(monster).__mro__[1]:
            dodge_or_not = choice((monster.get_attack_info(), 0), p=[0.5, 0.5])
            self._health = self._health - dodge_or_not
            if dodge_or_not == 0:
                print(
                    "Вы мастерски увернулись от атаки, нанеся чудовищу серъёзный урон!"
                )
        else:
            self._health = self._health - monster.get_attack_info()
        return

    def save(self) -> ConcreteMemento:
        """Сохраняем состояние (текущие параметры) человека-мечника в объект-снимок."""
        return ConcreteMemento(
            self._health, self._attack_value, self._weapon, tuple(self._bag)
        )

    def restore(self, memento: ConcreteMemento) -> None:
        """Восстанавливает состояние человека-мечника из объекта снимка."""
        self._health = memento.get_state()[0]
        self._attack_value = memento.get_state()[1]
        self._weapon = memento.get_state()[2]
        self._bag = list(memento.get_state()[3])

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится воин."""
        return "Мечник"


class HumanArcher(AbstractArcher):
    """Класс для представления человека-лучника."""

    def __init__(self, hp: int, attack_value: int):
        """Конструктор параметров человека-лучника."""
        self._health = hp
        self._attack_value = attack_value
        self._weapon: Union[None, str] = None
        self._bag: List[Any] = []

    def get_health_info(self) -> int:
        """Получаем текущее значение уровня жизни."""
        return self._health

    def get_attack_info(self) -> int:
        """Получаем текущее значение силы атаки."""
        return self._attack_value

    def get_weapon_info(self) -> Any[str]:
        """Получаем информацию о наименовании текущего оружия."""
        return self._weapon

    def add_item_to_bag(self, item: Any, initial_weapon: bool = False) -> None:
        """Добавляем предметы в инвентарь. Обновляем информацию о предметах в инвентаре."""
        if initial_weapon:
            self._weapon = item.__str__()
            self._attack_value = item.get_damage_info()
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            self._bag.append(item)
        elif item_index is not None and item.__str__() == self._weapon:
            self._bag[item_index] = item
            self._attack_value = item.get_damage_info()
        else:
            self._bag[item_index] = item

    def remove_item_from_bag(self, item: Any) -> None:
        """Удаляем предметы из инвентаря."""
        item_index = next(
            i for i, x in enumerate(self._bag) if isinstance(x, type(item))
        )
        del self._bag[item_index]

    def show_bag(self) -> List[str]:
        """Представляем предметы инвентаря списком их наименований."""
        return [f"{item.__str__()}: {item.get_damage_info()}" for item in self._bag]

    def check_item_in_bag(self, item: Any) -> bool:
        """Проверяем наличие предмета в инвентаре."""
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            return False
        else:
            return True

    @staticmethod
    def __check_completeness(npc_bag: list) -> list:
        """Проверяем инвентарь воина на наличие боеприпасов и оружия их использующего.

        При успешной проверки возвращаем список доступного для использования оружия.
        В список не включаются не боевые предметы.

        """
        if not any(item.__str__() == "ЛУК" for item in npc_bag) or not any(
            item.__str__() == "СТРЕЛЫ" for item in npc_bag
        ):
            return [
                item
                for item in npc_bag
                if item.__str__() != "ЛУК"
                and item.__str__() != "СТРЕЛЫ"
                and item.__str__() != "ТОТЕМ"
            ]
        else:
            return [
                item
                for item in npc_bag
                if item.__str__() != "СТРЕЛЫ" and item.__str__() != "ТОТЕМ"
            ]

    def select_weapon(self) -> None:
        """Из имеющегося в инвентаре оружия выбираем доступное для атаки."""
        while True:
            try:
                npc_bag_for_select = self.__check_completeness(self._bag)
                readable_bag = [
                    f"{n + 1} - {item.__str__()}: {item.get_damage_info()}"
                    for n, item in enumerate(npc_bag_for_select)
                ]
                request = "Выберете оружие: "
                for _ in range(len(readable_bag)):
                    request = request + "{}. "
                decision = int(input(request.format(*readable_bag)))
                if decision > 3 or decision < 1:
                    raise ValueError()
                self._attack_value = npc_bag_for_select[decision - 1].get_damage_info()
                self._weapon = npc_bag_for_select[decision - 1].__str__()
            except ValueError:
                print("Неккоректный ввод! Повторите!")
            else:
                break
        return

    def increase_health(self, hp: int) -> None:
        """Увеличиваем уровень здоровья на заданное значение."""
        self._health = self._health + hp

    def get_attack(
        self, monster: Union[MonsterSwordsman, MonsterArcher, MonsterWizard]
    ) -> None:
        """Атакуем противника.

        Можем увернуться от его встречной атаки, если противник Лучник.
        Получаем новое значение уровня жизни после атаки.

        """
        if type(self).__mro__[1] == type(monster).__mro__[1]:
            dodge_or_not = choice((monster.get_attack_info(), 0), p=[0.5, 0.5])
            self._health = self._health - dodge_or_not
            if dodge_or_not == 0:
                print(
                    "Вы мастерски увернулись от атаки, нанеся чудовищу серъёзный урон!"
                )
        else:
            self._health = self._health - monster.get_attack_info()
        return

    def save(self) -> ConcreteMemento:
        """Сохраняем состояние (текущие параметры) человека-лучника в объект-снимок."""
        return ConcreteMemento(
            self._health, self._attack_value, self._weapon, tuple(self._bag)
        )

    def restore(self, memento: ConcreteMemento) -> None:
        """Восстанавливает состояние (текущие параметры) человека-лучника из объекта-снимка."""
        self._health = memento.get_state()[0]
        self._attack_value = memento.get_state()[1]
        self._weapon = memento.get_state()[2]
        self._bag = list(memento.get_state()[3])

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится воин."""
        return "Лучник"


class HumanWizard(AbstractWizard):
    """Класс для представления человека-мага."""

    def __init__(self, hp: int, attack_value: int):
        """Конструктор параметров человека-мага."""
        self._health = hp
        self._attack_value = attack_value
        self._weapon: Union[None, str] = None
        self._bag: List[Any] = []

    def get_health_info(self) -> int:
        """Получаем текущее значение уровня жизни."""
        return self._health

    def get_attack_info(self) -> int:
        """Получаем текущее значение силы атаки."""
        return self._attack_value

    def get_weapon_info(self) -> Any[str]:
        """Получаем информацию о наименовании текущего оружия."""
        return self._weapon

    def add_item_to_bag(self, item: Any, initial_weapon: bool = False) -> None:
        """Добавляем предметы в инвентарь. Обновляем информацию о предметах в инвентаре."""
        if initial_weapon:
            self._weapon = item.__str__()
            self._attack_value = item.get_damage_info()

        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            self._bag.append(item)
        elif item_index is not None and item.__str__() == self._weapon:
            self._bag[item_index] = item
            self._attack_value = item.get_damage_info()
        else:
            self._bag[item_index] = item

    def remove_item_from_bag(self, item: Any) -> None:
        """Удаляем предметы из инвентаря."""
        item_index = next(
            i for i, x in enumerate(self._bag) if isinstance(x, type(item))
        )
        del self._bag[item_index]

    def show_bag(self) -> list:
        """Представляем предметы инвентаря списком их наименований."""
        return [f"{item.__str__()}: {item.get_damage_info()}" for item in self._bag]

    def check_item_in_bag(self, item: Any) -> bool:
        """Проверяем наличие предмета в инвентаре."""
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            return False
        else:
            return True

    @staticmethod
    def __check_completeness(npc_bag: list) -> list:
        """Проверяем инвентарь воина на наличие боеприпасов и оружия их использующего.

        При успешной проверки возвращаем список доступного для использования оружия.
        В список не включаются не боевые предметы.

        """
        if not any(item.__str__() == "ЛУК" for item in npc_bag) or not any(
            item.__str__() == "СТРЕЛЫ" for item in npc_bag
        ):
            return [
                item
                for item in npc_bag
                if item.__str__() != "ЛУК"
                and item.__str__() != "СТРЕЛЫ"
                and item.__str__() != "ТОТЕМ"
            ]
        else:
            return [
                item
                for item in npc_bag
                if item.__str__() != "СТРЕЛЫ" and item.__str__() != "ТОТЕМ"
            ]

    def select_weapon(self) -> None:
        """Из имеющегося в инвентаре оружия выбираем доступное для атаки."""
        while True:
            try:
                npc_bag_for_select = self.__check_completeness(self._bag)
                readable_bag = [
                    f"{n + 1} - {item.__str__()}: {item.get_damage_info()}"
                    for n, item in enumerate(npc_bag_for_select)
                ]
                request = "Выберете оружие: "
                for _ in range(len(readable_bag)):
                    request = request + "{}. "
                decision = int(input(request.format(*readable_bag)))
                if decision > 3 or decision < 1:
                    raise ValueError()
                self._attack_value = npc_bag_for_select[decision - 1].get_damage_info()
                self._weapon = npc_bag_for_select[decision - 1].__str__()
            except ValueError:
                print("Неккоректный ввод! Повторите!")
            else:
                break
        return

    def increase_health(self, hp: int) -> None:
        """Увеличиваем уровень здоровья на заданное значение."""
        self._health = self._health + hp

    def get_attack(
        self, monster: Union[MonsterSwordsman, MonsterArcher, MonsterWizard]
    ) -> None:
        """Атакуем противника.

        Можем увернуться от его встречной атаки, если противник - мечник.
        Получаем новое значение уровня жизни после атаки.

        """
        if type(self).__mro__[1] == type(monster).__mro__[1]:
            dodge_or_not = choice((monster.get_attack_info(), 0), p=[0.5, 0.5])
            self._health = self._health - dodge_or_not
            if dodge_or_not == 0:
                print(
                    "Вы мастерски увернулись от атаки, нанеся чудовищу серъёзный урон!"
                )
        else:
            self._health = self._health - monster.get_attack_info()
        return

    def save(self) -> ConcreteMemento:
        """Сохраняем состояние (текущие параметры) человека-мага в объект-снимок."""
        return ConcreteMemento(
            self._health, self._attack_value, self._weapon, tuple(self._bag)
        )

    def restore(self, memento: ConcreteMemento) -> None:
        """Восстанавливает состояние (текущие параметры) человека-мага из объекта-снимка."""
        self._health = memento.get_state()[0]
        self._attack_value = memento.get_state()[1]
        self._weapon = memento.get_state()[2]
        self._bag = list(memento.get_state()[3])

    def __str__(self) -> str:
        """Получаем наименование класса, к которому относится воин."""
        return "Маг"


class Memento(ABC):
    """Базовый класс объкта-снимка для хранения состояния (параметров) игрового персонажа."""

    @abstractmethod
    def get_name(self) -> str:
        """Базовый метод для реализации отображения сохранённого состояния (параметров) игрового персонажа."""
        pass


class ConcreteMemento(Memento):
    """Класс объкта-снимка для хранения состояния (параметров) игрового персонажа."""

    def __init__(
        self, health: int, attack_value: int, weapon: Any[str], bag: tuple
    ) -> None:
        """Конструктор объкта-снимка."""
        self._health = health
        self._attack_value = attack_value
        self._weapon = weapon
        self._bag = bag

    def get_state(self) -> Tuple[int, int, Any[str], Tuple[Any, ...]]:
        """Создатель использует этот метод, когда восстанавливает своё состояние."""
        return self._health, self._attack_value, self._weapon, self._bag

    def get_name(self) -> str:
        """Остальные методы используются Опекуном для отображения метаданных."""
        return f"({self._health}, {self._attack_value}, {self._weapon}, {self._bag})"


class Storage:
    """Класс для представления хранилища объёктов-снимков.

    Управлят процессами сохранения и восстановления состояния игрового персонажа.

    """

    def __init__(
        self, originator: Union[HumanSwordsman, HumanArcher, HumanWizard]
    ) -> None:
        """Конструктор парметров объекта-хранилища."""
        self._mementos: List[Any] = []
        self._originator = originator

    def backup(self) -> None:
        """Сохраняем в объект-снимок текущее состояние (параметры) игрового персонажа."""
        print("Игра сохранена!")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        """Восстанавливаем из объекта-снимка состояние (параметры) игрового персонажа."""
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        """Показываем историю сохранений."""
        for memento in self._mementos:
            print(memento.get_name())
