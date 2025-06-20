# Copyright (c) 2025 Sorebard. Licensed under the MIT license.
# See the LICENSE file in the repository root for full license text.


class UnionFind:
    def __init__(self, vertices: list[str]) -> None:
        self.parent: dict[str, str] = {vertex: vertex for vertex in vertices}
        self.rank: dict[str, int] = {vertex: 0 for vertex in vertices}


    def find(self, vertex: str) -> str:
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])

        return self.parent[vertex]


    def union(self, vtx1: str, vtx2: str) -> None:
        vtx1: str = self.find(vtx1)
        vtx2: str = self.find(vtx2)

        if vtx1 == vtx2: return

        if self.rank[vtx1] < self.rank[vtx2]:
            (vtx1, vtx2) = (vtx2, vtx1)

        self.parent[vtx2] = vtx1

        if self.rank[vtx1] == self.rank[vtx2]:
            self.rank[vtx1] += 1