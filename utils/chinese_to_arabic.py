""" 中文'數字'轉換後 +1 """


def increment_chinese_name(name):
    """對 NAME 的中文數字部分加 1, 返回更新後的名稱"""
    chinese_to_arabic = {
        "零": 0,
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
    }
    arabic_to_chinese = {v: k for k, v in chinese_to_arabic.items()}  # 將對應表反向
    # 提取非數字部分（例如 "打工"）
    name_prefix = "".join(
        [c for c in name if c not in chinese_to_arabic]
    )
    # 提取數字部分（例如 "一"）
    if name_number := "".join([c for c in name if c in chinese_to_arabic]):
        # 將中文數字轉換為阿拉伯數字，加 1，然後再轉回中文數字
        arabic_number = sum(
            chinese_to_arabic[c] * (10**i) for i, c in enumerate(reversed(name_number))
        )
        new_number = arabic_number + 1
        # 將加 1 後的阿拉伯數字轉回中文數字
        new_name_number = "".join(
            arabic_to_chinese[int(digit)] for digit in str(new_number)
        )
    else:
        new_name_number = "一"

    return f"{name_prefix}{new_name_number}"


if __name__ == "__main__":
    NAME = "測試中文數字轉換一"
    NEW_NAME = increment_chinese_name(NAME)
    print(f"{NAME} > {NEW_NAME}")
