from importlib.util import module_from_spec, spec_from_file_location
path = '__pycache__/op.cpython-win32-311.pyc'
spec = spec_from_file_location('op.cpython-win32-311', path)
op = module_from_spec(spec)
spec.loader.exec_module(op)
print(op.Bar.decrypt_flag(op.Foo.get_flag()))