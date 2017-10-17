"""
Pipeline abstractions
"""
import subprocess

__all__ = ['Pipeline', 'ProcessingNode', 'DataProduct']

class Pipeline(list):
    def __init__(self, name):
        super(Pipeline, self).__init__()
        self.name = name

    def add_processing_node(self, name):
        processing_node = ProcessingNode(name)
        self.append(processing_node)
        return processing_node

    @property
    def data_products(self):
        dps = list()
        for processing_node in self:
            dps.extend(processing_node.inputs + processing_node.outputs)
        return set(dps)

    def _write_dag_shapes(self, output):
        output.write('; '.join(['node [shape=ellipse]'] +
                               [x.name for x in self]) + '\n')
        output.write(';'.join(['node [shape=box]'] +
                              ['"%s"' % x.name for x in self.data_products])
                     + '\n')

    def write_dag(self, pngfile):
        dotfile = '.'.join(pngfile.split('.')[:-1]) + '.dot'
        with open(dotfile, 'w') as output:
            output.write('digraph %s {\n' % self.name.replace(' ', '_'))
            self._write_dag_shapes(output)
            for node in self:
                node.write_dag(output)
            output.write('}\n')
        subprocess.check_call('dot -Tpng %s > %s' % (dotfile, pngfile),
                              shell=True)

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

    def write_dag(self, output):
        for dp in self.inputs:
            output.write('"%s" -> %s;\n' % (dp.name, self.name))
        for dp in self.outputs:
            output.write('%s -> "%s";\n' % (self.name, dp.name))

class DataProduct(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._parent = parent

    @property
    def parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent
