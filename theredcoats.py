#Author: Richard Tea
#Email: rtea@csu.fullerton.edu
#CPSC 386 Project 5
#Description: Project of a space invasion game that tests the reaction and management of player skill.

import pygame, sys
import random
from pygame.locals import *
import time

loc = [0,0,0,0,0,0]
score = [0]
def randLetter(q, w, e, a, s, d, z, x, c):
	done = True
	while done:
		letter = random.randint(0,8)
		if letter == 0 and q['active'] != 1:
			return q
			done = False
		elif letter == 1 and w['active'] != 1:
			return w
			done = False
		elif letter == 2 and e['active'] != 1:
			return e
			done = False
		elif letter == 3 and a['active'] != 1:
			return a
			done = False
		elif letter == 4 and s['active'] != 1:
			return s
			done = False
		elif letter == 5 and d['active'] != 1:
			return d
			done = False
		elif letter == 6 and z['active'] != 1:
			return z
			done = False
		elif letter == 7 and x['active'] != 1:
			return x
			done = False
		elif letter == 8 and c['active'] != 1:
			return c
			done = False



def spawnRect(a):
	done = True
	if menuChoice == 1:
		while done:
			location = random.randint(0,4)
			if location == 0 and loc[0] != 1:
				a['rect'].left = 115
				a['rect'].top = 102
				a['loc'] = 0
				loc[0] = 1
				done = False
			elif location == 1 and loc[1] != 1:
				a['rect'].left = 925
				a['rect'].top = 100
				a['loc'] = 1
				loc[1] = 1
				done = False
			elif location == 2 and loc[2] != 1:
				a['rect'].left = 64
				a['rect'].top = 600
				a['loc'] = 2
				loc[2] = 1
				done = False
			elif location == 3 and loc[3] != 1:
				a['rect'].left = 985
				a['rect'].top = 600
				a['loc'] = 3
				loc[3] = 1
				done = False
			elif location == 4 and loc[4] != 1:
				a['rect'].left = 478
				a['rect'].top = 350
				a['loc'] = 4
				loc[4] = 1
				done = False
		a['active'] = 1
	if menuChoice == 3:
		a['rect'].left = 950
		a['rect'].top = 84
		a['active'] = 1
		loc[5] = 1
def activeRect(a):
	a['active'] = 1

def despawnRect(a):
	if a != boss and a != nuke:
		a['rect'].top = -100
		a['rect'].left = 1400
		a['active'] = 0

def spawnMissles():
	missle1['active'] = 1
	missle2['active'] = 1
	missle3['active'] = 1
	missle1['rect'].left = 1300
	missle1['rect'].top = 500
	missle2['rect'].left = 1300
	missle2['rect'].top = 600
	missle3['rect'].left = 1300
	missle3['rect'].top = 700

def checkoutofBounds():
	for i in missles:
		if i['rect'].left <= 0:
			earthHP[0] -= 1
			print(str(earthHP))
			despawnRect(i)

def drawObj(a):
	if a['active'] == 1:
		screen.blit(alphaRect, (a['rect'].left, c['rect'].top))
		pygame.draw.rect(alphaRect, a['color'], a['rect'])
		if a == missle1 or a == missle2 or a == missle3:
			a['rect'].left -= 10
			pygame.draw.rect(alphaRect, a['color'], a['rect'])

def drawImg(a):
	if a['active'] == 1 and a != nukeCont and a != HBs:
		screen.blit(a['image'], a['rect']['rect'])
	elif a == nukeCont and a['active'] == 1:
		screen.blit(a['image'], (a['rect']['rect'].left - 35, a['rect']['rect'].top - 30))
	elif a == HBs and a['active'] == 1 and menuChoice == 1:
		screen.blit(a['image'], (115,182))
		screen.blit(a['image'], (925, 180))
		screen.blit(a['image'], (64, 678))
		screen.blit(a['image'], (985, 680))
		screen.blit(a['image'], (478, 426))
	elif a == HBs and (menuChoice == 2 or menuChoice == 3):
		screen.blit(a['image'], (1124, 329))
		

def checkCollision(a, mouse):
	if (a['rect'].left < mouse[0]) and (a['rect'].right > mouse[0]) and (a['rect'].top < mouse[1]) and (a['rect'].bottom > mouse[1]):
		a['active'] = 0
		a['rect'].left = 1400
		a['rect'].top = -100
		if a == missle1 or a == missle2 or a == missle3:
			explosion.play()
		if menuChoice == 1:
			loc[a['loc']] = 0
		score[0] += 1
		if a != boss and a != nuke and a != missle1 and a != missle2 and a != missle3 and menuChoice == 3:
			loc[5] = 0
			nuke['hp'] -= 1
			print(str(nuke['hp']))
			if nuke['hp'] <= 0:
				for i in obj:
					if i != boss:
						i['active'] = 0
						nuke['hp'] = 8
			elif nuke['hp'] > 0 and nuke['active'] == 1 and loc[5] == 0:
				spawnRect(randLetter(q,w,e,a,s,d,z,x,c))



pygame.init()
screen = pygame.display.set_mode((1300, 800), 0, 32)
initialTime = 0
timeleft = pygame.font.SysFont("Garamond", 60)
playerscore = pygame.font.SysFont("Garamond", 60)
presstobegin = pygame.font.SysFont("Garamond", 60)
title = pygame.font.SysFont("Garamond", 80)
inform = pygame.font.SysFont("Garamond", 40)
stage1 = pygame.font.SysFont("Garamond", 40)
stage1inst = pygame.font.SysFont("Garamond", 35)
notes = pygame.font.SysFont("Garamond", 35)
stage2 = pygame.font.SysFont("Garamond", 40)
stage2inst = pygame.font.SysFont("Garamond", 35)
blaster = pygame.mixer.Sound('blaster.wav')
explosion = pygame.mixer.Sound('explosion.wav')
backgroundmusic = pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1,0.0)
q = {'rect':pygame.Rect(-100,-100,100,100), 'color': (255,0,0), 'active': 0, 'loc': -1}
w = {'rect':pygame.Rect(-100,-100,100,100), 'color': (0,255,0), 'active': 0, 'loc': -1}
e = {'rect':pygame.Rect(-100,-100,100,100), 'color': (0,0,255), 'active': 0, 'loc': -1}
a = {'rect':pygame.Rect(-100,-100,100,100), 'color': (255,100,100), 'active': 0, 'loc': -1}
s = {'rect':pygame.Rect(-100,-100,100,100), 'color': (100,255,100), 'active': 0, 'loc': -1}
d = {'rect':pygame.Rect(-100,-100,100,100), 'color': (100,100,255), 'active': 0, 'loc': -1}
z = {'rect':pygame.Rect(-100,-100,100,100), 'color': (100,100,100), 'active': 0, 'loc': -1}
x = {'rect':pygame.Rect(-100,-100,100,100), 'color': (0,25,0), 'active': 0}
c = {'rect':pygame.Rect(-100,-100,100,100), 'color': (25,0,0), 'active': 0}
boss = {'rect':pygame.Rect(1300,84,125,265), 'color': (100,100,100), 'active': 1}
Boss = pygame.image.load('boss.png')
BOSS = {'image': pygame.transform.scale(Boss, (125,265)), 'active': 1, 'rect': boss}
bosshp = 25
bosshealth = pygame.font.SysFont("Garamond", 60)
initTime = 0
lastMissle = 0
lastNuke = 0
nuke = {'rect':pygame.Rect(1400,84,150,150), 'color': (255,0,0), 'active':0, 'hp': 8, 'time': 0}
nukecontrol = pygame.image.load('nukecontrol.png')
nukeCont = {'image':pygame.transform.scale(nukecontrol, (175,175)), 'active': 1, 'rect': nuke}
nuketime = pygame.font.SysFont("Garamond", 60)
missle1 = {'rect':pygame.Rect(1400,-100,600,110), 'color': (0,0,255), 'active':0, 'hp': 1}
missle2 = {'rect':pygame.Rect(1400,-100,600,110), 'color': (0,0,255), 'active':0, 'hp': 1}
missle3 = {'rect':pygame.Rect(1400,-100,600,110), 'color': (0,0,255), 'active':0, 'hp': 1}
M = pygame.image.load('missle.png')
Ms1 = {'image': pygame.transform.scale(M, (385,100)), 'active': 1, 'rect': missle1}
Ms2 = {'image': pygame.transform.scale(M, (385,100)), 'active': 1, 'rect': missle2}
Ms3 = {'image': pygame.transform.scale(M, (385,100)), 'active': 1, 'rect': missle3}
missles = [missle1,missle2,missle3]
obj = [boss,nuke,q,w,e,a,s,d,z,x,c]
alphaRect = pygame.Surface((100, 100))
alphaRect.set_alpha(0)
alphaRect.fill((0,0,0))
Q = pygame.image.load('q.png')
W = pygame.image.load('w.png')
E = pygame.image.load('e.png')
A = pygame.image.load('a.png')
S = pygame.image.load('s.png')
D = pygame.image.load('d.png')
Z = pygame.image.load('z.png')
X = pygame.image.load('x.png')
C = pygame.image.load('c.png')
Qs = {'image':pygame.transform.scale(Q, (100,100)), 'active': 1, 'rect': q}
Ws = {'image':pygame.transform.scale(W, (100,100)), 'active': 1, 'rect': w}
Es = {'image':pygame.transform.scale(E, (100,100)), 'active': 1, 'rect': e}
As = {'image':pygame.transform.scale(A, (100,100)), 'active': 1, 'rect': a}
Ss = {'image':pygame.transform.scale(S, (100,100)), 'active': 1, 'rect': s}
Ds = {'image':pygame.transform.scale(D, (100,100)), 'active': 1, 'rect': d}
Zs = {'image':pygame.transform.scale(Z, (100,100)), 'active': 1, 'rect': z}
Xs = {'image':pygame.transform.scale(X, (100,100)), 'active': 1, 'rect': x}
Cs = {'image':pygame.transform.scale(C, (100,100)), 'active': 1, 'rect': c}
hb = pygame.image.load('hoverboard.png')
HBs = {'image':pygame.transform.scale(hb, (100, 39)), 'active': 1}
img = [nukeCont,HBs,Qs,Ws,Es,As,Ss,Ds,Zs,Xs,Cs,BOSS,Ms1,Ms2,Ms3]

menuChoice = 0
mouseLocation = [0,0]
earth = pygame.image.load('Earth.png')
earthScaled = pygame.transform.scale(earth, (1300, 800))
earthHP = [5]
earthhealth = pygame.font.SysFont("Garamond", 60)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	if menuChoice == 0:
		screen.blit(earthScaled, (0,0))
		drawTitle = title.render("The Red Coats", 1, (255,255,255))
		screen.blit(drawTitle, (400, 100))
		drawName = stage1.render("by Richard Tea",1,(255,255,255))
		screen.blit(drawName, (485, 150))
		drawPress = presstobegin.render("Click anywhere to start. Press 'i' for instructions.", 1, (255,255,255))
		screen.blit(drawPress, (100, 200))
		if event.type == MOUSEBUTTONDOWN:
			menuChoice = 1
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
		if event.type == KEYDOWN:
			if event.key == ord('i'):
				menuChoice = 1.5
			if event.key == ord('n'):
				menuChoice = 2
			if event.key == ord('m'):
				menuChoice = 3
			if event.key == ord(','):
				menuChoice = 4
			if event.key == ord('.'):
				menuChoice = 5
		pygame.display.update()
	if menuChoice == 1.5:
		screen.blit(earthScaled, (0,0))
		drawInform = inform.render("The English alphabet has declared war on Earth and are sending a group to invade!", 1, (255,255,255))
		screen.blit(drawInform, (100, 0))
		drawStage1 = stage1.render("Stage 1:", 1, (255,255,255))
		screen.blit(drawStage1, (1100, 50))
		drawstage1inst = stage1inst.render("Hover the mouse over the letters and click the corresponding key on the keyboard.", 1, (255,255,255))
		screen.blit(drawstage1inst, (268, 100))
		drawNotes = notes.render("Destroy 15 in 15 seconds to move onto Stage 2. Avoid moving mouse when pressing key on keyboard.", 1, (255,255,255))
		screen.blit(drawNotes, (40, 150))
		drawStage2 = stage2.render("Stage 2:", 1, (255,255,255))
		screen.blit(drawStage2, (1100, 200))
		drawstage2inst = stage2inst.render("Left mouse click the boss to inflict damage. Destroy nuke control and missles that he sends.", 1, (255,255,255))
		screen.blit(drawstage2inst, (150, 250))
		drawPress = presstobegin.render("Click anywhere to start.", 1, (0,255,0))
		screen.blit(drawPress, (330, 600))
		if event.type == MOUSEBUTTONDOWN:
			menuChoice = 1
		pygame.display.update()
	if menuChoice == 1:
		if initialTime == 0:
			initialTime = time.time()
		if event.type == MOUSEBUTTONDOWN:
			print(str(event.pos[0]) + ', ' + str(event.pos[1]))
		if event.type == KEYDOWN:
				blaster.play()
				listofevents = pygame.event.get()
				mouseLocation = pygame.mouse.get_pos()
				if event.key == ord('q'):
					checkCollision(q, mouseLocation)
				if event.key == ord('w'):
					checkCollision(w, mouseLocation)
				if event.key == ord('e'): 
                                        checkCollision(e, mouseLocation) 
				if event.key == ord('a'): 
                                        checkCollision(a, mouseLocation) 
				if event.key == ord('s'): 
                                        checkCollision(s, mouseLocation) 
				if event.key == ord('d'): 
                                        checkCollision(d, mouseLocation)
				if event.key == ord('z'): 
                                        checkCollision(z, mouseLocation) 
				if event.key == ord('x'): 
                                        checkCollision(x, mouseLocation) 
				if event.key == ord('c'): 
                                        checkCollision(c, mouseLocation) 
		screen.blit(earthScaled, (0,0))
		for i in obj:
			drawObj(i)
		for j in img:
			drawImg(j)
		if loc[0] == 0 and loc[1] == 0 and loc[2] == 0 and loc[3] == 0 and loc[4] == 0:
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))

		if score[0] >= 15:
			menuChoice = 2
			for i in obj:
				despawnRect(i)
		if int(time.time() - initialTime) >= 15:
			menuChoice = 5
		drawTime = timeleft.render("Time: " + str((15 - int(time.time()-initialTime))), 1, (0,255,0))
		screen.blit(drawTime, (500,0))
		drawScore = playerscore.render("Score: " + str(score[0]), 1, (0,255,0))
		screen.blit(drawScore, (0,0))
		pygame.display.update()
	if menuChoice == 2:
		HBs['active'] = 0
		screen.blit(earthScaled, (0,0))
		if boss['rect'].left > 1112:
			boss['rect'].left -= 8
		else:
			menuChoice = 3
		for i in obj:
			drawObj(i)
		for j in img:
			drawImg(j)
		pygame.display.update()
	if menuChoice == 3:
		screen.blit(earthScaled, (0,0))
		if initTime == 0:
			initTime = time.time()
			lastMissle = time.time()
			lastNuke = time.time()
		if int(time.time() - lastMissle) >= 5 and missle1['active'] == 0 and missle2['active'] == 0 and missle3['active'] == 0:
			spawnMissles()
			lastMissle = time.time()
		if int(time.time() - lastNuke) >= 12:
			print("Spawning Nuke!")
			spawnRect(nuke)
			spawnRect(randLetter(q,w,e,a,s,d,z,x,c))
			nuke['time'] = time.time()
			lastNuke = time.time()	
		if event.type == MOUSEBUTTONDOWN:
			blaster.play()
			mouseLocation = pygame.mouse.get_pos()
			time.sleep(0.01)
			if  (boss['rect'].left < event.pos[0]) and (boss['rect'].right > event.pos[0]) and (boss['rect'].top < event.pos[1]) and (boss['rect'].bottom > event.pos[1]):
				bosshp -= 0.2
			checkCollision(missle1, mouseLocation)
			checkCollision(missle2, mouseLocation)
			checkCollision(missle3, mouseLocation)
		if event.type == KEYDOWN:
			time.sleep(0.01)
			mouseLocation = pygame.mouse.get_pos()
			if event.key == ord('q'):
				checkCollision(q, mouseLocation)
			if event.key == ord('w'):
				checkCollision(w, mouseLocation)
			if event.key == ord('e'):
				checkCollision(e, mouseLocation)
			if event.key == ord('a'):
				checkCollision(a, mouseLocation)
			if event.key == ord('s'):
				checkCollision(s, mouseLocation)
			if event.key == ord('d'):
				checkCollision(d, mouseLocation)
			if event.key == ord('z'):
				checkCollision(z, mouseLocation)
			if event.key == ord('x'):
				checkCollision(x, mouseLocation)
			if event.key == ord('c'):
				checkCollision(c, mouseLocation)
		checkoutofBounds()
		if bosshp <= 0:
			menuChoice = 4
		if earthHP[0] <= 0:
			menuChoice = 5
		for i in obj:
			drawObj(i)
		for k in missles:
			drawObj(k)
		for j in img:
			drawImg(j)
		if (time.time() - lastNuke >= 8) and nuke['active'] == 1:
			menuChoice = 5
		drawBossHP = bosshealth.render("BOSS HP: " + str(int(bosshp)), 1, (0,255,0))
		screen.blit(drawBossHP, (1020, 0))
		drawEarthHP = earthhealth.render("Earth HP: " + str(earthHP[0]), 1, (0,255,0))
		screen.blit(drawEarthHP, (0,0))
		if (nuke['active'] == 1):
			drawNukeTime = nuketime.render(str(8 - int(time.time() - lastNuke)), 1, (255,0,0))
			screen.blit(drawNukeTime, (875, 100))
		pygame.display.update()
	if menuChoice == 4:
		screen.blit(earthScaled, (0,0))
		drawWin = presstobegin.render("You saved Earth!", 1, (255,255,255))
		screen.blit(drawWin, (450, 200))
		pygame.display.update()
	if menuChoice == 5:
		screen.blit(earthScaled, (0,0))
		drawLose = presstobegin.render("Game Over. You Lost.", 1, (255,255,255))
		screen.blit(drawLose, (425,200))
		pygame.display.update()






















