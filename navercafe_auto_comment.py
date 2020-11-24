from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time
import pyperclip

# 로그인 창
win = Tk()
win.geometry('200x120')
win.title('Login')

# ID 입력창
idLabel = Label(win, text="ID")
idLabel.pack()
idEntry = Entry(win)
idEntry.pack()

# password 입력
pwLabel = Label(win, text="Password")
pwLabel.pack()
pwEntry = Entry(win, show='*')
pwEntry.pack()


def login():
    # 네이버 로그인 열기
    driver = webdriver.Chrome()
    driver.get('https://nid.naver.com/nidlogin.login')

    # id, pw 입력할 곳을 찾습니다.
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    time.sleep(1)

    # id 입력
    tag_id.click()
    pyperclip.copy(idEntry.get())
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw 입력
    tag_pw.click()
    pyperclip.copy(pwEntry.get())
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼을 클릭합니다
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()

    # 슬립을 꼭 넣어줘야 한다.
    # 그렇지 않으면 로그인 끝나기도 전에 다음 명령어가 실행되어 제대로 작동하지 않는다.
    time.sleep(3)

    # 카페로 이동
    driver.get('https://cafe.naver.com/stockschart')
    time.sleep(2)

    # 첫글부터 클릭
    # 필독이 있을 가능성이 있다. 필독은 2개까지 가능하므로 상위 2개까지는 좋아요가 눌러져있어도 그냥 다음 글로 넘어가게 세팅
    # 3번부터는 눌러져있으면 아래는 이미 다 달았던 글이므로 프로그램 종료(공지한 시간순으로 위에 쌓임)
    for i in range(1, 11):
        # 본문은 iframe으로 이뤄져있다.
        driver.switch_to_frame("cafe_main")
        driver.find_element_by_xpath(
            f'/html/body/div[1]/div/div/div/div/div[1]/div[3]/div/div/table/tbody/tr[{i}]/td[1]/div[2]/div/a').click()
        time.sleep(2)
        try:
            like = driver.execute_script(
                "return document.querySelector('#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a').getAttribute('aria-pressed')")
        except:
            continue
        # 종료 조건. 필독이 아니면서 좋아요가 눌러져있으면 종료.
        if like == 'true' and i > 2:
            driver.quit()
        # false일 때 좋아요 누르기 및 댓글 쓰기.
        elif like == 'true':
            driver.refresh()
            time.sleep(2)
        else:
            driver.execute_script(
                'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a > span").click()')
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > a").click()')
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > div > div > div > div > ul > li.active > div > ul > li:nth-child(15) > button").click()'
            )
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.register_box > a").click()')
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > a").click()'
            )
            time.sleep(1)
            driver.execute_script('document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.attach_box > div > div > div > div > ul > li.active > div > ul > li:nth-child(23) > button").click()')
            time.sleep(1)
            driver.execute_script(
                'document.querySelector("#app > div > div > div.ArticleContentBox > div.article_container > div.CommentBox > div.CommentWriter > div.comment_attach > div.register_box > a").click()')
            time.sleep(1)
            # 새로고침해서 밖으로 빠져나가기
            driver.refresh()
            time.sleep(3)
    # 브라우저 종료
    driver.quit()


# login 버튼
loginButton = Button(win, text="Login", command=login)
loginButton.pack()

win.mainloop()
