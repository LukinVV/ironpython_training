class Group:

    def __init__(self, name=None):

        self.name = name
        self.id = id

    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return self.name == other.name


    def key(self):
            return self.name
