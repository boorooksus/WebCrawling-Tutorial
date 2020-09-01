import pyautogui
import time

print(pyautogui.position())

# 절대위치 - 화면의 어느 지점으로 이동시킬 때
# pyautogui.moveTo(86, 781, 2)
# 상대위치 - 현재 위치 기준에서 마우스 움직일 때
#pyautogui.moveRel(0, 300, 2)

#pyautogui.moveTo(349, 1003)
#pyautogui.click()

#pyautogui.moveTo(33, 31)
#pyautogui.doubleClick()

pyautogui.moveTo(240, 925)
pyautogui.doubleClick()
time.sleep(0.5)
pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter'])
pyautogui.typewrite('World')
