This test contains the following:

- python_server\server.py
    - A minimal Python webserver using http.server package
- python_client\client.py
    - A minimal Python client using httplib2 that performs some GET and POST to the server

- client.Dockerfile and server.Dockerfile
    - Docker files for building an images of both python scripts

- build_images.bat
    - Calls docker build with some parameters for both docker files

- run_containters.bat
    - Creates a network
    - Calls docker run with some parameters for both docker files
    - Both containers connects to the network and have aliases
    - Alias is used in python_client\client.py to connect to the server in the other container

