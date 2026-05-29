set dotenv-load

# Mostrar comandos disponibles
default:
    @just --list

# Ejecutar el programa IoT
run:
    uv run python3 -u src/main.py

# Leer todos los topics del broker
all:
    mosquitto_sub -h "${MQTT_BROKER}" -t "#" -v

# Leer todos los topics de un prefijo específico
topic t:
    mosquitto_sub -h "${MQTT_BROKER}" -t "{{t}}/#" -v

# Leer solo los topics de un nodo específico
node n:
    mosquitto_sub -h "${MQTT_BROKER}" -t "${MQTT_TOPIC_PREFIX}/{{n}}/#" -v

# Leer un sensor específico de cualquier nodo
sensor s:
    mosquitto_sub -h "${MQTT_BROKER}" -t "${MQTT_TOPIC_PREFIX}/+/{{s}}" -v
