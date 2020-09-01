import pyautogui

# 화면에서 이미지 인식 후 좌표 구함 -> 좌표의 센터 위치 구함 -> 클릭
# i = pyautogui.locateOnScreen('cal.PNG')
# print(i)
# q = pyautogui.center(i)
# pyautogui.click(q)

# 위와 같은 결과가 나오는 코드
i = pyautogui.locateCenterOnScreen('cal.PNG')
pyautogui.click(i)

# 이미지를 캡쳐 후 해당 이미지 클릭
# print(pyautogui.position())
# pyautogui.screenshot('1.png', region=(212, 930, 60, 40))
# i = pyautogui.locateOnScreen('1.png')
# pyautogui.click(i)

