FROM alpine:3.17.2

WORKDIR /.

RUN apk add build-base
RUN apk add g++
RUN apk add cmake

COPY ./src ./src

#Either to stuff here (will run when building image)
RUN cmake -S src -B build -DCMAKE_INSTALL_PREFIX=build/install 
#RUN cmake --build build --config=Release


#Or run stuff here (will run when running container)
CMD cmake --build build --config=Release; \ 
    cmake --install build;                \
    ./build/install/bin/Test_03_build_cpp "hello from docker"
