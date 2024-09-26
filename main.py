def on_forever():
    # 1. Ir hacia el objeto (Avanzar hacia el objeto)
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)  # Ambos motores giran hacia adelante
    basic.pause(2000)  # El Maqueen avanza durante 2 segundos
    
    # 2. Parar al llegar al objeto
    maqueen.motor_stop(maqueen.Motors.ALL)  # Se detienen todos los motores
    basic.pause(500)  # Pausa breve de 0.5 segundos

    # 3. Bajar la pala para recoger el objeto
    maqueen.servo_run(maqueen.Servos.S1, 120)  # El servo baja la pala cargadora
    basic.pause(1000)  # Pausa de 1 segundo para asegurarse que la pala baja completamente

    # 4. Avanzar un poco más para cargar el objeto
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)  # Avanzar con la pala bajada
    basic.pause(1000)  # Avanza durante 1 segundo para "cargar" el objeto
    maqueen.motor_stop(maqueen.Motors.ALL)  # Parar después de cargar
    basic.pause(500)

    # 5. Subir la pala para levantar el objeto
    maqueen.servo_run(maqueen.Servos.S1, 60)  # Sube la pala
    basic.pause(1000)  # Pausa de 1 segundo para asegurarse que la pala se levanta completamente

    # 6. Retroceder hacia el punto de partida
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 50)  # Ambos motores giran en reversa
    basic.pause(1000)  # Retrocede durante 1 segundo

    # 7. Dar media vuelta (girar 180 grados)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)  # Gira solo la rueda izquierda
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)  # Gira solo la rueda derecha
    basic.pause(1500)  # Gira durante 1.5 segundos (ajusta si es necesario)
    maqueen.motor_stop(maqueen.Motors.ALL)  # Detén el giro
    basic.pause(500)  # Pausa breve

    # 8. Volver al punto de partida
    maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)  # Avanza de regreso al punto de partida
    basic.pause(2000)  # Avanza durante 2 segundos para llegar al punto de partida
    maqueen.motor_stop(maqueen.Motors.ALL)  # Parar al llegar

# Ejecutar el ciclo continuamente
basic.forever(on_forever)
