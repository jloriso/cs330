# Memo #

## Coding language ##

The implementation of the security device was scripted in Python

## Description ##

The device will always start in the Locked state.
The program has two main functions of entry for the security device.
First is the manual entry in which it allows the user to freely input a string
to lock and unlock the security device. After an input is entered the program will
discard any character that are not the digits 0-9.
It will then create a Finite State Machine for the Unlock code and lock code.
Using a searching algorithm it will use the FSM to find instances of the Unlock and lock codes in the user input scanning it from left to right.
After checking the current state (locked or unlocked) of the device it will lock and unlock accordingly.
The second function of the program is the forced entry of the security device.
In this function it will randomly generate input with a limit of 24 digits until the device is unlocked.
Once the device is unlocked it will print out how many individual digits were generated to unlock the device.

## Testing ##
In a case of 40 tests using the forced entry:
min: 3,288
max: 5,372,616
avg: 884,053