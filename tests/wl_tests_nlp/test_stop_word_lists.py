# ----------------------------------------------------------------------
# Wordless: Tests - NLP - Stop Word Lists
# Copyright (C) 2018-2022  Ye Lei (叶磊)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import pytest

from tests import wl_test_init
from wordless.wl_nlp import wl_stop_word_lists

main = wl_test_init.Wl_Test_Main()

test_stop_word_lists = []

for lang, stop_word_lists in main.settings_global['stop_word_lists'].items():
    if 'custom' not in stop_word_lists:
        stop_word_lists.append('Missing Custom List')

    for stop_word_list in stop_word_lists:
        test_stop_word_lists.append((lang, stop_word_list))

@pytest.mark.parametrize('lang, stop_word_list', test_stop_word_lists)
def test_get_stop_word_list(lang, stop_word_list):
    stop_words = wl_stop_word_lists.wl_get_stop_word_list(main, lang, stop_word_list = stop_word_list)

    print(f'{lang} / {stop_word_list}:')
    print(f'{stop_words}\n')

    if stop_word_list == 'custom':
        # Check if custom list is empty
        assert stop_words == set()
    else:
        # Check for missing custom lists
        assert stop_word_list != 'Missing Custom List'
        # Check if the list is empty
        assert stop_words
        # Check if there are empty tokens in the list
        assert all((stop_word.strip() for stop_word in stop_words))

def test_filter_stop_words():
    assert wl_stop_word_lists.wl_filter_stop_words(main, items = ['a'], lang = 'eng_us') == []
    assert wl_stop_word_lists.wl_filter_stop_words(main, items = [], lang = 'eng_us') == []

if __name__ == '__main__':
    for lang, stop_word_list in test_stop_word_lists:
        test_get_stop_word_list(lang, stop_word_list)

    test_filter_stop_words()