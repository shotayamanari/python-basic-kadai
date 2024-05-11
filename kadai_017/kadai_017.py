# クラス
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def check_adult(self):
        if self.age >= 20: 
            print(self.name + "は、成人です")
        else:
            print(self.name + "は、未成年です")

# Humanクラスのインスタンスを複数生成してリストに追加
humnan_list = [Human("侍太郎",20),Human("侍花子",19)]

# リストの要素数分だけcheck_adultメソッドを呼び出す
for human in humnan_list:
    human.check_adult()
