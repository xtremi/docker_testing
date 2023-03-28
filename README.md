# Docker testing

## Test_01_py_server_client

### Run:

- `build_images.bat`
- `run_containers.bat`
- check log of client container - should show some responses

*(If not on Windows, run the equivalent commands from the `.bat` files)*

### Description:

This test contains the following:

- `python_server\server.py`
    - A minimal Python webserver using `http.server` package
- `python_client\client.py`
    - A minimal Python client using `httplib2` that performs some `GET` and `POST` requests to the server

- `client.Dockerfile` and `server.Dockerfile`
    - Docker files for building an images of both Python scripts

- `build_images.bat`
    - Calls docker build with some parameters for both docker files

- `run_containters.bat`
    - Creates a network
    - Calls docker run with some parameters for both docker files
    - Both containers connects to the network and have aliases
    - Alias is used in python_client\client.py to connect to the server in the other container

## Test_02_docker_compose_py_server_client

### Run:

- `docker-compose up -d` 
- check log of `py_client-1` container - should show some responses

### Description:

Similar to **Test_01_py_server_client**:

- But instead of `.bat` files, uses docker compose `.yml` file
to build images and run containters for python server and client scripts.



## Test_03_build_cpp

### Run (docker compose):

- `docker-compose up -d` 
- Check output in console for `hello world (hello from docker)` and `hello world (hello from second docker file)` 
 
### Run (docker build/run):

- run `bat_scripts\docker_build_and_run.bat`
- Check output in console for `hello world (hello from docker)` and `hello world (hello from second docker file)` 

*(If not on Windows, run the equivalent commands from the `.bat` file)*


### Run (cmake):

- run `cmake-all.bat` 
- Check output in console for `hello world (hello from docker)` and `hello world (hello from bat script)` 
- Or run the 4 cmake scripts in the order (1) configure, (2) build, (3) install, then run the build application
*(If not on Windows, run the equivalent commands from the `.bat` file)*

### Description:

- `src\main.cpp`
    - is the code for a simple cpp application that prints out hello world + first argument.

- `build.Dockerfile`
    - defines an image using alpine + minimum dependecies to build the cpp file with cmake
    - Creating the make files using cmake is done on image build (`docker build`)
    - Building and install using cmake is done on container run (`docker run`) (it also runs the application)
    
- `run.Dockerfile`
    - defines an image using alpine + `libstdc++` and shares the install directory as a docker volume with `build.Dockerfile`
    - Runs the application built from running the container from `build.Dockerfile`
    
- `docker-compose.yml`
    - Defines a setup with the above two images and a shared volume, etc. (run with `docker-compose up`)
    



