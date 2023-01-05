from utils.should_debug import should_debug

def debug(*args, sep=' '):
    if not should_debug(): return
    print(f'[\033[38;2;20;72;220mChestnut\033[0m]\033[31;32m debug: {sep.join([str(a) for a in args])}\033[0m')

def warn(*args, sep=' '):
    print(f'[\033[38;2;20;72;220mChestnut\033[0m]\033[31;33m warn: {sep.join([str(a) for a in args])}\033[0m')

def error(*args, sep=' '):
    print(f'[\033[38;2;20;72;220mChestnut\033[0m]\033[31;91m error: {sep.join([str(a) for a in args])}\033[0m')

def info(*args, sep=' '):
    print(f'[\033[38;2;20;72;220mChestnut\033[0m]\033[31;90m info: {sep.join([str(a) for a in args])}\033[0m')