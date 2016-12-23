from ActivationFunctions.ActivationFunction import ActivationFunction
from Neuron import Neuron
from Weight import Weight


class Layer(object):
    def __init__(self, neurons_amount: int, activation_function: ActivationFunction):
        """
        Instantiate a new Layer
        :param neurons_amount: int
        :param activation_function: ActivationFunction
        """
        super().__init__()

        self._neurons = tuple(Neuron(activation_function) for _ in range(1, neurons_amount))

    @property
    def neurons(self):
        return self._neurons

    def connect_layer(self, layer):
        """
        Add weights between the neurons in two layers (from: layer, to: self)
        :param layer:
        :return:
        """
        for subject_neuron in enumerate(layer.neurons):
            for neuron in enumerate(self.neurons):
                weight = Weight()
                weight.neuron_from = subject_neuron
                weight.neuron_to = neuron
