from random import random

from Neuron import Neuron


class Weight(object):
    def __init__(self):
        super().__init__()
        self._weight = random()
        self._neuron_from = None
        self._neuron_to = None

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value: int):
        self._weight = value

    @property
    def neuron_from(self):
        return self._neuron_from

    @neuron_from.setter
    def neuron_from(self, source_neuron: Neuron):
        self._neuron_from = source_neuron

    @property
    def neuron_to(self):
        return self._neuron_to

    @neuron_to.setter
    def neuron_to(self, target_neuron: Neuron):
        self._neuron_to = target_neuron
