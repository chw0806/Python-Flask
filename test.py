
import hashlib
string="pythonpool.com"
encoded=string.encode()
result = hashlib.sha256(encoded)
print("String : ", end ="")
print(string)

print(result.hexdigest())


