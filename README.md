# Simulador IoT de Sensores

Proyecto del taller de IoT que simula sensores de temperatura, humedad y presión,
y envía los datos a un broker MQTT local (Mosquitto).

## Dependencias

- Mosquitto (broker MQTT)
- mosquitto-clients (para poder usar `mosquitto_sub` y `mosquitto_pub`)
- Python ≥ 3.13
- [uv](https://github.com/astral-sh/uv) 
- [just](https://github.com/casey/just)

## Instalación

```bash
git clone https://github.com/sebasflorezo/IoT_Sensors_Simulation.git
cd IoT_Sensors_Simulation
uv sync
```

## Uso (tener en cuenta las variables de entorno)

```bash
# Primero se levanta el server de mosquitto
sudo systemctl start mosquitto.service

# Ahora sí podemos escuchar los topics que lleguen al server
just all

# Y se levanta la aplicación de simulación de estos sensores
just run
```


```bash
just            # Mostrar comandos disponibles
just run        # Ejecutar simulación de sensores
just all        # Escuchar todos los topics MQTT
just casa       # Escuchar topics bajo casa/
just node nodo_1     # Escuchar solo nodo_1
just node nodo_2     # Escuchar solo nodo_2
just sensor tempsensor # Escuchar sensor específico (humesensor, presssensor)
```

## Capturas de prueba

<!-- TODO: Agregar capturas aquí -->
