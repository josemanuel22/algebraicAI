import numpy as np
import queue as Q 


def bfs_shortest_path(graph, weights, start, end):
	# keep track of explored nodes
	explored = []
	# keep track of all the paths to be checked
	queue = [[start]]

	# keeps looping until all possible paths have been checked
	while queue:
		# pop the first path from the queue
		path = queue.pop(0)
		# get the last node from the path
		node = path[-1]
		if node not in explored:
			neighbours = graph[node]
		else:
			continue
		if node == end:
			return path
		# go through all neighbour nodes, construct a new path and
		# push it into the queue
		for neighbour in neighbours:
			new_path = list(path)
			new_path.append(neighbour)
			#w += weights[node]
			queue.append(new_path)
			# mark node as explored
			explored.append(node)

	return path

if __name__ == "__main__":
	#Generate radom hypothesis matrix
	N = 4 #N hypothesis 
	b = np.random.randint(0, 2, size = (N,N))
	b_symm = (b + b.T)/2
	np.fill_diagonal(b_symm, 1)
	b_symm = np.ceil(b_symm)

	print("Our Literals matix:")
	print(b_symm)

	# Generate weights
	weights = np.random.randint(100, size=N)

	# we genereted the graph corresponding to this matrix
	graph = {}; i=0;
	for l1 in b:
		i+=1;
		graph["l"+str(i)]=[];
		j=0;
		for l_aux in l1:
			j+=1;
			if i==j:
				continue;
			if l_aux == 1:
				graph["l"+str(i)].append("l"+str(j))

	nodes_weights={}; i=0;
	for weight in weights:
		i+=1;	
		nodes_weights["l"+str(i)] = weight

	print("The graph ass to the matrix is:")
	print(graph)
	print("And the weights are:")
	print(weights)
	q = Q.PriorityQueue(); i=0;
	for l1 in b_symm:
		i+=1;j=0;
		for l_aux in l1:
			j+=1;
			path = bfs_shortest_path(graph, nodes_weights, "l"+str(i), "l"+str(j))
			w=0;
			for node in path:
				w+=nodes_weights[node]
			q.put((-w, path))
	(w, path) = q.get()
	print("and the shortest path is (weight, node sequence):")
	print((-w, path))


 

