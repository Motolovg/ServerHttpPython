import chunk
import http.client

conn = http.client.HTTPSConnection("127.0.0.1")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()
conn.request("GET", "/")
r1 = conn.getresponse()
while chunk != r1.read(200):
    print(repr(chunk))

conn = http.client.HTTPSConnection("127.0.0.1")
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()
print(r2.status, r2.reason)

data2 = r2.read()
conn.close()