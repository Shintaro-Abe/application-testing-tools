import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#タスク追加画面へアクセス
driver = webdriver.Chrome()
driver.get('https://test.lifewithpiano-cloudpractice.com/create-page')

#処理時間スタートポイント
point1 = time.time()

#追加ボタンを指定した回数クリック
for i in range(100):
    #create要素のボタンをクリック
    driver.find_element(By.NAME, 'create').click()

#処理時間ゴールポイント
point2 = time.time()

#ウインドウを閉じる
driver.quit()

#処理時間の計算
processing_time = point2 - point1
print(f"アクセス処理時間: {processing_time}")