from Element import element, repr 

class First(repr):
    name = element()
    value = element()

    def __init__(self, name: str = None, value: float = None):
        self.name = name
        self.value = value


def test_XML():
    first = First('first', 1024)
    assert first.name == '<name>first</name>'
    assert first.value == '<value>1024</value>'
