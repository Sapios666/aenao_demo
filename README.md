# Smart bin workflow

The smart bin workflow consits of 4 processes that run in parallel, namely:
1. weight (door switch driven)
2. current (time elapsed driven)
3. sound
4. vibration
5. have you lost your way?

## Door Switch
This code snippet is based on [this project](https://simonprickett.dev/playing-with-raspberry-pi-door-sensor-fun/).
The purpose is to initiate the measuring process through a door switch event. While the door switch is connected directly to the RPi GPIO pins, the weight sensor is connected to an Arduino Nano and the output is channeled to the RPi via USB.

![image](/images/nano_pinout.png)