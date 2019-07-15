from tokens import MACHINE_NAME
from parser import parse

compiled_script = parse('''
# This is a quick compiler that I slapped together to target Dragon.
# Hopefully this will get better in the future!
class std::fs::File {
	fn new(self) {
		self.filename = "IT WORKED"
		return self
	}

	fn map(self) {
		self.filename = "mapped!"
	}

	fn open(self, filename) {
		print("You're trying to open '")
		print(filename)
		println("'")
		self.filename = filename
		return self
	}
}


File = std::fs::File
a = File().new()
b = a
a.open("test")
println(b.open("hmm"))



fn(a, b) {

	return fn(f) {
		print("testing: {a=")
		print(a)
		print(", b=")
		print(b)
		println("}")
		print("also c is ")
		println(f)
	}

}(1, 2)(0)



''')


print(f'''#include "dragon.hpp"
#include <iostream>

using namespace dragon;
typedef Function<Machine &, void, Machine> Fn;

void table(Machine& {MACHINE_NAME}) {{
	{MACHINE_NAME}.push(Object::Map());
}}

void print(Machine& {MACHINE_NAME}) {{
	std::cout << {MACHINE_NAME}.pop()->format();
}}

void println(Machine& {MACHINE_NAME}) {{
	std::cout << {MACHINE_NAME}.pop()->format() << std::endl;
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
	{MACHINE_NAME}.push(Object::Fn(Fn(table, {MACHINE_NAME})));
	{MACHINE_NAME}.push(Object::String("std::Table"));
	{MACHINE_NAME}.store();
	{MACHINE_NAME}.push(Object::Fn(Fn(print, {MACHINE_NAME})));
	{MACHINE_NAME}.push(Object::String("print"));
	{MACHINE_NAME}.store();
	{MACHINE_NAME}.push(Object::Fn(Fn(println, {MACHINE_NAME})));
	{MACHINE_NAME}.push(Object::String("println"));
	{MACHINE_NAME}.store();
	{MACHINE_NAME}.push(Object::Fn(Fn(list, {MACHINE_NAME})));
	{MACHINE_NAME}.push(Object::String("std::List"));
	{MACHINE_NAME}.store();
	
	{compiled_script}
	std::cout << {MACHINE_NAME}.format() << std::endl;
}}

''')