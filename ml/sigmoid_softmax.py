import numpy as np
import matplotlib.pyplot as plt


def sigmoid(inputs):
    """
    计算sigmoid
    :param inputs:
    :return:
    """
    return [1 / float(1 + np.exp(-x)) for x in inputs]


def line_graph(x, y, x_title, y_title):
    """
    画sigmoid的图
    :param x:
    :param y:
    :param x_title:
    :param y_title:
    :return:
    """
    plt.plot(x, y)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.show()


def softmax(inputs):
    """
    计算softmax
    :param inputs:
    :return:
    """
    return np.exp(inputs) / float(sum(np.exp(inputs)))


graph_x = range(-20, 20, 1)
graph_y_sigmoid = sigmoid(graph_x)
graph_y_softmax = softmax(graph_x)
print(f"graph x readings: {graph_x}")
print(f"grahp y readings: {graph_y_sigmoid}")
print(f"grahp y readings: {graph_y_softmax}")
line_graph(graph_x, graph_y_sigmoid, "inputs", "sigmoid scores")
line_graph(graph_x, graph_y_softmax, "inputs", "softmax scores")


