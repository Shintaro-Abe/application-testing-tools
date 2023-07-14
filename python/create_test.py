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
driver.get('https://test.lifewithpiano-cloudpractice.com/create-page')

#タスクの要素をリスト化('estimate_hour'はnum変数のため除く)
elements = ['task_name', 'task_description', 'assign_person_name']

#処理時間スタートポイント
point1 = time.time()

#char変数を入力
for name in elements:
    driver.find_element(By.NAME, name).send_keys(char)
driver.find_element(By.NAME, 'estimate_hour').send_keys(num)

#create要素のボタンをクリック
driver.find_element(By.NAME, 'create').click()

#処理時間ゴールポイント
point2 = time.time()

#処理時間の計算
processing_time = point2 - point1
print(f"アクセス処理時間: {processing_time}")

#確認時間
time.sleep(60)

#ウインドウを閉じる
driver.quit()