# from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import geopandas as gpd

test = gpd.read_file('../shapefiles/BEAT.shp')
# test = GeoDataFrame.from_file('../shapefiles/BEAT.shp')
# test.set_index('id', inplace=True)
# test.sort()
print(test['geometry'])
BLUE = '#6699cc'
print(len(test['geometry']))
for i in range(0, len(test['geometry'])):
    poly= test['geometry'][i]
    fig = plt.figure()
    ax = plt.gca()
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().axes.get_xaxis().set_visible(False)
    # ax=fig.add_subplot(111)
    ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))
    ax.axis('scaled')

    # Remove whitespace from around the image
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    f_name = 'beat' + str(i)
    plt.savefig(f_name, bbox_inches='tight', pad_inches = 0)
    plt.close()