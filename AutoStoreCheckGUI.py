import tkinter

class GUIT():
    def __init__(self):
        #카테고리 변수들
        self.Site = ''
        self.Category = ''

        self.Sites = ["https://www.unrealengine.com/marketplace/ko/content-cat/assets/2d?count=20&sortBy=effectiveDate&sortDir=DESC&start=0"]
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/archvis?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/materials?count=20&sortBy=effectiveDate&sortDir=DESC&start=0&lang=ko")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/megascans?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/weapons?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/environments?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/blueprints?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/soundfx?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/props?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/animations?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/showcasedemos?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/music?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/fx?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/characters?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/codeplugins?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append("https://www.unrealengine.com/marketplace/ko/content-cat/assets/textures?count=20&sortBy=effectiveDate&sortDir=DESC&start=0")
        self.Sites.append('https://www.unrealengine.com/marketplace/ko/vault?sessionInvalidated=true')

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
        self.Categorys.append("Vault")

        self.tkhandler = tkinter.Tk()
        self.tkhandler.geometry('600x400')
        self.tkhandler.title('Esset Check Program')

        self.label_title = tkinter.Label(self.tkhandler, text='Auto Program')
        self.label_title.pack(pady=10)

        #ID입력창
        self.ID_frame = tkinter.Frame(self.tkhandler)
        self.ID_frame.pack(fill='x')

        self.label_ID = tkinter.Label(self.ID_frame, text='Unreal ID', width=15)
        self.label_ID.pack(side='left', padx=10, pady=5)

        self.text_ID = tkinter.Text(self.ID_frame, height=1)
        self.text_ID.pack(fill='x', padx=10, expand=True)

        #패스워드 입력창
        self.Pass_frame = tkinter.Frame(self.tkhandler)
        self.Pass_frame.pack(fill='x')

        self.label_Pass = tkinter.Label(self.Pass_frame, text='Password', width=15)
        self.label_Pass.pack(side='left', padx=10, pady=5)

        self.text_Pass = tkinter.Text(self.Pass_frame, height=1)
        self.text_Pass.pack(fill='x', padx=10, expand=True)

        #스토어 카테고리 선택
        self.SelecBtn_frame = tkinter.Frame(self.tkhandler)
        self.SelecBtn_frame.pack(fill='x', expand=True)

        self.RadioVariety = tkinter.IntVar()
        self.RadioVariety.set(-1)

        self.radio_2DAsset = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[0], value=0, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_2DAsset.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.radio_ArchVis = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[1], value=1, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_ArchVis.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.radio_Materials = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[2], value=2, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Materials.grid(row=0, column=2, padx=10, pady=5, sticky='w')
        self.radio_Megascans = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[3], value=3, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Megascans.grid(row=0, column=3, padx=10, pady=5, sticky='w')
        self.radio_Weapons = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[4], value=4, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Weapons.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.radio_Environments = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[5], value=5, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Environments.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.radio_Blueprints = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[6], value=6, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Blueprints.grid(row=1, column=2, padx=10, pady=5, sticky='w')
        self.radio_SoundFx = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[7], value=7, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_SoundFx.grid(row=1, column=3, padx=10, pady=5, sticky='w')
        self.radio_Props = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[8], value=8, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Props.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.radio_Animations = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[9], value=9, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Animations.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        self.radio_Showcasedeoms = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[10], value=10, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Showcasedeoms.grid(row=2, column=2, padx=10, pady=5, sticky='w')
        self.radio_Music = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[11], value=11, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Music.grid(row=2, column=3, padx=10, pady=5, sticky='w')
        self.radio_Fx = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[12], value=12, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Fx.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.radio_Characters = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[13], value=13, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Characters.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        self.radio_CodePlugins = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[14], value=14, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_CodePlugins.grid(row=3, column=2, padx=10, pady=5, sticky='w')
        self.radio_Textures = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[15], value=15, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Textures.grid(row=3, column=3, padx=10, pady=5, sticky='w')
        self.radio_Stock = tkinter.Radiobutton(self.SelecBtn_frame, text=self.Categorys[16], value=16, variable=self.RadioVariety, command=self.GetRadioBtn)
        self.radio_Stock.grid(row=4, column=1, padx=10, pady=5, sticky='e')

        #시작 버튼
        self.StartBtn = tkinter.Button(self.tkhandler, text='Start', width=30, command=self.runAutoSystem)
        self.StartBtn.pack(side='bottom', pady=10)
        
        #테스트용 라벨
        self.label_test = tkinter.Label(self.tkhandler, text='카테고리')
        self.label_test.pack(side='bottom')
    
    def GetRadioBtn(self):
        CategoryNum = self.RadioVariety.get()
        self.SelectCategory(CategoryNum)

    def SelectCategory(self, CategoryNum=0):
        self.Category = self.Categorys[CategoryNum]
        self.Site = self.Sites[CategoryNum]
        self.label_test.config(text=str(self.Category))


    def runAutoSystem(self):
        self.label_test.config(self.Category)

    def run(self):
        self.tkhandler.mainloop()

g = GUIT()
g.run()
        
        