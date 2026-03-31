cmake_minimum_required(VERSION 3.10)
project(python_caller)

set(CMAKE_CXX_STANDARD 11)

add_library(python_caller python_caller.cpp)
target_include_directories(python_caller PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(test test.cpp)
target_link_libraries(test python_caller)
