#!/bin/usr/env python

import random,sys,pygame,time

pygame.init()

c=0
black = (0,0,0)
white=(255,255,255)
red = (200,0,0)
L_red = (251,39,199)
L_blue = (39,251,199)
blue=(40,100,199)


tela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jeremias on the fire ,-,")
je=pygame.image.load("jeremias.png")
jed=pygame.image.load("jeremiasd.png")
pente= pygame.image.load("pente.png")
pente2 = pygame.transform.scale(pente,(10,20))
coxinha = pygame.image.load("coxinha.png")
cox = pygame.transform.scale(coxinha,(20,20))
pygame.display.set_icon(coxinha)

clock=pygame.time.Clock()

first = True
#Mov
x = 380
xt= False
xx = False

y = 222
yt=False
yy=False


lorr=False
#Fmov




def thig(x,y,h,w,color):
	pygame.draw.rect(tela,color,[x,y,h,w])
def text_object(text,font):
	text_surface=font.render(text,True,black)
	return text_surface,text_surface.get_rect()	
def score(count):
	font = pygame.font.SysFont(None,25)
	text = font.render("coxinhas: "+str(count),True,black)
	tela.blit(text,(0,0))	
def message_display(text):
	ltext = pygame.font.Font("freesansbold.ttf",60)
	textsurf,textrect=text_object(text,ltext)
	textrect.center=((800/2),(600/2)) 
	tela.blit(textsurf,textrect)
	pygame.display.flip()
	
	time.sleep(0.5)
	gameloop()
def char(x,y,teste):
	tela.fill([255,255,255])
	if teste:
		tela.blit(jed,(x,y))
	else:
		tela.blit(je,(x,y))
def pen (x,y):
	tela.blit(pente2,(x,y))	
def r_rect(x,y,char_x,char_y,rx,ry,rh,rw,rx1,ry1,rh1,rw1,rx2,ry2,rh2,rw2,rxw,ryw,rhw,rww,coxas): 	
	global c
	musica = pygame.mixer.music
	
	
	if (x > rx and x <= rx + rw or x + char_x > rx and x+char_x < rx+rw) and (y > ry and y < ry+rh or y+char_y > ry and y+char_y < ry+rh):
		musica.load("a.mp3")
		musica.play()
		#thig(rx,ry,rh,rw,white)
		pen(rx+3,ry+7)
		message_display("Pente ;-;")
		clock.tick(1)
	else:
		thig(rx,ry,rh,rw,black)
	if (x > rx1 and x <= rx1 + rw1 or x + char_x > rx1 and x+char_x < rx1+rw1) and (y > ry1 and y < ry1+rh1 or y+char_y > ry1 and y+char_y < ry1+rh1):
		musica.load("a.mp3")
		musica.play()
		pen(rx1+3,ry1+7)
		message_display("Pente ;-;")
		clock.tick(1)
	else:
		thig(rx1,ry1,rh1,rw1,black)
	if (x > rx2 and x <= rx2 + rw2 or x + char_x > rx2 and x+char_x < rx2+rw2) and (y > ry2 and y < ry2+rh2 or y+char_y > ry2 and y+char_y < ry2+rh2):
		musica.load("a.mp3")
		musica.play()
		pen(rx2+3,ry2+7)
		message_display("Pente ;-;")
		clock.tick(1)
	else:
		thig(rx2,ry2,rh2,rw2,black)
	if (x > rxw and x <= rxw + rww or x + char_x > rxw and x+char_x < rxw+rww) and (y > ryw and y < ryw+rhw or y+char_y > ryw and y+char_y < ryw+rhw):
		musica.load("sound.mp3")
		musica.play()
		c = coxas +1
		tela.blit(cox,(rxw+6,ryw+7))
		score(coxas)
		message_display("Coxinha ^^")
	else:
		thig(rxw,ryw,rhw,rww,black)

def button(msg,x,y,w,h,color,inative_color,action = None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if (x + w > mouse[0] > x) and (y + h > mouse[1] > y):
		thig(x,y,w,h,inative_color)
		if click[0] == 1 and action is not None:
			if action == "play":
				gameloop()
			if action=="quit":
				pygame.quit()
				sys.exit()
	else:
		thig(x,y,w,h,color)
	sfont = pygame.font.Font("freesansbold.ttf",20)
	textsurfs,textrects = text_object(msg,sfont)
	textrects.center=((x+(w/2)),(y+(h/2)))
	tela.blit(textsurfs,textrects)
	

def menu():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		tela.fill(white)
		ltext = pygame.font.Font("freesansbold.ttf",60)
		textsurf,textrect=text_object("Jeremias life",ltext)
		textrect.center=((400),(200)) 
		tela.blit(textsurf,textrect)
		
		button("Start",350,350,100,50,blue,L_blue,"play")
		button("Quit",350,450,100,50,red,L_red,"quit")
		
		pygame.display.flip()
		clock.tick(15)
			
def gameloop():
	
	first = True
	musica = pygame.mixer.music
	musica.load("darkness.mp3")
	musica.play()
	coxas = c
	#Mov
	x = 380
	xt= False
	xx = False

	y = 222
	yt=False
	yy=False

	lorr=False
	#Fmov
	rh=50
	rw=50
	rx=random.randrange(0,800 - rw)
	ry=random.randrange(0,600 - rh)
	
	rh1=50
	rw1=50
	rx1=random.randrange(0,800 - rw1)
	ry1=random.randrange(0,600 - rh1)
	
	rh2=50
	rw2=50
	rx2=random.randrange(0,800 - rw2)
	ry2=random.randrange(0,600 - rh2)
	
	rhw=50
	rww=50
	rxw=random.randrange(0,800 - rw2)
	ryw=random.randrange(0,600 - rh2)
	
	#Dimensao
	char_x= 25
	char_y= 35
	while 1:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d or event.key==pygame.K_RIGHT:
					xt = True
				if event.key == pygame.K_a or event.key==pygame.K_LEFT:
					xx = True
				if event.key == pygame.K_w or event.key==pygame.K_UP:
					yt = True
				if event.key == pygame.K_s or event.key==pygame.K_DOWN:
					yy = True
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_d or event.key==pygame.K_RIGHT:
					xt = False
				if event.key == pygame.K_a or event.key==pygame.K_LEFT:
					xx = False
				if event.key == pygame.K_w or event.key==pygame.K_UP:
					yt = False
				if event.key == pygame.K_s or event.key==pygame.K_DOWN:
					yy = False
		
		


		
		tela.fill([255,255,255])
		tela.blit(jed,(x,y))
		score(coxas)

		if xt:
			if x >= 770:
				x = 769
				message_display("limite")
			x+=5
			lorr=True
			char(x,y,lorr)
			score(coxas)
			
			
			ejere=False
			lorr=True
		if xx:
			if x <= 0:
				x = 1
				message_display("limite")
			x-=5
			lorr=False
			char(x,y,lorr)
			score(coxas)
		if yt:
			if y <= 0:
				y=1
				message_display("limite")
			y-=5
			char(x,y,lorr)
			score(coxas)
		if yy:
			if y >= 555:
				y=554
				message_display("limite")
			y+=5
			char(x,y,lorr)
			score(coxas)
		r_rect(x,y,char_x,char_y,rx,ry,rh,rw,rx1,ry1,rh1,rw1,rx2,ry2,rh2,rw2,rxw,ryw,rhw,rww,coxas)
			
		
			
			
				
		pygame.display.flip()
		
		first = False
		clock.tick(30)
menu()

