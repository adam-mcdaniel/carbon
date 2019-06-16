from tokens import MACHINE_NAME
from parser import parse

compiled_script = parse('''
def testing():
	a = 5
	return a


def nested():
	return "test"

def std::fs::write():
    return nested(), testing()

whoa = std::fs::write


def sub(a, b):
    return a, b


sub(27, 28)
''')


print(f'''#include "dragon.hpp"
#include <iostream>

using namespace dragon;

int main() {{
	auto {MACHINE_NAME} = Machine();
	{compiled_script}
	std::cout << {MACHINE_NAME}.format() << std::endl;
}}

''')