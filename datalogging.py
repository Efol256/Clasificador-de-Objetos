import machine
import utime
import lcd_api
import pico_i2c_lcd
import os

# Configuración de los pines de entrada y salida
led1_pin = machine.Pin(28, machine.Pin.OUT)
led2_pin = machine.Pin(27, machine.Pin.OUT)
led3_pin = machine.Pin(2, machine.Pin.OUT)
button_pin = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Configuración de la pantalla LCD
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=400000)
lcd = pico_i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)

# Inicialización de variables
button_presses = 0
last_button_state = False
button_state = False
color = ""

# Función para mostrar el color en la pantalla LCD
def show_color(color):
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr('Color obtenido:')
    lcd.move_to(0, 1)
    lcd.putstr(color)

# Función para crear un archivo de registro
def create_log_file():
    current_time = utime.localtime()
    file_name = "{:04d}-{:02d}-{:02d}_{:02d}-{:02d}-{:02d}_log.txt".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])
    with open(file_name, 'w') as f:
        f.write("Fecha de creación: {}-{}-{} {}:{}:{}\n".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5]))
    return file_name

# Función para agregar una entrada al archivo de registro
def add_log_entry(file_name, entry):
    with open(file_name, 'a') as f:
        f.write(entry + "\n")

# Crear un nuevo archivo de registro
log_file = create_log_file()

# Bucle principal
while True:
    # Detectar el estado del botón
    button_state = button_pin.value()

    # Si el botón se pulsa
    if button_state == True:
        button_presses += 1

        # Encender los LED correspondientes al número de pulsaciones
        if button_presses == 1:
            led1_pin.high()
            led2_pin.low()
            led3_pin.low()
            color = 'Amarillo'
        elif button_presses == 2:
            led1_pin.low()
            led2_pin.high()
            led3_pin.low()
            color = 'Rojo'
        elif button_presses == 3:
            led1_pin.low()
            led2_pin.low()
            led3_pin.high()
            color = 'Verde'
        elif button_presses == 4:
            led1_pin.low()
            led2_pin.low()
            led3_pin.low()
            color = 'Error!'
            button_presses = 0

        # Mostrar el color en la pantalla LCD
        show_color(color)

        # Agregar una entrada al archivo de registro
        current_time = utime.localtime()
        log_entry = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} - {}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5], color)
        add_log_entry(log_file, log_entry)

        # Esperar un tiempo breve para evitar lecturas erróneas del botón
        utime.sleep_ms(50)

        # Actualizar el estado del botón
        last_button_state = button_state
        
        print(button_presses)