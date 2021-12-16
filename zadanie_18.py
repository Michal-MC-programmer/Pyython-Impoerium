def wiecej_niz(text: str, prog: int) -> set:
    """Zwraca zbior znakow wystepujacych w text wiece niz prog razy
    >> wiecej_niz("", 4)
    {}
    """
    result = set()
    for znak in set(text):
        if text.count(znak) > prog:
            result.add(znak)
    return result


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 4) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaa", 1) == {"a"}

