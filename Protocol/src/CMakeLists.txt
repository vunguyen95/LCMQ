cmake_minimum_required(VERSION 3.2)
project(source)

set(SOURCE_FILES
    tag.h
    tag.cc
)

add_library(lcmq_source STATIC ${SOURCE_FILES})

