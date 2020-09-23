import pygame

pygame.init()
win=pygame.display.set_mode((636,636))
pygame.display.set_caption("Second Game")

#image
walkRight = [pygame.image.load('PR1.png'), pygame.image.load('PR2.png'), pygame.image.load('PR3.png'), pygame.image.load('PR4.png'), pygame.image.load('PR5.png'), pygame.image.load('PR6.png'), pygame.image.load('PR7.png'), pygame.image.load('PR8.png'), pygame.image.load('PR9.png')]
walkLeft = [pygame.image.load('PL1.png'), pygame.image.load('PL2.png'), pygame.image.load('PL3.png'), pygame.image.load('PL4.png'), pygame.image.load('PL5.png'), pygame.image.load('PL6.png'), pygame.image.load('PL7.png'), pygame.image.load('PL8.png'), pygame.image.load('PL9.png')]
walkRight2 = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft2 = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg=pygame.image.load("bg.jpg")
#win.blit(bg,(0,0))

clock=pygame.time.Clock()
score=0
score1=0

#for player1
class player():
	
	def __init__(self,x,y,width,heigth):
		self.x=x
		self.y=y
		self.width=width
		self.heigth=heigth
		self.vel=5  
		self.isJump=False
		self.jumpcount=10
		self.left=False
		self.right=False
		self.walkcount=0
		self.standing=True
		self.hitbox=(self.x+13,self.y+5,45,65)
		self.health_player1=10
		self.visible=True
		
	def draw(self,win):
		if self.visible:
			if self.walkcount +1 >=27:
				self.walkcount=0
			if not (self.standing):
				if self.left:
					win.blit(walkLeft[self.walkcount//3],(self.x,self.y)) #displaying different images for walking left as in animations
					self.walkcount+=1
				elif self.right:
					win.blit(walkRight[self.walkcount//3],(self.x,self.y)) #displaying different images for walking right as in animations
					self.walkcount+=1
			else:
				if self.right:
					win.blit(walkRight[0],(self.x,self.y))
				else:
					win.blit(walkLeft[0],(self.x,self.y))
			#pygame.draw.rect(win,(255,0,0),self.hitbox,2)#hitbox
			pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))#health bar
			pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health_player1)),10))#healthbar-attack 
			self.hitbox=(self.x+13,self.y+5,45,65)
			
	
	def hit(self):
		if self.health_player1>0:
			self.health_player1-=1
		else:
			self.visible=False
		

#for player 2
class player2():

	def __init__(self,x,y,width,heigth):
		self.x=x
		self.y=y
		self.width=width
		self.heigth=heigth
		self.vel=5
		self.isJump=False
		self.jumpcount=10
		self.left=False
		self.right=False
		self.walkcount=0
		self.standing=True
		self.hitbox=(self.x+17,self.y+10,29,57)
		self.health_player2=10
		self.visible=True

	def draw(self,win):
		if self.visible:
			if self.walkcount+1>=27:
				self.walkcount=0
			if not self.standing:
				if self.left:
					win.blit(walkLeft2[self.walkcount//3],(self.x,self.y))
					self.walkcount+=1
				elif self.right:
					win.blit(walkRight2[self.walkcount//3],(self.x,self.y))
					self.walkcount+=1
			else:
				if self.right:
					win.blit(walkRight2[0],(self.x,self.y))
				else:
					win.blit(walkLeft2[0],(self.x,self.y))
			#pygame.draw.rect(win,(255,0,0),self.hitbox,2)#hitbox
			pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))#health bar
			pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health_player2)),10))#healthbar-attack 
			self.hitbox=(self.x+17,self.y+10,29,57)

	def hit(self):
		if self.health_player2>0:
			self.health_player2-=1
		else:
			self.visible=False
			

class projectile():

	def __init__(self,x,y,radius,color,facing):
		self.x=x
		self.y=y
		self.radius=radius
		self.color=color
		self.facing=facing
		self.vel=8*facing

	def draw(self,win):
			pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

def redrawGamewindow():

	win.blit(bg,(0,0))
	text=font.render("Score : "+str(score),1,(255,0,0))
	text2=font.render("Score : "+str(score1),1,(0,255,0))
	win.blit(text,(60,10))
	win.blit(text2,(500,10))
	man.draw(win)
	man2.draw(win)

	for bullet in bullets:
		bullet.draw(win)

	for bullet1 in bullets_2:
		bullet1.draw(win)

	if score==11:
		pygame.time.delay(150)
		text3=font2.render("Winner is player1",1,(255,255,255))
		win.blit(text3,(250,250))

	if score1==11:
		pygame.time.delay(150)
		text4=font2.render("Winner is player2",1,(255,255,255))
		win.blit(text4,(250,250))

	pygame.display.update()

#main loop
font=pygame.font.SysFont("comicsans",30,True)
font2=pygame.font.SysFont("lato",40,True)
run=True
man=player(200,410,64,64)
man2=player2(500,410,64,64)
bullets=[]
bullets_2=[]
shootloop=0

while run:
	#pygame.time.delay(100)
	clock.tick(27)
	if shootloop>0:
		shootloop+=1
	if shootloop>3:
		shootloop=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

	for bullet in bullets:
		for bullet1 in bullets_2:
			if bullet.x==bullet1.x and bullet.y==bullet1.y and bullet.radius==bullet1.radius:
				#if bullet.radius==bullet1.radius:
				bullets.pop(bullets.index(bullet))
				bullets_2.pop(bullets_2.index(bullet1))

	#shooting for player1
	for bullet in bullets:
		if bullet.y-bullet.radius<man2.hitbox[1]+man2.hitbox[3] and bullet.y+bullet.radius>man2.hitbox[1]:
			if bullet.x+bullet.radius>man2.hitbox[0] and bullet.x-bullet.radius<man2.hitbox[0]+man2.hitbox[2]:
					bullets.pop(bullets.index(bullet))
					man2.hit()
					score+=1
		if bullet.x<636 and bullet.x>0:
			bullet.x+=bullet.vel
		else:
			bullets.pop(bullets.index(bullet))

	#shooting for player2
	for bullet1 in bullets_2:
		if bullet1.y-bullet1.radius<man.hitbox[1]+man.hitbox[3] and bullet1.y+bullet1.radius>man.hitbox[1]:
			if bullet1.x+bullet1.radius>man.hitbox[0] and bullet1.x-bullet1.radius<man.hitbox[0]+man.hitbox[2]:
					bullets_2.pop(bullets_2.index(bullet1))
					man.hit()
					score1+=1
		if bullet1.x<636 and bullet1.x>0:
			bullet1.x+=bullet1.vel
		else:
			bullets_2.pop(bullets_2.index(bullet1))


	keys=pygame.key.get_pressed()

	if keys[pygame.K_SPACE] and shootloop==0:
		if man.left:
			facing=-1
		else:
			facing=1
		if len(bullets)<3:
			bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.heigth//2),6,(255,0,0),facing))
		shootloop=1

	if keys[pygame.K_LEFT] and man.x>man.vel:
		man.x-=man.vel
		man.left=True
		man.right=False
		man.standing=False
	elif keys[pygame.K_RIGHT] and man.x<636-man.width-man.vel:
		man.x+=man.vel
		man.right=True
		man.left=False
		man.standing=False
	else:
		man.standing=True
		man.walkcount=0
	if not (man.isJump):
		if keys[pygame.K_UP]:
			man.isJump=True
			man.right=False
			man.left=False
	else:
		if man.jumpcount>=-10:
			neg=1
			if man.jumpcount<0:
				neg=-1
			man.y-=(man.jumpcount**2)*0.5*neg
			man.jumpcount-=1
		else:
			man.isJump=False
			man.jumpcount=10

	if keys[pygame.K_f] and shootloop==0:
		if man2.left:
			facing=-1
		else:
			facing=1
		if len(bullets_2)<3:
			bullets_2.append(projectile(round(man2.x+man2.width//2),round(man2.y+man2.heigth//2),6,(0,255,0),facing))
		shootloop=1

	if keys[pygame.K_a] and man2.x>man2.vel:
		man2.x-=man2.vel
		man2.left=True
		man2.right=False
		man2.standing=False
	elif keys[pygame.K_d] and man2.x<636-man2.width-man2.vel:
		man2.x+=man2.vel
		man2.left=False
		man2.right=True
		man2.standing=False
	else:
		man2.standing=True
		man2.walkcount=0
	if not (man2.isJump):
		if keys[pygame.K_w]:
			man2.isJump=True
			man2.right=False
			man2.left=False
	else:
		if man2.jumpcount>=-10:
			neg=1
			if man2.jumpcount<0:
				neg=-1
			man2.y-=(man2.jumpcount**2)*0.5*neg
			man2.jumpcount-=1
		else:
			man2.isJump=False
			man2.jumpcount=10

	redrawGamewindow()
pygame.quit()