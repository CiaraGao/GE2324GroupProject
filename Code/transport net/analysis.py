import networkx as nx
from reader import parse_data
import json
# 分析betweeness & closeness


def calc_betweeness(conn):
    # 创建无向图
    G = nx.Graph()
    G.add_edges_from(conn.keys())

    # ===== 计算中介中心性 =====
    betweeness = nx.betweenness_centrality(G, normalized=True)  # normalized=True进行归一化
    # ===== 计算接近中心性 =====
    closeness = nx.closeness_centrality(G, wf_improved=True)
    return betweeness, closeness


geo, conn = parse_data()
print(f"{len(geo)} stations in total")

betweeness, closeness = calc_betweeness(conn)
with open("between.txt", "w") as f1:
    json.dump(betweeness, f1)
with open("closeness.txt", "w") as f2:
    json.dump(closeness, f2)

