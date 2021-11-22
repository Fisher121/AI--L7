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
            activation += weights[i] * inputs[i]
        return activation
