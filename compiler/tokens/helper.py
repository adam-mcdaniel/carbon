from .constants import MACHINE_NAME


def store(name):
    return f'{MACHINE_NAME}.push(Object::Str({name})); {MACHINE_NAME}.store();'

def push(name):
    return f'{MACHINE_NAME}.push({name});'

def load(name):
    return f'{MACHINE_NAME}.push(Object::Str({name})); {MACHINE_NAME}.load();'

def assign(name):
    return f'{MACHINE_NAME}.push(Object::Str({name})); {MACHINE_NAME}.assign();'