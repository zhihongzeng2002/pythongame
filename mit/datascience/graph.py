class Node(object):
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children

    def __str__(self):
        return self.name 

    def print_children(self):
        for child in self.children:
            print(child)

def build_graph(info_dict):
    # build nodes
    nodes = {}
    for k in info_dict:
        nodes[k] = Node(k)

    # build edges
    for k, v in info_dict.items():
        print(k, v)
        children = [nodes[name] for name in v]
        nodes[k].children = children
        # for child_name in v:
        #     print(nodes[k])
        #     nodes[k].children.append(nodes[child_name])
        #     print_nodes(nodes)
            # print(len(nodes[k].children))
            # print(nodes[k].print_children())
    return nodes

def print_graph(nodes):
    for k, v in nodes.items():
        print('{} -> {}'.format(k, v))
        v.print_children()
        print()


data = {
    'boston': ['providence', 'new york'],
    'providence': ['boston', 'new york'],
    'new york': ['chicago'],
    'chicago': ['denver', 'phoenix'],
    'denver': ['phoenix', 'new york'],
    'phoenix': [],
    'los angles': ['boston']
}
n = build_graph(data)
print_graph(n)


