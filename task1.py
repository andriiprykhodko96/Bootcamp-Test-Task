from hashlib import md5

# The task did not mention the hashing algorithm
# So, I chose MD5 at my discretion


def hash_string(string):
    return md5(string.encode()).hexdigest()


if __name__ == '__main__':
    s = "Python Bootcamp"
    hashed = hash_string(s)
    print(hashed)
