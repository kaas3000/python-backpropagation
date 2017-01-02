from ActivationFunctions.ActivationFunction import ActivationFunction


class StepFunction(ActivationFunction):
    def __init__(self):
        super().__init__()

    @staticmethod
    def calculate_output(self, input):
        result = 0

        if (input >= 0):
            result = 1
        else:
            result = -1

        return result
