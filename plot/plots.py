from matplotlib import pyplot as plt
from numpy import (
    max,
    min,
    mean,
)

from cluster.models import Cluster


def figure(func):
    """
    A decorator for creating a new Matplotlib figure before executing a plotting function.

    This decorator can be applied to functions that generate Matplotlib plots. It ensures that a new
    Matplotlib figure is created before the decorated function is called. This can be useful to prevent
    multiple plots from overlaying each other in the same figure.

    Parameters:
        func (function): The plotting function to be decorated.

    Returns:
        function: A wrapped function that creates a new Matplotlib figure and then calls the original function.
    """

    def wrapper(*args, **kwargs):
        plt.figure()
        func(*args, **kwargs)

    return wrapper


@figure
def linear_plot(data: list, y_label: str, title: str) -> None:
    """
    Creates a line plot based on the provided data and saves it to a file.
    :param data: List of data for plotting.
    :param y_label: Label for the y-axis.
    :param title: Title of the plot.

    :return: No return value. Saves the linear chart as 'images/linear.png'.
    """
    plt.plot(data)
    plt.ylabel(y_label)
    plt.axhline(value := min(data), color='red', linestyle='--', label=f'Min: {value:.4}')
    plt.axhline(value := max(data), color='green', linestyle='--', label=f'Max: {value:.4}')
    plt.axhline(value := float(mean(data)), color='blue', linestyle='--', label=f'Mean: {value:.4}')
    plt.legend()
    plt.title(title)
    plt.savefig(f'images/linear.png')


@figure
def circular_plot(clusters: list[Cluster], title: str) -> None:
    """
    Creates a pie chart based on cluster data and saves it as an image.

    :param clusters :type clusters list[Cluster]: List of Cluster objects representing data clusters.
    :param title: Title for the pie chart.
    :return: No return value. Saves the pie chart as 'images/circular.png'.
    """
    counts, labels = zip(*[
        (cluster.count, f"Count: {cluster.count}\nRange: {cluster.range}")
        for cluster in clusters
    ])

    plt.figure(figsize=(15, 18))
    plt.pie(counts, labels=labels)
    plt.axis('equal')
    plt.title(title)
    plt.savefig(f'images/circular.png')


@figure
def columnar_plot(clusters: list[Cluster], title: str) -> None:
    """
    Creates a bar chart based on cluster data and saves it as an image.

    :param clusters: List of Cluster objects representing data clusters.
    :param title: Title for the bar chart.
    :return: No return value. Saves the bar chart as 'images/columnar.png'.
    """
    plt.figure(figsize=(12, 8))
    counts, labels = zip(*[
        (cluster.count, f"Count: {cluster.count}\nRange: {cluster.range}")
        for cluster in clusters
    ])

    plt.bar(labels, counts)
    plt.title(title)
    plt.savefig(f'images/columnar.png')
