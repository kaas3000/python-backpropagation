from ActivationFunctions.ActivationFunction import ActivationFunction


class Neuron:
    def __init__(self, activation_function: ActivationFunction):
        self.activationFunction = activation_function
        self.value = 0
