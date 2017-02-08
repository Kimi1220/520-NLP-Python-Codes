Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 15:51:26) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import nltk
ImportError: No module named 'nltk'
>>> import nltk
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> nltk.help.upenn_tagset()
$: dollar
    $ -$ --$ A$ C$ HK$ M$ NZ$ S$ U.S.$ US$
'': closing quotation mark
    ' ''
(: opening parenthesis
    ( [ {
): closing parenthesis
    ) ] }
,: comma
    ,
--: dash
    --
.: sentence terminator
    . ! ?
:: colon or ellipsis
    : ; ...
CC: conjunction, coordinating
    & 'n and both but either et for less minus neither nor or plus so
    therefore times v. versus vs. whether yet
CD: numeral, cardinal
    mid-1890 nine-thirty forty-two one-tenth ten million 0.5 one forty-
    seven 1987 twenty '79 zero two 78-degrees eighty-four IX '60s .025
    fifteen 271,124 dozen quintillion DM2,000 ...
DT: determiner
    all an another any both del each either every half la many much nary
    neither no some such that the them these this those
EX: existential there
    there
FW: foreign word
    gemeinschaft hund ich jeux habeas Haementeria Herr K'ang-si vous
    lutihaw alai je jour objets salutaris fille quibusdam pas trop Monte
    terram fiche oui corporis ...
IN: preposition or conjunction, subordinating
    astride among uppon whether out inside pro despite on by throughout
    below within for towards near behind atop around if like until below
    next into if beside ...
JJ: adjective or numeral, ordinal
    third ill-mannered pre-war regrettable oiled calamitous first separable
    ectoplasmic battery-powered participatory fourth still-to-be-named
    multilingual multi-disciplinary ...
JJR: adjective, comparative
    bleaker braver breezier briefer brighter brisker broader bumper busier
    calmer cheaper choosier cleaner clearer closer colder commoner costlier
    cozier creamier crunchier cuter ...
JJS: adjective, superlative
    calmest cheapest choicest classiest cleanest clearest closest commonest
    corniest costliest crassest creepiest crudest cutest darkest deadliest
    dearest deepest densest dinkiest ...
LS: list item marker
    A A. B B. C C. D E F First G H I J K One SP-44001 SP-44002 SP-44005
    SP-44007 Second Third Three Two * a b c d first five four one six three
    two
MD: modal auxiliary
    can cannot could couldn't dare may might must need ought shall should
    shouldn't will would
NN: noun, common, singular or mass
    common-carrier cabbage knuckle-duster Casino afghan shed thermostat
    investment slide humour falloff slick wind hyena override subhumanity
    machinist ...
NNP: noun, proper, singular
    Motown Venneboerger Czestochwa Ranzer Conchita Trumplane Christos
    Oceanside Escobar Kreisler Sawyer Cougar Yvette Ervin ODI Darryl CTCA
    Shannon A.K.C. Meltex Liverpool ...
NNPS: noun, proper, plural
    Americans Americas Amharas Amityvilles Amusements Anarcho-Syndicalists
    Andalusians Andes Andruses Angels Animals Anthony Antilles Antiques
    Apache Apaches Apocrypha ...
NNS: noun, common, plural
    undergraduates scotches bric-a-brac products bodyguards facets coasts
    divestitures storehouses designs clubs fragrances averages
    subjectivists apprehensions muses factory-jobs ...
PDT: pre-determiner
    all both half many quite such sure this
POS: genitive marker
    ' 's
PRP: pronoun, personal
    hers herself him himself hisself it itself me myself one oneself ours
    ourselves ownself self she thee theirs them themselves they thou thy us
PRP$: pronoun, possessive
    her his mine my our ours their thy your
RB: adverb
    occasionally unabatingly maddeningly adventurously professedly
    stirringly prominently technologically magisterially predominately
    swiftly fiscally pitilessly ...
RBR: adverb, comparative
    further gloomier grander graver greater grimmer harder harsher
    healthier heavier higher however larger later leaner lengthier less-
    perfectly lesser lonelier longer louder lower more ...
RBS: adverb, superlative
    best biggest bluntest earliest farthest first furthest hardest
    heartiest highest largest least less most nearest second tightest worst
RP: particle
    aboard about across along apart around aside at away back before behind
    by crop down ever fast for forth from go high i.e. in into just later
    low more off on open out over per pie raising start teeth that through
    under unto up up-pp upon whole with you
SYM: symbol
    % & ' '' ''. ) ). * + ,. < = > @ A[fj] U.S U.S.S.R * ** ***
TO: "to" as preposition or infinitive marker
    to
UH: interjection
    Goodbye Goody Gosh Wow Jeepers Jee-sus Hubba Hey Kee-reist Oops amen
    huh howdy uh dammit whammo shucks heck anyways whodunnit honey golly
    man baby diddle hush sonuvabitch ...
VB: verb, base form
    ask assemble assess assign assume atone attention avoid bake balkanize
    bank begin behold believe bend benefit bevel beware bless boil bomb
    boost brace break bring broil brush build ...
VBD: verb, past tense
    dipped pleaded swiped regummed soaked tidied convened halted registered
    cushioned exacted snubbed strode aimed adopted belied figgered
    speculated wore appreciated contemplated ...
VBG: verb, present participle or gerund
    telegraphing stirring focusing angering judging stalling lactating
    hankerin' alleging veering capping approaching traveling besieging
    encrypting interrupting erasing wincing ...
VBN: verb, past participle
    multihulled dilapidated aerosolized chaired languished panelized used
    experimented flourished imitated reunifed factored condensed sheared
    unsettled primed dubbed desired ...
VBP: verb, present tense, not 3rd person singular
    predominate wrap resort sue twist spill cure lengthen brush terminate
    appear tend stray glisten obtain comprise detest tease attract
    emphasize mold postpone sever return wag ...
VBZ: verb, present tense, 3rd person singular
    bases reconstructs marks mixes displeases seals carps weaves snatches
    slumps stretches authorizes smolders pictures emerges stockpiles
    seduces fizzes uses bolsters slaps speaks pleads ...
WDT: WH-determiner
    that what whatever which whichever
WP: WH-pronoun
    that what whatever whatsoever which who whom whosoever
WP$: WH-pronoun, possessive
    whose
WRB: Wh-adverb
    how however whence whenever where whereby whereever wherein whereof why
``: opening quotation mark
    ` ``
>>> 
>>> text = word_tokenize("They wind back the clock, while we chase after the wind.")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text = word_tokenize("They wind back the clock, while we chase after the wind.")
NameError: name 'word_tokenize' is not defined
>>> 
>>> import nltk
>>> text = word_tokenize("They wind back the clock, while we chase after the wind.")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    text = word_tokenize("They wind back the clock, while we chase after the wind.")
NameError: name 'word_tokenize' is not defined
>>> 
>>> 
>>> from nltk import pos_tag, word_tokenize
>>> text = word_tokenize("They wind back the clock, while we chase after the wind.")
>>> nltk.pos_tag(text)
[('They', 'PRP'), ('wind', 'VBP'), ('back', 'RB'), ('the', 'DT'), ('clock', 'NN'), (',', ','), ('while', 'IN'), ('we', 'PRP'), ('chase', 'VBP'), ('after', 'IN'), ('the', 'DT'), ('wind', 'NN'), ('.', '.')]
>>> 
>>> d={}
>>> d
{}
>>> d['we'] = 'Noun'
>>> d['do'] = 'Verb'
>>> d['sports'] = 'Noun'
>>> d['we'] = 'Pronoun'
>>> d
{'we': 'Pronoun', 'do': 'Verb', 'sports': 'Noun'}
>>> d['do']
'Verb'
>>> d['xyz']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d['xyz']
KeyError: 'xyz'
>>> list(d)
['we', 'do', 'sports']
>>> list(d.keys())
['we', 'do', 'sports']
>>> list(d,values())
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list(d,values())
NameError: name 'values' is not defined
>>> list(d.values())
['Pronoun', 'Verb', 'Noun']
>>> list(d.items())
[('we', 'Pronoun'), ('do', 'Verb'), ('sports', 'Noun')]
>>> for key,value in sorted(d.items()):
	print (key + ":" + values)

	
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    print (key + ":" + values)
NameError: name 'values' is not defined
>>> for key,value in sorted(d.items()):
	print (key + ":" + value)

	
do:Verb
sports:Noun
we:Pronoun
>>> 
>>> d = {'abc':'noun', 'def':'pronoun'}
>>> del d['abc']
>>> d
{'def': 'pronoun'}
>>> d1 = {'we':'}
      
SyntaxError: EOL while scanning string literal
>>> 
>>> d1 = {'we': 'pronoun', 'love':'verb', 'python':'noun'}
>>> d1
{'we': 'pronoun', 'python': 'noun', 'love': 'verb'}
>>> d2 = {'python':'noun', 'is':'copula', 'hard':'adjective'}
>>> d2
{'is': 'copula', 'hard': 'adjective', 'python': 'noun'}
>>> d1.update(d2)
>>> d1
{'is': 'copula', 'we': 'pronoun', 'python': 'noun', 'love': 'verb', 'hard': 'adjective'}
>>> 
>>> from nltk.corpus import wordnet
>>> wordnet.categories
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    wordnet.categories
  File "C:\Users\yyang\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\corpus\util.py", line 119, in __getattr__
    return getattr(self, attr)
AttributeError: 'WordNetCorpusReader' object has no attribute 'categories'
>>> wordnet
<WordNetCorpusReader in 'C:\\Users\\yyang\\AppData\\Roaming\\nltk_data\\corpora\\wordnet'>
>>> from nltk.corpus import brown
>>> brown.categories
<bound method CategorizedCorpusReader.categories of <CategorizedTaggedCorpusReader in 'C:\\Users\\yyang\\AppData\\Roaming\\nltk_data\\corpora\\brown'>>
>>> brown.categories[:10
		 ]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    brown.categories[:10
TypeError: 'method' object is not subscriptable
>>> brown.categories()
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
>>> 
>>> from nltk.corpus import brown
>>> brown.categories()
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
>>> brown_tagger = brown.tagged_sents(categories = "adventure")
>>> brown_sents = brown.sents(categories = "adventure")
>>> size = int(len(brown.tagger)*0.9)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    size = int(len(brown.tagger)*0.9)
AttributeError: 'CategorizedTaggedCorpusReader' object has no attribute 'tagger'
>>> size = int(len(brown_tagger)*0.9)
>>> size
4173
>>> brown_train = brown_sents[:size}
SyntaxError: invalid syntax
>>> brown_train = brown_sents[:size]
>>> brown_test =brown_sents[size:]
>>> unigram_tagger = nltk.UnigramTagger(brown_train)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    unigram_tagger = nltk.UnigramTagger(brown_train)
  File "C:\Users\yyang\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\tag\sequential.py", line 340, in __init__
    backoff, cutoff, verbose)
  File "C:\Users\yyang\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\tag\sequential.py", line 287, in __init__
    self._train(train, cutoff, verbose)
  File "C:\Users\yyang\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\tag\sequential.py", line 178, in _train
    tokens, tags = zip(*sentence)
ValueError: not enough values to unpack (expected 2, got 1)
>>> 
>>> 
>>> from nltk.corpus import brown
>>> brown.categories()
['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
>>> brown_tagged_sents = brown.tagged_sents(categories = "adventure")
>>> size = int(len(brown_tagger)*0.9)
>>> size
4173
>>> brown_train = brown_tagged_sents[:size]
>>> brown_test =brown_tagged_sents[size:]
>>> unigram_tagger = nltk.UnigramTagger(brown_train)
>>> unigram_tagger.evaluate(brown_test)
0.8117068117068117
>>> unigram_tagger.tag(brown.test[100])
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    unigram_tagger.tag(brown.test[100])
AttributeError: 'CategorizedTaggedCorpusReader' object has no attribute 'test'
>>> unigram_tagger.tag(brown_test[100])
[(('``', '``'), None), (('Time', 'NN'), None), (('for', 'IN'), None), (('books', 'NNS'), None), (("''", "''"), None), ((',', ','), None), (('she', 'PPS'), None), (('yelled', 'VBD'), None), ((',', ','), None), (('jingling', 'VBG'), None), (('a', 'AT'), None), (('little', 'AP'), None), (('five-and-dime', 'NN'), None), (('store', 'NN'), None), (('bell', 'NN'), None), (('in', 'IN'), None), (('her', 'PP$'), None), (('right', 'JJ'), None), (('hand', 'NN'), None), (('.', '.'), None)]
>>> 
