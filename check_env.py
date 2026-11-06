import sys
import netmiko

print("Python:", sys.version.split()[0])
print("venv:", sys.prefix)
print("netmiko:", netmiko.__version__)