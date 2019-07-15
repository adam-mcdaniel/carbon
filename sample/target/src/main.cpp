#include "dragon.hpp"
#include <iostream>

using namespace dragon;
typedef Function<Machine &, void, Machine> Fn;

void table(Machine& carbon) {
	carbon.push(Object::Map());
}

void print(Machine& carbon) {
	std::cout << carbon.pop()->format();
}

void println(Machine& carbon) {
	std::cout << carbon.pop()->format() << std::endl;
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
	carbon.push(Object::Fn(Fn(table, carbon)));
	carbon.push(Object::String("std::Table"));
	carbon.store();
	carbon.push(Object::Fn(Fn(print, carbon)));
	carbon.push(Object::String("print"));
	carbon.store();
	carbon.push(Object::Fn(Fn(println, carbon)));
	carbon.push(Object::String("println"));
	carbon.store();
	carbon.push(Object::Fn(Fn(list, carbon)));
	carbon.push(Object::String("std::List"));
	carbon.store();
	
	carbon.push(Object::Fn(Fn([](Machine& carbon) {carbon.push(Object::String("std::Table"));;carbon.load();carbon.call();
carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::Fn(Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::String("IT WORKED"));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();

}, carbon)));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("new"));;carbon.index();carbon.assign();
carbon.push(Object::Fn(Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();
carbon.push(Object::String("mapped!"));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
}, carbon)));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("map"));;carbon.index();carbon.assign();
carbon.push(Object::Fn(Fn([](Machine& carbon) {carbon.push(Object::String("self"));;carbon.store();carbon.push(Object::String("filename"));;carbon.store();
carbon.push(Object::String("You're trying to open '"));carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("filename"));;carbon.load();carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("'"));carbon.push(Object::String("println"));;carbon.load();carbon.call();
carbon.push(Object::String("filename"));;carbon.load();;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("filename"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();

}, carbon)));;
carbon.push(Object::String("self"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.assign();
carbon.push(Object::String("self"));;carbon.load();}, carbon)));carbon.push(Object::String("std::fs::File"));;carbon.store();
carbon.push(Object::String("std::fs::File"));;carbon.load();carbon.clone();carbon.push(Object::String("File"));;carbon.store();
carbon.push(Object::String("File"));;carbon.load();carbon.call();carbon.push(Object::String("File"));;carbon.load();carbon.call();;
carbon.push(Object::String("new"));;carbon.index();carbon.call();carbon.clone();carbon.push(Object::String("a"));;carbon.store();
carbon.push(Object::String("a"));;carbon.load();carbon.clone();carbon.push(Object::String("b"));;carbon.store();
carbon.push(Object::String("test"));carbon.push(Object::String("a"));;carbon.load();carbon.push(Object::String("a"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.call();
carbon.push(Object::String("hmm"));carbon.push(Object::String("b"));;carbon.load();carbon.push(Object::String("b"));;carbon.load();;
carbon.push(Object::String("open"));;carbon.index();carbon.call();carbon.push(Object::String("println"));;carbon.load();carbon.call();
carbon.push(Object::Number(0));carbon.push(Object::Number(2));carbon.push(Object::Number(1));carbon.push(Object::Fn(Fn([](Machine& carbon) {carbon.push(Object::String("a"));;carbon.store();carbon.push(Object::String("b"));;carbon.store();;carbon.push(Object::Fn(Fn([](Machine& carbon) {carbon.push(Object::String("f"));;carbon.store();;carbon.push(Object::String("testing: {a="));carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("a"));;carbon.load();carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String(", b="));carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("b"));;carbon.load();carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("}"));carbon.push(Object::String("println"));;carbon.load();carbon.call();
carbon.push(Object::String("also c is "));carbon.push(Object::String("print"));;carbon.load();carbon.call();
carbon.push(Object::String("f"));;carbon.load();carbon.push(Object::String("println"));;carbon.load();carbon.call();
}, carbon)));

}, carbon)));carbon.call();carbon.call();
	std::cout << carbon.format() << std::endl;
}


