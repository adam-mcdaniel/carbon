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


void list(Machine& carbon) {
	std::vector<std::shared_ptr<Object>> list;
	auto length = carbon.pop()->get<double>().unwrap();

	for (int i=0; i < length; i++) {
		list.push_back(carbon.pop());
	}

	carbon.push(Object::List(list));
}


int main() {
	auto carbon = Machine();
	carbon.push(Object::Fn(table));
	carbon.push(Object::String("std::Table"));
	carbon.store();
	carbon.push(Object::Fn(print));
	carbon.push(Object::String("print"));
	carbon.store();
	carbon.push(Object::Fn(list));
	carbon.push(Object::String("std::List"));
	carbon.store();
	
	carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("std::Table"));;carbon.load();carbon.call();
carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::String("IT WORKED"));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();

}));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("new"));;carbon.index();carbon.assign();
carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::String("mapped!"));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
}));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("map"));;carbon.index();carbon.assign();
carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();carbon.push(Object::String("filename"));;carbon.store();
carbon.push(Object::String("'"));carbon.push(Object::String("filename"));;carbon.load();carbon.push(Object::String("You're trying to open '"));carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("filename"));;carbon.load();;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
}));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();}));carbon.push(Object::String("std::fs::File"));;carbon.store();
carbon.push(Object::String("std::fs::File"));;carbon.load();carbon.clone();carbon.push(Object::String("File"));;carbon.store();
carbon.push(Object::String("File"));;carbon.load();carbon.call();carbon.push(Object::String("File"));;carbon.load();carbon.call();;
carbon.push(Object::String("new"));;carbon.index();carbon.call();carbon.clone();carbon.push(Object::String("a"));;carbon.store();
carbon.push(Object::String("a"));;carbon.load();carbon.clone();carbon.push(Object::String("b"));;carbon.store();
carbon.push(Object::String("test"));carbon.push(Object::String("a"));;carbon.load();carbon.push(Object::String("a"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.call();
carbon.push(Object::String("b"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.push(Object::String("print"));;carbon.load();carbon.call();
	std::cout << carbon.format() << std::endl;
}


