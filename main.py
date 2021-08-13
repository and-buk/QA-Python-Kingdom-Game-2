from __future__ import annotations

import random
import sys
from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, Union

from numpy.random import choice

import creatures_creator as cc
import item_creator as ic


class Game:
    """Класс объекта, определяющий интерфейс управления событиями в игре."""

    _event: Any

    def __init__(self, event_list: Union[Any]) -> None:
        """Конструктор параметров интерфейса управления объектами-событиями в игре."""
        self.event_list = event_list
        random_event = choice(event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        self.transition_to(random_event)

    def transition_to(self, event: Any) -> None:
        """Меняем объект-событие во время игры."""
        self._event = event
        self._event.game = self

    def run(self) -> None:
        """Запускаем функционал переданного в качестве аргумента объекта-события."""
        self._event.start()


class Event(ABC):
    """Базовый класс для представления событий в игре."""

    _game = None

    @property
    def game(self) -> Any:
        """Возвращаем объект управления событиями в игре - геттер."""
        return self._game

    @game.setter
    def game(self, game: Game) -> None:
        """Задаём ссылку на объект управления событиями в игре - сеттер."""
        self._game = game

    @abstractmethod
    def start(self) -> None:
        """Базовый метод для запуска разработанного в событии функционал."""
        pass


class EventApple(Event):
    """Класс для представления события «Яблочко» в игре.

    Игровой персонаж находит яблоко, повышающее значение уровня его жизни.

    """

    def __init__(
        self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]
    ) -> None:
        """Конструктор параметров объекта-события."""
        self.npc = npc

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        print("-------------------")
        apple = ic.AppleTree().create_standart_item()
        self.npc.increase_health(apple.get_hp_info())
        print(
            f"Вы нашли яблочко здоровья! +{apple.get_hp_info()} к здоровью героя. "
            f"У героя {self.npc.get_health_info()} жизней."
        )
        next_event = random.choice(self.game.event_list)
        self.game.transition_to(next_event)


class EventSword(Event):
    """Класс для представления события «Меч» в игре.

    Игровой персонаж находит меч со случайным показателем атаки.
    Игровой персонаж класса «Мечник» с большей вероятностью, чем игровой персонаж другого класса,
    может найти меч с увеличенным случайным (уникальным) показателем атаки.

    """

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        """Конструктор параметров объекта-события."""
        self.npc = npc

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        print("-------------------")
        next_event = choice(self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        if issubclass(type(self.npc), cc.AbstractSwordsman):
            swords: Any = (
                ic.SwordFactory().create_standart_item(),
                ic.SwordFactory().create_unique_item(),
            )
            discovered_swords = choice(swords, p=[0.4, 0.6])
            decision = item_decision(npc_info=self.npc, weapon_info=discovered_swords)
            if decision == 1:
                self.npc.add_item_to_bag(discovered_swords)
                self.game.transition_to(next_event)
            else:
                self.game.transition_to(next_event)
        else:
            discovered_sword = ic.SwordFactory().create_standart_item()
            decision = item_decision(npc_info=self.npc, weapon_info=discovered_sword)
            if decision == 1:
                self.npc.add_item_to_bag(discovered_sword)
                self.game.transition_to(next_event)
            else:
                self.game.transition_to(next_event)


class EventBow(Event):
    """Класс для представления события «Лук» в игре.

    Игровой персонаж находит лук со случайным показателем атаки.
    Игровой персонаж класса «Лучник» с большей вероятностью, чем игровой персонаж другого класса,
    может найти лук с увеличенным случайным (уникальным) показателем атаки.

    """

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        """Конструктор параметров объекта-события."""
        self.npc = npc

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        print("-------------------")
        next_event = choice(self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        if issubclass(type(self.npc), cc.AbstractArcher):
            bows: Any = (
                ic.BowFactory().create_standart_item(),
                ic.BowFactory().create_unique_item(),
            )
            discovered_bow = choice(bows, p=[0.4, 0.6])
            decision = item_decision(npc_info=self.npc, weapon_info=discovered_bow)
            if decision == 1:
                self.npc.add_item_to_bag(discovered_bow)
            else:

                self.game.transition_to(next_event)
        else:
            discovered_bow = ic.BowFactory().create_standart_item()
            decision = item_decision(npc_info=self.npc, weapon_info=discovered_bow)
            if decision == 1:
                self.npc.add_item_to_bag(discovered_bow)
                self.game.transition_to(next_event)
            else:
                self.game.transition_to(next_event)


class EventSpellBook(Event):
    """Класс для представления в игре события «Книга заклинаний».

    Игровой персонаж находит книгу с заклинаниями со случайным показателем их разрушительной силы.
    Игровой персонаж класса «Маг» с большей вероятностью, чем игровой персонаж другого класса,
    может найти книгу с заклинаниями с увеличенным случайным (уникальным) показателем их разрушительной силы.

    """

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        """Конструктор параметров объекта - события."""
        self.npc = npc

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        print("-------------------")
        next_event = choice(self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        if issubclass(type(self.npc), cc.AbstractWizard):
            books: Any = (
                ic.MagicAcademy().create_standart_item(),
                ic.MagicAcademy().create_unique_item(),
            )
            discovered_spell_books: Union[Any] = choice(books, p=[0.4, 0.6])
            decision = item_decision(
                npc_info=self.npc, weapon_info=discovered_spell_books
            )
            if decision == 1:
                self.npc.add_item_to_bag(discovered_spell_books)
                self.game.transition_to(next_event)
            else:
                self.game.transition_to(next_event)
        else:
            discovered_spell_book = ic.MagicAcademy().create_standart_item()
            decision = item_decision(
                npc_info=self.npc, weapon_info=discovered_spell_book
            )
            if decision == 1:
                self.npc.add_item_to_bag(discovered_spell_book)
                self.game.transition_to(next_event)
            else:
                self.game.transition_to(next_event)


class EventArrow(Event):
    """Класс для представления события «Стрелы» в игре.

    Игровой персонаж находит стрелы, необходимые для активации возможности использования лука во время боя.

    """

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        """Конструктор параметров объекта-события."""
        self.npc = npc

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        print("-------------------")
        next_event = choice(self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        discovered_arrow = ic.ArrowFactory().create_standart_item()
        decision = item_decision(npc_info=self.npc, weapon_info=discovered_arrow)
        if decision == 1:
            self.npc.add_item_to_bag(discovered_arrow)

            self.game.transition_to(next_event)
        else:
            self.game.transition_to(next_event)


class EventTotem(Event):
    """Класс объекта для представления в игре события «Тотем».

    Игровой персонаж находит волшебный тотем,
    дающий возможность игроку сохранить текущее состояние игрового персонажа и
    при его гибели начать игру с параметрами, действующими на момент сохранения.

    """

    def __init__(
        self,
        npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard],
        life_keeper: Any,
    ):
        """Конструктор параметров объекта-события."""
        self.npc = npc
        self.life_keeper = life_keeper

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        print("-------------------")
        next_event = choice(self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        discovered_totem = ic.MysteriousPlace().create_standart_item()
        decision = item_decision(
            npc_info=self.npc, weapon_info=discovered_totem, totem=True
        )
        if decision == 1:
            self.npc.add_item_to_bag(discovered_totem)
            self.life_keeper.backup()
            self.game.transition_to(next_event)
        else:
            self.game.transition_to(next_event)


class EventBattle(Event):
    """Класс для представления события «Бой» в игре.

    Игровой персонаж встречает чудовище случайного класса и случайными показателями уровня жизни и силы атаки.
    При гибели игрового персонажа у игрока имеется возможность загрузить игру,
    если игровой персонаж ранее находил волшебный тотем.

    """

    def __init__(
        self,
        npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard],
        life_keeper: Any,
        monster_health: Tuple[int, int],
        monster_attack: Tuple[int, int],
    ) -> None:
        """Конструктор параметров объекта-события."""
        self.npc = npc
        self.life_keeper = life_keeper
        self.monster_health = monster_health
        self.monster_attack = monster_attack

    def start(self) -> None:
        """Запускаем работу объекта-события."""
        try:
            print("-------------------")
            next_event = choice(
                self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3]
            )
            random_monster_health = random.randint(
                self.monster_health[0], self.monster_health[1]
            )
            random_monster_attack = random.randint(
                self.monster_attack[0], self.monster_attack[1]
            )
            random_monster: Union[Any] = random.choice(
                [
                    cc.MonsterFactory(
                        random_monster_health, random_monster_attack
                    ).create_swordsman(),
                    cc.MonsterFactory(
                        random_monster_health, random_monster_attack
                    ).create_archer(),
                    cc.MonsterFactory(
                        random_monster_health, random_monster_attack
                    ).create_wizard(),
                ]
            )
            print(
                f"БОЙ! Вы встретили чудовище класса '{random_monster.__str__()}'. "
                f"Жизней {random_monster.get_health_info()}. "
                f"Сила атаки {random_monster.get_attack_info()}."
            )
            decision = battle_decision(npc_info=self.npc)
            if decision == 1:
                while (
                    random_monster.get_health_info() > 0
                    and self.npc.get_health_info() > 0
                ):
                    self.npc.get_attack(random_monster)
                    random_monster.get_attack(self.npc)
                    if (
                        self.npc.get_health_info() > 0
                        and random_monster.get_health_info() > 0
                    ):
                        print(
                            f"БОЙ! Чудовище ранено! Осталось жизней {random_monster.get_health_info()}. "
                            f"Сила атаки {random_monster.get_attack_info()}."
                        )
                        decision = battle_decision(npc_info=self.npc)
                        if decision == 1:
                            self.npc.get_attack(random_monster)
                            random_monster.get_attack(self.npc)
                        elif decision == 2:

                            self.game.transition_to(next_event)
                if (
                    self.npc.get_health_info() <= 0
                    and random_monster.get_health_info() <= 0
                ):
                    print("-------------------")
                    print(
                        "ПОРАЖЕНИЕ. Вы избавили мир от великого зла, ценой своей жизни! "
                        "Ваш подвиг будет согревать сердца людей близлежащей деревни. "
                        "\nВ вашу честь закатили пирушку и благополучно забыли через год. "
                        "Возможно, в следующей жизни вам повезёт больше!"
                    )
                    if load_save_decision(self.npc):
                        self.life_keeper.undo()
                        self.npc.remove_item_from_bag(ic.Totem())
                        self.game.transition_to(next_event)
                    else:
                        sys.exit(0)
                if self.npc.get_health_info() <= 0:
                    print("-------------------")
                    print("ПОРАЖЕНИЕ")
                    if load_save_decision(self.npc):
                        self.life_keeper.undo()
                        self.npc.remove_item_from_bag(ic.Totem())
                        self.game.transition_to(next_event)
                    else:
                        sys.exit(0)
                global monster_counter
                monster_counter += 1
                self.game.transition_to(next_event)
            elif decision == 2:
                self.game.transition_to(next_event)
        except SystemExit:
            raise


def load_save_decision(
    npc_info: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]
) -> Any:
    """Получаем от игрока решение о продолжении игры путём загрузки сохранения.

    Проверяем наличие волшебного тотема в инвентаре игрового персонажа. В случае положительного результата проверки
    получаем от игрока решение об его использовании.

    """
    while True:
        try:
            if npc_info.check_item_in_bag(ic.Totem()):
                decision = int(input("Использовать волшебный ТОТЕМ: 1 - Да. 2 - Нет. "))
                if decision == 1:
                    return True
                elif decision == 2:
                    return False
                elif decision > 3 or decision < 1:
                    raise ValueError()
            else:
                return False
        except ValueError:
            print("Неккоректный ввод! Повторите!")
        else:
            break


def npc_decision() -> Optional[int]:
    """Даём игроку выбрать класс игрового персонажа, которым игрок будет проходить игру."""
    while True:
        try:
            decision = int(
                input("Выберете КЛАСС персонажа: 1 - Мечник. 2 - Лучник. 3 - Маг. ")
            )
            if decision > 3 or decision < 1:
                raise ValueError()
        except ValueError:
            print("Неккоректный ввод! Повторите!")
        else:
            break
    return decision


def battle_decision(
    npc_info: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]
) -> Optional[int]:
    """Получаем от игрока решение о его действии при встрече с чудовищем.

    Даём возможность сменить оружие для атаки из доступного в инвентаре.

    """
    while True:
        try:
            decision = int(
                input(
                    f"У рыцаря {npc_info.get_health_info()} жизней, "
                    f"используемое оружие: '{npc_info.get_weapon_info()}': {npc_info.get_attack_info()}! "
                    f"1 - Атаковать. 2 - Отступить. 3 - Выбрать другое оружие для атаки. "
                )
            )
            if decision == 3:
                npc_info.select_weapon()
                decision = int(
                    input(
                        f"У рыцаря {npc_info.get_health_info()} жизней, "
                        f"используемое оружие {npc_info.get_weapon_info()}: {npc_info.get_attack_info()}! "
                        f"1 - Атаковать. 2 - Отступить. "
                    )
                )
            if decision > 3 or decision < 1:
                raise ValueError()
        except ValueError:
            print("Неккоректный ввод! Повторите!")
        else:
            break
    return decision


def item_decision(
    npc_info: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard],
    weapon_info: Union[
        ic.Sword,
        ic.UniqueSword,
        ic.Bow,
        ic.UniqueBow,
        ic.SpellBook,
        ic.UniqueSpellBook,
        ic.Arrow,
        ic.Totem,
    ],
    totem: bool = False,
) -> Optional[int]:
    """Получаем от игрока решение о его действии при нахождении волшебного тотема и оружия."""
    while True:
        try:
            if totem:
                print(
                    "Вам повезло, вы нашли ТОТЕМ Корлуна Могучего, "
                    "способного обмануть смерть раз в 3 месяца, "
                    "\nно вы не Корлун и можете использовать ТОТЕМ лишь однажды, "
                    "чтобы повернуть время вспять и вернуться к жизни!"
                )
                decision = int(
                    input(
                        "1 - Сохранить игру, взяв ТОТЕМ с собой! 2 - Оставить на месте. "
                    )
                )
                if decision > 2 or decision < 1:
                    raise ValueError()
            else:
                print(
                    f"Найден предмет: {weapon_info.__str__()}! Сила атаки {weapon_info.get_damage_info()}."
                )
                print("Сумка героя:", npc_info.show_bag())
                decision = int(
                    input("1 - Взять найденный предемет. 2 - Оставить на месте. ")
                )
                if decision > 2 or decision < 1:
                    raise ValueError()
        except ValueError:
            print("Неккоректный ввод! Повторите!")
        else:
            break
    return decision


def weapon_decision(
    npc_info: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard],
    weapon_info: Union[Any],
) -> Optional[int]:
    """Получаем от игрока решение о его действии при нахождении волшебного тотема и оружия."""
    while True:
        try:
            print(
                f"Найден предмет: {weapon_info.__str__()}! Сила атаки {weapon_info.get_damage_info()}."
            )
            print("Сумка героя:", npc_info.show_bag())
            decision = int(
                input("1 - Взять найденный предемет. 2 - Оставить на месте. ")
            )
            if decision > 2 or decision < 1:
                raise ValueError()
        except ValueError:
            print("Неккоректный ввод! Повторите!")
        else:
            break
    return decision


def create_npc(
    npc_user_choice: Optional[int], npc_hp: int, npc_attack: int
) -> Any[object]:
    """В зависимости от выбора игрока создаём игрового персонажа.

    Добавляем в инвентарь меч со случайным показателем уровня атаки.

    """
    npc: Union[None, cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard] = None
    initial_weapon = ic.SwordFactory().create_standart_item()
    if npc_user_choice == 1:
        npc = cc.HumanFactory(npc_hp, npc_attack).create_swordsman()
        npc.add_item_to_bag(initial_weapon, initial_weapon=True)
        print(f"Выбран класс: '{npc}'")
    elif npc_user_choice == 2:
        npc = cc.HumanFactory(npc_hp, npc_attack).create_archer()
        npc.add_item_to_bag(initial_weapon, initial_weapon=True)
        print(f"Выбран класс: '{npc}'")
    elif npc_user_choice == 3:
        npc = cc.HumanFactory(npc_hp, npc_attack).create_wizard()
        npc.add_item_to_bag(initial_weapon, initial_weapon=True)
        print(f"Выбран класс: '{npc}'")
    return npc


monster_counter = 0
initial_monster_hp_range = (10, 25)
initial_monster_attack_range = (10, 30)
initial_npc_hp = 15
initial_npc_attack = 15


def main() -> None:
    """Запускаем игру в соответствии с заданным игровым сценарием."""
    try:
        my_npc = create_npc(npc_decision(), initial_npc_hp, initial_npc_attack)
        lifekeeper = cc.Storage(my_npc)
        ev_list = (
            EventApple(my_npc),
            EventSword(my_npc),
            EventBow(my_npc),
            EventSpellBook(my_npc),
            EventArrow(my_npc),
            EventTotem(my_npc, lifekeeper),
            EventBattle(
                my_npc,
                lifekeeper,
                initial_monster_hp_range,
                initial_monster_attack_range,
            ),
        )
        my_game = Game(ev_list)
        while monster_counter != 10:
            my_game.run()
        print("-------------------")
        print("ПОБЕДА")
        sys.exit(0)
    except SystemExit:
        raise


if __name__ == "__main__":
    main()
