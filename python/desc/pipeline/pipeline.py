"""
Pipeline abstractions
"""
__all__ = ['Pipeline', 'ProcessingNode', 'DataProduct']

class Pipeline(list):
    def __init__(self, name):
        super(Pipeline, self).__init__()
        self.name = name

    def add_processing_node(self, name):
        processing_node = ProcessingNode(name)
        self.append(processing_node)
        return processing_node

class ProcessingNode(object):
    def __init__(self, name):
        self.name = name
        self._inputs = []
        self._outputs = []

    @property
    def inputs(self):
        return self._inputs

    def set_input(self, *args):
        for data_product in args:
            self._inputs.append(data_product)

    @property
    def outputs(self):
        return self._outputs

    def set_output(self, *args):
        for data_product in args:
            data_product.set_parent(self)
            self._outputs.append(data_product)

class DataProduct(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

