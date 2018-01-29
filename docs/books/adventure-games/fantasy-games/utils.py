# open the file, output in groups of 8 bytes
filename = "/home/adlaws/Desktop/characters.901225-01.bin"
with open(filename, "rb") as f:
    char_bytes = f.read(8)
    while char_bytes != b'':
        print('{},'.format(str([x for x in char_bytes])))
        char_bytes = f.read(8)


# open the file, reverse the bits and output in groups of 8 bytes
filename = "/home/adlaws/Desktop/characters.901225-01.bin"
with open(filename, "rb") as f:
    char_bytes = f.read(8)
    while char_bytes != b'':
        bit_reversed_bytes = []
        for b in char_bytes:
            bit_reversed_byte = int(format(b, '08b')[::-1], 2)
            bit_reversed_bytes.append(bit_reversed_byte)
        print('{},'.format(str([x for x in bit_reversed_bytes])))
        char_bytes = f.read(8)



for chunk in range(0,len(bytes),16):
    print(str([x for x in bytes[chunk:chunk+16]])+',')