import time


def run_loop(readings: list[tuple], interval: float = 1.0) -> None:
    try:
        while True:
            print("- Sensores ", "-" * 38)
            batch: list[tuple] = []

            for cloud, sensor in readings:
                valor = sensor.get_data()
                batch.append((cloud, sensor, valor))
                print(
                    f"{cloud.node} | {sensor.name} - SENSOR_{sensor.node_number} | {sensor.data_type}: {valor}"
                )

            print("-" * 50)

            for cloud, sensor, valor in batch:
                cloud.send(sensor, valor)

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSaliendo...")
    finally:
        print("Programa detenido con éxito")
