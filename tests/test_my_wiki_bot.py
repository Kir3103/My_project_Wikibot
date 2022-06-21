"""Тест модуля my_wiki_bot"""
from unittest.mock import patch

import ddt
import my_wiki_bot
import unittest


@ddt.ddt
class TestWikiBot(unittest.TestCase):
    """Тестовый случай для функции get_wiki_information"""

    def setUp(self) -> None:
        self.text = my_wiki_bot.get_wiki_information

    # @ddt.ddt(
    #     ('31', '31 марта — 90-й день года  по григорианскому календарю. До конца года остаётся '
    #            '275 дней. До 15 октября 1582 года — 31 марта по юлианскому календарю, с 15 октября '
    #            '1582 года — 31 марта по григорианскому календарю. В XX и XXI веках соответствует '
    #            '18 марта по юлианскому календарю. Ноль  — целое число, которое при сложении '
    #            'с любым числом или вычитании из него не меняет последнее, то есть даёт результат, '
    #            'равный этому последнему; умножение любого числа на ноль даёт ноль. '
    #            'Большой толковый словарь Кузнецова  приводит обе формы слова: ноль, нуль — как '
    #            'равнозначные, хотя имеется некоторое различие в употреблении.', True),
    #     ('[]', 'Ничего не могу найти по Вашему запросу. Возможно Вам нужно найти что-то еще?', True)
    #
    # )
    # @ddt.unpack
    # def test_get_text_from_wiki(self, user_request, wiki_answer, expect):
    #     """Тестовый случай для запроса от пользователя {0} и ответа бота {1}"""
    #     result = self.text(user_request) == wiki_answer
    #     self.assertEqual(result, expect)

    # def test_exception(self):
    #     with self.assertRaises(Exception):
    #         self.text('[]')
    @patch('my_wiki_bot.wikipedia')
    def test_good(self, req_mock):
        req_mock.get_wiki_information.return_value = 'Ничего не могу найти по Вашему запросу. ' \
                                                     'Возможно Вам нужно найти что-то еще?'
        result = 'Ничего не могу найти по Вашему запросу. Возможно Вам нужно найти что-то еще?'
        self.assertEqual(result, self.text('[]'))
