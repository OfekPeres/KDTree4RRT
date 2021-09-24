# Ofek Peres - 2D Tree for RRT

## Getting Started

- Clone this repo or download the zip (it has two files)
  - `KDTree.py`
  - `KDTreeNode.py`

## TLDR

- Create a KDTree instance (defaults to creating a root node at 0,0)
- Add points to the KDtree using the insert method
  - The insert method returns the instance of the new node
- Call the set_goal_path() function on your goal node.
  - This will set each parent node, to the root, as a member of the goal path, which will highlight them in blue when plotted
- Plot the tree using the

```python
tree = KDTree()

tree.insert([0,1])
tree.insert([0,2])

goal_node = tree.insert([1,1])
goal_node.set_goal_path()


fig, ax = plt.subplots()

tree.PlotTree(tree.root, fig, ax)

plt.show()
```

### KDTreeNode

This class represents a single node in the tree. It has overloaded methods for comparisons like:

1. greater than
1. less than
1. equal

It contains helper methods to calculate distance to another node or to a point in space that is a tuple/array

Can define a node and all of its parents as the goal path by using the set_goal_path() function

### KDTree

- Can create a KDTree with a root anywhere, defaults to (0,0)
- Can insert a point into the KDTree. The insert function returns the node in the tree containing that point
- Can get all of the points in the tree (in order tree traversal aka they will be sorted)
- Can plot the tree
    - Any nodes on the goal path will be have the path between them rendered in blue



