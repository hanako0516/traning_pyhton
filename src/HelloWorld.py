
print("ハローワールド")

# 変数定義
a = 7
b = 'あ'

print(str(a) + str(type(a)))
print(b + str(type(b)))

# 四則演算
print(str(8+2))
print(str(8-2))
print(str(8/2))
print(str(type(8/2)))  # 割り算をすると型のタイプがfloatになる
print(str(8*2))

# 条件分岐

a = 'あ'
b = "あ" # ダブルくぉーとも使える
c = 'い'
if a == b:
    print("true")
else:
    print("false")

# 入れ子はインデントで管理される
if a == b:
    print("入れ元")
    if (a == c): #カッコ記号使える
        
          print("入れ子したもの")
        
    print("入れ元(入れ子から出てきた)")

#Pythonにはcaseもswitchもないよ！悲しいね！
#似たようなことをするには、if else を重ねまくるか
#辞書を使う[dic_and_method.py]で試してみる



