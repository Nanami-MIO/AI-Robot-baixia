#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""方向 B 自动探索器：在迷宫格点图上用 A* 规划到终点的路径。"""

import heapq
import math

from maze import build_maze

LIN = 1.6
ANG_MAX = 2.2
K_ANG = 3.0
TURN_FIRST = 0.6
REACH_TOL = 0.12


def astar(neighbors, start, goal):
    """Return the shortest cell path from start to goal with Manhattan A*."""
    openq = [(0, start)]
    came = {start: None}
    g = {start: 0}

    def heuristic(cell):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    while openq:
        _, current = heapq.heappop(openq)
        if current == goal:
            break

        for nxt in neighbors(current):
            next_cost = g[current] + 1
            if nxt not in g or next_cost < g[nxt]:
                g[nxt] = next_cost
                came[nxt] = current
                heapq.heappush(openq, (next_cost + heuristic(nxt), nxt))

    if goal not in came:
        return []

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came[current]
    return path[::-1]


class Planner:
    def __init__(self):
        self.m = build_maze()
        self.grid = self.m["grid"]
        self.waypoints = None
        self.idx = 0

    def _to_cell(self, x, y):
        origin = self.grid["origin"]
        cell = self.grid["cell"]
        ci = min(self.grid["cols"] - 1, max(0, round((x - origin - cell / 2) / cell)))
        cj = min(self.grid["rows"] - 1, max(0, round((y - origin - cell / 2) / cell)))
        return (ci, cj)

    def _plan(self, x, y):
        start = self._to_cell(x, y)
        cells = astar(self.m["neighbors"], start, self.m["goal_cell"])
        cell_center = self.m["cell_center"]
        self.waypoints = [(cell_center(i), cell_center(j)) for (i, j) in cells]
        self.idx = 1 if len(self.waypoints) > 1 else 0

    def decide(self, state):
        if state.get("rule", {}).get("goal_reached"):
            return 0.0, 0.0

        x = state["pose"]["x"]
        y = state["pose"]["y"]
        theta = state["pose"]["theta"]
        if x == 0.0 and y == 0.0:
            return 0.0, 0.0

        if self.waypoints is None:
            self._plan(x, y)

        if not self.waypoints or self.idx >= len(self.waypoints):
            return 0.0, 0.0

        tx, ty = self.waypoints[self.idx]
        if math.hypot(tx - x, ty - y) < REACH_TOL:
            self.idx += 1
            return 0.0, 0.0

        desired = math.atan2(ty - y, tx - x)
        err = math.atan2(math.sin(desired - theta), math.cos(desired - theta))
        angular = max(-ANG_MAX, min(ANG_MAX, K_ANG * err))
        linear = 0.0 if abs(err) > TURN_FIRST else LIN
        return linear, angular


if __name__ == "__main__":
    planner = Planner()
    planner._plan(planner.m["start"]["x"], planner.m["start"]["y"])
    print("planned cells:", len(planner.waypoints))
