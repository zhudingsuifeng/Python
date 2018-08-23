#coding=utf-8
import sys,pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#在画sprite时使用的图像和矩形
		self.image=pygame.image.load('weight.png').convert()    #载入秤砣的图像
		self.rect=self.image.get_rect()
		self.reset()
	def reset(self):
		"""将秤砣移动到屏幕顶端的随机位置"""
		self.rect.top=-self.rect.height
		self.rect=randrange(screen_size[0])
	def update(self):
		"""更新秤砣，显示下一帧"""
		self.rect.top+=1
		if self.rect.top>screen_size[1]:
			self.reset()

#初始化
pygame.init()   #初始化pygame，为使用硬件做准备
screen_size=1440,900
pygame.display.set_mode(screen_size)   #创建一个窗口
pygame.mouse.set_visible(0)     #隐藏鼠标

#创建一个子图形组(sprite group)，增加Weight
sprites=pygame.sprite.RenderUpdates()
sprites.add(Weight())

#获取屏幕表面，并且填充
screen=pygame.display.get_surface()
bg=(255,255,255)
screen.fill(bg)
pygame.display.flip()

#用于清除子图形
def clear_callback(surf,rect):
	surf.fill(bg,rect)

while True:
	#检查退出事件
	for event in pygame.event.get():
		if event.type==QUIT:
			sys.exit()
		if event.type==KEYDOWN and event.key==K_ESCAPE:
			sys.exit()
#清除前面的位置
sprites.clear(screen,clear_callback)
#更新所有子图形
sprites.update()
#绘制所有子图形
updates=sprites.draw(screen)
#更新所需的显示部分
pygame.display.update(updates)