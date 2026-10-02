import pkgutil
from importlib import import_module

for _, name, _ in pkgutil.iter_modules(__path__):
    globals()[name] = import_module(f"{__name__}.{name}")


for _, name, _ in pkgutil.walk_packages(__path__, prefix=f"{__name__}."):
    module = import_module(name)

    symbol_name = name.rsplit(".", 1)[-1]

    if hasattr(module, symbol_name):
        globals()[symbol_name] = getattr(module, symbol_name)