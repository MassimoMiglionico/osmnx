import pytest
from .downloader import nominatim_request, overpass_request, _get_osm_filter, _create_overpass_query
from collections import OrderedDict

################## nominatim_request() #####################################
def test_nominatim_request_valid_search():
    params = OrderedDict()
    params["format"] = "json"
    params["q"] = "Namur"
    result = nominatim_request(params=params)
    assert type(result[0]) == dict

def test_nominatim_request_unvalid_search():
    params = OrderedDict()
    params["format"] = "json"
    params["q"] = "R2192363"
    result = nominatim_request(params=params)
    assert len(result) == 0

def test_nominatim_request_valid_reverse():
    params = OrderedDict()
    params["format"] = "json"
    params["lat"] = "23"
    params["lon"] = "23"
    result = nominatim_request(params=params, request_type="reverse")
    assert type(result) == dict

def test_nominatim_request_unvalid_reverse():
    params = OrderedDict()
    params["format"] = "json"
    params["lat"] = "-100"
    params["lon"] = "247"
    result = nominatim_request(params=params, request_type="reverse")
    assert result['error']

def test_nominatim_request_valid_lookup():
    params = OrderedDict()
    params["format"] = "json"
    params["osm_ids"] =  "R2192363"
    result = nominatim_request(params=params, request_type="lookup")
    assert type(result[0]) == dict

def test_nominatim_request_unvalid_lookup():
    params = OrderedDict()
    params["format"] = "json"
    params["osm_ids"] =  "V2192363"
    result = nominatim_request(params=params, request_type="lookup")
    assert len(result) == 0

################## _get_osm_filter() #####################################

def test_get_osm_filter_valid():
    filters = ["drive", "drive_service", "walk", "bike", "all", "all_private"]
    for filter in filters:
        result = _get_osm_filter(filter)
        assert type(result) == str

def test_get_osm_filter_unvalid():
    with pytest.raises(ValueError):
        result = _get_osm_filter("test")
################## overpass_request() #####################################
# def test_overpass_request():
#     result = _create_overpass_query([48.8584, 2.2945, 48.8606, 2.2979], {})
#     overpass_request(result)
#     print(result)
    

