from cesar.cesar import encripta


def test_encripta_eduardo_retorna_rqhneqb():
    assert encripta("eduardo") == "rqhneqb"


def test_encripta_eduardo_retorna_eduardo():
    assert encripta("rqhneqb") == "eduardo"


def test_encripta_deve_retornar_minusculas():
    assert encripta("A").islower()


def test_encripta_deve_preservar_os_espacos():
    resultado = encripta("e a")
    assert resultado[1] == " "
