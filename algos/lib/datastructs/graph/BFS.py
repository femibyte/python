"""
  Implementation of BFS algorithm as specified in CLR's Introduction to Algorithms
"""

from  collections import deque

# Definitions
colors={}
distances={}
preds={}
neighbors={}
GRAY = "GRAY"
BLACK = "BLACK"
WHITE = "WHITE"

"""
Basic BFS algorithm. The assumption is that the graph is stored in a list T or map.
The graph is described as follows:

If T[v] = v, then v is the source vertex
else if T[v] = w, then v and w are connected 

It makes use of a FIFO queue to ensure that the nodes are traversed
in a breadth-first manner, i.e. all the neighbors of node N at the same distance from it before 
traversing nodes at a greater distance - hence the snippets
 u=q.popleft() 
 for v in neighbors[u]
     ... 
     q.append(v)
"""

def BFS(T):
	source=initAll(T)
	if source is None:
		return []
	neighbors = getAllNeighbors(T)
	q = deque()
	q.append(source)
	while q:
		u = q.popleft()
		for v in neighbors[u]:
			if colors[v]==WHITE:
				colors[v]=GRAY   # mark as seen so distance will be calc'ed only once
				distances[v]=distances[u]+1    # 
				preds[v] = u
				q.append(v)
		colors[u]=BLACK
	return


# Create adjacency list for all nodes of graph

def getAllNeighbors(T):
	size=len(T)
	neighbors = { n: set([]) for n in range(size)}

	for n in range(len(T)):
		v = T[n]
		if v !=n:
			neighbors[n].add(v)
			neighbors[v].add(n)
	return neighbors

# Initialize all helper data structures - colors, distances, neighbors, preds

def initAll(T):
	source=None
	colors.clear()
	distances.clear()
	neighbors.clear()
	preds.clear()
	for i in range(len(T)):
		if T[i]==i:
			distances[i]=0
			source=i
			colors[i]=GRAY
		else:
			distances[i] = float("inf")
			colors[i]=WHITE
		preds[i]=None
	return source