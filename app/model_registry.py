import importlib
import pkgutil
import sys
from traceback import (
    print_tb,
)

import app


def onerror(name):
    print("Error importing module %s" % name)
    type_, value, traceback = sys.exc_info()
    print_tb(traceback)


def autodiscover_models():
    """
    Function to autoimport models.
    This is necessary so that the alembic can find all the models.
    """
    imported = []
    for module_info in pkgutil.walk_packages(app.__path__, app.__name__ + ".", onerror=onerror):
        if module_info.name.startswith("app.models"):
            importlib.import_module(module_info.name)
            imported.append(module_info.name)

    return imported
