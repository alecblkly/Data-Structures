class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # We want to check to see if there is a root value
        # If there is no root value, then we want to set the value coming in as the root value
        if self.value is None:
            self.value = value
        # Once there is the root value, then we check to see if the new value is less than the current value
        # if the value is less than the value, then we insert the new value on the left
        # if the value is greater than the value, we use recursion for the next check
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        # If the new value is greater than the current value, then we insert the new value on the right
        # if this value is less than the current value, then we use recursion to go back to the check to insert on the left
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If the target is equal to the root value, returning true
        if target == self.value:
            return True
        # If True is not achieved with the first target, will check if the target is less than the root value
        # Checking less than, would be looking towards the left
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
        # If the target is not on the left, will need to check the right
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # going through left then right node values
        # printing values low to high
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # BFT
    # initialize a queue
    # push root to queue
    # while stack is not empty
    # pop top item out of queue into temp
    # Print/Return what you're doing (low to high, given node, etc.)
    # If temp has right, put into queue
    # If temp has left, put into queue

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # DFT
    # Initialize a stack
    # Push root to stack
    # while stack is not empty
    # pop top item out of stack into temp variable
    # Print/Return what you're doing (low to high, given node, etc.)
    # If temp has right, put it into stack
    # If temp has left, put into stack
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
