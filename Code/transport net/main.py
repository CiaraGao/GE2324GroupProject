from reader import parse_data
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

# 读取公交站点数据
geo, conn = parse_data()
bus_stops = pd.DataFrame({
    'geometry': [Point(r[0], r[1]) for r in geo.values()]  # 从坐标创建点
})
# 转换为GeoDataFrame并设置坐标系
bus_gdf = gpd.GeoDataFrame(bus_stops, crs="EPSG:4326")
fig, ax = plt.subplots(figsize=(12, 10))  # fig是容器（画布） ax是内容

# 绘制公交站点
bus_gdf.plot(ax=ax, color='#FF1278', markersize=3, alpha=0.8, label='Bus Stops')

# 画路线
routes = []
for (start, end), count in conn.items():
    routes.append({
        "geometry": LineString([geo[start], geo[end]]),
        "connection_count": count
    })

routes_gdf = gpd.GeoDataFrame(routes, crs="EPSG:4326")

# 绘制连接线（线宽表示连接数量）
routes_gdf.plot(
    ax=ax,
    column='connection_count',
    linewidth=routes_gdf['connection_count'] / 20,  # 线宽放大倍数
)

# 添加地图元素
ax.axis("off")
ax.set_facecolor("none")
fig.patch.set_alpha(0.0)
plt.title("Hong Kong Bus Stops Distribution", fontsize=16)
plt.legend()

# 保存和显示
plt.tight_layout()
plt.savefig("hk_bus_map.pdf", dpi=300, bbox_inches='tight')
plt.show()
