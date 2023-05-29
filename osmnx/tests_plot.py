from .graph import graph_from_place
from .plot import get_colors, plot_graph
import pytest, networkx

################## get_colors() #####################################

def test_get_colors_null():
  with pytest.raises(TypeError):
    get_colors(n=None)

def test_get_colors_zero():
  result = get_colors(0)

  assert(type(result) == list)
  assert result == []

def test_get_colors_one():
  result = get_colors(1)
  assert type(result) == list
  assert len(result) == 1

def test_get_colors_many():
  result = get_colors(5)

  assert type(result) == list
  assert len(result) == 5

def test_get_colors_negative():
  with pytest.raises(ValueError):
    get_colors(-1)

def test_get_colors_invalid_cmap():
  with pytest.raises(KeyError):
    get_colors(1, cmap="hsufh")

def test_get_colors_empty_colorspace():
  r1 = get_colors(1, stop=0)
  r2 = get_colors(1, start=1)

  assert type(r1) == type(r2)
  assert len(r1) == len(r2)

def test_get_colors_wide_colorspace():
  r1 = get_colors(1, stop=100)
  r2 = get_colors(1, start=-100)

  assert type(r1) == type(r2)
  assert len(r1) == len(r2)

#####################################################################
################## plot_graph() #####################################

def test_plot_graph_null():
  with pytest.raises(AttributeError):
    plot_graph(None)

def test_plot_graph_empty():
  with pytest.raises(KeyError):
    G = networkx.MultiDiGraph()
    plot_graph(G)

def test_plot_graph_invalid():
  with pytest.test((KeyError, AttributeError)):
    G = networkx.MultiDiGraph()

    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    G.add_edge(1, 2, key='edge')
    G.add_edge(2, 3, key='edge')
    G.add_edge(3, 1, key='edge')

  plot_graph(G)

def test_plot_graph_valid():
  G = graph_from_place("Bruxelles, Belgique", network_type="drive", retain_all=True)
  result = plot_graph(G)

  assert type(result) == tuple
  assert len(result) > 1

