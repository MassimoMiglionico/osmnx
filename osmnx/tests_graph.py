from ._errors import EmptyOverpassResponse
from .graph import graph_from_polygon, graph_from_bbox, graph_from_place
import pytest, shapely, networkx
import timeout_decorator


################## graph_from_polygon() ####################################

def test_graph_from_polygon_none():
  with pytest.raises(AttributeError):
    graph_from_polygon(polygon=None)

def test_graph_from_polygon_wrong_type():
  with pytest.raises(AttributeError):
    graph_from_polygon(polygon="polygon")
  
def test_graph_from_polygon_valid_clean_periphery():
  # Coordonnées géographiques de la zone autour de Paris
  north = 48.90
  south = 48.80
  east = 2.50
  west = 2.30

  # Création du polygone à partir des coordonnées
  polygon = shapely.geometry.Polygon([(west, north), (east, north),
  (east, south), (west, south)])

  # Utilisation du polygone pour obtenir le graphe
  result = graph_from_polygon(polygon, clean_periphery=True)

  assert (type(result) == networkx.MultiDiGraph)
  assert len(result.nodes) > 0
  assert len(result.edges) > 0

def test_graph_from_polygon_valid_not_clean_periphery():
  # Coordonnées géographiques de la zone autour de Paris
  north = 48.90
  south = 48.80
  east = 2.50
  west = 2.30

  # Création du polygone à partir des coordonnées
  polygon = shapely.geometry.Polygon([(west, north), (east, north),
  (east, south), (west, south)])

  # Utilisation du polygone pour obtenir le graphe
  result = graph_from_polygon(polygon, clean_periphery=False)

  assert (type(result) == networkx.MultiDiGraph)
  assert len(result.nodes) > 0
  assert len(result.edges) > 0

############################################################################

################## graph_from_bbox() #######################################

def test_graph_from_bbox_empty():
  with pytest.raises(EmptyOverpassResponse):
    north = 0.0
    south = -1.0
    east = 0.0
    west = -1.0
    
    graph_from_bbox(north, south, east, west)

def test_graph_from_bbox_valid():
  north = 48.90
  south = 48.80
  east = 2.50
  west = 2.30

  graph = graph_from_bbox(north, south, east, west)
  assert isinstance(graph, networkx.MultiDiGraph)
  assert len(graph.nodes) > 0
  assert len(graph.edges) > 0

@timeout_decorator.timeout(60)
def test_graph_from_bbox_invalid():
  with pytest.raises(timeout_decorator.timeout_decorator.TimeoutError):
    north = 48.90
    south = -48.80
    east = 2.50
    west = 2.30

    graph = graph_from_bbox(north, south, east, west)

############################################################################

################## graph_from_place() ######################################

def test_graph_from_place_none():
  with pytest.raises(TypeError):
    graph_from_place(None)

def test_graph_from_place_empty():
  with pytest.raises(ValueError):
    graph_from_place("")

def test_graph_from_place_invalid():
  with pytest.raises(ValueError):
    graph_from_place("Namure Belgik 21 grandgagnage rue")

def test_graph_from_place_valid():
  graph = graph_from_place("Rue grandgagnage 21, Namur, Belgique")

  assert isinstance(graph, networkx.MultiDiGraph)
  assert len(graph.nodes) > 0
  assert len(graph.edges) > 0