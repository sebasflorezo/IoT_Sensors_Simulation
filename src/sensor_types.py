import random

from models import Valor


TEMP_RANGE = (20.0, 40.0)
HUM_RANGE = (30.0, 90.0)
PRESS_RANGE = (900.0, 1100.0)
LIGHT_RANGE = (0.0, 100000.0)
AQI_RANGE = (0.0, 500.0)
NOISE_RANGE = (30.0, 120.0)
CO2_RANGE = (400.0, 2000.0)


def temperatura() -> Valor:
    return Valor(round(random.uniform(*TEMP_RANGE), 2), "°C")


def humedad() -> Valor:
    return Valor(round(random.uniform(*HUM_RANGE), 2), "%")


def presion() -> Valor:
    return Valor(round(random.uniform(*PRESS_RANGE), 2), "hPa")


def luz() -> Valor:
    return Valor(round(random.uniform(*LIGHT_RANGE), 1), "lux")


def calidad_aire() -> Valor:
    return Valor(round(random.uniform(*AQI_RANGE), 1), "AQI")


def ruido() -> Valor:
    return Valor(round(random.uniform(*NOISE_RANGE), 1), "dB")


def co2() -> Valor:
    return Valor(round(random.uniform(*CO2_RANGE), 1), "ppm")
