from Element import element, repr 

class First(repr):
    name = element()
    value = element()
    list = element()

    def __init__(self, name: str = None, value: float = None, list: list = None):
        self.name = name
        self.value = value
        self.list = list

class Second(repr):
    value = element()

    def __init__(self, value: float = None):
        self.value = value

def test_XML():
    first = First('first', 1024)
    assert first.name == '<name>first</name>'
    assert first.value == '<value>1024</value>'

def test_XML_repr():
    p = {'name': 'first', 'value': 1024}
    first = First(**p)
    assert str(first) == '<First><name>first</name><value>1024</value><list></list></First>'

def test_XML_List():    
    f = First('first', 1024)
    s = [Second(1024), Second(2048)]

    f.list = s

    assert str(f) == '<First><name>first</name><value>1024</value><list><Second><value>2048</value></Second><Second><value>2048</value></Second></list></First>'

