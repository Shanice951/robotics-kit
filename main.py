def turnright(time: number):
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(400)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)

def on_button_pressed_a():
    driveforward(1500)
    turnright(400)
    driveforward(1000)
    turnleft(400)
    driveforward(1500)
    turnleft(400)
    driveforward(2000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def reverse(time2: number):
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(400)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)

def on_button_pressed_b():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(5000)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def driveforward(time3: number):
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(400)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
def turnleft(time4: number):
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(400)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
basic.show_icon(IconNames.HAPPY)
kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
    kitronik_klip_motor.MotorDirection.FORWARD,
    100)
kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
    kitronik_klip_motor.MotorDirection.FORWARD,
    100)
basic.pause(5000)
kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)