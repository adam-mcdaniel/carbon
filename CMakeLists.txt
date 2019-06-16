cmake_minimum_required(VERSION 3.10)
project(dragon VERSION 0.1 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -O3")

include(ExternalProject)
set(EXTERNAL_INSTALL_LOCATION ${CMAKE_BINARY_DIR}/external)
ExternalProject_Add(dragon
  GIT_REPOSITORY    https://github.com/adam-mcdaniel/dragon
  CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${EXTERNAL_INSTALL_LOCATION}
)

add_executable(carbon src/main.cpp)
add_dependencies(carbon dragon)
target_include_directories(carbon PUBLIC ${EXTERNAL_INSTALL_LOCATION}/include/)
target_link_libraries(carbon PRIVATE ${EXTERNAL_INSTALL_LOCATION}/lib/libdragon.a)