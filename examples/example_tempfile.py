from tempfile import NamedTemporaryFile

temporary_file = NamedTemporaryFile(suffix='.meyer', mode='rw')
temporary_file.write("Hello World")
temporary_file.flush()

print(temporary_file.readline())