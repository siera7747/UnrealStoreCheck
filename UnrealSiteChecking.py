##jkleviathan.com
##contact@jkleviathan.com
##이 프로그램은 저작권의 보호를 받고 있으며, 불법 재배포 및 재판매 등을 금지합니다.
##Programming by H.J Ryu
##Planning by J.K Lee


#Auto System#
#자동화 시스템#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl
from keyboard import press
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox

#variable init
#기본 변수들 설정
def AutoStoreCheck(Id='', Pw='', Site='', Category=''):
    driver = webdriver.Chrome('./chromedriver')
    wb = openpyxl.load_workbook('StoreCheck.xlsx')
    sheet1 = wb.create_sheet(Category)

    #Wait var create
    #대기용 객체 생성
    wait = WebDriverWait(driver, 60)

    #All Page Check variable
    #모든 페이지 검색 확인 변수
    Allcheck = False

    #Crawling Start
    #크롤링 시작
    try:
        driver.get(Site)
        time.sleep(10)
    
        #if Category is Vault, Login
        #로그인(보관함인 경우에만)
        if Category == "Vault":
            #wait until Id element is clickable
            #아이디창 클릭 가능할 때까지 대기
            wait.until(EC.visibility_of_element_located((By.ID, "email")))
            elem = driver.find_element_by_id("email")
            elem.send_keys(Id)
            elem = driver.find_element_by_id("password")
            elem.send_keys(Pw)
            elem.send_keys(Keys.RETURN)

        #Read the data
        #데이터 읽기
        while True:
            #Wait until element loading
            #요소가 로딩될때까지 대기
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-container")))

            elem = driver.find_element_by_class_name("category-container")

            #read esset data
            #에셋 정보 읽기
            datas = elem.find_elements_by_class_name("asset-container")

            driver.execute_script("arguments[0].scrollIntoView(false)", datas[0])
            time.sleep(5)

            for data in datas:
                #esset explain
                #에셋 설명
                imagedata = data.find_element_by_class_name("image-box")
                imagetitledata = imagedata.find_element_by_xpath("./div/div/div/a/img")
                imagetitle = imagetitledata.get_attribute('title')

                Alldata = data.find_element_by_class_name("info")

                #title data
                #타이틀 정보
                titledata = Alldata.find_element_by_xpath("./h3/a")
                title = titledata.text

                #creater data
                #제작자 정보
                createrdata = Alldata.find_element_by_xpath("./div[1]/a")
                creater = createrdata.text

                #rating data
                #별점 정보
                ratingcheck = Alldata.find_elements_by_xpath("./div[2]/div")
                if len(ratingcheck) == 0:
                    rating = "Not Yet Rated"
                else:
                    ratingpop = Alldata.find_element_by_xpath("./div[2]/div[1]/span[2]")
                    webdriver.ActionChains(driver).move_to_element(ratingpop).perform()
                    ratingdata = Alldata.find_element_by_xpath("./div[2]/div[2]/div/div[2]/span")
                    rating = ratingdata.text

                #price data
                #가격 정보
                pricedata = Alldata.find_elements_by_xpath("./div[3]/span")
                #check price exist. if price is exist, check the esset is sailed
                #가격이 존재하는지 확인. 존재하는 경우에는 할인하는지 여부 확인
                if len(pricedata) != 0:
                    pricecheck = Alldata.find_element_by_xpath("./div[3]/span[1]")
                    if pricecheck.get_attribute('class') == 'asset-discount-note':
                        price1 = Alldata.find_element_by_xpath("./div[3]/span/span").text
                        price2 = Alldata.find_element_by_xpath("./div[3]/span[2]").text
                        price3 = price2.split('₩')
                        price = price1 + " / " + "₩" + price3[2]
                    else:
                        price = Alldata.find_element_by_xpath("./div[3]/span").text
                else:
                    price = "Vault Asset Data"

                #category data
                #카테고리 정보
                detaildata = Alldata.find_elements_by_xpath("./ul/li/ul[1]/div/li")
                if len(detaildata) == 0:
                    detail = ""
                else:
                    detail = Alldata.find_element_by_xpath("./ul/li/ul[1]/div/li/a").text

                #Save to excel
                #엑셀로 저장
                sheet1.append([title, creater, rating, price, detail, imagetitle])

            #move mouse to delete rating popup
            #마우스오버로 별점박스 없애기
            webdriver.ActionChains(driver).move_to_element(titledata).perform()

            #search next page button
            #다음 페이지 버튼 찾기
            pagenation = driver.find_element_by_class_name("pagination")
            pages = pagenation.find_elements_by_xpath("./li")
         
            for page in pages:
                pagedata = page.find_elements_by_xpath("./a")
                if len(pagedata) == 0:
                    continue
                nextpage = page
                if nextpage.get_attribute('class') == "next disabled":
                    Allcheck = True
                    break
                if nextpage.get_attribute('class') == "next":
                    break

            #All page check
            #모든 페이지 검색 여부 확인
            if Allcheck == True:
                break

            #initialize page variable
            #페이지 변수 초기화
            Allcheck = False

            #next page button click
            #다음 페이지 버튼 클릭
            webdriver.ActionChains(driver).move_to_element(nextpage).click(nextpage).perform()
            time.sleep(10)
            
    except Exception as e:
        messagebox.showinfo("Alert", "Failed!")
        print(e)
    finally:
        wb.save('StoreCheck.xlsx')
        driver.quit()


#GUI
import tkinter

class GUIT():
    def __init__(self):
        #Category Variables
        #카테고리 변수들
        self.Site = ''
        self.Category = ''

        self.SiteBasic = "https://www.unrealengine.com/marketplace/en-US/content-cat/assets/2d"

        #Category List
        #카테고리 리스트
        self.Categorys = ["2D Asset"]
        self.Categorys.append("Architectural Visualization")
        self.Categorys.append("Materials")
        self.Categorys.append("Megascans")
        self.Categorys.append("Weapons")
        self.Categorys.append("Environments")
        self.Categorys.append("Blueprints")
        self.Categorys.append("Sound Effects")
        self.Categorys.append("Props")
        self.Categorys.append("Animations")
        self.Categorys.append("Epic Content")
        self.Categorys.append("Music")
        self.Categorys.append("Visual Effects")
        self.Categorys.append("Characters")
        self.Categorys.append("Code Plugins")
        self.Categorys.append("Textures")
        self.Categorys.append("On Sale")
        self.Categorys.append("Vault")

        #Site Url List
        #사이트 주소 리스트
        self.SiteString = ["/content-cat/assets/2d"]
        self.SiteString.append("/content-cat/assets/archvis")
        self.SiteString.append("/content-cat/assets/materials")
        self.SiteString.append("/content-cat/assets/megascans")
        self.SiteString.append("/content-cat/assets/weapons")
        self.SiteString.append("/content-cat/assets/environments")
        self.SiteString.append("/content-cat/assets/blueprints")
        self.SiteString.append("/content-cat/assets/soundfx")
        self.SiteString.append("/content-cat/assets/props")
        self.SiteString.append("/content-cat/assets/animations")
        self.SiteString.append("/content-cat/assets/showcasedemos")
        self.SiteString.append("/content-cat/assets/music")
        self.SiteString.append("/content-cat/assets/fx")
        self.SiteString.append("/content-cat/assets/characters")
        self.SiteString.append("/content-cat/assets/codeplugins")
        self.SiteString.append("/content-cat/assets/textures")
        self.SiteString.append("/on-sale")
        self.SiteString.append("/vault?sessionInvalidated=true")

        #Category Num
        #카테고리 갯수
        self.CategoryAllNum = len(self.SiteString)-1

        #Create Window
        #윈도우 생성
        self.tkhandler = tkinter.Tk()
        self.tkhandler.geometry('600x500')
        self.tkhandler.title('Esset Check Program')

        self.label_title = tkinter.Label(self.tkhandler, text='Auto Program')
        self.label_title.pack(pady=10)

        #ID input
        #ID입력창
        self.ID_frame = tkinter.Frame(self.tkhandler)
        self.ID_frame.pack(fill='x')

        self.label_ID = tkinter.Label(self.ID_frame, text='Unreal ID', width=15)
        self.label_ID.pack(side='left', padx=10, pady=5)

        self.text_ID = tkinter.Text(self.ID_frame, height=1)
        self.text_ID.pack(fill='x', padx=10, expand=True)

        #password input
        #패스워드 입력창
        self.Pass_frame = tkinter.Frame(self.tkhandler)
        self.Pass_frame.pack(fill='x')

        self.label_Pass = tkinter.Label(self.Pass_frame, text='Password', width=15)
        self.label_Pass.pack(side='left', padx=10, pady=5)

        self.text_Pass = tkinter.Text(self.Pass_frame, height=1)
        self.text_Pass.pack(fill='x', padx=10, expand=True)

        #Label which alart Id or Password input
        #ID, 패스워드 입력 알림 라벨
        self.label_AlaerInput = tkinter.Label(self.tkhandler, text='Alert')
        self.label_AlaerInput.pack(fill='x', padx=10, pady=5, expand=True)

        #category select Button
        #카테고리 선택 버튼
        self.SelecBtn_frame = tkinter.Frame(self.tkhandler)
        self.SelecBtn_frame.pack(fill='x', expand=True)

        self.RadioVariety = tkinter.IntVar()
        #init radiobutton to not select state
        #아무것도 선택되지 않은 상태로 설정하기
        self.RadioVariety.set(-1)

        row = 0
        btnnum = 0

        #Create Button
        #버튼 생성
        while(True):
            for n in range(0, 4):
                tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[btnnum], value=btnnum, variable=self.RadioVariety, command=self.GetRadioBtn).grid(row=row, column=n, padx=10, pady=5, sticky='w')
                btnnum = btnnum + 1
                if btnnum > self.CategoryAllNum:
                    tkinter.Radiobutton(self.SelecBtn_frame, text="All", value=btnnum, variable=self.RadioVariety, command=self.GetRadioBtn).grid(row=row+1, column=1, padx=10, pady=5, sticky='e')
                    tkinter.Radiobutton(self.SelecBtn_frame, text="Search", value=btnnum + 1, variable=self.RadioVariety, command=self.GetRadioBtn).grid(row=row+2, column=1, padx=10, pady=5, sticky='e')
                    break
            row = row + 1
            if btnnum > self.CategoryAllNum:
                break
        
        #Search Input
        #검색창
        self.SearchInput_frame = tkinter.Frame(self.tkhandler)
        self.SearchInput_frame.pack(fill='x')

        self.label_search = tkinter.Label(self.SearchInput_frame, text='Search', width=15)
        self.label_search.pack(side='left', padx=10, pady=5)

        self.text_search = tkinter.Text(self.SearchInput_frame, height=1)
        self.text_search.pack(fill='x', padx=10, expand=True)

        #start button
        #시작 버튼
        self.StartBtn = tkinter.Button(self.tkhandler, text='Start', width=30, command=self.runAutoSystem)
        self.StartBtn.pack(side='bottom', pady=10)
        
        #Label which indicate selected category
        #선택한 카테고리 표시 라벨
        self.label_Category = tkinter.Label(self.tkhandler, text='Category')
        self.label_Category.pack(side='bottom')

    #Radio Button Func
    #라디오버튼 입력 함수
    def GetRadioBtn(self):
        CategoryNum = self.RadioVariety.get()
        self.SelectCategory(CategoryNum)

    #Set Category Data according to Button input Func
    #버튼 입력에 따른 카테고리 정보 설정 함수
    def SelectCategory(self, CategoryNum=0):
        Search = self.text_search.get('1.0', 'end').strip()

        #Select All
        #All 선택
        if CategoryNum == self.CategoryAllNum + 1:
            self.Category = "All"
            self.label_Category.config(text=str(self.Category))
        #Select Search
        #Search 선택
        elif CategoryNum == self.CategoryAllNum + 2:
            #Not have Search Keyword - Alert Message
            #검색 키워드가 없는 경우 - 경고 메시지
            if Search == '':
                messagebox.showinfo("Alert", "Input Search Keyword!")
                self.RadioVariety.set(-1)
            else:
                self.Category = "Search : " + Search
                self.Site = self.SiteBasic.replace("/content-cat/assets/2d", "/assets?keywords=" + Search)
                self.label_Category.config(text=str(self.Category))
        #Select General Category
        #일반 카테고리 선택
        else:
            self.Category = self.Categorys[CategoryNum]
            self.Site = self.SiteBasic.replace("/content-cat/assets/2d", self.SiteString[CategoryNum])
            self.label_Category.config(text=str(self.Category))

    #Run Program
    #프로그램 실행
    def runAutoSystem(self):
        time.sleep(1)
        Id = self.text_ID.get('1.0', 'end').strip()
        Pw = self.text_Pass.get('1.0', 'end').strip()

        #If Category is "Valult" or "All", Check Id and Password
        #카테고리가 보관함이거나 전부라면 ID와 패스워드 체크
        if self.Category == "Vault" or self.Category == "All":
            if Id == '':
                messagebox.showinfo("Alert", "Input the ID")
            elif Pw == '':
                messagebox.showinfo("Alert", "Input the PW")
            else:
                if self.Category == "Vault":
                    AutoStoreCheck(Id, Pw, self.Site, self.Category)
                else:
                    #If Category is "All", Loop All Category
                    #카테고리가 All인 경우 모든 카테고리 루프
                    Index = 0
                    while True:
                        self.Site = self.SiteBasic.replace("/content-cat/assets/2d", self.SiteString[Index])
                        AutoStoreCheck(Id, Pw, self.Site, self.Categorys[Index])
                        Index = Index + 1
                        if Index == self.CategoryAllNum + 1:
                            break
        #Not Select Category - Alert Message
        #카테고리가 선택되지 않은 경우 - 경고 메세지
        elif self.Category == "":
            self.label_AlaerInput.config(text="Select Category")
        #Select General Category
        #일반 카테고리 선택
        else:
            AutoStoreCheck(Id, Pw, self.Site, self.Category)

        #All Crawling Compelete - Inform Message
        #모든 크롤링 완료 - 알림 메세지
        messagebox.showinfo("Message", "All Page Check!")

    def run(self):
        self.tkhandler.mainloop()

g = GUIT()
g.run()