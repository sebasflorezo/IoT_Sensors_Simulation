import random

from models import Valor


TEMP_RANGE = (20.0, 40.0)
HUM_RANGE = (30.0, 90.0)
PRESS_RANGE = (900.0, 1100.0)


def temperatura() -> Valor:
    return Valor(round(random.uniform(*TEMP_RANGE), 2), "°C")


def humedad() -> Valor:
    return Valor(round(random.uniform(*HUM_RANGE), 2), "%")


def presion() -> Valor:
    return Valor(round(random.uniform(*PRESS_RANGE), 2), "hPa")
