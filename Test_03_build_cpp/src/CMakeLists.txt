cmake_minimum_required(VERSION 3.2)
project(Test_03_build_cpp)

add_executable(${PROJECT_NAME} main.cpp)

install(TARGETS ${PROJECT_NAME} DESTINATION bin)