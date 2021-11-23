from random import random
from Neuron import Neuron

class Stare:
    x1 = []
    x2 = []
    y = []
    matrix = []
    n = 0  # numarul de epoci
    LR = 0  # rata de invatare
    network = list()

    # calculati rata de eroare

    def __init__(self, filename, n, lr):
        self.n = n
        self.LR = lr

        ml = 0
        with open(filename) as file:
            for line in file:
                line = line.replace(" ", ",")
                line = line.replace("\n", "")
                l = line.split(",")
                self.x1.append(l[0])
                self.x2.append(l[1])
                self.y.append(l[2])
                self.matrix.append([])
                self.matrix[ml].append(l[0])
                self.matrix[ml].append(l[1])
                self.matrix[ml].append(l[2])
                ml += 1

    def initialize_network(self,n_inputs, n_hidden, n_outputs):
        network = list()
        hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
        network.append(hidden_layer)
        output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
        network.append(output_layer)
        self.network = network
        return network

    def train_network(self,l_rate, n_epoch, n_outputs):
        for epoch in range(n_epoch):
            sum_error = 0
            for row in self.matrix:
                outputs = Neuron.forward_propagate(self.network, row)
                expected = [0 for i in range(n_outputs)]
                expected[int(row[-1])] = 1
                sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
                Neuron.backward_propagate_error(self.network, expected)
                Neuron.update_weights(self.network, row, l_rate)
            print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))

    def predict(self, row):
        outputs = Neuron.forward_propagate(self.network, row)
        return outputs.index(max(outputs))