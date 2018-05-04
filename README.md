# python grpc demo

## install package:

```
pip install -r requirements.txt
```

## simple rpc demo

[sayhi](sayhi/)

server: define a rpc function Greeter receive a parameter name and return a string as 'hi {name}'.

client: connect grpc server and call Greeter function.

test:

terminal 1:
```
> python server.py
```
out put:
```
grpc server running...
```


terminal 2:
```
> python client.py
```

out put:
```
Greet client received:hi grpc
```

