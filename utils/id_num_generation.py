""" 身分證產生器 """

import random

def generate_id_number() -> str:
    """生成符合台灣規範的隨機身分證號"""
    area_codes = {  # 台灣地區代碼字母對應表
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 34,
        "J": 18,
        "K": 19,
        "L": 20,
        "M": 21,
        "N": 22,
        "O": 35,
        "P": 23,
        "Q": 24,
        "R": 25,
        "S": 26,
        "T": 27,
        "U": 28,
        "V": 29,
        "W": 32,
        "X": 30,
        "Y": 31,
        "Z": 33,
    }
    # 隨機選擇地區代碼和對應數值
    area_letter = random.choice(list(area_codes.keys()))
    area_value = area_codes[area_letter]
    # 隨機生成性別數字 (1: 男, 2: 女)
    gender_digit = random.choice([1, 2])
    # 生成隨機的後7位數字
    random_digits = [random.randint(0, 9) for _ in range(7)]
    # 計算檢查碼
    id_without_checksum = (
        [int(d) for d in f"{area_value:02}"] + [gender_digit] + random_digits
    )
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    checksum = sum(d * w for d, w in zip(id_without_checksum, weights)) % 10
    checksum_digit = (10 - checksum) % 10
    return f"{area_letter}{gender_digit}{''.join(map(str, random_digits))}{checksum_digit}"


if __name__ == "__main__":
    # 測試生成器
    GENERATED_ID = generate_id_number()
    print("生成的身分證號是:", GENERATED_ID)
