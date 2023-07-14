import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#入力値の変数
char = "あいうえおかきくけこ"
num = "100"

#入力する文字列と数値の長さを設定
for i in range(999):
    char += "あいうえおかきくけこ"
for i in range(99):
    num += "000"
    
#タスク追加画面へアクセス
driver = webdriver.Chrome()
driver.get('https://test.lifewithpiano-cloudpractice.com/edit-page/2')

#タスクの要素をリスト化
elements = ['task_name', 'task_description', 'assign_person_name', 'estimate_hour']

#処理時間スタートポイント
point1 = time.time()

#既入力値を削除
for name in elements:
    driver.find_element(By.NAME, name).clear()

#新しい値を入力
del elements[-1] #'estimate_hour'はnum変数のため、リストから除外
for name in elements:
    driver.find_element(By.NAME, name).send_keys(char)
driver.find_element(By.NAME, 'estimate_hour').send_keys(num)

#edit要素のボタンをクリック
driver.find_element(By.NAME, 'edit').click()

#処理時間ゴールポイント
point2 = time.time()

#処理時間の計算
processing_time = point2 - point1
print(f"アクセス処理時間: {processing_time}")

#確認時間
time.sleep(60)

#ウインドウを閉じる
driver.quit()