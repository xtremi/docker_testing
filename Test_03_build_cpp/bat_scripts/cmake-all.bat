call %~pd0/cmake-configure.bat
call %~pd0/cmake-build.bat
call %~pd0/cmake-install.bat
call %~pd0../build/install/bin/Test_03_build_cpp.exe "hello from bat script"