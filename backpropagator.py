from ActivationFunctions.ActivationFunction import ActivationFunction
from Layer import Layer


def main():
    activation_function = ActivationFunction()

    input_layer = Layer(100, activation_function)
    hidden_layer = Layer(10, activation_function)
    output_layer = Layer(100, activation_function)

    input_layer.connect_layer(hidden_layer)
    hidden_layer.connect_layer(output_layer)


if __name__ == "__main__":
    main()
