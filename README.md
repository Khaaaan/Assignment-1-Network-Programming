# Assignment-1-Network-Programming
## Description
This is an application based on low-lewel network programming ( socket programming)
to send packets by UDP from client to server and create possibility of pasckets dropping to make application a bit close to real conditions. Moreover it uses exponential backoff technique to avoid packet loss.


## Installation

To clone this repository to your local device


```bash
git clone https://github.com/Khaaaan/Assignment-1-Network-Programming.git
```
To download requirements modules 
```bash
pip install -r requirements.txt
```

## Usage
To run a server with 0.0.0.0 IP address which accept connections not only from other applications on the same device but also from other devices
```python
python3 Task_1_OOP.py server ""
```
To run a client
```python
python3 Task_1_OOP.py client ""
```
You could choose another port for you server (default is 1060)
```python
python3 Task_1_OOP.py server "" [yourPort]
```
