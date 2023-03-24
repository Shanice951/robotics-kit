function turnright (time: number) {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 100)
    basic.pause(400)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
}
input.onButtonPressed(Button.A, function () {
    driveforward(1500)
    turnright(400)
    driveforward(1000)
    turnleft(400)
    driveforward(1500)
    turnleft(400)
    driveforward(2000)
})
function reverse (time2: number) {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 100)
    basic.pause(400)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
}
function driveforward (time3: number) {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 100)
    basic.pause(400)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
}
function turnleft (time4: number) {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 100)
    basic.pause(400)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
}
basic.showIcon(IconNames.Happy)
basic.pause(2000)
basic.showString("HELLO")
