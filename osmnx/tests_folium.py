from . import nearest_nodes, shortest_path
from .folium import plot_graph_folium, plot_route_folium
from .geocoder import geocode
from .graph import graph_from_place
import pytest, networkx, folium


################## plot_graph_folium() #####################################

def test_plot_graph_folium_none():
  with pytest.raises(AttributeError):
    plot_graph_folium(None)

def test_plot_graph_folium_empty():
  with pytest.raises(KeyError):
    graph = networkx.MultiDiGraph()
    plot_graph_folium(graph)


def test_plot_graph_folium_address_none():
  with pytest.raises(TypeError):
    place_name = None
    graph = graph_from_place(place_name, network_type="drive")

    result = plot_graph_folium(graph)

def test_plot_graph_folium_address_empty():
  with pytest.raises(ValueError):
    place_name = ""
    graph = graph_from_place(place_name, network_type="drive")

    result = plot_graph_folium(graph)

def test_plot_graph_folium_invalid():
  with pytest.raises(ValueError):
    place_name = "Bruksel, Belgik"
    graph = graph_from_place(place_name, network_type="drive")

    result = plot_graph_folium(graph)

def test_plot_graph_folium_valid():
  place_name = "Bruxelles, Belgique"
  graph = graph_from_place(place_name, network_type="drive")

  result = plot_graph_folium(graph)

  assert(type(result) == folium.folium.Map)

def test_plot_graph_folium_graph_map_invalid():
  with pytest.raises(ValueError):
    place_name = "Bruksel, Belgik"
    graph = graph_from_place(place_name, network_type="drive")

    location = geocode(place_name)
    map_center = [location[1], location[0]]
    m = folium.Map(location=map_center, zoom_start=12)

    result = plot_graph_folium(graph, graph_map=m)

def test_plot_graph_folium_graph_map_valid():
  place_name = "Bruxelles, Belgique"
  graph = graph_from_place(place_name, network_type="drive")

  location = geocode(place_name)
  print(location)
  map_center = [location[1], location[0]]
  m = folium.Map(location=map_center, zoom_start=12)

  result = plot_graph_folium(graph, graph_map=m)

  assert(type(result) == folium.folium.Map)
  assert(type(m) == folium.folium.Map)

def test_plot_graph_folium_graph_map_valid_attrnone():
  place_name = "Bruxelles, Belgique"
  graph = graph_from_place(place_name, network_type="drive")

  location = geocode(place_name)
  print(location)
  map_center = [location[1], location[0]]
  m = folium.Map(location=map_center, zoom_start=12)

  result = plot_graph_folium(graph, graph_map=m, popup_attribute=None,
    tiles=None, zoom=None, fit_bounds=None)

  assert(type(result) == folium.folium.Map)
  assert(type(m) == folium.folium.Map)

def test_plot_graph_folium_graph_map_valid_attrempty():
  place_name = "Bruxelles, Belgique"
  graph = graph_from_place(place_name, network_type="drive")

  location = geocode(place_name)
  print(location)
  map_center = [location[1], location[0]]
  m = folium.Map(location=map_center, zoom_start=12)

  result = plot_graph_folium(graph, graph_map=m, popup_attribute=None,
    tiles="", zoom=None, fit_bounds=None)

  assert(type(result) == folium.folium.Map)
  assert(type(m) == folium.folium.Map)

def test_plot_graph_folium_graph_map_valid_attrfalse():
  with pytest.raises(KeyError):
    place_name = "Bruxelles, Belgique"
    graph = graph_from_place(place_name, network_type="drive")

    location = geocode(place_name)
    print(location)
    map_center = [location[1], location[0]]
    m = folium.Map(location=map_center, zoom_start=12)

    result = plot_graph_folium(graph, graph_map=m, popup_attribute="FALSE",
      tiles=0, zoom="FALSE", fit_bounds="FALSE")




############################################################################

################## plot_route_folium() #####################################

def test_plot_route_folium_none():
  with pytest.raises(TypeError):
    plot_route_folium(G=None, route=None)

def test_plot_route_folium_empty():
  with pytest.raises(TypeError):
    G= networkx.MultiDiGraph
    plot_route_folium(G=G, route=[])

def test_plot_route_folium_invalid():
  with pytest.raises(ValueError):
    start = 000000000
    end = 99999999999999999

    route = [start, end]

    G = graph_from_place('Namur, Belgique', network_type='drive')

    plot_route_folium(G=G, route=route)

def test_plot_route_folium_valid(): # déprécié
  G = graph_from_place('Namur, Belgique', network_type='drive')

  start = 145013
  end = 2479827

  route = shortest_path(G, start, end)

  result = plot_route_folium(G, route)

  assert result != None