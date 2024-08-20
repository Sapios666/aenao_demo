# Smart bin workflow

The smart bin workflow consits of 4 processes that run in parallel, namely:
1. weight (door switch driven)
2. current (time elapsed driven)
3. sound
4. vibration

## Door Switch
This code snippet is based on [this project](https://simonprickett.dev/playing-with-raspberry-pi-door-sensor-fun/).
The purpose is to initiate the measuring procedure through a door switch event.