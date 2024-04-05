from seleniumbase import Driver
from selenium.webdriver.common.by import By

imfor= dict()
driver= Driver(uc= True, incognito= False)

try:
    driver.get("https://www.wantgoo.com/global")
    figures= driver.find_elements(By.CSS_SELECTOR,"#mainIndex > div > div > table > tbody> tr")
except:
    print("搜集指數資料錯誤")
    
for figure in figures:
    try:
        if figure.find_element(By.CSS_SELECTOR, "td.lt").text== "費城半導體":
            imfor['SOX']= {}
            imfor['SOX']['CLOSE']= float(figure.find_element(By.NAME, "close").text)
            try:imfor['SOX']['CHANGE']= float((figure.find_element(By.NAME, "change").text)[1:])
            except:imfor['SOX']['CHANGE']= 0
            imfor['SOX']['RATE']= float(figure.find_element(By.NAME, "changeRate").text)
    except:
        print("費城半導體資料採掘錯誤")
    
    try:
        if figure.find_element(By.CSS_SELECTOR, "td.lt").text== "加權指數":
            imfor['TAIEX']= {}
            imfor['TAIEX']['CLOSE']= float(figure.find_element(By.NAME, "close").text)
            try:imfor['TAIEX']['CHANGE']= float((figure.find_element(By.NAME, "change").text)[1:])
            except:imfor['TAIEX']['CHANGE']= 0
            imfor['TAIEX']['RATE']= float(figure.find_element(By.NAME, "changeRate").text)
    except:
        print("加權指數資料採掘錯誤")
        
        
    try:
        if figure.find_element(By.CSS_SELECTOR, "td.lt").text== "台指期":
            imfor['TIF']= {}
            imfor['TIF']['CLOSE']= float(figure.find_element(By.NAME, "close").text)
            try:imfor['TIF']['CHANGE']= float((figure.find_element(By.NAME, "change").text)[1:])
            except:imfor['TIF']['CHANGE']= 0
            imfor['TIF']['RATE']= float(figure.find_element(By.NAME, "changeRate").text)
    except:
        print("台指期資料採掘錯誤")
    
    try:
        if figure.find_element(By.CSS_SELECTOR, "td.lt").text== "台積電ADR":
            imfor['TSMC']= {}
            imfor['TSMC']['CLOSE']= float(figure.find_element(By.NAME, "close").text)
            try:imfor['TSMC']['CHANGE']= float((figure.find_element(By.NAME, "change").text)[1:])
            except:imfor['TSMC']['CHANGE']= 0
            imfor['TSMC']['RATE']= float(figure.find_element(By.NAME, "changeRate").text)
    except:
        print("台積電ADR資料採掘錯誤")
    
    try:
        if figure.find_element(By.CSS_SELECTOR, "td.lt").text== "道瓊指數":
            imfor['DJIA']= {}
            imfor['DJIA']['CLOSE']= float(figure.find_element(By.NAME, "close").text)
            try:imfor['DJIA']['CHANGE']= float((figure.find_element(By.NAME, "change").text)[1:])
            except:imfor['DJIA']['CHANGE']= 0
            imfor['DJIA']['RATE']= float(figure.find_element(By.NAME, "changeRate").text)
    except:
        print("道瓊指數資料採掘錯誤")

print(imfor)
