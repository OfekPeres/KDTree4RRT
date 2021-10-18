from KDTree4RRT.KDTreeNode import KDTreeNode
from typing import List, Text
from pprint import pprint

import matplotlib.pyplot as plt

class KDTree:
    def __init__(self, point=(0, 0)):
        self.root = KDTreeNode(point, 0)

    def insert(self, point):
        '''
        Inserts a new KDTreeNode into the KDTree thru an iterative approach
        returns the node that was created
        '''
        depth = 0
        current_node = self.root
        new_node = KDTreeNode(point, depth)
        new_node.parent = self.nearest_neighbor(point)
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

    def getPoints_InOrderTraversal(self, node, output_list: List):
        """
        Takes in a list to populate with all of the nodes in the tree in 
        ascending order. This method recursively does in order traversal
        """
        if node is None:
            return
        self.getPoints_InOrderTraversal(node.left, output_list)
        output_list.append(node)
        self.getPoints_InOrderTraversal(node.right, output_list)

    def visualize_inOrderTraversal(self, node: KDTreeNode, side: Text):
        """
        takes in a kdtree node and a string representing if the node is on the 
        left or right side.
        will eventually be placed with a plotting function
        """
        if node is None:
            return
        self.visualize_inOrderTraversal(node.left, "left")
        pprint("Side:{}, node:{}".format(side, node))
        self.visualize_inOrderTraversal(node.right, "right")

    def inOrderTraversal_func(self, node, func):
        """
        A method to run an in order traversal on the tree and call the inputted
        function "func" on every single node in the tree
        """
        if node is None:
            return
        self.inOrderTraversal_func(node.left, func)
        func(node)
        self.inOrderTraversal_func(node.right, func)

    def GetAllNodes(self):
        """
        Returns a list of all nodes in the tree using an In Order Traversal
        """
        nodes = []
        self.getPoints_InOrderTraversal(self.root, nodes)
        return nodes

    def closer_distance(self, target, p1: KDTreeNode, p2: KDTreeNode):
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

    def __nearest_neighbor(self, root: KDTreeNode, point):
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
        best: KDTreeNode = self.closer_distance(
            point, self.__nearest_neighbor(next_branch, point), root)
        # If the splitting plane is closer than the current best, search the other
        # branch in case it contains a closer node
        if best.distance_to_point(point) > root.distance_to_splitting_plane(
                point):
            best = self.closer_distance(
                point, self.__nearest_neighbor(opposite_branch, point), best)

        return best
    def nearest_neighbor(self, point):
        return self.__nearest_neighbor(self.root, point)

    def __PlotTree(self, node: KDTreeNode, fig, ax):
        """
        takes in a kdtree node and plots it on the input figure
        will eventually be placed with a plotting function
        """
        if node is None:
            return
        self.__PlotTree(node.left, fig, ax)
        point_color = "black"
        point_size = 10
        if node.parent is None:
            point_color = "green"
            point_size = 50
        ax.scatter(node.p[0], node.p[1], c=point_color, s=point_size)
        if node.parent is not None:
            line_color = "black"
            if node.isOnGoalPath:
                line_color = 'blue'
            x = [node.p[0], node.parent.p[0]]
            y = [node.p[1], node.parent.p[1]]
            ax.plot(x,y, c=line_color)
        self.__PlotTree(node.right, fig, ax)

    def PlotTree(self, fig, ax):
        self.__PlotTree(self.root, fig, ax)

if __name__ == '__main__':
    tree = KDTree((11, 10))
    tree.insert((4, 7))
    node = tree.insert((16, 10))
    tree.insert((7, 13))
    tree.insert((14, 11))
    tree.insert((9, 4))
    tree.insert((15, 3))
    node.set_goal_path()
    outputList = tree.GetAllNodes()

    pivot = [14,9]
    print(tree.nearest_neighbor(pivot))
    fig, ax = plt.subplots()
    
    tree.PlotTree(fig, ax)

    plt.show()
    
    
