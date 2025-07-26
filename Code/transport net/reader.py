import json
from collections import defaultdict


def parse_data():
    with open('D:/JSON_BUS.json', 'r', encoding="utf-8-sig") as f:
        data = json.load(f)

    geo = dict()  # 站点id&坐标
    conn = defaultdict(int)  # 两个站点id间有多少条不同线路
    route, prev_s = 0, 0
    # routeSeq路线编号（去程回程编号不同）
    for d in data["features"]:
        dt = d["properties"]
        geo[dt["stopId"]] = d["geometry"]["coordinates"]
        if dt["routeId"] == route:  # 还在一条线上，连接
            conn[(dt["stopId"], prev_s)] += 1
        route = dt["routeId"]
        prev_s = dt["stopId"]

    return geo, conn
