import unittest
from unittest import TestCase
from unittest.mock import patch

import main as rpg


class SwordsmanRpgTestCase(TestCase):
    """Юнит тест для проверки работоспособности игры при игре мечником."""

    def setUp(self) -> None:
        """Начальные условия для тестов."""
        self.input = ""
        self.victory_count = 0
        self.fail_count = 0
        self.load_count = 0

    def fake_io_with_asserts(self, *args):
        """Обработка print() и input() в программе с проверками результата."""
        last_io = "".join(args)
        if "КЛАСС" in last_io:
            self.input = "1"
        elif "МЕЧ" in last_io:
            self.input = "1"
        elif "ЛУК" in last_io:
            self.input = "1"
        elif "КНИГА ЗАКЛИНАНИЙ" in last_io:
            self.input = "1"
        elif "СТРЕЛЫ" in last_io:
            self.input = "1"
        elif "ТОТЕМ" in last_io:
            self.input = "1"
        elif "БОЙ" in last_io:
            self.input = "1"
        elif "РАНЕНО" in last_io:
            self.input = "1"
        elif "ПОБЕДА" in last_io:
            self.assertEqual(rpg.monster_counter, 10)
            self.victory_count += 1
            self.input = "\n"
        elif "ПОРАЖЕНИЕ" in last_io:
            self.assertTrue(rpg.monster_counter < 10)
            self.fail_count += 1
            self.input = "\n"
        elif "ЗАГРУЗИТЬ" in last_io:
            self.input = "1"
            self.load_count += 1
        else:
            self.input = "\n"
        return last_io

    def test_game_e2e(self):
        """Тест, выполняющий полностью прохождение игры."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                with self.assertRaises(SystemExit):
                    rpg.run_game()

    def test_game_e2e_until_at_least_one_victory(self):
        """Тест, проверяющий что в игру возможно когда-нибудь выиграть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.victory_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.run_game()
        self.assertEqual(self.victory_count, 1)

    def test_game_e2e_until_at_least_one_load(self):
        """Тест, проверяющий что при наличии сохранения, игру можно загрузить и продолжить играть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.load_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.run_game()
        self.assertGreater(self.load_count, 0)

    def tearDown(self):
        rpg.monster_counter = 0


class ArcherRpgTestCase(TestCase):
    """Юнит тест для проверки работоспособности игры при игре лучником."""

    def setUp(self) -> None:
        """Начальные условия для тестов."""
        self.input = ""
        self.victory_count = 0
        self.fail_count = 0
        self.load_count = 0

    def fake_io_with_asserts(self, *args):
        """Обработка print() и input() в программе с проверками результата."""
        last_io = "".join(args)
        if "КЛАСС" in last_io:
            self.input = "2"
        elif "МЕЧ" in last_io:
            self.input = "1"
        elif "ЛУК" in last_io:
            self.input = "1"
        elif "КНИГА ЗАКЛИНАНИЙ" in last_io:
            self.input = "1"
        elif "СТРЕЛЫ" in last_io:
            self.input = "1"
        elif "ТОТЕМ" in last_io:
            self.input = "1"
        elif "БОЙ" in last_io:
            self.input = "1"
        elif "РАНЕНО" in last_io:
            self.input = "1"
        elif "ПОБЕДА" in last_io:
            self.assertEqual(rpg.monster_counter, 10)
            self.victory_count += 1
            self.input = "\n"
        elif "ПОРАЖЕНИЕ" in last_io:
            self.assertTrue(rpg.monster_counter < 10)
            self.fail_count += 1
            self.input = "\n"
        elif "ЗАГРУЗИТЬ" in last_io:
            self.input = "1"
            self.load_count += 1
        else:
            self.input = "\n"
        return last_io

    def test_game_e2e(self):
        """Тест, выполняющий полностью прохождение игры."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                with self.assertRaises(SystemExit):
                    rpg.run_game()

    def test_game_e2e_until_at_least_one_victory(self):
        """Тест, проверяющий что в игру возможно когда-нибудь выиграть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.victory_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.run_game()
        self.assertEqual(self.victory_count, 1)

    def test_game_e2e_until_at_least_one_load(self):
        """Тест, проверяющий что при наличии сохранения, игру можно загрузить и продолжить играть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.load_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.run_game()
        self.assertGreater(self.load_count, 0)

    def tearDown(self):
        rpg.monster_counter = 0


class WizardRpgTestCase(TestCase):
    """Юнит тест для проверки работоспособности игры при игре магом."""

    def setUp(self) -> None:
        """Начальные условия для тестов."""
        self.input = ""
        self.victory_count = 0
        self.fail_count = 0
        self.load_count = 0

    def fake_io_with_asserts(self, *args):
        """Обработка print() и input() в программе с проверками результата."""
        last_io = "".join(args)
        if "КЛАСС" in last_io:
            self.input = "3"
        elif "МЕЧ" in last_io:
            self.input = "1"
        elif "ЛУК" in last_io:
            self.input = "1"
        elif "КНИГА ЗАКЛИНАНИЙ" in last_io:
            self.input = "1"
        elif "СТРЕЛЫ" in last_io:
            self.input = "1"
        elif "ТОТЕМ" in last_io:
            self.input = "1"
        elif "БОЙ" in last_io:
            self.input = "1"
        elif "РАНЕНО" in last_io:
            self.input = "1"
        elif "ПОБЕДА" in last_io:
            self.assertEqual(rpg.monster_counter, 10)
            self.victory_count += 1
            self.input = "\n"
        elif "ПОРАЖЕНИЕ" in last_io:
            self.assertTrue(rpg.monster_counter < 10)
            self.fail_count += 1
            self.input = "\n"
        elif "ЗАГРУЗИТЬ" in last_io:
            self.input = "1"
            self.load_count += 1
        else:
            self.input = "\n"
        return last_io

    def test_game_e2e(self):
        """Тест, выполняющий полностью прохождение игры."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                with self.assertRaises(SystemExit):
                    rpg.run_game()

    def test_game_e2e_until_at_least_one_victory(self):
        """Тест, проверяющий что в игру возможно когда-нибудь выиграть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.victory_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.run_game()
        self.assertEqual(self.victory_count, 1)

    def test_game_e2e_until_at_least_one_load(self):
        """Тест, проверяющий что при наличии сохранения, игру можно загрузить и продолжить играть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.load_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.run_game()
        self.assertGreater(self.load_count, 0)

    def tearDown(self):
        rpg.monster_counter = 0


if __name__ == "__main__":
    unittest.main()
