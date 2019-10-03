#
# Wordless: Tests - Text - Text Processing - POS Tagging
#
# Copyright (C) 2018-2019  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

import sys

sys.path.append('.')

import pytest

from wordless_tests import test_init
from wordless_text import wordless_text_processing
from wordless_utils import wordless_conversion

POS_TAGGERS = []

SENTENCE_ZHO_CN = '汉语，又称汉文、中文、中国话、中国语、华语、华文、唐话[2]，或被视为一个语族，或被视为隶属于汉藏语系汉语族之一种语言。'
SENTENCE_ZHO_TW = '漢語，又稱漢文、中文、中國話、中國語、華語、華文、唐話[2]，或被視為一個語族，或被視為隸屬於漢藏語系漢語族之一種語言。'
SENTENCE_NLD = 'Het Nederlands is een West-Germaanse taal en de moedertaal van de meeste inwoners van Nederland, België en Suriname.'
SENTENCE_ENG = 'English is a West Germanic language that was first spoken in early medieval England and eventually became a global lingua franca.[5][6]'
SENTENCE_FRA = 'Le français est une langue indo-européenne de la famille des langues romanes.'
SENTENCE_DEU = 'Die deutsche Sprache bzw. Deutsch ([dɔʏ̯t͡ʃ]; abgekürzt dt. oder dtsch.) ist eine westgermanische Sprache.'
SENTENCE_ELL = 'Η ελληνική γλώσσα ανήκει στην ινδοευρωπαϊκή οικογένεια[9] και συγκεκριμένα στον ελληνικό κλάδο, μαζί με την τσακωνική, ενώ είναι η επίσημη γλώσσα της Ελλάδος και της Κύπρου.'
SENTENCE_ITA = "L'italiano ([itaˈljaːno][Nota 1] ascolta[?·info]) è una lingua romanza parlata principalmente in Italia."
SENTENCE_JPN = '日本語（にほんご、にっぽんご[注 1]）は、主に日本国内や日本人同士の間で使用されている言語である。'
SENTENCE_POR = 'A língua portuguesa, também designada português, é uma língua românica flexiva ocidental originada no galego-português falado no Reino da Galiza e no norte de Portugal.'
SENTENCE_RUS = 'Ру́сский язы́к ([ˈruskʲɪi̯ jɪˈzɨk] Информация о файле слушать)[~ 3][⇨] — один из восточнославянских языков, национальный язык русского народа.'
SENTENCE_SPA = 'El español o castellano es una lengua romance procedente del latín hablado.'
SENTENCE_THA = 'ภาษาไทย หรือ ภาษาไทยกลาง เป็นภาษาราชการและภาษาประจำชาติของประเทศไทย'
SENTENCE_BOD = '༄༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་སཏྭ་ཙརྻ་ཨ་བ་ཏ་ར། བོད་སྐད་དུ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། །སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང༌། །ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །བདེ་གཤེགས་སྲས་ཀྱི་སྡོམ་ལ་འཇུག་པ་ནི། །ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། །'
SENTENCE_UKR = 'Украї́нська мо́ва (МФА: [ukrɑ̽ˈjɪnʲsʲkɑ̽ ˈmɔwɑ̽], історичні назви — ру́ська, руси́нська[9][10][11][* 2]) — національна мова українців.'
SENTENCE_VIE = 'Tiếng Việt, còn gọi tiếng Việt Nam[5], tiếng Kinh hay Việt ngữ, là ngôn ngữ của người Việt (dân tộc Kinh) và là ngôn ngữ chính thức tại Việt Nam.'

main = test_init.Test_Main()

for lang, pos_taggers in main.settings_global['pos_taggers'].items():
    for pos_tagger in pos_taggers:
        # Temporarily disable testing of pybo's POS tagger due to memory issues
        if lang != 'bod':
            POS_TAGGERS.append((lang, pos_tagger))

@pytest.mark.parametrize('lang, pos_tagger', POS_TAGGERS)
def test_pos_tag(lang, pos_tagger):
    lang_text = wordless_conversion.to_lang_text(main, lang)

    tokens = wordless_text_processing.wordless_word_tokenize(main, globals()[f'SENTENCE_{lang.upper()}'],
                                                             lang = lang)

    tokens_tagged = wordless_text_processing.wordless_pos_tag(main, tokens,
                                                              lang = lang,
                                                              pos_tagger = pos_tagger)
    tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, tokens,
                                                                        lang = lang,
                                                                        pos_tagger = pos_tagger,
                                                                        tagset = 'universal')
    # print(tokens_tagged)
    # print(tokens_tagged_universal)

    if lang == 'zho_cn':
        assert tokens_tagged == [('汉语', 'nz'), ('，', 'x'), ('又称', 'n'), ('汉文', 'nz'), ('、', 'x'), ('中文', 'nz'), ('、', 'x'), ('中国', 'ns'), ('话', 'n'), ('、', 'x'), ('中国', 'ns'), ('语', 'ng'), ('、', 'x'), ('华语', 'nz'), ('、', 'x'), ('华文', 'nz'), ('、', 'x'), ('唐', 'nr'), ('话', 'n'), ('[', 'x'), ('2', 'x'), (']', 'x'), ('，', 'x'), ('或', 'c'), ('被', 'p'), ('视为', 'v'), ('一个', 'm'), ('语族', 'n'), ('，', 'x'), ('或', 'c'), ('被', 'p'), ('视为', 'v'), ('隶属于', 'n'), ('汉藏语系', 'nz'), ('汉语', 'nz'), ('族', 'ng'), ('之', 'u'), ('一种', 'm'), ('语言', 'n'), ('。', 'x')]
        assert tokens_tagged_universal == [('汉语', 'PROPN'), ('，', 'PUNCT/SYM'), ('又称', 'NOUN'), ('汉文', 'PROPN'), ('、', 'PUNCT/SYM'), ('中文', 'PROPN'), ('、', 'PUNCT/SYM'), ('中国', 'PROPN'), ('话', 'NOUN'), ('、', 'PUNCT/SYM'), ('中国', 'PROPN'), ('语', 'NOUN'), ('、', 'PUNCT/SYM'), ('华语', 'PROPN'), ('、', 'PUNCT/SYM'), ('华文', 'PROPN'), ('、', 'PUNCT/SYM'), ('唐', 'PRONP'), ('话', 'NOUN'), ('[', 'PUNCT/SYM'), ('2', 'PUNCT/SYM'), (']', 'PUNCT/SYM'), ('，', 'PUNCT/SYM'), ('或', 'CONJ'), ('被', 'ADP'), ('视为', 'VERB'), ('一个', 'NUM'), ('语族', 'NOUN'), ('，', 'PUNCT/SYM'), ('或', 'CONJ'), ('被', 'ADP'), ('视为', 'VERB'), ('隶属于', 'NOUN'), ('汉藏语系', 'PROPN'), ('汉语', 'PROPN'), ('族', 'NOUN'), ('之', 'PART'), ('一种', 'NUM'), ('语言', 'NOUN'), ('。', 'PUNCT/SYM')]
    elif lang == 'zho_tw':
        assert tokens_tagged == [('漢語', 'nz'), ('，', 'x'), ('又', 'd'), ('稱', 'v'), ('漢文', 'nz'), ('、', 'x'), ('中文', 'nz'), ('、', 'x'), ('中國', 'ns'), ('話', 'n'), ('、', 'x'), ('中國', 'ns'), ('語', 'n'), ('、', 'x'), ('華語', 'nz'), ('、', 'x'), ('華文', 'nz'), ('、', 'x'), ('唐', 'nr'), ('話', 'n'), ('[', 'x'), ('2', 'x'), (']', 'x'), ('，', 'x'), ('或', 'c'), ('被', 'p'), ('視為', 'v'), ('一個', 'm'), ('語族', 'n'), ('，', 'x'), ('或', 'c'), ('被', 'p'), ('視為', 'v'), ('隸', 'j'), ('屬', 'v'), ('於', 'nr'), ('漢藏語', 'nz'), ('系漢', 'n'), ('語族', 'n'), ('之一', 'r'), ('種語', 'n'), ('言', 'vg'), ('。', 'x')]
        assert tokens_tagged_universal == [('漢語', 'PROPN'), ('，', 'PUNCT/SYM'), ('又', 'ADV'), ('稱', 'VERB'), ('漢文', 'PROPN'), ('、', 'PUNCT/SYM'), ('中文', 'PROPN'), ('、', 'PUNCT/SYM'), ('中國', 'PROPN'), ('話', 'NOUN'), ('、', 'PUNCT/SYM'), ('中國', 'PROPN'), ('語', 'NOUN'), ('、', 'PUNCT/SYM'), ('華語', 'PROPN'), ('、', 'PUNCT/SYM'), ('華文', 'PROPN'), ('、', 'PUNCT/SYM'), ('唐', 'PRONP'), ('話', 'NOUN'), ('[', 'PUNCT/SYM'), ('2', 'PUNCT/SYM'), (']', 'PUNCT/SYM'), ('，', 'PUNCT/SYM'), ('或', 'CONJ'), ('被', 'ADP'), ('視為', 'VERB'), ('一個', 'NUM'), ('語族', 'NOUN'), ('，', 'PUNCT/SYM'), ('或', 'CONJ'), ('被', 'ADP'), ('視為', 'VERB'), ('隸', 'X'), ('屬', 'VERB'), ('於', 'PRONP'), ('漢藏語', 'PROPN'), ('系漢', 'NOUN'), ('語族', 'NOUN'), ('之一', 'PRON'), ('種語', 'NOUN'), ('言', 'VERB'), ('。', 'PUNCT/SYM')]
    elif lang == 'nld':
        assert tokens_tagged == [('Het', 'Art|bep|onzijd|neut__Definite=Def|Gender=Neut|PronType=Art'), ('Nederlands', 'Adj|zelfst|stell|onverv__Degree=Pos'), ('is', 'V|hulpofkopp|ott|3|ev__Aspect=Imp|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'), ('een', 'Art|onbep|zijdofonzijd|neut__Definite=Ind|Number=Sing|PronType=Art'), ('West-Germaanse', 'Adj|attr|stell|vervneut__Case=Nom|Degree=Pos'), ('taal', 'N|soort|ev|neut__Number=Sing'), ('en', 'Conj|neven___'), ('de', 'Art|bep|zijdofmv|neut__Definite=Def|PronType=Art'), ('moedertaal', 'N|soort|ev|neut__Number=Sing'), ('van', 'Prep|voor__AdpType=Prep'), ('de', 'Art|bep|zijdofmv|neut__Definite=Def|PronType=Art'), ('meeste', 'Num__Case=Nom|Degree=Sup|NumType=Card|PronType=Ind'), ('inwoners', 'N|soort|mv|neut__Number=Plur'), ('van', 'Prep|voor__AdpType=Prep'), ('Nederland', 'N|eigen|ev|neut__Number=Sing'), (',', 'Punc|komma__PunctType=Comm'), ('België', 'N|eigen|ev|neut__Number=Sing'), ('en', 'Conj|neven___'), ('Suriname', 'N|eigen|ev|neut__Number=Sing'), ('.', 'Punc|punt__PunctType=Peri')]
        assert tokens_tagged_universal == [('Het', 'DET'), ('Nederlands', 'ADJ'), ('is', 'VERB'), ('een', 'DET'), ('West-Germaanse', 'ADJ'), ('taal', 'NOUN'), ('en', 'CONJ'), ('de', 'DET'), ('moedertaal', 'NOUN'), ('van', 'ADP'), ('de', 'DET'), ('meeste', 'NUM'), ('inwoners', 'NOUN'), ('van', 'ADP'), ('Nederland', 'NOUN'), (',', 'PUNCT'), ('België', 'NOUN'), ('en', 'CONJ'), ('Suriname', 'NOUN'), ('.', 'PUNCT')]
    elif lang == 'eng':
        if pos_tagger == 'NLTK - Perceptron POS Tagger':
            assert tokens_tagged == [('English', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('West', 'NNP'), ('Germanic', 'NNP'), ('language', 'NN'), ('that', 'WDT'), ('was', 'VBD'), ('first', 'RB'), ('spoken', 'VBN'), ('in', 'IN'), ('early', 'JJ'), ('medieval', 'NN'), ('England', 'NNP'), ('and', 'CC'), ('eventually', 'RB'), ('became', 'VBD'), ('a', 'DT'), ('global', 'JJ'), ('lingua', 'NN'), ('franca.[5][6', 'NN'), (']', 'NN')]
            assert tokens_tagged_universal == [('English', 'PROPN'), ('is', 'VERB'), ('a', 'DET'), ('West', 'PROPN'), ('Germanic', 'PROPN'), ('language', 'NOUN'), ('that', 'DET'), ('was', 'VERB'), ('first', 'ADV'), ('spoken', 'VERB'), ('in', 'ADP/SCONJ'), ('early', 'ADJ'), ('medieval', 'NOUN'), ('England', 'PROPN'), ('and', 'CCONJ'), ('eventually', 'ADV'), ('became', 'VERB'), ('a', 'DET'), ('global', 'ADJ'), ('lingua', 'NOUN'), ('franca.[5][6', 'NOUN'), (']', 'NOUN')]
        elif pos_tagger == 'spaCy - English POS Tagger':
            assert tokens_tagged == [('English', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('West', 'NNP'), ('Germanic', 'NNP'), ('language', 'NN'), ('that', 'WDT'), ('was', 'VBD'), ('first', 'RB'), ('spoken', 'VBN'), ('in', 'IN'), ('early', 'JJ'), ('medieval', 'JJ'), ('England', 'NNP'), ('and', 'CC'), ('eventually', 'RB'), ('became', 'VBD'), ('a', 'DT'), ('global', 'JJ'), ('lingua', 'FW'), ('franca.[5][6', 'NNP'), (']', '-RRB-')]
            assert tokens_tagged_universal == [('English', 'PROPN'), ('is', 'VERB'), ('a', 'DET'), ('West', 'PROPN'), ('Germanic', 'PROPN'), ('language', 'NOUN'), ('that', 'DET'), ('was', 'VERB'), ('first', 'ADV'), ('spoken', 'VERB'), ('in', 'ADP/SCONJ'), ('early', 'ADJ'), ('medieval', 'ADJ'), ('England', 'PROPN'), ('and', 'CCONJ'), ('eventually', 'ADV'), ('became', 'VERB'), ('a', 'DET'), ('global', 'ADJ'), ('lingua', 'X'), ('franca.[5][6', 'PROPN'), (']', 'PUNCT')]
    elif lang == 'fra':
        assert tokens_tagged == [('Le', 'DET__Definite=Def|Gender=Masc|Number=Sing|PronType=Art'), ('français', 'NOUN__Gender=Masc|Number=Sing'), ('est', 'AUX__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'), ('une', 'DET__Definite=Ind|Gender=Fem|Number=Sing|PronType=Art'), ('langue', 'NOUN__Gender=Fem|Number=Sing'), ('indo-européenne', 'NOUN__Gender=Fem|Number=Sing'), ('de', 'ADP___'), ('la', 'DET__Definite=Def|Gender=Fem|Number=Sing|PronType=Art'), ('famille', 'NOUN__Gender=Fem|Number=Sing'), ('des', 'DET__Definite=Ind|Number=Plur|PronType=Art'), ('langues', 'NOUN__Gender=Fem|Number=Plur'), ('romanes', 'ADJ__Gender=Fem|Number=Plur'), ('.', 'PUNCT___')]
        assert tokens_tagged_universal == [('Le', 'DET'), ('français', 'NOUN'), ('est', 'AUX'), ('une', 'DET'), ('langue', 'NOUN'), ('indo-européenne', 'NOUN'), ('de', 'ADP'), ('la', 'DET'), ('famille', 'NOUN'), ('des', 'DET'), ('langues', 'NOUN'), ('romanes', 'ADJ'), ('.', 'PUNCT')]
    elif lang == 'deu':
        assert tokens_tagged == [('Die', 'ART'), ('deutsche', 'ADJA'), ('Sprache', 'NN'), ('bzw.', 'ADJA'), ('Deutsch', 'NN'), ('(', '$('), ('[', 'NN'), ('dɔʏ̯t͡ʃ', 'NE'), (']', 'NE'), (';', '$.'), ('abgekürzt', 'VVPP'), ('dt', 'NE'), ('.', 'NN'), ('oder', 'KON'), ('dtsch', 'ADJD'), ('.', '$.'), (')', '$('), ('ist', 'VAFIN'), ('eine', 'ART'), ('westgermanische', 'ADJA'), ('Sprache', 'NN'), ('.', '$.')]
        assert tokens_tagged_universal == [('Die', 'DET'), ('deutsche', 'ADJ'), ('Sprache', 'NOUN'), ('bzw.', 'ADJ'), ('Deutsch', 'NOUN'), ('(', 'PUNCT'), ('[', 'NOUN'), ('dɔʏ̯t͡ʃ', 'PROPN'), (']', 'PROPN'), (';', 'PUNCT'), ('abgekürzt', 'VERB'), ('dt', 'PROPN'), ('.', 'NOUN'), ('oder', 'CCONJ'), ('dtsch', 'ADJ'), ('.', 'PUNCT'), (')', 'PUNCT'), ('ist', 'AUX'), ('eine', 'DET'), ('westgermanische', 'ADJ'), ('Sprache', 'NOUN'), ('.', 'PUNCT')]
    elif lang == 'ell':
        assert tokens_tagged == [('Η', 'DET'), ('ελληνική', 'ADJ'), ('γλώσσα', 'NOUN'), ('ανήκει', 'VERB'), ('στην', 'ADJ'), ('ινδοευρωπαϊκή', 'ADJ'), ('οικογένεια[9', 'NOUN'), (']', 'PROPN'), ('και', 'CCONJ'), ('συγκεκριμένα', 'ADV'), ('στον', 'ADV'), ('ελληνικό', 'ADJ'), ('κλάδο', 'NOUN'), (',', 'PUNCT'), ('μαζί', 'ADV'), ('με', 'ADP'), ('την', 'DET'), ('τσακωνική', 'ADJ'), (',', 'PUNCT'), ('ενώ', 'SCONJ'), ('είναι', 'AUX'), ('η', 'DET'), ('επίσημη', 'ADJ'), ('γλώσσα', 'NOUN'), ('της', 'DET'), ('Ελλάδος', 'PROPN'), ('και', 'CCONJ'), ('της', 'DET'), ('Κύπρου', 'PROPN'), ('.', 'PUNCT')]
        assert tokens_tagged_universal == [('Η', 'DET'), ('ελληνική', 'ADJ'), ('γλώσσα', 'NOUN'), ('ανήκει', 'VERB'), ('στην', 'ADJ'), ('ινδοευρωπαϊκή', 'ADJ'), ('οικογένεια[9', 'NOUN'), (']', 'PROPN'), ('και', 'CCONJ'), ('συγκεκριμένα', 'ADV'), ('στον', 'ADV'), ('ελληνικό', 'ADJ'), ('κλάδο', 'NOUN'), (',', 'PUNCT'), ('μαζί', 'ADV'), ('με', 'ADP'), ('την', 'DET'), ('τσακωνική', 'ADJ'), (',', 'PUNCT'), ('ενώ', 'SCONJ'), ('είναι', 'AUX'), ('η', 'DET'), ('επίσημη', 'ADJ'), ('γλώσσα', 'NOUN'), ('της', 'DET'), ('Ελλάδος', 'PROPN'), ('και', 'CCONJ'), ('της', 'DET'), ('Κύπρου', 'PROPN'), ('.', 'PUNCT')]
    elif lang == 'ita':
        assert tokens_tagged == [("L'", 'RD__Definite=Def|Number=Sing|PronType=Art'), ('italiano', 'S__Gender=Masc|Number=Sing'), ('(', 'FB___'), ('[', 'FB___'), ('itaˈljaːno][Nota', 'V__Mood=Imp|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin'), ('1', 'N__NumType=Card'), (']', 'FB___'), ('ascolta[?·info', 'S___'), (']', 'FB___'), (')', 'FB___'), ('è', 'V__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'), ('una', 'RI__Definite=Ind|Gender=Fem|Number=Sing|PronType=Art'), ('lingua', 'S__Gender=Fem|Number=Sing'), ('romanza', 'S__Gender=Fem|Number=Sing'), ('parlata', 'V__Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part'), ('principalmente', 'B___'), ('in', 'E___'), ('Italia', 'SP___'), ('.', 'FS___')]
        assert tokens_tagged_universal == [("L'", 'DET'), ('italiano', 'NOUN'), ('(', 'PUNCT'), ('[', 'PUNCT'), ('itaˈljaːno][Nota', 'VERB'), ('1', 'NUM'), (']', 'PUNCT'), ('ascolta[?·info', 'NOUN'), (']', 'PUNCT'), (')', 'PUNCT'), ('è', 'VERB'), ('una', 'DET'), ('lingua', 'NOUN'), ('romanza', 'NOUN'), ('parlata', 'VERB'), ('principalmente', 'ADV'), ('in', 'ADP'), ('Italia', 'PROPN'), ('.', 'PUNCT')]
    elif lang == 'jpn':
        assert tokens_tagged == [('日本', '名詞'), ('語', '名詞'), ('(', '補助記号'), ('にほんご', '名詞'), ('、', '補助記号'), ('にっぽん', '名詞'), ('ご', '接尾辞'), ('[', '補助記号'), ('注', '名詞'), ('1', '名詞'), (']', '補助記号'), (')', '補助記号'), ('は', '助詞'), ('、', '補助記号'), ('主に', '副詞'), ('日本', '名詞'), ('国', '接尾辞'), ('内', '接尾辞'), ('や', '助詞'), ('日本', '名詞'), ('人', '接尾辞'), ('同士', '接尾辞'), ('の', '助詞'), ('間', '名詞'), ('で', '助詞'), ('使用', '名詞'), ('さ', '動詞'), ('れ', '助動詞'), ('て', '助詞'), ('いる', '動詞'), ('言語', '名詞'), ('で', '助動詞'), ('ある', '動詞'), ('。', '補助記号')]
        assert tokens_tagged_universal == [('日本', 'NOUN'), ('語', 'NOUN'), ('(', 'PUNCT/SYM'), ('にほんご', 'NOUN'), ('、', 'PUNCT/SYM'), ('にっぽん', 'NOUN'), ('ご', 'PART'), ('[', 'PUNCT/SYM'), ('注', 'NOUN'), ('1', 'NOUN'), (']', 'PUNCT/SYM'), (')', 'PUNCT/SYM'), ('は', 'PART'), ('、', 'PUNCT/SYM'), ('主に', 'ADV'), ('日本', 'NOUN'), ('国', 'PART'), ('内', 'PART'), ('や', 'PART'), ('日本', 'NOUN'), ('人', 'PART'), ('同士', 'PART'), ('の', 'PART'), ('間', 'NOUN'), ('で', 'PART'), ('使用', 'NOUN'), ('さ', 'VERB'), ('れ', 'AUX'), ('て', 'PART'), ('いる', 'VERB'), ('言語', 'NOUN'), ('で', 'AUX'), ('ある', 'VERB'), ('。', 'PUNCT/SYM')]
    elif lang == 'por':
        assert tokens_tagged == [('A', '<artd>|ART|F|S|@>N'), ('língua', '<np-def>|N|F|S|@SUBJ>'), ('portuguesa', 'ADJ|F|S|@N<'), (',', 'PU|@PU'), ('também', 'ADV|@ADVL>'), ('designada', '<mv>|V|PCP|F|S|@ICL-N<PRED'), ('português', '<np-idf>|N|M|S|@<SUBJ'), (',', 'PU|@PU'), ('é', '<mv>|V|PR|3S|IND|@FS-STA'), ('uma', '<arti>|ART|F|S|@>N'), ('língua', '<np-idf>|N|F|S|@<SC'), ('românica', 'ADJ|F|S|@N<'), ('flexiva', 'ADJ|F|S|@N<'), ('ocidental', 'ADJ|F|S|@N<'), ('originada', '<mv>|V|PCP|F|S|@ICL-N<'), ('no', '<artd>|ART|M|P|@>N'), ('galego-português', '<np-idf>|N|F|S|@P<'), ('falado', '<mv>|V|PCP|M|S|@ICL-N<'), ('no', 'PROPN'), ('Reino', 'PROPN'), ('da', 'ADP'), ('Galiza', 'PROP|@P<'), ('e', '<co-prparg>|KC|@CO'), ('no', 'PROP|@N<'), ('norte', '<np-idf>|N|M|S|@P<'), ('de', 'PRP|@N<'), ('Portugal', 'PROP|M|S|@P<'), ('.', 'PU|@PU')]
        assert tokens_tagged_universal == [('A', 'DET'), ('língua', 'NOUN'), ('portuguesa', 'ADJ'), (',', 'PUNCT'), ('também', 'ADV'), ('designada', 'VERB'), ('português', 'NOUN'), (',', 'PUNCT'), ('é', 'VERB'), ('uma', 'DET'), ('língua', 'NOUN'), ('românica', 'ADJ'), ('flexiva', 'ADJ'), ('ocidental', 'ADJ'), ('originada', 'VERB'), ('no', 'DET'), ('galego-português', 'NOUN'), ('falado', 'VERB'), ('no', 'PROPN'), ('Reino', 'PROPN'), ('da', 'ADP'), ('Galiza', 'PROPN'), ('e', 'CCONJ'), ('no', 'PROPN'), ('norte', 'NOUN'), ('de', 'ADP'), ('Portugal', 'PROPN'), ('.', 'PUNCT')]
    elif lang == 'rus':
        if pos_tagger == 'NLTK - Perceptron POS Tagger':
            assert tokens_tagged == [('Ру́сский', 'A=m'), ('язы́к', 'S'), ('(', 'NONLEX'), ('[', 'NONLEX'), ('ˈruskʲɪi̯', 'NONLEX'), ('jɪˈzɨk', 'NONLEX'), (']', 'NONLEX'), ('Информация', 'S'), ('о', 'PR'), ('файле', 'S'), ('слушать', 'V'), (')', 'NONLEX'), ('[', 'NONLEX'), ('~', 'NONLEX'), ('3', 'NUM=ciph'), (']', 'NONLEX'), ('[', 'NONLEX'), ('⇨', 'NONLEX'), (']', 'NONLEX'), ('—', 'NONLEX'), ('один', 'A-PRO=m'), ('из', 'PR'), ('восточнославянских', 'A=pl'), ('языков', 'S'), (',', 'NONLEX'), ('национальный', 'A=m'), ('язык', 'S'), ('русского', 'A=m'), ('народа', 'S'), ('.', 'NONLEX')]
            assert tokens_tagged_universal == [('Ру́сский', 'ADJ'), ('язы́к', 'NOUN'), ('(', 'PUNCT'), ('[', 'PUNCT'), ('ˈruskʲɪi̯', 'PUNCT'), ('jɪˈzɨk', 'PUNCT'), (']', 'PUNCT'), ('Информация', 'NOUN'), ('о', 'ADP'), ('файле', 'NOUN'), ('слушать', 'VERB'), (')', 'PUNCT'), ('[', 'PUNCT'), ('~', 'PUNCT'), ('3', 'NUM'), (']', 'PUNCT'), ('[', 'PUNCT'), ('⇨', 'PUNCT'), (']', 'PUNCT'), ('—', 'PUNCT'), ('один', 'PRON'), ('из', 'ADP'), ('восточнославянских', 'ADJ'), ('языков', 'NOUN'), (',', 'PUNCT'), ('национальный', 'ADJ'), ('язык', 'NOUN'), ('русского', 'ADJ'), ('народа', 'NOUN'), ('.', 'PUNCT')]
        elif pos_tagger == 'pymorphy2 - Morphological Analyzer':
            assert tokens_tagged == [('Ру́сский', 'NOUN'), ('язы́к', 'NOUN'), ('(', 'PNCT'), ('[', 'PNCT'), ('ˈruskʲɪi̯', 'UNKN'), ('jɪˈzɨk', 'UNKN'), (']', 'PNCT'), ('Информация', 'NOUN'), ('о', 'PREP'), ('файле', 'NOUN'), ('слушать', 'INFN'), (')', 'PNCT'), ('[', 'PNCT'), ('~', 'UNKN'), ('3', 'NUMB'), (']', 'PNCT'), ('[', 'PNCT'), ('⇨', 'UNKN'), (']', 'PNCT'), ('—', 'PNCT'), ('один', 'ADJF'), ('из', 'PREP'), ('восточнославянских', 'ADJF'), ('языков', 'NOUN'), (',', 'PNCT'), ('национальный', 'ADJF'), ('язык', 'NOUN'), ('русского', 'ADJF'), ('народа', 'NOUN'), ('.', 'PNCT')]
            assert tokens_tagged_universal == [('Ру́сский', 'NOUN'), ('язы́к', 'NOUN'), ('(', 'PUNCT'), ('[', 'PUNCT'), ('ˈruskʲɪi̯', 'SYM/X'), ('jɪˈzɨk', 'SYM/X'), (']', 'PUNCT'), ('Информация', 'NOUN'), ('о', 'ADP'), ('файле', 'NOUN'), ('слушать', 'VERB'), (')', 'PUNCT'), ('[', 'PUNCT'), ('~', 'SYM/X'), ('3', 'NUM'), (']', 'PUNCT'), ('[', 'PUNCT'), ('⇨', 'SYM/X'), (']', 'PUNCT'), ('—', 'PUNCT'), ('один', 'ADJ'), ('из', 'ADP'), ('восточнославянских', 'ADJ'), ('языков', 'NOUN'), (',', 'PUNCT'), ('национальный', 'ADJ'), ('язык', 'NOUN'), ('русского', 'ADJ'), ('народа', 'NOUN'), ('.', 'PUNCT')]
    elif lang == 'spa':
        assert tokens_tagged == [('El', 'DET__Definite=Def|Gender=Masc|Number=Sing|PronType=Art'), ('español', 'NOUN__Gender=Masc|Number=Sing'), ('o', 'CCONJ___'), ('castellano', 'NOUN__Gender=Masc|Number=Sing'), ('es', 'AUX__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin'), ('una', 'DET__Definite=Ind|Gender=Fem|Number=Sing|PronType=Art'), ('lengua', 'NOUN__Gender=Fem|Number=Sing'), ('romance', 'NOUN__Gender=Masc|Number=Sing'), ('procedente', 'ADJ__Number=Sing'), ('del', 'ADP__AdpType=Preppron|Gender=Masc|Number=Sing'), ('latín', 'NOUN__Gender=Masc|Number=Sing'), ('hablado', 'ADJ__Gender=Masc|Number=Sing|VerbForm=Part'), ('.', 'PUNCT__PunctType=Peri')]
        assert tokens_tagged_universal == [('El', 'DET'), ('español', 'NOUN'), ('o', 'CCONJ'), ('castellano', 'NOUN'), ('es', 'AUX'), ('una', 'DET'), ('lengua', 'NOUN'), ('romance', 'NOUN'), ('procedente', 'ADJ'), ('del', 'ADP'), ('latín', 'NOUN'), ('hablado', 'ADJ'), ('.', 'PUNCT')]
    elif lang == 'tha':
        if pos_tagger == 'PyThaiNLP - Perceptron POS Tagger - ORCHID Corpus':
            assert tokens_tagged == [('ภาษาไทย', 'NPRP'), ('หรือ', 'JCRG'), ('ภาษาไทย', 'NPRP'), ('กลาง', 'VATT'), ('เป็น', 'VSTA'), ('ภาษาราชการ', 'NCMN'), ('และ', 'JCRG'), ('ภาษาประจำชาติ', 'NCMN'), ('ของ', 'RPRE'), ('ประเทศไทย', 'NPRP')]
            assert tokens_tagged_universal == [('ภาษาไทย', 'PROPN'), ('หรือ', 'CCONJ'), ('ภาษาไทย', 'PROPN'), ('กลาง', 'VERB'), ('เป็น', 'VERB'), ('ภาษาราชการ', 'NOUN'), ('และ', 'CCONJ'), ('ภาษาประจำชาติ', 'NOUN'), ('ของ', 'ADP'), ('ประเทศไทย', 'PROPN')]
        elif pos_tagger == 'PyThaiNLP - Perceptron POS Tagger - PUD Corpus':
            assert tokens_tagged == [('ภาษาไทย', 'NOUN'), ('หรือ', 'CCONJ'), ('ภาษาไทย', 'NOUN'), ('กลาง', 'NOUN'), ('เป็น', 'AUX'), ('ภาษาราชการ', 'NOUN'), ('และ', 'CCONJ'), ('ภาษาประจำชาติ', 'NOUN'), ('ของ', 'ADP'), ('ประเทศไทย', 'PROPN')]
            assert tokens_tagged_universal == [('ภาษาไทย', 'NOUN'), ('หรือ', 'CCONJ'), ('ภาษาไทย', 'NOUN'), ('กลาง', 'NOUN'), ('เป็น', 'AUX'), ('ภาษาราชการ', 'NOUN'), ('และ', 'CCONJ'), ('ภาษาประจำชาติ', 'NOUN'), ('ของ', 'ADP'), ('ประเทศไทย', 'PROPN')]
    elif lang == 'bod':
        assert tokens_tagged == [('༄༅། །', 'PUNCT'), ('རྒྱ་གར་', 'PROPN'), ('སྐད་', 'VERB'), ('དུ', 'ADP'), ('།', 'PUNCT'), ('བོ་', 'PART'), ('དྷི་', 'NON_WORD'), ('སཏྭ་', 'NON_WORD'), ('ཙརྻ་', 'NON_WORD'), ('ཨ་བ་', 'OOV'), ('ཏ་', 'OTHER'), ('ར', 'ADP'), ('།', 'PUNCT'), ('བོད་སྐད་', 'PROPN'), ('དུ', 'ADP'), ('།', 'PUNCT'), ('བྱང་ཆུབ་', 'NOUN'), ('སེམས་དཔ', 'NOUN'), ('འི་', 'PART'), ('སྤྱོད་པ་', 'VERB'), ('ལ་', 'ADP'), ('འཇུག་པ', 'VERB'), ('། །', 'PUNCT'), ('སངས་རྒྱས་', 'NOUN'), ('དང་', 'ADP'), ('བྱང་ཆུབ་', 'NOUN'), ('སེམས་དཔའ་', 'NOUN'), ('ཐམས་ཅད་', 'DET'), ('ལ་', 'ADP'), ('ཕྱག་', 'NOUN'), ('འཚལ་', 'VERB'), ('ལོ', 'PART'), ('། །', 'PUNCT'), ('བདེ་གཤེགས་', 'NOUN'), ('ཆོས་', 'NOUN'), ('ཀྱི་', 'ADP'), ('སྐུ་', 'NOUN'), ('མངའ་', 'VERB'), ('སྲས་', 'NOUN'), ('བཅས་', 'VERB'), ('དང༌', 'ADP'), ('། །', 'PUNCT'), ('ཕྱག་འོས་', 'OOV'), ('ཀུན་', 'DET'), ('ལ', 'ADP'), ('འང་', 'PART'), ('གུས་པ', 'VERB'), ('ར་', 'PART'), ('ཕྱག་', 'NOUN'), ('འཚལ་', 'VERB'), ('ཏེ', 'SCONJ'), ('། །', 'PUNCT'), ('བདེ་གཤེགས་', 'NOUN'), ('སྲས་', 'NOUN'), ('ཀྱི་', 'ADP'), ('སྡོམ་', 'NOUN'), ('ལ་', 'ADP'), ('འཇུག་པ་', 'VERB'), ('ནི', 'PART'), ('། །', 'PUNCT'), ('ལུང་', 'NOUN'), ('བཞིན་', 'NOUN'), ('མདོར་བསྡུས་', 'ADJ'), ('ནས་', 'SCONJ'), ('ནི་', 'PART'), ('བརྗོད་པ', 'VERB'), ('ར་', 'PART'), ('བྱ', 'VERB'), ('། །', 'PUNCT')]
        assert tokens_tagged_universal == [('༄༅། །', 'PUNCT'), ('རྒྱ་གར་', 'PROPN'), ('སྐད་', 'VERB'), ('དུ', 'ADP'), ('།', 'PUNCT'), ('བོ་', 'PART'), ('དྷི་', 'X'), ('སཏྭ་', 'X'), ('ཙརྻ་', 'X'), ('ཨ་བ་', 'X'), ('ཏ་', 'X'), ('ར', 'ADP'), ('།', 'PUNCT'), ('བོད་སྐད་', 'PROPN'), ('དུ', 'ADP'), ('།', 'PUNCT'), ('བྱང་ཆུབ་', 'NOUN'), ('སེམས་དཔ', 'NOUN'), ('འི་', 'PART'), ('སྤྱོད་པ་', 'VERB'), ('ལ་', 'ADP'), ('འཇུག་པ', 'VERB'), ('། །', 'PUNCT'), ('སངས་རྒྱས་', 'NOUN'), ('དང་', 'ADP'), ('བྱང་ཆུབ་', 'NOUN'), ('སེམས་དཔའ་', 'NOUN'), ('ཐམས་ཅད་', 'DET'), ('ལ་', 'ADP'), ('ཕྱག་', 'NOUN'), ('འཚལ་', 'VERB'), ('ལོ', 'PART'), ('། །', 'PUNCT'), ('བདེ་གཤེགས་', 'NOUN'), ('ཆོས་', 'NOUN'), ('ཀྱི་', 'ADP'), ('སྐུ་', 'NOUN'), ('མངའ་', 'VERB'), ('སྲས་', 'NOUN'), ('བཅས་', 'VERB'), ('དང༌', 'ADP'), ('། །', 'PUNCT'), ('ཕྱག་འོས་', 'X'), ('ཀུན་', 'DET'), ('ལ', 'ADP'), ('འང་', 'PART'), ('གུས་པ', 'VERB'), ('ར་', 'PART'), ('ཕྱག་', 'NOUN'), ('འཚལ་', 'VERB'), ('ཏེ', 'SCONJ'), ('། །', 'PUNCT'), ('བདེ་གཤེགས་', 'NOUN'), ('སྲས་', 'NOUN'), ('ཀྱི་', 'ADP'), ('སྡོམ་', 'NOUN'), ('ལ་', 'ADP'), ('འཇུག་པ་', 'VERB'), ('ནི', 'PART'), ('། །', 'PUNCT'), ('ལུང་', 'NOUN'), ('བཞིན་', 'NOUN'), ('མདོར་བསྡུས་', 'ADJ'), ('ནས་', 'SCONJ'), ('ནི་', 'PART'), ('བརྗོད་པ', 'VERB'), ('ར་', 'PART'), ('བྱ', 'VERB'), ('། །', 'PUNCT')]
    elif lang == 'ukr':
        assert tokens_tagged == [('Украї́нська', 'ADJF'), ('мо́ва', 'ADJF'), ('(', 'PNCT'), ('МФА', 'UNKN'), (':', 'PNCT'), ('[', 'PNCT'), ('ukrɑ̽ˈjɪnʲsʲkɑ̽', 'UNKN'), ('ˈmɔwɑ̽', 'UNKN'), (']', 'PNCT'), (',', 'PNCT'), ('історичні', 'ADJF'), ('назви', 'NOUN'), ('—', 'PNCT'), ('ру́ська', 'ADJF'), (',', 'PNCT'), ('руси́нська[9][10][11', 'UNKN'), (']', 'PNCT'), ('[', 'PNCT'), ('*', 'PNCT'), ('2', 'NUMB'), (']', 'PNCT'), (')', 'PNCT'), ('—', 'PNCT'), ('національна', 'ADJF'), ('мова', 'NOUN'), ('українців', 'NOUN'), ('.', 'PNCT')]
        assert tokens_tagged_universal == [('Украї́нська', 'ADJ'), ('мо́ва', 'ADJ'), ('(', 'PUNCT'), ('МФА', 'SYM/X'), (':', 'PUNCT'), ('[', 'PUNCT'), ('ukrɑ̽ˈjɪnʲsʲkɑ̽', 'SYM/X'), ('ˈmɔwɑ̽', 'SYM/X'), (']', 'PUNCT'), (',', 'PUNCT'), ('історичні', 'ADJ'), ('назви', 'NOUN'), ('—', 'PUNCT'), ('ру́ська', 'ADJ'), (',', 'PUNCT'), ('руси́нська[9][10][11', 'SYM/X'), (']', 'PUNCT'), ('[', 'PUNCT'), ('*', 'PUNCT'), ('2', 'NUM'), (']', 'PUNCT'), (')', 'PUNCT'), ('—', 'PUNCT'), ('національна', 'ADJ'), ('мова', 'NOUN'), ('українців', 'NOUN'), ('.', 'PUNCT')]
    elif lang == 'vie':
        assert tokens_tagged == [('Tiếng', 'N'), ('Việt', 'Np'), (',', 'CH'), ('còn', 'C'), ('gọi', 'V'), ('tiếng', 'N'), ('Việt Nam', 'Np'), ('[', 'V'), ('5', 'M'), (']', 'CH'), (',', 'CH'), ('tiếng Kinh', 'N'), ('hay', 'C'), ('Việt ngữ', 'V'), (',', 'CH'), ('là', 'V'), ('ngôn ngữ', 'N'), ('của', 'E'), ('người', 'Nc'), ('Việt', 'Np'), ('(', 'CH'), ('dân tộc', 'N'), ('Kinh', 'Np'), (')', 'CH'), ('và', 'C'), ('là', 'V'), ('ngôn ngữ', 'N'), ('chính thức', 'A'), ('tại', 'E'), ('Việt Nam', 'Np'), ('.', 'CH')]
        assert tokens_tagged_universal == [('Tiếng', 'NOUN'), ('Việt', 'PROPN'), (',', 'PUNCT'), ('còn', 'CCONJ'), ('gọi', 'VERB'), ('tiếng', 'NOUN'), ('Việt Nam', 'PROPN'), ('[', 'VERB'), ('5', 'NUM'), (']', 'PUNCT'), (',', 'PUNCT'), ('tiếng Kinh', 'NOUN'), ('hay', 'CCONJ'), ('Việt ngữ', 'VERB'), (',', 'PUNCT'), ('là', 'VERB'), ('ngôn ngữ', 'NOUN'), ('của', 'ADP'), ('người', 'NOUN'), ('Việt', 'PROPN'), ('(', 'PUNCT'), ('dân tộc', 'NOUN'), ('Kinh', 'PROPN'), (')', 'PUNCT'), ('và', 'CCONJ'), ('là', 'VERB'), ('ngôn ngữ', 'NOUN'), ('chính thức', 'ADJ'), ('tại', 'ADP'), ('Việt Nam', 'PROPN'), ('.', 'PUNCT')]

'''
for lang, pos_taggers in main.settings_global['pos_taggers'].items():
    for pos_tagger in pos_taggers:
        if lang not in ['bod']:
            test_pos_tag(lang, pos_tagger)
'''
