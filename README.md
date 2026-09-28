# AN TOÀN VÀ BẢO MẬT THÔNG TIN

## Tìm hiểu các thuật toán mã hóa DES, AES và RSA

Bài tập tìm hiểu về các thuật toán mã hóa hiện đại DES, AES và thuật toán mã hóa bất đối xứng RSA. Đồng thời thực hiện cài đặt AES bằng Python, so sánh tốc độ giữa AES và RSA và tìm hiểu cách kết hợp hai thuật toán.

## Thông tin sinh viên:
+ **Họ và tên:** Trần Lâm Vũ
+ **Lớp:** K59KMT.K01
+ **Mã số sinh viên:** K235510205299
+ **Trường:** Đại học Kỹ thuật Công nghiệp Thái Nguyên

---

# 1. Thuật toán mã hóa DES và AES

## 1.1. DES

DES (Data Encryption Standard) là thuật toán mã hóa đối xứng, sử dụng cùng một khóa bí mật cho cả quá trình mã hóa và giải mã.

### Đặc điểm

- Dữ liệu được chia thành các khối 64 bit.
- Khóa DES có 64 bit, trong đó 56 bit được sử dụng cho mã hóa.
- Quá trình mã hóa gồm 16 vòng.
- Mã hóa và giải mã sử dụng cùng một khóa.
- Hiện nay DES không còn đủ an toàn do kích thước khóa nhỏ.

### Quy trình

```text
Bản rõ
   ↓
Khóa bí mật
   ↓
Mã hóa DES
   ↓
Bản mã
   ↓
Giải mã DES
   ↓
Bản rõ ban đầu
```

---

## 1.2. AES

AES (Advanced Encryption Standard) là thuật toán mã hóa đối xứng được sử dụng phổ biến hiện nay.

AES xử lý dữ liệu theo khối 128 bit và hỗ trợ ba kích thước khóa:

| Phiên bản | Độ dài khóa | Số vòng |
|---|---:|---:|
| AES-128 | 128 bit | 10 |
| AES-192 | 192 bit | 12 |
| AES-256 | 256 bit | 14 |

### Các bước chính của AES

```text
SubBytes
   ↓
ShiftRows
   ↓
MixColumns
   ↓
AddRoundKey
```

Trong vòng cuối của AES không thực hiện bước `MixColumns`.

Quá trình giải mã sử dụng các phép biến đổi ngược để khôi phục lại dữ liệu ban đầu.

---

## 1.3. So sánh DES và AES

| Tiêu chí | DES | AES |
|---|---|---|
| Loại mã hóa | Đối xứng | Đối xứng |
| Kích thước khối | 64 bit | 128 bit |
| Kích thước khóa | 56 bit | 128/192/256 bit |
| Số vòng | 16 | 10/12/14 |
| Độ an toàn hiện nay | Thấp | Cao |
| Mức độ sử dụng | Ít sử dụng | Phổ biến |

AES có kích thước khóa lớn hơn và khả năng bảo mật tốt hơn nên được sử dụng thay thế DES trong nhiều hệ thống hiện nay.

---

# 2. Cài đặt AES bằng Python

Cài đặt thư viện:

```bash
pip install pycryptodome
```

Code AES:

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Dữ liệu cần mã hóa
data = "An toan va bao mat thong tin".encode("utf-8")

# Tạo khóa AES-128
key = get_random_bytes(16)

# Mã hóa
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(
    pad(data, AES.block_size)
)

print("Du lieu goc:", data.decode())
print("Khoa AES:", key.hex())
print("Ban ma:", ciphertext.hex())

# Giải mã
decipher = AES.new(
    key,
    AES.MODE_CBC,
    iv=cipher.iv
)

plaintext = unpad(
    decipher.decrypt(ciphertext),
    AES.block_size
)

print("Du lieu sau khi giai ma:", plaintext.decode())
```

### Kết quả

```text
Dữ liệu gốc
     ↓
Mã hóa AES
     ↓
Bản mã
     ↓
Giải mã AES
     ↓
Dữ liệu ban đầu
```

---

# 3. Thuật toán RSA

RSA là thuật toán mã hóa bất đối xứng.

Khác với AES, RSA sử dụng hai khóa:

```text
Public Key  → Khóa công khai
Private Key → Khóa bí mật
```

Public Key có thể được chia sẻ cho người khác, còn Private Key phải được chủ sở hữu giữ bí mật.

---

## 3.1. Nguyên lý sinh cặp khóa RSA

Quá trình sinh khóa RSA:

**Bước 1:** Chọn hai số nguyên tố `p` và `q`.

**Bước 2:** Tính:

```text
n = p × q
```

**Bước 3:** Tính:

```text
φ(n) = (p - 1)(q - 1)
```

**Bước 4:** Chọn `e` sao cho:

```text
gcd(e, φ(n)) = 1
```

**Bước 5:** Tính `d` sao cho:

```text
e × d ≡ 1 (mod φ(n))
```

Cuối cùng thu được:

```text
Public Key  = (e, n)
Private Key = (d, n)
```

Trong thực tế RSA sử dụng các số nguyên tố rất lớn để đảm bảo độ an toàn.

---

## 3.2. Tạo cặp khóa RSA bằng Python

```python
from Crypto.PublicKey import RSA

# Tạo cặp khóa RSA 2048 bit
key = RSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

print("PUBLIC KEY:")
print(public_key.decode())

print("\nPRIVATE KEY:")
print(private_key.decode())
```

---

# 4. Các mô hình áp dụng RSA

## 4.1. Bảo mật cho người nhận

Người gửi sử dụng Public Key của người nhận để mã hóa thông tin.

```text
Người gửi
    ↓
Public Key người nhận
    ↓
Mã hóa
    ↓
Bản mã
    ↓
Private Key người nhận
    ↓
Giải mã
    ↓
Người nhận
```

Chỉ người sở hữu Private Key tương ứng mới có thể giải mã dữ liệu.

---

## 4.2. Xác thực người gửi

RSA có thể được sử dụng để tạo chữ ký số.

```text
Dữ liệu
   ↓
Tạo giá trị Hash
   ↓
Private Key người gửi
   ↓
Tạo chữ ký
   ↓
Dữ liệu + Chữ ký
   ↓
Public Key người gửi
   ↓
Kiểm tra chữ ký
```

Người nhận sử dụng Public Key của người gửi để kiểm tra chữ ký, qua đó xác thực nguồn gốc và kiểm tra tính toàn vẹn của dữ liệu.

---

## 4.3. Kết hợp cả hai

Có thể kết hợp hai mô hình để vừa bảo mật dữ liệu vừa xác thực người gửi:

```text
Xác thực người gửi
        +
Bảo mật cho người nhận
        ↓
Bảo mật + Xác thực
```

---

# 5. So sánh AES và RSA

| Tiêu chí | AES | RSA |
|---|---|---|
| Loại | Đối xứng | Bất đối xứng |
| Số khóa | 1 khóa | 2 khóa |
| Tốc độ | Nhanh | Chậm hơn |
| Mã hóa dữ liệu lớn | Phù hợp | Không phù hợp |
| Công dụng chính | Mã hóa dữ liệu | Bảo vệ khóa, chữ ký số |

AES có tốc độ mã hóa và giải mã nhanh nên phù hợp với lượng dữ liệu lớn.

RSA yêu cầu nhiều phép tính phức tạp hơn nên có tốc độ chậm hơn AES. Vì vậy RSA thường được sử dụng để bảo vệ khóa hoặc tạo chữ ký số thay vì mã hóa toàn bộ dữ liệu.

---

# 6. Kết hợp RSA và AES

Có thể kết hợp ưu điểm của AES và RSA bằng phương pháp mã hóa lai (Hybrid Encryption).

```text
Tạo khóa AES
      ↓
AES mã hóa dữ liệu
      ↓
RSA mã hóa khóa AES
      ↓
Gửi dữ liệu
      ↓
RSA giải mã khóa AES
      ↓
AES giải mã dữ liệu
```

### Quy trình

1. Tạo ngẫu nhiên một khóa AES.
2. Sử dụng AES để mã hóa dữ liệu.
3. Sử dụng RSA Public Key của người nhận để bảo vệ khóa AES.
4. Gửi bản mã và khóa AES đã được bảo vệ.
5. Người nhận sử dụng RSA Private Key để lấy lại khóa AES.
6. Sử dụng khóa AES để giải mã dữ liệu.

Cách làm này tận dụng tốc độ xử lý nhanh của AES và khả năng bảo vệ, phân phối khóa của RSA.

---

# 7. Kết luận

Qua bài tập có thể thấy:

- DES là thuật toán mã hóa đối xứng nhưng hiện nay không còn đảm bảo mức độ an toàn cần thiết.
- AES là thuật toán mã hóa đối xứng có tốc độ nhanh và độ bảo mật cao.
- RSA là thuật toán bất đối xứng sử dụng Public Key và Private Key.
- AES phù hợp để mã hóa lượng dữ liệu lớn, trong khi RSA phù hợp cho bảo vệ khóa và chữ ký số.
- Kết hợp RSA và AES giúp tận dụng được ưu điểm của cả hai thuật toán.
