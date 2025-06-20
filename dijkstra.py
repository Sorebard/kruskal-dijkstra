# Copyright (c) 2025 Sorebard. Licensed under the MIT license.
# See the LICENSE file in the repository root for full license text.


from edge import Edge
from heapq import heapify, heappop, heappush


def _construct_adjacency_list(adjacency: dict[str, list[tuple[str, float]]], edges: list[Edge]) -> None:
    for edge in edges:
        adjacency[edge.first].append((edge.second, edge.distance))
        adjacency[edge.second].append((edge.first, edge.distance))


def dijkstra(vertices: list[str], edges: list[Edge], starting_vertex: str) -> dict[str, float]:
    adjacency: dict[str, list[tuple[str, float]]] = { vertex: [] for vertex in vertices }
    _construct_adjacency_list(adjacency, edges)

    distances: dict[str, float] = { vertex: float("inf") for vertex in vertices }
    queue: list[tuple[float, str]] = [ (0.0, starting_vertex) ]
    heapify(queue)
    distances[starting_vertex] = 0.0

    while queue:
        _, vertex_source = heappop(queue)
        for edge in adjacency[vertex_source]:
            vertex_destination, distance = edge

            if distances[vertex_destination] > distances[vertex_source] + distance:
                distances[vertex_destination] = distances[vertex_source] + distance
                heappush(queue, (distances[vertex_destination], vertex_destination))
    return distances