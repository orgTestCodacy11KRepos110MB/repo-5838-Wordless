#
# Wordless: Packaging - spec File
#
# Copyright (C) 2018-2022  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

import os
import platform
import sys

import PyInstaller
import pythainlp

block_cipher = None
datas = []

# botok
datas.extend(PyInstaller.utils.hooks.collect_data_files('botok'))
# jieba
datas.extend(PyInstaller.utils.hooks.collect_data_files('jieba'))
# langdetect
datas.extend(PyInstaller.utils.hooks.collect_data_files('langdetect'))
# nagisa
datas.extend(PyInstaller.utils.hooks.collect_data_files('nagisa', include_py_files = True))
# OpenCC
datas.extend(PyInstaller.utils.hooks.collect_data_files('opencc'))
# pkuseg
datas.extend(PyInstaller.utils.hooks.collect_data_files('pkuseg'))
# Python-scfsuite
datas.extend(PyInstaller.utils.hooks.collect_data_files('pycrfsuite', include_py_files = True))
# pymorphy2
datas.extend(PyInstaller.utils.hooks.copy_metadata('pymorphy2_dicts_ru'))
datas.extend(PyInstaller.utils.hooks.copy_metadata('pymorphy2_dicts_uk'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('pymorphy2_dicts_ru'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('pymorphy2_dicts_uk'))
# Pyphen
datas.extend(PyInstaller.utils.hooks.collect_data_files('pyphen'))
# PyThaiNLP
datas.extend(PyInstaller.utils.hooks.collect_data_files('pythainlp'))
# Sacremoses
datas.extend(PyInstaller.utils.hooks.collect_data_files('sacremoses'))
# spaCy
datas.extend(PyInstaller.utils.hooks.collect_data_files('spacy.lang', include_py_files = True))
datas.extend(PyInstaller.utils.hooks.copy_metadata('spacy_lookups_data'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('spacy_lookups_data', include_py_files = True))
datas.extend(PyInstaller.utils.hooks.collect_data_files('spacy_pkuseg'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('ca_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('zh_core_web_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('da_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('de_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('el_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('en_core_web_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('es_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('fr_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('it_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('lt_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('mk_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('nb_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('nl_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('pl_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('pt_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('ro_core_news_sm'))
datas.extend(PyInstaller.utils.hooks.collect_data_files('ru_core_news_sm'))
# ssg
datas.extend(PyInstaller.utils.hooks.collect_data_files('ssg'))
# TextBlob
datas.extend(PyInstaller.utils.hooks.collect_data_files('textblob'))
# Tokenizer
datas.extend(PyInstaller.utils.hooks.collect_data_files('tokenizer'))
# Underthesea
datas.extend(PyInstaller.utils.hooks.collect_data_files('underthesea'))
# wordcloud
datas.extend(PyInstaller.utils.hooks.collect_data_files('wordcloud'))

# Custom data files
datas.extend([
    ('src/lemmatization', 'lemmatization'),
    ('src/stop_word_lists', 'stop_word_lists'),
    # Measures
    ('src/wl_measures/dale_list_easy_words_769.txt', 'wl_measures'),
    ('src/wl_measures/dale_list_easy_words_3000.txt', 'wl_measures'),
    # PyThaiNLP
    (pythainlp.tools.get_pythainlp_data_path(), 'pythainlp-data'),

    ('src/imgs', 'imgs'),
    ('src/wl_acks.xlsx', '.'),

    ('src/CHANGELOG.md', '.'),
    ('src/VERSION', '.'),
    ('LICENSE.txt', '.')
])

# Data files for macOS
if platform.system() == 'Darwin':
    datas.extend(PyInstaller.utils.hooks.collect_data_files('PIL', include_py_files = True))

# Hidden imports
hiddenimports = [
    # pymorphy2
    'pymorphy2_dicts_ru',
    'pymorphy2_dicts_uk',

    # spaCy models
    'ca_core_news_sm',
    'zh_core_web_sm',
    'da_core_news_sm',
    'de_core_news_sm',
    'el_core_news_sm',
    'en_core_web_sm',
    'es_core_news_sm',
    'fr_core_news_sm',
    'it_core_news_sm',
    'lt_core_news_sm',
    'mk_core_news_sm',
    'nb_core_news_sm',
    'nl_core_news_sm',
    'pl_core_news_sm',
    'pt_core_news_sm',
    'ro_core_news_sm',
    'ru_core_news_sm'
]

# Exclusions
if platform.system() in ['Windows', 'Linux']:
    excludes = []
elif platform.system() == 'Darwin':
    excludes = [
        'PIL'
    ]

# Icons
if platform.system() in ['Windows', 'Linux']:
    icon = 'src/imgs/wl_icon.ico'
elif platform.system() == 'Darwin':
    icon = 'src/imgs/wl_icon.icns'

a = Analysis(
    ['src/wl_main.py'],
    pathex = [],
    binaries = [],
    datas = datas,
    hiddenimports = hiddenimports,
    hookspath = [],
    runtime_hooks = [],
    excludes = excludes,
    win_no_prefer_redirects = False,
    win_private_assemblies = False,
    cipher = block_cipher,
    noarchive = False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher = block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries = True,
    name = 'Wordless',
    debug = False,
    bootloader_ignore_signals = False,
    strip = False,
    upx = True,
    console = False,
    disable_windowed_traceback = False,
    target_arch = None,
    codesign_identity = None,
    entitlements_file = None,
    icon = icon
)

# Collect data files
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip = False,
    upx = True,
    upx_exclude = [],
    name = 'Wordless'
)

# Bundle application on macOS
if platform.system() == 'Darwin':
    app = BUNDLE(
        coll,
        name = 'Wordless.app',
        icon = icon,
        bundle_identifier = None,
        info_plist = {
           'NSHighResolutionCapable': 'True'
        }
    )
