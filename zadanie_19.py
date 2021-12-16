def policz_znaki(text, start="<", end=">"):
    licznik = 0
    poziom = 0

    for znak in text:
        if znak == start:
            poziom += 1
        elif znak == end:
            poziom -= 1
        else:
            licznik += poziom

    return licznik


def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('a <a<a<a>>>') == 6
    assert policz_znaki('a <a<a<a>>>', "(", ")") == 0
    assert policz_znaki("<a>") == 1
    assert policz_znaki("<<a>>") == 2
    assert policz_znaki("<<a>a>") == 3