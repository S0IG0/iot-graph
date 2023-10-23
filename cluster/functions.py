from sklearn.cluster import DBSCAN
import numpy as np

from cluster.models import Cluster

# Maximum distance between data points in a cluster
# Minimum number of data points required to form a cluster
SETTINGS = (0.1, 2)


def find_cluster(data: list, settings=None) -> list[Cluster]:
    """
    Find clusters in the given data using DBSCAN and return a list of clusters.

    :param settings:
    :param data: List of data points.
    :return: List of Cluster objects, each representing a cluster with count and interval.
    """
    data = np.array(data).reshape(-1, 1)  # Convert data to a format suitable for DBSCAN

    if settings is None:
        settings = SETTINGS

    eps, min_samples = settings

    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(data)

    labels = dbscan.labels_  # Get cluster labels
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)  # Determine the number of clusters
    clustered_data = [data[labels == i] for i in range(n_clusters)]  # Group data by clusters

    return [
        Cluster(len(cluster), (np.min(cluster), np.max(cluster)))
        for cluster in clustered_data if len(cluster) > 0
    ]
