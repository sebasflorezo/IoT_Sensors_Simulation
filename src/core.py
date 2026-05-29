import logging
import time

logger = logging.getLogger(__name__)


def run_loop(readings: list[tuple], interval: float = 1.0) -> None:
    try:
        while True:
            batch: list[tuple] = []

            for cloud, sensor in readings:
                valor = sensor.get_data()
                batch.append((cloud, sensor, valor))
                logger.info(
                    "%s | %s - SENSOR_%s | %s: %s",
                    cloud.node, sensor.name, sensor.node_number,
                    sensor.data_type, valor,
                )

            for cloud, sensor, valor in batch:
                cloud.send(sensor, valor)

            time.sleep(interval)
    except KeyboardInterrupt:
        logger.info("Saliendo...")
    finally:
        logger.info("Programa detenido con éxito")
