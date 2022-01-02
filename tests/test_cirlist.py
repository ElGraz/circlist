from src.circlist.circlist import CircList, CircListIter


def test_list_inst():
    cl = CircList(5)
    assert isinstance(cl, CircList)


def test_list_init_default():
    cl = CircList(5)
    # default should be int 0
    assert cl.as_list() == [0] * 5


def test_list_init():
    cl = CircList(5, 1)
    assert cl.as_list() == [1] * 5


def test_get():
    cl = CircList(3)
    assert cl.get() == 0


def test_put():
    cl = CircList(5, 1)
    cl.put(0)
    assert cl.as_list() == [1, 1, 1, 1, 0]


def test_get_whats_put():
    elm = 1
    cl = CircList(3)
    cl.put(elm)
    assert cl.get() == elm


def test_multi_put():
    cl = CircList(5, 1)
    for i in range(5):
        cl.put(i)
    assert cl.as_list() == list(range(5))


def test_iterate():
    cl = CircList(5, 1)
    for i in range(5):
        cl.put(i)
    tested = list()
    for elm in cl:
        tested.append(elm)

    assert cl.as_list() == tested


def test_multi_put_over():
    cl = CircList(5, 1)
    for i in range(25):
        cl.put(i)
    assert cl.as_list() == list(range(20, 25))
