rem call docker run -it testing/client:1.0 sh

call docker network create base_network
call docker run --name py_server --network base_network -d -p 3000:3000 testing/server:1.0
call docker run --name py_client --network base_network -d testing/client:1.0