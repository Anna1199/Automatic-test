import pytest
from string_utils import StringUtils

# #проверки метода для заглавной буквы
@pytest.mark.capitalLaters
@pytest.mark.parametrize('word1, expected', [('s', 'S'), ('samara', 'Samara'), (' ', ' '), ('Samara', 'Samara')])
def test_capitalize(word1, expected):
    word = StringUtils()
    res = word.capitilize(word1)
    assert res == expected

# проверки метода для удаления пробелов в начале строки
@pytest.mark.trim()
@pytest.mark.parametrize('word1, expected', [(' SkyPro', 'SkyPro'),('\tSkyPro\n', 'SkyPro'),('', '')])
def test_trim(word1, expected):
    word = StringUtils()
    res = word.trim(word1)
    assert res == expected

#проверки метода с преобразованием списка
@pytest.mark.to_list
@pytest.mark.parametrize('string, delimiter, expected', [('1,2,3,4,5,6', ',', ['1', '2', '3', '4', '5', '6']), ('1,2,3,4,5,6', '-', ['1 -', '2 -', '3 -', '4 -', '5 -', '6 -']), ('', ',', [])])
def test_to_list(string, delimiter, expected):
    string_utils = StringUtils()
    res = string_utils.to_list(string, delimiter)
    assert res == expected

# проверка метода с поиском символа
@pytest.mark.contains
@pytest.mark.parametrize('string, symbol, expected', [('Samara', 'S', True), ('Samara', 's', True), ('Samara', 't', False) ('', 'a', False)])
def test_contains(string, symbol, expected):
    string_utils = StringUtils()
    res = string_utils.contains(string, symbol)
    assert res == expected

# проверка метода для удаления подстрок
@pytest.mark.delet_symbol
@pytest.mark.parametrize('string, symbol, expected', [('Samara', 'S', 'amara'), ('K ', ' ', 'K'), ('123', '2', '13')])
def test_delet_symbol (string, symbol, expected):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(string, symbol)
    assert res == expected

# проверка метода для поиска первого символа
@pytest.mark.starts_with
@pytest.mark.parametrize('string, symbol, expected', [('Samara', 'S', True), ('123', '1', True), ('  ', ' ', True), ('Samara', 'A', False)])
def test_starts_with (string, symbol, expected):
    string_utils = StringUtils()
    res = string_utils.starts_with(string, symbol)
    assert res == expected

#проверка метода для проверки последднего символа в строке
@pytest.mark.ends_with
@pytest.mark.parametrize('string, symbol, expected', [('Samara', 'a', True), ('123', '3', True), ('  ', ' ', True), ('Samara', 'S', False)])
def test_starts_with (string, symbol, expected):
    string_utils = StringUtils()
    res = string_utils.end_with(string, symbol)
    assert res == expected

#проверка метода для проверки пустой строки
@pytest.mark.is_empty
@pytest.mark.parametrize('string, expected', [('Samara', True), ('', True), ('  ', True), ('Samara', False), ('  ', False)])
def test_starts_with (string, expected):
    string_utils = StringUtils()
    res = string_utils.is_empty(string)
    assert res == expected

#проверки метода с преобразованием списка №2
@pytest.mark.list_to_string
@pytest.mark.parametrize('list, joiner, expected', [(['1,2,3,4,5,6'], ',', '1,2,3,4,5,6'), ([1,2,3,4,5,6], '-', '1-2-3-4-5-6'), ('', ',', ''), (['Sky', 'Pro'], ':', 'Sky:Pro')])
def test_to_list(list, joiner, expected):
    string_utils = StringUtils()
    res = string_utils.list_to_string(list, joiner)
    assert res == expected