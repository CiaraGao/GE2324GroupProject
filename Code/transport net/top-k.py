import json
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from reader import parse_data

geo, conn = parse_data()

with open("between.txt", "r") as f1:
    betweeness = json.load(f1)

with open("closeness.txt", "r") as f1:
    closeness = json.load(f1)

bus_stops = pd.DataFrame({
    'geometry': [Point(r[0], r[1]) for r in geo.values()],
    'between': [betweeness[str(r)] for r in geo.keys()],
    'close': [closeness[str(r)] for r in geo.keys()],
})
print(1)
bus_gdf = gpd.GeoDataFrame(bus_stops, crs="EPSG:4326")
fig, ax = plt.subplots(figsize=(12, 10))
fig2, ax2 = plt.subplots(figsize=(12, 10))
bus_gdf.plot(ax=ax, color='#FF1278', markersize=bus_gdf["between"]*500, alpha=0.8, label='Bus Stops')
bus_gdf.plot(ax=ax2, color='#FF1278', markersize=bus_gdf["close"]*70, alpha=0.8, label='Bus Stops')
# 可以看出各站closeness比较接近，而betweeness有几个明显的大节点

print(2)
ax.axis("off")
ax2.axis("off")
ax.set_facecolor("none")
ax2.set_facecolor("none")
fig.patch.set_alpha(0.0)
fig2.patch.set_alpha(0.0)
ax.set_title("Bus Stops Betweeness", fontsize=16)
ax2.set_title("Bus Stops closeness", fontsize=16)
plt.legend()

# 保存和显示
plt.tight_layout()
fig.savefig("hk_bus_between.pdf", dpi=300, bbox_inches='tight')
fig2.savefig("hk_bus_close.pdf", dpi=300, bbox_inches='tight')
plt.show()
