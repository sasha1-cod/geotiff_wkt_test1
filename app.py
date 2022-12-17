from flask import Flask
from flask import request
from shapely import wkt
import shapely.ops
from geotiff import GeoTiff

geo_tiff = GeoTiff('srtm_N55E160.tif')

def wkt_loads(x):
    try:
        return wkt.loads(x)
    except Exception:
        return None

def get_elevation(x,y):
    try:
        area_box = [(x, y), (x+0.001, y+0.001)]
        array = geo_tiff.read_box(area_box)
        return array[0][0]
    except Exception:
        return 9999

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/elevation",methods = ['GET'])
def elevation():
    request_wkt = request.args.get('wkt')
    if request_wkt:
        request_wkt = request_wkt[1:-1]
    else:
        return 'Error var wkt'
    
    geom_data = wkt_loads(request_wkt)
    if geom_data != None:
        geom_data_z = shapely.ops.transform(lambda x, y: (x, y, get_elevation(x,y)), geom_data)
        return geom_data_z.wkt
    return 'Error no geom';
    