# import eventlet
# import socketio

# sio = socketio.Server(cors_allowed_origins='http://localhost:3000')
# app = socketio.WSGIApp(sio)

# @sio.event
# def connect(sid, environ):
#     print(f"User Connected: {sid}")

# @sio.event
# def join_room(sid, data):
#     print(f"Room Joined: {data}")
#     sio.enter_room(sid, data)

# @sio.event
# def send_message(sid, data):
#     print(f"Sending Message: {data}")
#     sio.emit("receive_message", data, room=data['room'], skip_sid=sid)

# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('localhost', 3001)), app)

import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='http://localhost:3000')
app = socketio.WSGIApp(sio)


# Possible events
@sio.event
def connect(sid, environ):
    print(f"User Connected: {sid}")

@sio.event
def join_room(sid, data):
    print(f"Room Joined: {data}")
    sio.enter_room(sid, data)

@sio.event
def send_message(sid, data):
    print(f"Sending Message: {data}")
    sio.emit("receive_message", data, room=data['room'], skip_sid=sid)

@sio.event
def debug_message(sid, data):
    print(f"Debug Message: {data} from {sid} @ {data['room']}")
    actualMsg = data["debugMsg"]
    print(f"\n\nDebug Message is: {actualMsg}\n\n")

    import socket

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 3005  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"STATUS!")
        # d = s.recv(1024)

    # print(f"Received {d!r}")

if __name__ == '__main__':
    print("""
    
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        PYTHON SOCKET SERVER BACKEND

    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    """)

    eventlet.wsgi.server(eventlet.listen(('localhost', 3001)), app)