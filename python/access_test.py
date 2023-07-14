import requests
import time

url = 'https://test.lifewithpiano-cloudpractice.com/'

#条件を満たす場合、True判定。
all_ok = True

#カウント変数の設定
count_200 = 0
count_not_200 = 0

#処理時間スタートポイント
point1 = time.time()

#アクセス回数を設定
for i in range(50):
    response = requests.get(url, timeout=1)
    print(response.status_code)
    
    #ステータスコードが200の場合、累算代入演算子によりcount_200に1ずつプラス
    if response.status_code == 200:
        count_200 += 1

    #上記を満たさない場合、all_ok判定はFalse、累算代入演算子によりcount_not_200に1ずつプラス
    else :
        all_ok = False
        count_not_200 += 1

#処理時間ゴールポイント
point2 = time.time()

if all_ok:
    print("Success")
else:
    print("Failed")
#f-stringでカウント変数を文字列内にフォーマットとして出力
print(f"Success: {count_200}")
print(f"Failed: {count_not_200} ")

#処理時間の計算
processing_time = point2 - point1
print(f"アクセス処理時間: {processing_time}")