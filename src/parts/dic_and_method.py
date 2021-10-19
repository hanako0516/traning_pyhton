
#参考にしたサイト[https://qiita.com/Afo_guard_enthusiast/items/3d6d1c7398f6cfef05c5]


#まずは関数作成
#足し算関数
def cal_add(num1, num2):
    return num1 + num2

#引き算関数
def cal_hiki(num1,num2):
    return num1 - num2

#掛け算関数
def cal_kake(num1, num2):
    return num1 * num2

#割り算関数
def cal_wari(num1, num2):
    return num1 / num2


func_cal = {
    'add' : cal_add,
    'hiki' : cal_hiki,
    'kake' : cal_kake,
    'wari' : cal_wari
}

def calcuration(str ,num1 ,num2):
    val = func_cal[str](num1,num2)
    print(val)
    return val




