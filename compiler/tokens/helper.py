from .constants import MACHINE_NAME


def store(name):
    return f'{str(name)};{MACHINE_NAME}.store();'

def push(name):
    return f'{MACHINE_NAME}.push({str(name)});'

def load(name):
    return f'{str(name)};{MACHINE_NAME}.load();'

def assign():
    return f'{MACHINE_NAME}.assign();'