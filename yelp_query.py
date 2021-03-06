import os
from yelpapi.geojson import make_geojson, getgeojsonid
from yelpapi.query import my_query, NoYelpBusiness
import pickle
import json

def yelpid(term,location,verbose=False):
    try:
        business_id, response=my_query(term,location,verbose)
        geojson=getgeojsonid(response)
        return geojson, business_id, response

    except NoYelpBusiness:
        return None