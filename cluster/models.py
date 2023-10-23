from typing import NamedTuple


class Cluster(NamedTuple):
    count: int
    interval: tuple[float, float]

    @property
    def range(self):
        min_value, max_value = self.interval
        return f"{min_value:.4} - {max_value:.4}"