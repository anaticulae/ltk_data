import nltk.classify.textcat


def test_textcat():
    textcat = nltk.classify.textcat.TextCat()
    result = textcat.guess_language('Hier wohnt ein Mensch')
    assert result == 'deu'
