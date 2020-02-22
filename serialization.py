"""
Antti Vilkman
0521281
CT30A3401 Distributed Systems
Data serialization
"""
import os
import time
import timeit
import pickle
import matplotlib.pyplot as plt 
import csv
import dicttoxml
import json
import msgpack
import yaml
import xml.etree.ElementTree as ET
import pandas as pd


native = {}

for i in range(1,100000):
    key = "key" + str(i)
    native[key] = i


ser_times = []
deser_times = []


def xml_serialize():
    xml = dicttoxml.dicttoxml(native)
    with open('x.xml', 'w') as f:
        f.write(xml.decode())


def json_serialize():
    json_ = json.dumps(native)
    with open('x.json', 'w') as f:
        f.write(json_)


def yaml_serialize():
    yaml_ = yaml.dump(native)
    with open('x.yaml', 'w') as f:
        f.write(yaml_)


def native_deserialize():
    a = pickle.load(open("native.p", "rb"))


def xml_deserialize():
    tree = ET.parse('x.xml')
    root = tree.getroot()


def json_deserialize():
    a = json.load(open('x.json', 'r'))


def msgpack_deserialize():
    a = msgpack.unpack(open("msg.msgpack", 'rb'))


def yaml_deserialize():
    a = yaml.load(open('x.yaml', 'r'), Loader=yaml.FullLoader)


funs = [pickle.dump(native, open("native.p", "wb")),
        xml_serialize(),
        json_serialize(),
        msgpack.pack(native, open("msg.msgpack", 'wb')),
        yaml_serialize()
        ]


de_funs = [native_deserialize(),
           xml_deserialize(),
           json_deserialize(),
           msgpack_deserialize(),
           yaml_deserialize()
           ]


# Plot serialization times
for f in funs:
    ser_times.append(timeit.timeit(str(f), number=1))


plt.figure()
plt.title("Serialization times")
plt.bar(["Pickle (native)", "XML", "JSON", "MessagePack", "YAML"], ser_times)
#plt.show()


# Plot file sizes
files = ['native.p', 'x.xml', 'x.json', 'msg.msgpack', 'x.yaml']
sizes = []

for f in files:
    sizes.append(os.path.getsize(f))

plt.figure()
plt.title("File sizes (bytes)")
plt.bar(["Pickle (native)", "XML", "JSON", "MessagePack", "YAML"], sizes)
#plt.show()


# De-serialization times
for f in de_funs:
    deser_times.append(timeit.timeit(str(f), number=1))

plt.figure()
plt.title("De-serialization times")
plt.bar(["Pickle (native)", "XML", "JSON", "MessagePack", "YAML"], deser_times)
plt.show()

