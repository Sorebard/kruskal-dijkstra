# Copyright (c) 2025 Sorebard. Licensed under the MIT license.
# See the LICENSE file in the repository root for full license text.


from edge import Edge
from union_find import UnionFind


def mst_kruskal(vertices: list[str], edges: list[Edge]) -> list[Edge]:
    tree: list[Edge] = []
    union_find: UnionFind = UnionFind(vertices)

    for edge in edges:
        if union_find.find(edge.first) != union_find.find(edge.second):
            tree.append(edge)
            union_find.union(edge.first, edge.second)

    return tree