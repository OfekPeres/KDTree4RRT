import numpy as np


class KDTreeNode:

    def __init__(self, point=np.array((0, 0)), depth=0):
        '''
        Point: The position of the node
        depth: the depth of the node in the tree
          
        '''
        self.p = np.array(point)
        self.depth = depth

        # The dimension of the splitting plane (i.e. 0 -> the x dimension, 1-> y )
        self.axis = depth % len(point)

        # The children nodes
        self.left = None
        self.right = None

        # I will define the parent as the closest neighbor to this node
        # at the time this node was added to the tree
        self.parent = None
        # The index in the kdtree array representation. Only the root node should have a value of -1 as it has no parents
        self.index = 0 
        self.isOnGoalPath = False
    def set_depth(self, depth):
        self.depth =depth
        self.axis = depth % len(self.p)

    def distance_to_node(self, other):
        '''
        returns the distance between the current node and the input node
        '''
        return np.linalg.norm(self.p - other.p)
    
    def distance_to_point(self, other):
        '''
        returns the distance between the current node and the input point 
        (array)
        '''
        return np.linalg.norm(self.p - other)

    def distance_to_splitting_plane(self, other):
        '''
        returns the distance between the current node's splitting axis 
        and the input points value at that axis.
        i.e. if the splitting plane is the x axis, compare the node's x value
        to the point's x value
        '''
        axis = self.axis
        return abs(self.p[axis] - other[axis])

    def compare_to_point(self, point):
        axis = self.axis
        return self.p[axis] - point[axis]


    def node_to_dict(self):
        parentIndex = -1
        if self.parent is not None:
            parentIndex = self.parent.index
        return {
            "x":self.p[0],
            "y":self.p[1],
            "parentIndex": parentIndex}

    def __lt__(self, other):
        '''
        Operator overload for the < (less than)
        compares the current node and another node's values at the dimension of 
        the other node (i.e. if the other node is at dimension 0, compare the x
        values)
        '''
        axis = other.axis
        p = self.p
        return p[axis] <= other.p[axis]

    def __gt__(self, other):
        '''
        Operator overload for the > (greater than)
        compares the current node and another node's values at the dimension of 
        this node (i.e. if this node is at dimension 0, compare the )
        '''
        axis = self.axis
        p = self.p
        return p[axis] > other.p[axis]
    
    def __eq__(self, other):
        '''
        Operator overload for the == (equals)
        compares the current node and another node's values at the dimension of 
        this node (i.e. if this node is at dimension 0, compare the )
        '''
        return self.p == other.p

    def __repr__(self):
        return "Point: {}, Depth: {}, Splitting Axis: {}".format(self.p, self.depth, self.axis)

    def set_goal_path(self):
        cur_node = self
        while cur_node is not None:
            cur_node.isOnGoalPath = True
            cur_node = cur_node.parent
if __name__ == '__main__':
    a = KDTreeNode((-1,-1),1)
    b = KDTreeNode((2,2),1)
    
    print(b.distance_to_splitting_plane((10,11)))