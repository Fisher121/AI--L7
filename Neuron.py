from math import exp


class Neuron:
    # The sigmoid function
    @staticmethod
    def transfer(activation):
        return 1.0 / (1.0 + exp((-1) * activation))

    # The function used for computing activation above
    @staticmethod
    def activate(weights, inputs):
        activation = weights[-1]
        for i in range(len(weights) - 1):
            activation += weights[i] * float(inputs[i])
        return activation

    @staticmethod
    def forward_propagate(network, row):
        inputs = row
        for layer in network:
            new_inputs = []
            for neuron in layer:
                activation = Neuron.activate(neuron['weights'], inputs)
                neuron['output'] = Neuron.transfer(activation)
                new_inputs.append(neuron['output'])
            inputs = new_inputs
        return inputs

    @staticmethod
    def transfer_derivative(output):
        return output * (1.0 - output)

    @staticmethod
    def backward_propagate_error(network, expected):
        for i in reversed(range(len(network))):
            layer = network[i]
            errors = list()
            if i != len(network) - 1:
                for j in range(len(layer)):
                    error = 0.0
                    for neuron in network[i + 1]:
                        error += (neuron['weights'][j] * neuron['delta'])
                    errors.append(error)
            else:
                for j in range(len(layer)):
                    neuron = layer[j]
                    errors.append(neuron['output'] - expected[j])
            for j in range(len(layer)):
                neuron = layer[j]
                neuron['delta'] = errors[j] * Neuron.transfer_derivative(neuron['output'])
    @staticmethod
    def update_weights(network, row, l_rate):
        for i in range(len(network)):
            inputs = row[:-1]
            if i != 0:
                inputs = [neuron['output'] for neuron in network[i - 1]]
            for neuron in network[i]:
                for j in range(len(inputs)):
                    neuron['weights'][j] -= l_rate * neuron['delta'] * float(inputs[j])
                neuron['weights'][-1] -= l_rate * neuron['delta']
