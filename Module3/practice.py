# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
password = 25

# 1.告訴使用者需要輸入的數字範圍 input()
while True:
    try:
        num = int(input("請輸入數字1~100:"))
    except:
        print("請輸入數字")
        continue

    if num == password:
        print("恭喜中獎")
        break
    elif num > 100 or num < 1:
        print("超出範圍請重新輸入")
        continue
    elif num > password:
        print("請輸入更小的數字")
        continue
    elif num < password:
        print("請輸入更大的數字")
        continue

# 2.使用者猜對要回傳「恭喜中獎」，並結束迴圈的執行


# 3.超出範圍要顯示「超出範圍請重新輸入」


# 4.數字太大 要提示「請輸入更小的數字」


# 5.數字太小 要提示「請輸入更大的數字」


