call docker build -t xtremi/test_cpp:1.0 -f %~pd0/../build.Dockerfile .
call docker run -v install:/build/install/bin xtremi/test_cpp:1.0

call docker build -t xtremi/test_cpp_run:1.0 -f %~pd0/../run.Dockerfile .
call docker run -v install:/install/bin xtremi/test_cpp_run:1.0