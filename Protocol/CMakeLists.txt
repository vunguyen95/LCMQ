cmake_minimum_required(VERSION 3.2)

project(lcmq)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -lboost_system -O3")
set(SOURCE_FILES test.cc)
include_directories(src)

add_subdirectory(src)


add_executable(test ${SOURCE_FILES})
target_link_libraries(test lcmq_source)
