from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Tạo khóa AES 128 bit
key = get_random_bytes(16)

# Dữ liệu cần mã hóa
data = "Hello AES".encode()

# Mã hóa
cipher = AES.new(key, AES.MODE_CBC)
encrypted = cipher.encrypt(
    pad(data, AES.block_size)
)

print("Du lieu ban dau:", data.decode())
print("Du lieu ma hoa:", encrypted)

# Giải mã
decipher = AES.new(
    key,
    AES.MODE_CBC,
    cipher.iv
)

decrypted = unpad(
    decipher.decrypt(encrypted),
    AES.block_size
)

print("Du lieu giai ma:", decrypted.decode())