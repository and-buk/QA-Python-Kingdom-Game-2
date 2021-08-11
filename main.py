from __future__ import annotations
import random
import sys
from abc import ABC, abstractmethod
from numpy.random import choice
from typing import Any, Optional, Union
import creatures_creator as cc
import item_creator as ic


class GameWorld:
    """Класс объекта, определяющий интерфейс управления игрой: игровыми событиями."""

    _event: Any

    def __init__(self, event_list: Union[Any]) -> None:
        self.event_list = event_list
        random_event = choice(event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        self.transition_to(random_event)

    def transition_to(self, event: Any) -> None:
        """Меняем состояние игры - гровое Событие во время игры."""
        self._event = event
        self._event.game = self

    def run(self) -> None:
        """Запускаем игру и  функционал, связанных с ней игровых событий."""
        self._event.start()


class Event(ABC):
    """Базовый класс События в игре."""

    _game = None

    @property
    def game(self) -> Any:
        return self._game

    @game.setter
    def game(self, game: GameWorld) -> None:
        self._game = game

    @abstractmethod
    def start(self) -> None:
        pass


class EventApple(Event):
    """Событие, возникновение которого в игре, позволяет найти яблоко, повышающее здоровье игрового персонажа."""

    def __init__(
        self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]
    ) -> None:
        self.npc = npc

    def start(self) -> None:
        print("-------------------")
        apple = ic.MagicTree().create_standart_item()
        self.npc.increase_health(apple.get_hp_info())
        print(
            f"Вы нашли яблочко здоровья! +{apple.get_hp_info()} к здоровью героя. "
            f"У героя {self.npc.get_health_info()} жизней."
        )
        next_event = random.choice(self.game.event_list)
        self.game.transition_to(next_event)


class EventSword(Event):
    """Событие, возникновение которого в игре, позволяет найти клинковое оружие класса "Меч"."""

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        self.npc = npc

    def start(self) -> None:
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
    """Событие, возникновение которого в игре, позволяет найти метательное оружие класса "Лук"."""

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        self.npc = npc

    def start(self) -> None:
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
    """Событие, возникновение которого в игре, позволяет найти книгу с боевыми магическими заклинаниями."""

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        self.npc = npc

    def start(self) -> None:
        print("-------------------")
        next_event = choice(self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
        if issubclass(type(self.npc), cc.AbstractWizard):
            books: Any = (
                ic.MagicLibrary().create_standart_item(),
                ic.MagicLibrary().create_unique_item(),
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
            discovered_spell_book = ic.MagicLibrary().create_standart_item()
            decision = item_decision(
                npc_info=self.npc, weapon_info=discovered_spell_book
            )
            if decision == 1:
                self.npc.add_item_to_bag(discovered_spell_book)
                self.game.transition_to(next_event)
            else:
                self.game.transition_to(next_event)


class EventArrow(Event):
    """Событие, возникновение которого в игре, позволяет найти метательный снаряд класса "Стрела"."""

    def __init__(self, npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard]):
        self.npc = npc

    def start(self) -> None:
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
    """Событие, возникновение которого в игре, позволяет найти предмет: "Тотем",
    сохранить, и при гибели игрового персонажа, загрузить текущее состояние игры, соответственно."""

    def __init__(
        self,
        npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard],
        life_keeper: Any,
    ):
        self.npc = npc
        self.life_keeper = life_keeper

    def start(self) -> None:
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
    """Событие, возникновение которого приводит к встрече и сражению игрового персонажа со случайным чудовищем."""

    def __init__(
        self,
        npc: Union[cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard],
        life_keeper: Any,
    ) -> None:
        self.npc = npc
        self.life_keeper = life_keeper

    def start(self) -> None:
        try:
            print("-------------------")
            next_event = choice(
                self.game.event_list, p=[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3]
            )
            random_monster: Union[Any] = random.choice(
                [
                    cc.MonsterFactory().create_swordsman(),
                    cc.MonsterFactory().create_archer(),
                    cc.MonsterFactory().create_wizard(),
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
    """Обеспечиваем ."""
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
    """."""
    while True:
        try:
            decision = int(
                input("Выберете класс персонажа: 1 - Мечник. 2 - Лучник. 3 - Маг. ")
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
    """."""
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
    """."""
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
    """."""
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


def create_npc(npc_user_choice: Optional[int]) -> Any[object]:
    """."""
    npc: Union[None, cc.HumanSwordsman, cc.HumanArcher, cc.HumanWizard] = None
    initial_weapon = ic.SwordFactory().create_standart_item()
    if npc_user_choice == 1:
        npc = cc.HumanFactory().create_swordsman()
        npc.add_item_to_bag(initial_weapon, initial_weapon=True)
        print(f"Выбран класс: '{npc}'")
    elif npc_user_choice == 2:
        npc = cc.HumanFactory().create_archer()
        npc.add_item_to_bag(initial_weapon, initial_weapon=True)
        print(f"Выбран класс: '{npc}'")
    elif npc_user_choice == 3:
        npc = cc.HumanFactory().create_wizard()
        npc.add_item_to_bag(initial_weapon, initial_weapon=True)
        print(f"Выбран класс: '{npc}'")
    return npc


monster_counter = 0


def main() -> None:
    try:
        my_npc = create_npc(npc_decision())
        lifekeeper = cc.Lifekeeper(my_npc)
        ev_list = (
            EventApple(my_npc),
            EventSword(my_npc),
            EventBow(my_npc),
            EventSpellBook(my_npc),
            EventArrow(my_npc),
            EventTotem(my_npc, lifekeeper),
            EventBattle(my_npc, lifekeeper),
        )
        my_game = GameWorld(ev_list)
        while monster_counter != 10:
            my_game.run()
        print("-------------------")
        print("ПОБЕДА")
        sys.exit(0)
    except SystemExit:
        raise


if __name__ == "__main__":
    main()
