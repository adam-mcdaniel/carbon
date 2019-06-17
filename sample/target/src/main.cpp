#include "dragon.hpp"
#include <iostream>

using namespace dragon;


void table(Machine& carbon) {
	carbon.push(Object::Map());
}


void print(Machine& carbon) {
	auto param = *carbon.pop();
	while (!param.is_none()) {
		std::cout << param.format();
		param = *carbon.pop();
	}
	std::cout << std::endl;
}


int main() {
	auto carbon = Machine();
	carbon.push(Object::Fn(table));
	carbon.push(Object::String("Table"));
	carbon.store();
	carbon.push(Object::Fn(print));
	carbon.push(Object::String("print"));
	carbon.store();
	
	carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("Table"));;carbon.load();carbon.call();
carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();carbon.push(Object::String("filename"));;carbon.store();
carbon.push(Object::String("'"));carbon.push(Object::String("filename"));;carbon.load();carbon.push(Object::String("You're trying to open '"));carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("filename"));;carbon.load();;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
}));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();}));carbon.push(Object::String("std::fs::File"));;carbon.store();
carbon.push(Object::String("std::fs::File"));;carbon.load();carbon.push(Object::String("File"));;carbon.store();
carbon.push(Object::String("File"));;carbon.load();carbon.call();carbon.push(Object::String("f"));;carbon.store();
carbon.push(Object::String("testing"));carbon.push(Object::String("f"));;carbon.load();carbon.push(Object::String("f"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.call();
carbon.push(Object::String("f"));;carbon.load();carbon.push(Object::String("print"));;carbon.load();carbon.call();
	std::cout << carbon.format() << std::endl;
}


