# Copyright (c) 2025 Sorebard. Licensed under the MIT license.
# See the LICENSE file in the repository root for full license text.


class Edge:
    def __init__(self, first: str, second: str, distance: float) -> None:
        self.first: str = first
        self.second: str = second
        self.distance: float = distance


    def __repr__(self) -> str:
        return f"{self.first} <-> {self.second} ({self.distance} km)"
