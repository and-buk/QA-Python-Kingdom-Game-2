from __future__ import annotations
from abc import ABC, abstractmethod
import random
from numpy.random import choice
from typing import Any, List, Union, Tuple

initial_hp = 15
initial_attack_value = 15


class AbstractFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые возвращают
    абстрактные классы войнов (вариацию), вооруженных различным оружием.
    """

    @abstractmethod
    def create_swordsman(self) -> Union[MonsterSwordsman, HumanSwordsman]:
        pass

    @abstractmethod
    def create_archer(self) -> Union[MonsterArcher, HumanArcher]:
        pass

    @abstractmethod
    def create_wizard(self) -> Union[MonsterWizard, HumanWizard]:
        pass


class MonsterFactory(AbstractFactory):
    """Фабрика монстров - войнов."""

    def __init__(self) -> None:
        self.health = random.randint(10, 25)
        self.attack_value = random.randint(10, 30)

    def create_swordsman(self) -> MonsterSwordsman:
        return MonsterSwordsman(self.health, self.attack_value)

    def create_archer(self) -> MonsterArcher:
        return MonsterArcher(self.health, self.attack_value)

    def create_wizard(self) -> MonsterWizard:
        return MonsterWizard(self.health, self.attack_value)


class HumanFactory(AbstractFactory):
    """Фабрика людей - войнов."""

    def __init__(self) -> None:
        self.health = initial_hp
        self.attack_value = initial_attack_value

    def create_swordsman(self) -> HumanSwordsman:
        return HumanSwordsman(self.health, self.attack_value)

    def create_archer(self) -> HumanArcher:
        return HumanArcher(self.health, self.attack_value)

    def create_wizard(self) -> HumanWizard:
        return HumanWizard(self.health, self.attack_value)


class AbstractSwordsman(ABC):
    """Базовый интерфейс абстрактного класса "Мечник"."""

    @abstractmethod
    def get_health_info(self) -> int:
        pass

    @abstractmethod
    def get_attack_info(self) -> int:
        pass


class AbstractArcher(ABC):
    """Базовый интерфейс абстрактного класса "Лучник"."""

    @abstractmethod
    def get_health_info(self) -> int:
        pass

    @abstractmethod
    def get_attack_info(self) -> int:
        pass


class AbstractWizard(ABC):
    """Базовый интерфейс абстрактного класса "Маг"."""

    @abstractmethod
    def get_health_info(self) -> int:
        pass

    @abstractmethod
    def get_attack_info(self) -> int:
        pass


class MonsterSwordsman(AbstractSwordsman):
    """."""

    def __init__(self, hp: int, attack_value: int) -> None:
        self.health = hp
        self.attack_value = attack_value

    def get_health_info(self) -> int:
        return self.health

    def get_attack_info(self) -> int:
        return self.attack_value

    def get_attack(self, human: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> int:
        self.health = self.health - human.get_attack_info()
        return self.health

    def __str__(self) -> str:
        return "Мечник"


class MonsterArcher(AbstractArcher):
    def __init__(self, hp: int, attack_value: int) -> None:
        self.health = hp
        self.attack_value = attack_value

    def get_health_info(self) -> int:
        return self.health

    def get_attack_info(self) -> int:
        return self.attack_value

    def get_attack(self, human: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> int:
        self.health = self.health - human.get_attack_info()
        return self.health

    def __str__(self) -> str:
        return "Лучник"


class MonsterWizard(AbstractWizard):
    """."""

    def __init__(self, hp: int, attack_value: int) -> None:
        self.health = hp
        self.attack_value = attack_value

    def get_health_info(self) -> int:
        return self.health

    def get_attack_info(self) -> int:
        return self.attack_value

    def get_attack(self, human: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> int:
        self.health = self.health - human.get_attack_info()
        return self.health

    def __str__(self) -> str:
        return "Маг"


class HumanSwordsman(AbstractSwordsman):
    """."""
    # _health = None
    # _attack_value = None
    # _weapon = None
    # _bag: List[Any] = None

    def __init__(self, hp: int, attack_value: int):
        self._health = hp
        self._attack_value = attack_value
        self._weapon = Union[None, str]
        self._bag: List[Any] = []

    def get_health_info(self) -> int:
        return self._health

    def get_attack_info(self) -> int:
        return self._attack_value

    def get_weapon_info(self) -> Any[str]:
        return self._weapon

    def add_item_to_bag(self, item: Any, initial_weapon: bool = False) -> None:
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
        item_index = next(i for i, x in enumerate(self._bag) if isinstance(x, type(item)))
        del self._bag[item_index]

    def show_bag(self) -> List[str]:
        return [f"{item.__str__()}: {item.get_damage_info()}" for item in self._bag]

    def check_item_in_bag(self, item: Any) -> bool:
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            return False
        else:
            return True

    @staticmethod
    def __check_completeness(npc_bag: list) -> list:
        if not any(item.__str__() == "Лук" for item in npc_bag) or not any(
                item.__str__() == "Стрелы" for item in npc_bag):
            return [item for item in npc_bag if
                    item.__str__() != "Лук" and item.__str__() != "Стрелы" and item.__str__() != "Тотем"]
        else:
            return [item for item in npc_bag if item.__str__() != "Стрелы" and item.__str__() != "Тотем"]

    def select_weapon(self) -> None:
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
        self._health = self._health + hp

    def get_attack(self, monster: Union[MonsterSwordsman, MonsterArcher, MonsterWizard]) -> None:
        if type(self).__mro__[1] == type(monster).__mro__[1]:
            dodge_or_not = choice((monster.get_attack_info(), 0), p=[0.5, 0.5])
            self._health = self._health - dodge_or_not
            print("Вы мастерски увернулись от атаки, нанеся чудовищу серъёзный урон!")
        else:
            self._health = self._health - monster.get_attack_info()
        return

    def save(self) -> ConcreteMemento:
        """Сохраняет текущее состояние внутри снимка."""

        return ConcreteMemento(self._health, self._attack_value, self._weapon, tuple(self._bag))

    def restore(self, memento: ConcreteMemento) -> None:
        """Восстанавливает состояние Создателя из объекта снимка."""

        self._health = memento.get_state()[0]
        self._attack_value = memento.get_state()[1]
        self._weapon = memento.get_state()[2]
        self._bag = list(memento.get_state()[3])

    def __str__(self) -> str:
        return "Мечник"


class HumanArcher(AbstractArcher):
    """."""

    # _health = None
    # _attack_value = None
    # _weapon = None
    # _bag = None

    def __init__(self, hp: int, attack_value: int):
        self._health = hp
        self._attack_value = attack_value
        self._weapon = None
        self._bag: List[Any] = []

    def get_health_info(self) -> int:
        return self._health

    def get_attack_info(self) -> int:
        return self._attack_value

    def get_weapon_info(self) -> Any[str]:
        return self._weapon

    def add_item_to_bag(self, item: Any, initial_weapon: bool = False) -> None:
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
        item_index = next(i for i, x in enumerate(self._bag) if isinstance(x, type(item)))
        del self._bag[item_index]

    def show_bag(self) -> List[str]:
        return [f"{item.__str__()}: {item.get_damage_info()}" for item in self._bag]

    def check_item_in_bag(self, item: Any) -> bool:
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            return False
        else:
            return True

    @staticmethod
    def __check_completeness(npc_bag: list) -> list:
        if not any(item.__str__() == "Лук" for item in npc_bag) or not any(
                item.__str__() == "Стрелы" for item in npc_bag):
            return [item for item in npc_bag if
                    item.__str__() != "Лук" and item.__str__() != "Стрелы" and item.__str__() != "Тотем"]
        else:
            return [item for item in npc_bag if item.__str__() != "Стрелы" and item.__str__() != "Тотем"]

    def select_weapon(self) -> None:
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
        self._health = self._health + hp

    def get_attack(self, monster: Union[MonsterSwordsman, MonsterArcher, MonsterWizard]) -> None:
        if type(self).__mro__[1] == type(monster).__mro__[1]:
            dodge_or_not = choice((monster.get_attack_info(), 0), p=[0.5, 0.5])
            self._health = self._health - dodge_or_not
            print("Вы мастерски увернулись от атаки, нанеся чудовищу серъёзный урон!")
        else:
            self._health = self._health - monster.get_attack_info()
        return

    def save(self) -> ConcreteMemento:
        """Сохраняет текущее состояние внутри снимка."""

        return ConcreteMemento(self._health, self._attack_value, self._weapon, tuple(self._bag))

    def restore(self, memento: ConcreteMemento) -> None:
        """Восстанавливает состояние Создателя из объекта снимка."""

        self._health = memento.get_state()[0]
        self._attack_value = memento.get_state()[1]
        self._weapon = memento.get_state()[2]
        self._bag = list(memento.get_state()[3])

    def __str__(self) -> str:
        return "Лучник"


class HumanWizard(AbstractWizard):
    """."""

    # _health = None
    # _attack_value = None
    # _weapon = None
    # _bag = None

    def __init__(self, hp: int, attack_value: int):
        self._health = hp
        self._attack_value = attack_value
        self._weapon = Union[None, str]
        self._bag: List[Any] = []

    def get_health_info(self) -> int:
        return self._health

    def get_attack_info(self) -> int:
        return self._attack_value

    def get_weapon_info(self) -> Any[str]:
        return self._weapon

    def add_item_to_bag(self, item: Any, initial_weapon: bool = False) -> None:
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
        item_index = next(i for i, x in enumerate(self._bag) if isinstance(x, type(item)))
        del self._bag[item_index]

    def show_bag(self) -> list:
        return [f"{item.__str__()}: {item.get_damage_info()}" for item in self._bag]

    def check_item_in_bag(self, item: Any) -> bool:
        item_index = next(
            (i for i, x in enumerate(self._bag) if x.__str__() == item.__str__()), None
        )
        if item_index is None:
            return False
        else:
            return True

    @staticmethod
    def __check_completeness(npc_bag: list) -> list:
        if not any(item.__str__() == "Лук" for item in npc_bag) or not any(
                item.__str__() == "Стрелы" for item in npc_bag):
            return [item for item in npc_bag if
                    item.__str__() != "Лук" and item.__str__() != "Стрелы" and item.__str__() != "Тотем"]
        else:
            return [item for item in npc_bag if item.__str__() != "Стрелы" and item.__str__() != "Тотем"]

    def select_weapon(self) -> None:
        while True:
            try:
                npc_bag_for_select = self.__check_completeness(self._bag)
                readable_bag = [
                    f"{n + 1} - {item.__str__()}: {item.get_damage_info()}"
                    for n, item in enumerate(npc_bag_for_select)
                ]
                print(readable_bag)
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
        self._health = self._health + hp

    def get_attack(self, monster: Union[MonsterSwordsman, MonsterArcher, MonsterWizard]) -> None:
        if type(self).__mro__[1] == type(monster).__mro__[1]:
            dodge_or_not = choice((monster.get_attack_info(), 0), p=[0.5, 0.5])
            self._health = self._health - dodge_or_not
            print("Вы мастерски увернулись от атаки, нанеся чудовищу серъёзный урон!")
        else:
            self._health = self._health - monster.get_attack_info()
        return

    def save(self) -> ConcreteMemento:
        """Сохраняет текущее состояние внутри снимка."""

        return ConcreteMemento(self._health, self._attack_value, self._weapon, tuple(self._bag))

    def restore(self, memento: ConcreteMemento) -> None:
        """Восстанавливает состояние Создателя из объекта снимка."""

        self._health = memento.get_state()[0]
        self._attack_value = memento.get_state()[1]
        self._weapon = memento.get_state()[2]
        self._bag = list(memento.get_state()[3])

    def __str__(self) -> str:
        return "Маг"


class Memento(ABC):
    """
    Интерфейс Снимка предоставляет способ извлечения метаданных снимка, таких
    как дата создания или название. Однако он не раскрывает состояние Создателя.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, health: int, attack_value: int, weapon: Any[str], bag: tuple) -> None:
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


class Lifekeeper:
    """
    Опекун не зависит от класса Конкретного Снимка. Таким образом, он не имеет
    доступа к состоянию создателя, хранящемуся внутри снимка. Он работает со
    всеми снимками через базовый интерфейс Снимка.
    """

    def __init__(self, originator: Union[HumanSwordsman, HumanArcher, HumanWizard]) -> None:
        self._mementos: List[Any] = []
        self._originator = originator

    def backup(self) -> None:
        print("Игра сохранена!")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        # print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())
