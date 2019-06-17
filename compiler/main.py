from tokens import MACHINE_NAME
from parser import parse

compiled_script = parse('''
# This is a quick compiler that I slapped together to target Dragon.
# Hopefully this will get better in the future!
class std::fs::File:
	def open(self, filename):
		print("You're trying to open '", filename, "'")
		self.filename = filename

File = std::fs::File

f = File()
f.open("testing")
print(f)
''')


print(f'''#include "dragon.hpp"
#include <iostream>

using namespace dragon;


void table(Machine& {MACHINE_NAME}) {{
	{MACHINE_NAME}.push(Object::Map());
}}


void print(Machine& {MACHINE_NAME}) {{
	auto param = *{MACHINE_NAME}.pop();
	while (!param.is_none()) {{
		std::cout << param.format();
		param = *{MACHINE_NAME}.pop();
	}}
	std::cout << std::endl;
}}


int main() {{
	auto {MACHINE_NAME} = Machine();
	{MACHINE_NAME}.push(Object::Fn(table));
	{MACHINE_NAME}.push(Object::String("Table"));
	{MACHINE_NAME}.store();
	{MACHINE_NAME}.push(Object::Fn(print));
	{MACHINE_NAME}.push(Object::String("print"));
	{MACHINE_NAME}.store();
	
	{compiled_script}
	std::cout << {MACHINE_NAME}.format() << std::endl;
}}

''')