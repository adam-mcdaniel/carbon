
print("BUILD MERGE REQUEST")

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

list = ["testing", 1, [5, 6, 7, 8], 2, 3, "whoa", f]
print(list[2])
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


void list(Machine& {MACHINE_NAME}) {{
	std::vector<std::shared_ptr<Object>> list;
	auto length = {MACHINE_NAME}.pop()->get<double>().unwrap();

	for (int i=0; i < length; i++) {{
		list.push_back({MACHINE_NAME}.pop());
	}}

	{MACHINE_NAME}.push(Object::List(list));
}}


int main() {{
	auto {MACHINE_NAME} = Machine();
	{MACHINE_NAME}.push(Object::Fn(table));
	{MACHINE_NAME}.push(Object::String("Table"));
	{MACHINE_NAME}.store();
	{MACHINE_NAME}.push(Object::Fn(print));
	{MACHINE_NAME}.push(Object::String("print"));
	{MACHINE_NAME}.store();
	{MACHINE_NAME}.push(Object::Fn(list));
	{MACHINE_NAME}.push(Object::String("list"));
	{MACHINE_NAME}.store();
	
	{compiled_script}
	std::cout << {MACHINE_NAME}.format() << std::endl;
}}

''')
