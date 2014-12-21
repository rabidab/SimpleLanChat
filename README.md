# A minimal chat client that can be user over LAN

### Required packages:

* notify-send
* mtail (if you want to see messages continuously as of in a decent chat client ;) )

## How to use

### Server Side

* Open terminal
* Run server.py:

  `$ python server.py`

### Client Side

* Open new tab terminal
* Change username (alias for chat):

  `$ vim userinfo`
* Change hostname in client.py to IP Address of server:

  `$ vim client.py`
* Run client.py:

  `$ python client.py <message>`

### Stream Chat

* Open new tab terminal
* Stream file lanmessages, output from server.py

  `$ tail -f lanmessages`

## Future
* Stream chat and input chat in same tab
