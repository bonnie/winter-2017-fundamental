class Node(object):
    """Node for graph."""

    def __init__(self, input_name):
        """Assign data at instantiation."""

        # data
        self.name = input_name

        # adjacency list
        self.friends = set()

    def __repr__(self):
        """Handy representation when printed"""

        return "< Node name={} >".format(self.name)

    def make_friends(self, friend):
        """Make friends with person whose node is 'friend'"""

        self.friends.add(friend)
        friend.friends.add(self)


if __name__ == '__main__':

    melissa = Node('Melissa')
    ashley = Node('Ashley')
    stephanie = Node('Stephanie')