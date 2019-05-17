# Search methods

import search

ab = search.GPSProblem('O', 'G'
                       , search.romania)
# Breadth
print(search.breadth_first_graph_search(ab).path())
# Depth
print(search.depth_first_graph_search(ab).path())
#Branch and bound
print(search.Branch_and_Bound(ab).path())
#Branch and bound with heuristic
print(search.H_Branch_and_Bound(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
