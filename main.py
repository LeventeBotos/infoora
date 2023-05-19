import encode
import improv

inp = improv.inp("Add meg a stringet", str)
x = encode.encode_string(inp)
y = encode.decode_string(x)

print(f'encoded: {x} decoded: {y}')
