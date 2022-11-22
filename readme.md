# README #

## What is this repository for? ##

This repository contains Python code for Security Device that uses a FSM.

Here is the original assignment:
(http://cs.iit.edu/~virgil/cs330/mail.fall2022/pa.html).

This code implements a FSM that has 2 states. It unlocks when the digit 1 is in the input and locks when the digit is 4.

The program discards any other inputs whether it be 
alphabet characters or special characters.

## How do I get set up? ##

Instructions in this README file are for a Windows 11 environment

### Summary of set up ###

You must have 'pyinstaller' installed before you can complete set up.

### Configuration ###

1. Clone the repository:

```
$ git clone https://github.com/jloriso/cs330.git
```

2. Make sure all the unit tests pass:

```
$ pyinstaller --version
```

3. If pyinstaller is not installed then:

```
$ pip install pyinstaller
```

4. Build the executable:

```
$ pyinstaller.exe --onefile project.py
```

5. Change the directory:

```
$ cd dist
```

6. Run the executable:

```
$ "project.exe"
```

You can select for the computer to randomly generate numbers to try and break the lock
or you can select to manual break the lock

For manual enter characters from the keyboard follow by Enter/Return
The application will consume the characters and print 'Lock'/'Unlock' as it encounters 4 or 1 respectively.

### License ###

[GNU Public License](https://www.gnu.org/licenses/gpt-3.0.html)

### Who do I talk to? ###

Email jloriso@hawk.iit.edu