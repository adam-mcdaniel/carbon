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
carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::Number(20));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("five"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();

}));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("new"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();}));carbon.push(Object::String("Sprite"));;carbon.store();
carbon.push(Object::String("Sprite"));;carbon.load();carbon.call();carbon.push(Object::String("Sprite"));;carbon.load();carbon.call();;
carbon.push(Object::String("new"));;carbon.index();carbon.call();carbon.push(Object::String("s"));;carbon.store();
carbon.push(Object::String("s"));;carbon.load();carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("s"));;carbon.load();;
carbon.push(Object::String("new"));;carbon.index();carbon.push(Object::String("print"));;carbon.load();carbon.call();
	std::cout << carbon.format() << std::endl;
}


