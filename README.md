# Hobbits.py
[![Build Status](https://travis-ci.org/nanspro/Hobbits.py.svg?branch=master)](https://travis-ci.org/nanspro/Hobbits.py/)

Python implementation of hobbits(wire protocol for ethereum 2.0 network testing)

## Perfomance
- [Code Review](https://app.codacy.com/project/nanspro/Hobbits.py/dashboard?bid=13130041)
- Pylint Score 9.87 / 10
## Prerequisites
- Python3

## Installation
`pip install -r requirements.txt`

## Usage
Encode a message

```python
msg = {'protocol': 'EWP', 'call': 'RPC', 'version': '0.2', 'headers': '', 'body': '{"id":1,"method_id":0x00}'}
encoded = marshall(msg)
print(encoded)
```

Decode a message

```python
msg = 'EWP 0.2 RPC 0 25\n{"id":1,"method_id":0x00}'
decoded = parse(msg)
print(decoded)
```

Here is a demo server
```python
server = create()
server.bind(('127.0.0.1', 9000))    
server.listen(10)

while True:
    conn, addr = server.accept()
    print("Received client's request")
    msg = ''
    data = conn.recv(4096)
    msg += data.decode('utf-8')
```

## License

MIT &copy; [Pegasys](https://pegasys.tech/)
