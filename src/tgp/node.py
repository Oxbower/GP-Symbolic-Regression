class node:
    def __init__(self, res=None, op=None):
        self.res = res
        self.args = []
        self.op = op

    def set_res(self, res):
        self.res = res

    def set_arg(self, n_node):
        self.args.append(n_node)

    def set_op(self, op):
        self.op = op