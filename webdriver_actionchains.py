from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import time

# 웹 드라이버를 이용하여 자동으로 열기
# driver = webdriver.Chrome()
driver = webdriver.Edge()
url = 'https://google.com'
# _chrome_options = Options()
# _chrome_options.add_argument('disable-infobars')
# driver = webdriver.Chrome( chrome_options=_chrome_options)
driver.get(url)
driver.maximize_window()  # 제일 크게 열기(사실 없어도 됨)
action = ActionChains(driver)  # action 변수가 driver 진행 할 수 있도록 설정

# 구글 페이지에서 로그인 버튼 id로 찾기
driver.find_element_by_css_selector('#gb_70').click()
time.sleep(1)
# 로그인 페이지 들어가면 아이디 창이 이미 선택되어 있으므로 바로 id 입력
# ★☆★perform() 꼭 붙여야함(actionChains는 순차적으로 수행할 것을 더 추가가 가능하기 때문)
action.send_keys('boorooksus').perform()
action.reset_actions()  # ★☆★action 만든 뒤 리셋 해줘야 다음 action 때 오류 안생김
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
#비밀번호 페이지
driver.find_element_by_css_selector('비밀번호 창 태그 클래스').send_keys('비밀번호')
driver.find_element_by_css_selector('전송 버튼 태그 클래스').click()
time.sleep(2)

# 메일 페이지로 들어가기
driver.get('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
time.sleep(2)
driver.find_element_by_css_selector('편지쓰기 버튼 클래스').click()
time.sleep(1)

# 이메일 전송 버튼 클래스 변수에 저장
send_button = driver.find_element_by_css_selector('전송 버튼 태그 클래스')

# 받는 사람 입력 후 탭 두번 눌러서 제목 입력 후 탭 눌러서 내용 입력
# 괄호 안에 적으면 줄바꿈해도 한줄로 인식
(
action.send_keys('받는 사람 이메일 주소')
.pause(2)  # time.sleep 대신 쓸 수 있는 셀레니움 자체 일지정지 기능
.key_down(Keys.TAB)
.key_down(Keys.TAB)
.send_keys('메일 제목')
.key_down(Keys.TAB)
.send_keys('본문 내용 시작').key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('this is uppercase').key_up(Keys.SHIFT)  # 본문 내용 쉬프트 누른채로 입력
.move_to_element(send_button).click()  # 아까 변수에 저장한 전송 버튼 클릭(이 방식을 이용할때 장점: 요소만 알면 뭐든지 클릭 가능
.perform()
)