from machine import Pin, PWM
import time

servoP = PWM(Pin(20))
servo.freq(50)
servoRG = PWM(Pin(19))
servo.freq(50)
servoBP = PWM(Pin(18))
servo.freq(50)
servoEntrada = PWM(Pin(17))
servoEntrada.freq(50)

while True:
    if (CONDICIÓN) == (ROJO):
        time.sleep_ms(1000)
        servoP.duty_ns(500000) # 0°
        servoRG.duty_ns(500000) # 0°
        time.sleep_ms(1000)
        servo.Entrada(1500000) # Abrir entrada
        time.sleep_ms(3000) # 3 segundos
        servo.Entrada(500000) # Cerrar entrada
        

    elif (CONDICIÓN) == (VERDE):
        time.sleep_ms(1000)
        servoP.duty_ns(500000) # 0°
        servoRG.duty_ns(1500000) # 90°
        time.sleep_ms(1000)
        servo.Entrada(1500000) # Abrir entrada
        time.sleep_ms(3000) # 3 segundos
        servo.Entrada(500000) # Cerrar entrada

    elif (CONDICIÓN) == (AZUL):
        time.sleep_ms(1000)
        servoP.duty_ns(1500000) # 90°
        servoRG.duty_ns(500000) # 0°
        time.sleep_ms(1000)
        servo.Entrada(1500000) # Abrir entrada
        time.sleep_ms(3000) # 3 segundos
        servo.Entrada(500000) # Cerrar entrada

    elif (CONDICIÓN) == (BASURA):
        time.sleep_ms(1000)
        servoP.duty_ns(1500000) # 90°
        servoRG.duty_ns(1500000) # 90°
        time.sleep_ms(1000)
        servo.Entrada(1500000) # Abrir entrada
        time.sleep_ms(3000) # 3 segundos
        servo.Entrada(500000) # Cerrar entrada

    else:
        (MOSTRAR EN LA PANTALLA QUE NO SE DETECTA OBJETO)