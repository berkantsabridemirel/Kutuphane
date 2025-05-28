import time

# 11 harf: A'dan J'ye (A, B, ..., J)
letters = [chr(i) for i in range(ord('A'), ord('A') + 11)]  # ['A', 'B', ..., 'J']

# 10'dan 0'a geri sayım
print("Geri sayım başlıyor:")
for i in range(10, -1, -1):
    letter_index = 10 - i  # A için 0, J için 10
    print(f"{i} - {letters[letter_index]}")
    time.sleep(0.5)

# 0'dan 10'a ileri sayım
print("\nİleri sayım başlıyor:")
for i in range(0, 11):
    letter_index = i  # A için 0, J için 10
    print(f"{i} - {letters[letter_index]}")
    time.sleep(0.5)
