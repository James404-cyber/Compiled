# coding: utf-8

import py_compile
import os
import base64

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file_and_encode(filename):
    with open(filename, 'rb') as file:
        encoded_content = base64.b64encode(file.read()).decode('utf-8')
    return encoded_content

def decode_content(encoded_content):
    decoded_content = base64.b64decode(encoded_content).decode('utf-8')
    return decoded_content

def banner():
    clear()
    encoded_file_content = "CgogG1sxOzkybSAgICBfICAgICAgICAgIF8KG1sxOzkybSAgICAgXCAgICAgICAgLwobWzE7OTJtICAgIF9fXF9fX19fXy8KG1sxOzkybSAgICB8IFsbWzE7MzE7MW3CqRtbMTs5Mm1dICBbG1sxOzMxOzFtwqkbWzE7OTJtXSB84oCLCiAbWzE7OTJtICAgfCAgWxtbMTszM209PT09G1sxOzkybV0gIHwgWytdIEhBQ0tFUlMgQkFOR0xBREVTSCBbK10KG1sxOzkybeKVlOKVkOKVkG8wMOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkDAwb+KVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVlwobWzE7MzE7MW3iloggG1sxOzkybSBb4oCiXSAbWzE7MzE7MW1BdXRob3IgICAgOiAgG1sxOzkybSBKYW1lczQwNF8gICAgICAgICAgIBtbMTszMTsxbSDilogKG1sxOzMxOzFt4paIIBtbMTs5Mm0gW+KAol0gG1sxOzMxOzFtV2hhdHNhcHAgIDogIBtbMTs5Mm0gQmxhY2sgR29sZCAgICAgICAgICAbWzE7MzE7MW0g4paIChtbMTszMTsxbeKWiCAbWzE7OTJtIFvigKJdIBtbMTszMTsxbVdoYXRzYXBwICA6IBtbMTs5Mm0gIEJsYWNrNDA0XyAgICAgICAgICAgG1sxOzMxOzFtIOKWiAobWzE7MzE7MW3iloggG1sxOzkybSBb4oCiXSAbWzE7MzE7MW1Hb3J1cCBGYiAgOiAgG1sxOzkybSBUZXJtdXggQ29tbWFuZCBXb3JsZBtbMTszMTsxbSDilogKG1sxOzMxOzFt4paIIBtbMTs5Mm0gW+KAol0gG1sxOzMxOzFtVmVyc2lvbiAgIDogIBtbMTs5Mm0gMC4xMSAgICAgICAgICAgICAgICAgG1sxOzMxOzFt4paIChtbMTs5Mm3ilZrilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZDilZ0="  # Replace with your encoded file content
    decoded_file_content = decode_content(encoded_file_content)
    print(decoded_file_content)

banner()

# Enter Your File ,which one want to Compiled(Example file.py
print('You Can Compiled With C langauge  pyc Byte Compiled 100%......')
print('This Basically At the Time Safe Code ,You can Use This for your Script \n')
input_file = input("Enter the input file name: ")

# Enter the output file name (Example file.pyc )
output_file = input("Enter the output file name: ")

try:
    py_compile.compile(input_file, cfile=output_file)

    print(f"Successfully compiled '{input_file}' to '{output_file}'.")

except Exception as e:
    print(f"An error occurred while compiling: {e}")
