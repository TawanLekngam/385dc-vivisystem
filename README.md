# VIVIsystem
socketio server
## Setting up
```
git clone <this-repo>
pip install -r requirements.txt
```

## Running the Server
```
python server.py
```
> Default port is 5000

# Testing

Try testing by running the server and spinning up multiple clients in seperate terminals
```
python server.py
python example.py # Another terminal
python example.py whatever-pond
```

## Using the Client
Put the `models.py` and `client.py` in your own repo.
Just import the class from `client.py` and use it to connect with the server.
See `example.py` for usage example and handlers to register.
> You only need `websocket-client` package

## Deployment Plan
For integration, one guy deploy the server and other ponds with their client just connect to its URL.

For testing, we could just have 1 guy run it locally, use ngrok to forward to it, and others use the ngrok URL.
```
python server.py
ngrok http 5000 --region ap
```
Then get the URL, use `wss` instead of `https`, other clients can connect using this URL.

Another option: Better, but slower. No installation needed
```
python server.py
ssh -R 80:localhost:5000 serveo.net
```
Other clients can connect to URL - Get the forward from URL, use `ws` instead of `https`
> Same URL everytime on same machine, very nice

# Scaling?
Containarize the server.py and run with multiple instances, all connect to message queue like Redis.
Use reverse proxy to load balancer to server instances.
Client connect to reverse proxy.

## Making changes
If there's bug, just make changes. Or some missing fields, add it to models.