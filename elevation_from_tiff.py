from geotiff import GeoTiff

geo_tiff = GeoTiff('data/srtm_N55E160.tif')

def get_elevation(x,y):
    area_box = [(x, y), (x+0.001, y+0.001)]
    array = geo_tiff.read_box(area_box)
    return array[0][0]

print(get_elevation(160.01,55.01))