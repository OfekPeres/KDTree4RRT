from .KDTreeNode import KDTreeNode
from typing import List, Text
from pprint import pprint

import matplotlib.pyplot as plt

class KDTree:
    def __init__(self, point=(0, 0)):
        self.root = KDTreeNode(point, 0)
        self.TreeList = [self.root.node_to_dict()]

    def Insert(self, point):
        '''
        Inserts a new KDTreeNode into the KDTree thru an iterative approach
        returns the node that was created
        '''
        depth = 0
        current_node = self.root
        new_node = KDTreeNode(point, depth)
        new_node.parent = self.NearestNeighbor(point)
        new_node.index = len(self.TreeList)
        self.TreeList.append(new_node.node_to_dict())
        while True:
            # Case where new node is greater, go to the right
            if current_node < new_node:
                # If a node exists to the right, jump to it
                if current_node.right is not None:
                    current_node = current_node.right
                # If there is no right node, then place your new node here
                else:
                    new_node.set_depth(depth + 1)
                    current_node.right = new_node
                    break
            # Case where new node is smaller, go to the left
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    new_node.set_depth(depth + 1)
                    current_node.left = new_node
                    break
            depth = depth + 1
            new_node.set_depth(depth)
        return new_node

    def __GetPointsInOrderTraversal(self, node, output_list: List):
        """
        Takes in a list to populate with all of the nodes in the tree in 
        ascending order. This method recursively does in order traversal
        """
        if node is None:
            return
        self.__GetPointsInOrderTraversal(node.left, output_list)
        output_list.append(node)
        self.__GetPointsInOrderTraversal(node.right, output_list)


    def GetAllNodes(self):
        """
        Returns a list of all nodes in the tree using an In Order Traversal
        """
        nodes = []
        self.__GetPointsInOrderTraversal(self.root, nodes)
        return nodes

    def CloserKDTreeNode(self, target, p1: KDTreeNode, p2: KDTreeNode):
        '''
        Takes in
        target: a k-dimensional point
        p1, a tree node
        p2, another tree node
        returns the tree node closer to the point, None if both inputs are None
        '''
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        d1 = p1.distance_to_point(target)
        d2 = p2.distance_to_point(target)

        if d1 < d2:
            return p1
        else:
            return p2

    def __NearestNeighbor(self, root: KDTreeNode, point):
        if root is None:
            return None

        next_branch = None
        opposite_branch = None

        if root.compare_to_point(point) > 0:
            next_branch = root.left
            opposite_branch = root.right
        else:
            next_branch = root.right
            opposite_branch = root.left

        # Figure out what node is closest to our search point.
        # Compares the best result from the new branch to the current node we
        # are at
        best: KDTreeNode = self.CloserKDTreeNode(
            point, self.__NearestNeighbor(next_branch, point), root)
        # If the splitting plane is closer than the current best, search the other
        # branch in case it contains a closer node
        if best.distance_to_point(point) > root.distance_to_splitting_plane(
                point):
            best = self.CloserKDTreeNode(
                point, self.__NearestNeighbor(opposite_branch, point), best)

        return best
    def NearestNeighbor(self, point):
        return self.__NearestNeighbor(self.root, point)
    def GetTreeAsList(self):
        return self.TreeList


if __name__ == '__main__':
    tree = KDTree((11, 10))
    tree.Insert((4, 7))
    node = tree.Insert((16, 10))
    tree.Insert((7, 13))
    tree.Insert((14, 11))
    tree.Insert((9, 4))
    tree.Insert((15, 3))
    node.set_goal_path()
    outputList = tree.GetAllNodes()

    pivot = [14,9]
    print(tree.NearestNeighbor(pivot))
    pprint(tree.GetTreeAsList())

    
    
