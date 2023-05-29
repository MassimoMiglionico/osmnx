from .geocoder import geocode, geocode_to_gdf
import pytest
import geopandas


# geocoder
def test_geocode_empty_or_none():
    with pytest.raises(ValueError):
        geocode(None)
    with pytest.raises(ValueError):
        geocode("")
        
def test_geocode_invalid_query():
    with pytest.raises(ValueError):
        geocode("PaysImmaginaire")

    with pytest.raises(ValueError):
        geocode(0)


def test_geocode_valid_query():
    queries = ["Namur", 1, "5000"]
    for query in queries:
        coords = geocode(query)
        assert type(coords) == tuple
        assert len(coords) == 2
        assert -90 < coords[0] < 90
        assert -180 < coords[1] < 180
    
#geocode_to_gdf
def test_geocode_to_gdf_invalid_query():
    with pytest.raises(ValueError):
        geocode_to_gdf(1)
    with pytest.raises(ValueError):
        geocode_to_gdf(1.98)

    good_name_queries = ["Namur", "5000", {"country":"France", "city":"Paris"}, ["Namur", "Charleroi"]]
    bad_id_queries = [{}, ["M1537293", "N234", "DFSIHU"]]
    for query in good_name_queries + bad_id_queries:
        with pytest.raises(ValueError):
            geocode_to_gdf(query, by_osmid=True)
    
    good_id_queries = ["R2192363", ["R2192363", "N240109189", "W427818536"]]
    bad_name_queries = [{}, [], {"City":"Charleroi"}]
    for query in good_id_queries + bad_name_queries:
        with pytest.raises(ValueError):
            geocode_to_gdf(query)

def test_geocode_to_gdf_valid_query():
    name_queries = ["Namur", "5000", {"country":"France", "city":"Paris"}, ["Namur", "Charleroi"]]
    for query in name_queries:
        assert isinstance(geocode_to_gdf(query), geopandas.GeoDataFrame)

    id_queries = ["R2192363", ["R2192363", "N240109189", "W427818536"]]
    for query in id_queries:
        assert isinstance(geocode_to_gdf(query, by_osmid=True), geopandas.GeoDataFrame)

def test_geocode_to_gdf_invalid_whichresult():
    good_name_queries = ["Namur", "5000", {"country":"France", "city":"Paris"}, ["Namur", "Charleroi"]]
    whichresults = [-1, 10000]
    for query in good_name_queries:
        for result in whichresults:
            if result < 0:
                error = IndexError
            elif result == 10000:
                error = ValueError
            elif isinstance(result,str):
                error = TypeError
            with pytest.raises(error):
                geocode_to_gdf(query, which_result=result)

def test_geocode_to_gdf_valid_whichresult():
    good_name_queries = ["Namur", "5000", {"country":"France", "city":"Paris"}, ["Namur", "Charleroi"]]
    whichresults = [0, 1, 2, 3]
    for query in good_name_queries:
        for result in whichresults:
            assert isinstance(geocode_to_gdf(query, which_result=result), geopandas.GeoDataFrame)

    good_id_queries = ["R2192363", ["R2192363", "N240109189", "W427818536"]]
    for query in good_id_queries:
        for result in whichresults + [-1, 100000]:
            assert isinstance(geocode_to_gdf(query, which_result=result, by_osmid=True), geopandas.GeoDataFrame)

def test_geocode_query_to_gdf_valid_query():
    name_queries = ["Namur", "5000", {"country":"France", "city":"Paris"}]
    for query in name_queries:
        assert isinstance(geocode_to_gdf(query), geopandas.GeoDataFrame)

    id_queries = ["R2192363", "N240109189", "W427818536"]
    for query in id_queries:
        assert isinstance(geocode_to_gdf(query, by_osmid=True), geopandas.GeoDataFrame)

def test_geocode_query_to_gdf_invalid_query():
    good_name_queries = [{"Country":"France", "City":"Paris"}, ["Namur", "Charleroi"], 0]
    bad_id_queries = [{}, ["M1537293", "N234", "DFSIHU"], "M1537293", "N234", "DFSIHU", "162748", 1234]
    for query in good_name_queries + bad_id_queries:
        with pytest.raises(ValueError):
            geocode_to_gdf(query, by_osmid=True)
    
    good_id_queries = ["R2192363", "N240109189", "W427818536"]
    bad_name_queries = [{}, [], {"City":"Charleroi"}, 3, "jkhbfdsv"]
    for query in good_id_queries + bad_name_queries:
        with pytest.raises(ValueError):
            geocode_to_gdf(query)
