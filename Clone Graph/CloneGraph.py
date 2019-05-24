"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # create stack for nodes to visit
        stack = []
        stack.append(node)
        
        # initialise graph with the first node
        graph = {node.val : Node(node.val, [])}
        curr = node
        
        # once stack is empty we have visited all nodes
        while (stack):
            
            # pop node to visit off stack
            curr = stack[0]
            stack.pop(0)
                
            # for each neighbour add to stack and create node in graph if doesn't already exist
            for neighbour in curr.neighbors:
                if neighbour.val not in graph:
                    stack.append(neighbour)
                    graph[neighbour.val] = Node(neighbour.val, [])
                    
                # add neighbours to the current node in the graph
                graph[curr.val].neighbors.append(graph[neighbour.val])
                
        return graph[node.val]
