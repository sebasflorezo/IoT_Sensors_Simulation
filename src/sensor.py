from threading import Lock
from typing import Callable, ClassVar

from models import Valor


class Sensor:
    _sensor_counter: ClassVar[int] = 0
    _lock: ClassVar[Lock] = Lock()

    def __init__(
        self,
        name: str,
        data_type: str,
        data_function: Callable[[], Valor],
    ) -> None:
        if not callable(data_function):
            raise TypeError("data_function must be callable")

        self.name = name
        self.data_type = data_type
        self.data_function = data_function

        with Sensor._lock:
            Sensor._sensor_counter += 1
            self.node_number: int = Sensor._sensor_counter

    def get_data(self) -> Valor:
        return self.data_function()

    def __str__(self) -> str:
        valor = self.get_data()
        return f"{self.name}\t - SENSOR_{self.node_number} | {self.data_type}: {valor}"

    def __repr__(self) -> str:
        return (
            f"Sensor(name={self.name!r}, data_type={self.data_type!r}, "
            f"node_number={self.node_number})"
        )
