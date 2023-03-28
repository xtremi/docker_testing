FROM alpine:3.17.2

WORKDIR /.

RUN apk add libstdc++

#Or run stuff here (will run when running container)
CMD ["install/bin/Test_03_build_cpp", "hello from second docker file"]
