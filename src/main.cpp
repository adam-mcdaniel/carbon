#include "dragon.hpp"
#include <iostream>


int main() {
    auto dragon = dragon::Machine();

    std::cout << "Hello, dragon!" << std::endl;

    std::cout << dragon.format() << std::endl;

    return 0;
}