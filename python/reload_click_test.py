import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#タスク追加画面へアクセス
driver = webdriver.Chrome()
driver.get('https://test.lifewithpiano-cloudpractice.com/edit-page/2')

#処理時間スタートポイント
point1 = time.time()

#追加ボタンを指定した回数クリック
for i in range(100):
    #フォームの値をクリア。editボタンを押すとリロードして値が復活するため、for文の中に入れる
    driver.find_element(By.NAME, 'task_name').clear()
    driver.find_element(By.NAME, 'task_description').clear()
    driver.find_element(By.NAME, 'assign_person_name').clear()
    driver.find_element(By.NAME, 'estimate_hour').clear()

    #edit要素のボタンをクリック
    driver.find_element(By.NAME, 'edit').click()
    
#処理時間ゴールポイント
point2 = time.time()

#ウインドウを閉じる
driver.quit()

#処理時間の計算
processing_time = point2 - point1
print(f"アクセス処理時間: {processing_time}")
