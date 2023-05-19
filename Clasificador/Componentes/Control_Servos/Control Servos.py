from machine import PWM, Pin
import utime
import lcd_api
import pico_i2c_lcd
import os

# Configuración de los pines de entrada y salida
led1_pin = machine.Pin(11, machine.Pin.OUT)
led2_pin = machine.Pin(12, machine.Pin.OUT)
led3_pin = machine.Pin(14, machine.Pin.OUT)
led4_pin = machine.Pin(15, machine.Pin.OUT)
button_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Configuración de los pines de los servos
servoP = PWM(Pin(2))
servoP.freq(50)
servoRG = PWM(Pin(19))
servoRG.freq(50)
servoBT = PWM(Pin(20))
servoBT.freq(50)
servoEntrada = PWM(Pin(21))
servoEntrada.freq(50)

# Configuración de la pantalla LCD
i2c = machine.I2C(0, scl=machine.Pin(1), sda=machine.Pin(0), freq=400000)
lcd = pico_i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)

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

lcd.clear()
lcd.move_to(2, 0)
lcd.putstr('CLASIFICADOR')
lcd.move_to(4, 1)
lcd.putstr('DE COLOR')

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
    servoP.duty_ns(500000)
    servoRG.duty_ns(500000)
    servoBT.duty_ns(500000)
    servoEntrada.duty_ns(500000)

    # Si el botón se pulsa
    if button_state == True:
        button_presses += 1

        # Encender los LED correspondientes al número de pulsaciones
        if button_presses == 1:
            utime.sleep_ms(1000)
            servoP.duty_ns(500000) # 0°
            servoRG.duty_ns(500000) # 0°
            utime.sleep_ms(1000)
            servoEntrada.duty_ns(1500000) # Abrir entrada
            utime.sleep_ms(3000) # 3 segundos
            servoEntrada.duty_ns(500000) # Cerrar entrada
            led1_pin.high()
            led2_pin.low()
            led3_pin.low()
            led4_pin.low()
            color = 'Rojo'
            
        elif button_presses == 2:
            utime.sleep_ms(1000)
            servoP.duty_ns(500000) # 0°
            servoRG.duty_ns(1500000) # 90°
            utime.sleep_ms(1000)
            servoEntrada.duty_ns(1500000) # Abrir entrada
            utime.sleep_ms(3000) # 3 segundos
            servoEntrada.duty_ns(500000) # Cerrar entrada
            led1_pin.low()
            led2_pin.high()
            led3_pin.low()
            led4_pin.low()
            color = 'Verde'
            
        elif button_presses == 3:
            utime.sleep_ms(1000)
            servoP.duty_ns(1500000) # 90°
            servoRG.duty_ns(500000) # 0°
            utime.sleep_ms(1000)
            servoEntrada.duty_ns(1500000) # Abrir entrada
            utime.sleep_ms(3000) # 3 segundos
            servoEntrada.duty_ns(500000) # Cerrar entrada
            led1_pin.low()
            led2_pin.low()
            led3_pin.high()
            led4_pin.low()
            color = 'Azul'
            
        elif button_presses == 4:
            utime.sleep_ms(1000)
            servoP.duty_ns(1500000) # 90°
            servoRG.duty_ns(1500000) # 90°
            utime.sleep_ms(1000)
            servoEntrada.duty_ns(1500000) # Abrir entrada
            utime.sleep_ms(3000) # 3 segundos
            servoEntrada.duty_ns(500000) # Cerrar entrada
            led1_pin.low()
            led2_pin.low()
            led3_pin.low()
            led4_pin.high()
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