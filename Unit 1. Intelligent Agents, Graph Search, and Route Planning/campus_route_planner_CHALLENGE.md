# Challenge: Campus Route Planner

## Scenario

You need to get from Yachay Tech to your home (or another meaningful reference point) every day. Today you're going to build the program that finds you the best way there — not just *a* way, the *best* way, by your own definition of "best."

## Your task

Write a Python program that finds a route between two points on a street network using **A\* search**, and lets you define your own notion of "cost" beyond raw distance.

You choose the libraries, the data source, and the code structure. The only hard requirements are below.

## Requirements

**1. A graph with real structure**
Represent a street network as a graph: nodes are intersections/locations, edges are streets. Each edge needs some notion of cost (distance is enough to start). Options include:
- A real street network (e.g., via OpenStreetMap / OSMnx)
- A graph you build yourself, using coordinates you invent or pull from a map
- Any other structured dataset with a genuine sense of geographic distance

Minimum size: about 15–20 nodes. Trivial 4-node examples don't give A* anything interesting to do.

**2. A* implemented by you**
Your code must manage its own frontier (priority queue) using

```python
f(n) = g(n) + h(n)
```

where `g(n)` is the real accumulated cost from the start and `h(n)` is a heuristic estimate to the goal. Expand nodes in priority order and reconstruct the path from the search.

You may use a library's built-in shortest-path function **only to check your own answer** — it cannot be your actual solution. If your "A*" is one line calling someone else's solver, that's not the assignment.

**3. An admissible heuristic**
Your `h(n)` must never overestimate the true remaining cost (straight-line distance is the standard choice for geographic graphs — look up why it works here if you're not sure).

**4. A custom cost function**
Design your own criterion for "best route" — something beyond plain distance. Some directions (pick one, invent your own, or combine a few):
- Penalize road types you'd rather avoid (busy avenues, unpaved roads)
- Reward walkable/residential streets
- Invent a synthetic "risk" or "comfort" score and justify it

Your criterion doesn't have to be objectively correct. It has to be defensible.

**5. Evidence that it works**
Show — with printed numbers, a plot, or both — how your custom-cost route compares to the plain shortest-distance route: same path or different, longer or shorter, and why that trade-off makes sense given your criterion.

## Constraints

- No required library. NetworkX, OSMnx, `heapq` with your own dictionaries, igraph, or something else entirely — your call.

## Definition of done

- [ ] Graph has enough nodes to make search non-trivial, with a way to compute geographic distance between any two nodes
- [ ] `A*` search is your own code — frontier, priority, expansion, path reconstruction
- [ ] Heuristic is admissible and you can explain why
- [ ] Your A* matches a known-correct shortest path when cost = distance (this is your proof it actually works)
- [ ] Custom cost function implemented, with a stated criterion
- [ ] Comparison between baseline (BDs, DFS) and custom route, shown with evidence

## Grading Rubric

**PASS:** A* is your own search logic (not a wrapped library call), it matches the baseline on default cost, the custom cost has a real criterion behind it, and you can explain all of it live, in your own words.

- [ ] Explanation of the graph structure (1/1)
- [ ] Explanation of the selected heuristic (2/2)
- [ ] Explanation of the custom cost function (2/2)
- [ ] Explanation of the A* implementation (3/3)
- [ ] Comparison of the baseline and custom-cost routes (2/2)

Penalties:

- **Language:** Use of Spanish in the code or presentation: -5 points.
- **Time management:** -1 point per minute after the 5 min mark.
- **Late presentation:** -1 point per minute late, up to 10 points.