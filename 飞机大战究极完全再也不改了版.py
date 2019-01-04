

#飞机大战游戏的分析！！

#1.启动界面
#   内容：1.背景  2.文字动画 3.底部动图  4.开始按钮
#     类：开始界面类。
#              属性：图片列表，屏幕
#              方法：显示方法

#2.游戏界面
#    内容： 生命分数的显示，敌机，主角，奖励，背景
#      类：  敌机类， 属性： 图片 ，屏幕 ，移动速度，血量  方法：显示，碰撞，死亡
#           敌机工厂类：产生敌机
#           主角类， 属性： 图片 ，屏幕 ，移动速度，血量  方法：显示，碰撞，死亡
#           子弹类， 属性：图片，屏幕，移动速度，  方法：显示 ，碰撞
#           文本显示类，属性： 字体   方法：显示字体
#           背景类，属性：图片，屏幕，移动速度  方法：显示




#3.结束界面 ： 实现 历史成绩的 读取 和 更新





import pygame
import random,time,math,sys,os



# 初始化pygame
pygame.init()




#
# 奖励图片
jiangli_1_Imgs=[
    pygame.image.load("2D游戏素材/plane/image/jiangli1.png"),
    pygame.image.load("2D游戏素材/plane/image/jiangli2.png")
    ]
#
#奖励列表
jiangliList=[]


# 奖励类
class jiangli(pygame.sprite.Sprite):

    def __init__(self,imgs,screen,pos,hp,speed,tag) -> None:
        self.image=imgs[0]   #默认的一张
        self.imgs=imgs       #图片集合
        self.rect=self.image.get_rect()    #矩形区域
        self.rect.topleft=pos
        self.screen=screen
        self.hp=hp
        self.speed=speed
        self.tag=tag         #标签   用来区别  大，中，小，敌机

        self.imgIndex=0   #图片索引
        self.imgAddIndex=0
        jiangliList.append(self)

    def Move(self):

            self.rect = self.rect.move(0, self.speed)
            self.screen.blit(self.image, self.rect)

            # 出画面销毁
            if self.rect.y >= 800:
                if self in jiangliList:
                    jiangliList.remove(self)

            # 检测死亡
            self.Death()


    #敌机死亡
    def Death(self):
        if self.hp==0:
            if self in jiangliList:
                jiangliList.remove(self)

            #播放死亡动画  之后再销毁
        # self.rect = self.rect.move(0, 2)   #死亡时的速度
        # self.screen.blit(self.imgs[self.imgIndex], self.rect)
        # self.imgAddIndex+=1
        # if self.imgAddIndex==3:
        #     self.imgAddIndex=0
        #     self.imgIndex+=1
            #销毁敌机
            # if self.imgIndex==len(self.imgs):





#jiangli工厂
class jiangliFactory:
    #敌机产生的速度变量
    creatIndex=0

    @staticmethod
    def Createjiangli(screen):
        #随机产生 三架敌机    100   7：2:1
        jiangliFactory.creatIndex+=1
        if jiangliFactory.creatIndex==1000:    #每隔17帧产生一个奖励

            randNum=random.randint(1,100)
            if randNum<=70:
                jiangli(jiangli_1_Imgs,screen,(random.randint(0,429),-250),hp=1,speed=1,tag=1)
            elif randNum<=90:
                jiangli(jiangli_1_Imgs, screen,( random.randint(0, 411),-250),hp=1,speed=1, tag=2)
            else:
                jiangli(jiangli_1_Imgs, screen, (random.randint(0, 315),-250),hp=1,speed=1,tag=3)
            jiangliFactory.creatIndex=0

            #敌机移动
        for i in jiangliList:
            i.Move()


#敌机图片
enemy_1_Imgs=[
    pygame.image.load("2D游戏素材/plane/image/enemy0.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy0_down1.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy0_down2.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy0_down3.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy0_down4.png"),

]
enemy_2_Imgs=[
    pygame.image.load("2D游戏素材/plane/image/enemy1.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy1_down1.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy1_down2.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy1_down3.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy1_down4.png"),

]

enemy_3_Imgs=[
    pygame.image.load("2D游戏素材/plane/image/enemy2.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy2_down1.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy2_down2.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy2_down3.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy2_down4.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy2_down5.png"),
    pygame.image.load("2D游戏素材/plane/image/enemy2_down6.png"),

]

#敌机列表
enemyList=[]
#敌机类
class Enemy(pygame.sprite.Sprite):

    def __init__(self,imgs,screen,pos,hp,speed,tag) -> None:
        self.image=imgs[0]   #默认的一张
        self.imgs=imgs       #图片集合
        self.rect=self.image.get_rect()    #矩形区域
        self.rect.topleft=pos
        self.screen=screen
        self.hp=hp
        self.speed=speed
        self.tag=tag         #标签   用来区别  大，中，小，敌机

        self.imgIndex=0   #图片索引
        self.imgAddIndex=0
        enemyList.append(self)

    def Move(self):
        if self.hp>0:
            self.rect = self.rect.move(0, self.speed)
            self.screen.blit(self.image, self.rect)

            # 出画面销毁
            if self.rect.y >= 800:
                if self in enemyList:
                    enemyList.remove(self)
        else:
            # 检测死亡
            self.Death()


    #敌机死亡
    def Death(self):

            #播放死亡动画  之后再销毁
        self.rect = self.rect.move(0, 2)   #死亡时的速度
        self.screen.blit(self.imgs[self.imgIndex], self.rect)
        self.imgAddIndex+=1
        if self.imgAddIndex==3:
            self.imgAddIndex=0
            self.imgIndex+=1
            #销毁敌机
            if self.imgIndex==len(self.imgs):
                if self in enemyList:
                    #死亡前加分
                    if self.tag==1:
                        Hero.score+=1
                    elif self.tag==2:
                        Hero.score+=3
                    else:
                        Hero.score += 5
                    enemyList.remove(self)




#敌机工厂
class EnemyFactory:
    #敌机产生的速度变量
    creatIndex=0

    @staticmethod
    def CreateEnemy(screen):
        #随机产生 三架敌机    100   7：2:1
        EnemyFactory.creatIndex+=1
        if EnemyFactory.creatIndex==18:    #每隔17帧产生一架飞机

            randNum=random.randint(1,100)
            if randNum<=65:
                Enemy(enemy_1_Imgs,screen,(random.randint(0,429),-250),hp=1,speed=7,tag=1)
            elif randNum<90:
                Enemy(enemy_2_Imgs, screen,( random.randint(0, 411),-250),hp=5,speed=3, tag=2)
            else:
                Enemy(enemy_3_Imgs, screen, (random.randint(0, 315),-250),hp=12,speed=1,tag=3)
            EnemyFactory.creatIndex=0

            #敌机移动
        for i in enemyList:
            i.Move()

# 大招

dazhao=[pygame.image.load("2D游戏素材/plane/image/12345.png")]

#英雄图片列表
heroImgs=[
    pygame.image.load("2D游戏素材/plane/image/hero1.png"),
    pygame.image.load("2D游戏素材/plane/image/hero2.png")
]
#主角死亡动画
heroDeathImgs=[
    pygame.image.load("2D游戏素材/plane/image/hero_blowup_n1.png"),
    pygame.image.load("2D游戏素材/plane/image/hero_blowup_n2.png"),
    pygame.image.load("2D游戏素材/plane/image/hero_blowup_n3.png"),
    pygame.image.load("2D游戏素材/plane/image/hero_blowup_n4.png"),

]
MOUSEBUTTONDOWN=False
# 英雄类
class Hero(pygame.sprite.Sprite):
    #4个方向
    # up=False
    # down = False
    # left= False
    # right = False


    #全局的分数
    score=0

    def __init__(self,imgs,screen,speed,pos,hp) -> None:
        self.image=imgs[0]       #单张图片
        self.imgs=imgs          #图片列表
        self.screen=screen      #屏幕
        self.speed=speed        #速度
        self.rect=self.image.get_rect()      #图片的矩形区域
        self.rect.topleft=pos       #初始化位置
        self.hp=hp              #血量


        self.imgIndex=0      #主角图片索引
        self.imgAddIndex=0   #主角图片索引  变换变量

        #子弹的发射速度  变量
        self.bulletIndex=0

        #碰撞检测的bool
        self.canCollide=True
        self.collideIndex=0   #计算安全时间的变量

        #无敌闪烁的bool

        self.isTwinkle=False

        #死亡的图片索引
        self.deathIndex=0
        self.deathAddIndex=0


    def CtrlMove(self):
        global isPlay
        global angle
        if self.hp>0:
            # 主角两张图切换
            self.imgAddIndex += 1
            if self.imgAddIndex == 7:
                self.imgIndex += 1
                if self.imgIndex == len(self.imgs):
                    self.imgIndex = 0
                self.imgAddIndex = 0
            # 主角的控制  w  a  s  d
            # if Hero.up:
            #     self.rect = self.rect.move(0, -self.speed)
            # if Hero.down:
            #     self.rect = self.rect.move(0, self.speed)
            # if Hero.left:
            #     self.rect = self.rect.move(-self.speed, 0)
            # if Hero.right:
            #     self.rect = self.rect.move(self.speed, 0)

            # 区间约束
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 380:
                self.rect.x = 380  # 约束x轴
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > 626:
                self.rect.y = 626  # 约束y 轴

            self.rect.center=pygame.mouse.get_pos()     #主角鼠标跟随

            # 主角发射子弹
            self.bulletIndex += 1
            if self.bulletIndex == 6:  # 发射子弹  帧数间歇
                Bullet(buttleImgs[0], self.screen, 10, self.rect.midtop)
                if MOUSEBUTTONDOWN:
                    Bullet(buttleImgs[1], self.screen, 10, self.rect.midleft)
                    Bullet(buttleImgs[1], self.screen, 10, self.rect.midright)

                self.bulletIndex = 0


            # 子弹移动
            for i in bulletList:
                i.Move()

            # 边移动边检测    碰撞后有三秒无敌时间
            if self.canCollide:
                self.Collide()
                self.Collides()
                # 渲染主角
                self.screen.blit(self.imgs[self.imgIndex], self.rect)

            else:
                # 安全时间内的实现闪烁
                self.collideIndex += 1
                if self.collideIndex % 7 == 0:  # 每隔7个画面实现闪烁
                    self.isTwinkle = not self.isTwinkle  # 是否闪烁
                if self.isTwinkle:
                    # 显示
                    self.screen.blit(self.imgs[self.imgIndex], self.rect)
                if self.collideIndex == 180:
                    self.collideIndex = 0
                    self.canCollide = True
        else:
            #播放死亡动画后 返回主界面

            #渲染主角
            self.screen.blit(heroDeathImgs[self.deathIndex],self.rect)
            self.deathAddIndex+=1   #累加的变量
            if self.deathAddIndex==17:   #每隔 7 个画面播放一个图像
                self.deathIndex+=1      #图像索引加 1
                self.deathAddIndex=0   #0-7循环
                if self.deathIndex==len(heroDeathImgs):
                    pygame.time.delay(1000)    #时间的延时  1000是1秒
                    self.deathIndex=0

                    #判断 分数是都超过历史分数  超过更新历史分
                    if Hero.score>historyScore:
                        with open("score.txt","w")as f_w:
                            f_w.write(str(Hero.score))

                    isPlay=False





#主角碰撞检测
    def Collide(self):
        temp=pygame.sprite.spritecollideany(self,enemyList,pygame.sprite.collide_mask)
        if temp!=None:
            temp.hp=0
            self.hp-=1
            self.canCollide=False   #减血之后立刻无敌
    def Collides(self):
        temp=pygame.sprite.spritecollideany(self,jiangliList)
        if temp!=None:
            temp.hp=0
            for i in enemyList:
                i.hp=0



            # self.canCollide=False   #减血之后立刻无敌

#子弹列表  存储子弹
bulletList=[]

#子弹图片
buttleImgs=[
    pygame.image.load("2D游戏素材/plane/image/bullet.png"),
    pygame.image.load("2D游戏素材/plane/image/12.png"),
    pygame.image.load("2D游戏素材/plane/image/bullet2.png"),

]
#子弹类
class Bullet(pygame.sprite.Sprite):    #继承精灵

    def __init__(self,img,screen,speed,pos) -> None:
        self.image=img
        self.screen=screen
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.center=pos

        bulletList.append(self)   #将子弹存到列表中

    def Move(self):

        self.rect=self.rect.move(0,-self.speed)  #移动
        self.screen.blit(self.image,self.rect)  #渲染

        #子弹  超过画面 销毁
        if self.rect.y<-10:
            if self in bulletList:
                bulletList.remove(self)

        #子弹边移动，边 检测碰撞
        self.Collide()

    #检测敌机
    def Collide(self):
        #碰撞敌机列表，参数三collided是碰撞选项，默认是矩形碰撞
        temp=pygame.sprite.spritecollideany(self,enemyList,pygame.sprite.collide_mask)  #去除透明区域
        if temp!=None:
            #如果是敌机  就减血
            temp.hp-=1

            if self in bulletList:
                bulletList.remove(self)
                    #子弹命中敌人销毁


#游戏界面背景类

class Background:

    def __init__(self,image,screen,speed) -> None:
        self.image_1=image
        self.rect1=self.image_1.get_rect()    #图片1的位置
        self.image_2=image.copy()
        self.rect2=self.image_2.get_rect().move(0,-852)   #图片2的位置

        self.screen=screen
        self.speed=speed

    def Display(self):
        #移动
        self.rect1=self.rect1.move(0,self.speed)
        self.rect2=self.rect2.move(0, self.speed)

        if self.rect1.y>=760:
            self.rect1.y=self.rect2.y-852
        if self.rect2.y>=760:
            self.rect2.y=self.rect1.y-852
        #渲染
        self.screen.blit(self.image_1,self.rect1)
        self.screen.blit(self.image_2, self.rect2)

#开始界面图片
startImgList=[  pygame.image.load("2D游戏素材/plane/image/logo.png"),
                pygame.image.load("2D游戏素材/plane/image/name.png"),
                pygame.transform.scale(pygame.image.load("2D游戏素材/plane/image/loading.png"),(480,480)),
                pygame.image.load("2D游戏素材/plane/image/icon1.png"),

                          ]

startBottmoImgs=[   pygame.image.load("2D游戏素材/plane/image/game_loading1.png"),
                    pygame.image.load("2D游戏素材/plane/image/game_loading2.png"),
                    pygame.image.load("2D游戏素材/plane/image/game_loading3.png"),

                    ]

#开始界面类
class StartPanel:

    isInRect=False


    def __init__(self,imgs,bottomImgs,screen) -> None:
        self.imgs=imgs   #背景图片列表
        self.screen=screen   #屏幕
        self.nameY=0   #文字的上下浮动变量
        self.btmImgs=bottomImgs

        self.btmIndex=0     #底部图片索引
        self.btmIMgsAddindex=0     #用于计算帧数的变量

    def Display(self):
        #渲染背景
        self.screen.blit(self.imgs[0],(0,0))
        #渲染元气
        self.screen.blit(self.imgs[2], (0,100))
        #文字浮动变量
        self.nameY+=0.1
        if self.nameY>=100:
            self.nameY=0
        #渲染变量
        self.screen.blit(self.imgs[1], (25,100+50*math.sin(self.nameY)))
        #渲染按钮
        btnRect=self.screen.blit(self.imgs[3], (210,300))

        StartPanel.isInRect=btnRect.collidepoint(pygame.mouse.get_pos())      #得到鼠标位置


        #渲染底部三张图

        self.screen.blit(self.btmImgs[self.btmIndex],(150,600))

        self.btmIMgsAddindex+=1
        if self.btmIMgsAddindex==20:
            self.btmIndex+=1
            self.btmIMgsAddindex=0

        if self.btmIndex==len(self.btmImgs):
            self.btmIndex=0

#屏幕
screen=pygame.display.set_mode((480,750))

#主角对象
hero=Hero(heroImgs,screen,12,(200,600),3)



#背景音乐
pygame.mixer_music.load("2D游戏素材/plane/sound/game_music.mp3")
# pygame.mixer_music.load("2D游戏素材/plane/sound/123.mp3")
pygame.mixer.music.play(-1)

#文字对象
font=pygame.font.Font("apple.ttf",40)

#游戏是否开始
isPlay=False

#时间对象
clock=pygame.time.Clock()

#开始界面对象
startObj=StartPanel(startImgList,startBottmoImgs,screen)

#游戏背景对象
backGround=Background(startImgList[0],screen,2)

historyScore=0

#处理事件的方法
def AllEvent():
    global isPlay
    global historyScore
    global MOUSEBUTTONDOWN
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #鼠标事件
        if e.type==pygame.MOUSEBUTTONDOWN:
            if e.button == 1  and isPlay == True :
                MOUSEBUTTONDOWN=not MOUSEBUTTONDOWN
            if e.button==1 and StartPanel.isInRect and isPlay==False:
                print("你按下了左键,开始游戏")
                isPlay=True




                # 隐藏鼠标
                # pygame.mouse.set_visible(False)

                #初始化对象
                Hero.score=0
                hero.hp=3
                enemyList.clear()
                bulletList.clear()
                jiangliList.clear()
                hero.rect.topleft=(200,600)

                #读取历史分数
                if os.path.exists("score.txt"):
                    with open("score.txt","r") as f_r:
                        historyScore=int(f_r.read())
                else:
                    with open("score.txt","w")as f_w:
                        f_w.write("0")
                isPlay=True
                pygame.mixer_music.load("2D游戏素材/plane/sound/123.mp3")
                pygame.mixer.music.play(-1)



        #键盘事件

        if e.type==pygame.KEYDOWN:
                #空格实现全屏爆炸
            if e.key==pygame.K_F1:
                for i in enemyList:
                    i.hp=0
                for i in dazhao:
                    print(i)

            if e.key==pygame.K_ESCAPE:
                isPlay=False
            if e.key==pygame.K_w:
                Hero.up=True
            if e.key==pygame.K_s:
                Hero.down=True
            if e.key==pygame.K_a:
                Hero.left=True
            if e.key==pygame.K_d:
                Hero.right=True

        if e.type==pygame.KEYUP:
            if e.key==pygame.K_w:
                Hero.up=False
            if e.key==pygame.K_s:
                Hero.down=False
            if e.key==pygame.K_a:
                Hero.left=False
            if e.key==pygame.K_d:
                Hero.right=False



#主方法
def Main():
    global MOUSEBUTTONDOWN


    while True:
        AllEvent()

        screen.fill(pygame.Color("red"))

        if isPlay:

            #游戏界面的显示方法
            backGround.Display()

            #敌机产生
            EnemyFactory.CreateEnemy(screen)
            jiangliFactory.Createjiangli(screen)
            #主角控制
            hero.CtrlMove()

            #显示文字
            screen.blit(font.render("血量:%s"%(hero.hp),True,pygame.Color("Black")),(0,0))
            screen.blit(font.render("分数:%s"%(Hero.score),True,pygame.Color("Black")),(0,60))
            screen.blit(font.render("记录:%s"%(historyScore),True,pygame.Color("Black")),(0,120))

        else:
            startObj.Display()

        pygame.display.update()

        #设置帧频
        clock.tick(60)
        # print(pygame.mouse.get_pos())    打印鼠标位置

        # print(MOUSEBUTTONDOWN)

if __name__ == '__main__':
    Main()

