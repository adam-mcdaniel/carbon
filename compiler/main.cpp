#include "dragon.hpp"
#include <iostream>

using namespace dragon;

int main() {
	auto carbon = Machine();
	carbon.push(Object::Fn([](Machine& carbon) {
carbon.push(Object::Number(5));carbon.push(Object::String("a"));;carbon.store();
carbon.push(Object::String("a"));;carbon.load();

}));carbon.push(Object::String("testing"));;carbon.store();
carbon.push(Object::Fn([](Machine& carbon) {
carbon.push(Object::String("test"));

}));carbon.push(Object::String("nested"));;carbon.store();
carbon.push(Object::Fn([](Machine& carbon) {
carbon.push(Object::String("nested"));;carbon.load();carbon.call();
carbon.push(Object::String("testing"));;carbon.load();carbon.call();

}));carbon.push(Object::String("std::fs::write"));;carbon.store();
carbon.push(Object::String("std::fs::write"));;carbon.load();carbon.push(Object::String("whoa"));;carbon.store();
carbon.push(Object::Fn([](Machine& carbon) {carbon.push(Object::String("a"));;carbon.store();carbon.push(Object::String("b"));;carbon.store();
carbon.push(Object::String("a"));;carbon.load();
carbon.push(Object::String("b"));;carbon.load();

}));carbon.push(Object::String("sub"));;carbon.store();
carbon.push(Object::Number(28));carbon.push(Object::Number(27));carbon.push(Object::String("sub"));;carbon.load();carbon.call();
	std::cout << carbon.format() << std::endl;
}


