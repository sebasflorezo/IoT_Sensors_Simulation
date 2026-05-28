host := env_var_or_default("MQTT_BROKER", "localhost")
topic_prefix := env_var_or_default("MQTT_TOPIC_PREFIX", "casa")

# Mostrar comandos disponibles
default:
    @just --list

# Ejecutar el programa IoT
run:
    uv run python3 -u src/main.py

# Leer todos los topics del broker
all:
    mosquitto_sub -h {{host}} -t "#" -v

# Leer todos los topics de un prefijo específico
topic t:
    mosquitto_sub -h {{host}} -t "{{t}}/#" -v

# Leer solo los topics de un nodo específico
node n:
    mosquitto_sub -h {{host}} -t "{{topic_prefix}}/{{n}}/#" -v

# Leer un sensor específico de cualquier nodo
sensor s:
    mosquitto_sub -h {{host}} -t "{{topic_prefix}}/+/{{s}}" -v
