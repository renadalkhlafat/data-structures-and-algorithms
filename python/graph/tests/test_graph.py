from graph import __version__
from graph.graph import Graph, Vertex,business_trip
import pytest
def test_version():
    assert __version__ == '0.1.0'

def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

def test_breadth_first():
    graph = Graph()

    apple = graph.add_node('apple')
    cherry = graph.add_node('cherry')
    orange = graph.add_node('orange')
    banana = graph.add_node('banana')

    graph.add_edge(apple,banana)
    graph.add_edge(orange,banana)
    graph.add_edge(cherry,orange)
    graph.add_edge(banana,cherry)

    expected = 'apple ,banana ,cherry ,orange ,'
    actual = graph.breadth_first(apple)
    assert actual == expected

# ************************* business_trip ******************
@pytest.mark.skip("")
def test_business_trip():

    graph = Graph()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstropolis = graph.add_node('Monstropolis')
    naboo = graph.add_node('Naboo')
    narnia = graph.add_node('Narnia')

    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(metroville,pandora,82)

    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(arendelle,monstropolis,42)
    graph.add_edge(monstropolis,arendelle,42)

    graph.add_edge(monstropolis,metroville,105)
    graph.add_edge(metroville,monstropolis,105)
    graph.add_edge(monstropolis,naboo,73)
    graph.add_edge(naboo,monstropolis,73)

    graph.add_edge(metroville,naboo,26)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(narnia,metroville,37)

    graph.add_edge(naboo,narnia,250)
    graph.add_edge(narnia,naboo,250)

    assert [True, "$82"] == business_trip(graph,[metroville, pandora])
    assert [True, '$42'] == business_trip(graph,[arendelle,monstropolis, naboo])
    assert [False, "$0"] == business_trip(graph,[naboo, pandora])
    assert [True, '$250'] == business_trip(graph,[narnia, arendelle,naboo])

# *************************** depth_first ***********************
def test_breadth_first():
    graph = Graph()

    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h = graph.add_node('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)

    graph.add_edge(b,c)
    graph.add_edge(b,d)

    graph.add_edge(c,g)

    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)

    graph.add_edge(f,h)


    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actual = graph.depth_first(a)
    assert actual == expected
