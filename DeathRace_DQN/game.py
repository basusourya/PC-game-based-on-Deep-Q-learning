import cv2
import numpy as np
from PIL import Image
import copy
import timeit
import random
import sklearn
global PIL_background
global trick
global treat
global bug_o
global x_v
global y_v
global road
global road2
import os
import pygame
global coin
global crash





PIL_background=Image.open('images/grass.jpg')
PIL_background=PIL_background.resize((800,1000), Image.ANTIALIAS)

road=Image.open('images/road.jpg')
road=road.resize((400,1000), Image.ANTIALIAS)


road2=Image.open('images/road2.jpg')
road2=road2.resize((400,1000), Image.ANTIALIAS)


trick=Image.open('images/trick.png')
trick=trick.resize((100,100), Image.ANTIALIAS)

gold=Image.open('images/gold.png')
gold=gold.resize((100,100), Image.ANTIALIAS)

bug_o=Image.open('images/car.png')
bug_o=bug_o.resize((100,240), Image.ANTIALIAS)

fire1=Image.open('images/fire1.png')
fire1=fire1.resize((100,100), Image.ANTIALIAS)

fire2=Image.open('images/fire2.png')
fire2=fire2.resize((100,100), Image.ANTIALIAS)

pygame.init()
pygame.mixer.init()
coinm = pygame.mixer.Sound('sounds/coin.wav')
crash = pygame.mixer.Sound('sounds/crash.wav')


x_v=80
y_v=120

def userplay() :
	terminate_1=0
	terminate=0
	move_s=[]
	point_c=0
	Y=[]
	move=0
	obs_h=int(0)
	obs_a=0
	coin_c=0
	coin=0
	coin_m=0
	pygame.init()
	pygame.mixer.init()
	ft=40
	fire_timer=0
	#coinm=pygame.mixer.music.load('coin.mp3')
	#coinm = pygame.mixer.Sound('sounds/coin.wav')



	flag_t1=0
	flag_t2=0
	flag_t3=0
	flag_t4=0
	flag_star=0

	K=4
	A=21

	ux=200 + 100*int(random.random() * 4)
	uy=760
	pp=int(random.random() * 4)
	if pp==1 :
		flag_t1=1
	if pp==2 :
		flag_t2=1
	if pp==3 :
		flag_t3=1
	if pp==0 :
		flag_t4=1



	t1x=200 
	t1y=0

	t2x=300 
	t2y=0

	t3x=400 
	t3y=0

	t4x=500 
	t4y=0

	rand_time= A + int(random.random() * K)
	#X=np.zeros((1,1,y_v,x_v))
	#move_s.append(0)
	#Y.append(0.1)

	i=0
	while True:

		i+=1
		point=0.1

		frame=PIL_background.copy()
		if i%2 == 1 :
			frame.paste(road, (200,0))
		else :
			frame.paste(road2, (200,0))

		bug=bug_o.copy()
		if flag_t1==1 :
			frame.paste(trick, (t1x,t1y),trick)

		if flag_t2==1 :
			frame.paste(trick, (t2x,t2y),trick)

		if flag_t3==1 :
			frame.paste(trick, (t3x,t3y),trick)

		if flag_t4==1 :
			frame.paste(trick, (t4x,t4y),trick)

		if flag_t1==-1 :
			frame.paste(gold, (t1x,t1y),gold)

		if flag_t2==-1 :
			frame.paste(gold, (t2x,t2y),gold)

		if flag_t3==-1 :
			frame.paste(gold, (t3x,t3y),gold)

		if flag_t4==-1 :
			frame.paste(gold, (t4x,t4y),gold)


		
		frame.paste(bug, (ux,uy),bug)
		#x2i=frame.resize((y_v,x_v),Image.ANTIALIAS)
		#frame.paste(x2i, (600,0))
		if fire_timer!=0 :
			if (i/2)%2 == 1 :
				frame.paste(fire1, (ux,uy-40),fire1)
			else :
				frame.paste(fire2, (ux,uy-40),fire2)


		
		frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
		#x2i= cv2.cvtColor(np.array(x2i), cv2.COLOR_BGR2GRAY)
		#print x2i.shape
		#xi=np.reshape(x2i,(1,1,y_v,x_v))
		#val=int(point)
		font = cv2.FONT_HERSHEY_SIMPLEX

		#qval=model.predict_on_batch(xi)
		#move=np.argmax(qval)-1
		
		#X=np.concatenate((X,xi),axis=0)
		#move_s.append(move)
		cv2.putText(frame,'Time:' +str(i) ,(10,30), font, 1,(255,255,255),2)
		cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
		cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
		cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
		#cv2.putText(frame,'Current Reward: ' + str(point) ,(10,150), font, 1,(255,0,0),2)



		cv2.imshow('Gold Rush',frame)
		


		#print qval, move, 
		if move==1 :
			ux+=100
		if move==-1 :
			ux-=100
			

		if ux<200 :
			terminate=1
			point=-100
		elif ux>500 :
			terminate=1
			point=-100
			
	
		if abs(flag_t1)==1 :
			t1y=t1y+20

		if abs(flag_t2)==1 :
			t2y=t2y+20

		if abs(flag_t3)==1 :
			t3y=t3y+20

		if abs(flag_t4)==1 :
			t4y=t4y+20


		if abs(flag_t1)==1 :
			if abs(ux-t1x)<100 :
				if (uy-t1y)<100 and (t1y-uy)<=0 :
					#print '21'
					#terminate=int( 0.5 + 0.5*(flag_t1) )
					point= -75*flag_t1 + 25
					if flag_t1==-1 :
						coin_c+=1
						coinm.play()
					if flag_t1==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t1=0
					t1y=0
					
				

				if (t1y-uy)<240 and (uy-t1y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t1) )
					point= -75*flag_t1 + 25
					if flag_t1==-1 :
						coin_c+=1
						coinm.play()
					if flag_t1==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t1=0
					t1y=0



		if abs(flag_t2)==1 :
			if abs(ux-t2x)<100 :
				if (uy-t2y)<100 and (t2y-uy)<=0 :
					#print '21'
					#terminate=int( 0.5 + 0.5*(flag_t2) )
					point= -75*flag_t2 + 25
					if flag_t2==-1 :
						coin_c+=1
						coinm.play()
					if flag_t2==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t2=0
					t2y=0

				if (t2y-uy)<240 and (uy-t2y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t2) )
					point= -75*flag_t2 + 25
					if flag_t2==-1 :
						coin_c+=1
						coinm.play()
					if flag_t2==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t2=0
					t2y=0


		if abs(flag_t3)==1 :
			if abs(ux-t3x)<100 :
				if (uy-t3y)<100 and (t3y-uy)<=0 :
					#print '21'
					#terminate= int( 0.5 + 0.5*(flag_t3) )
					point= -75*flag_t3 + 25	
					if flag_t3==-1 :
						coin_c+=1
						coinm.play()
					if flag_t3==1 :
						obs_h+=1
						fire_timer=14
						crash.play()
					flag_t3=0
					t3y=0


				if (t3y-uy)<240 and (uy-t3y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t3) )
					point= -75*flag_t3 + 25
					if flag_t3==-1 :
						coin_c+=1
						coinm.play()
					if flag_t3==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t3=0
					t3y=0


		if abs(flag_t4)==1 :
			if abs(ux-t4x)<100 :
				if (uy-t4y)<100 and (t4y-uy)<=0 :
					#print '21'
					#terminate=int( 0.5 + 0.5*(flag_t4) )
					point= -75*flag_t4 + 25
					if flag_t4==-1 :
						coin_c+=1
						coinm.play()
					if flag_t4==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t4=0
					t4y=0


				if (t4y-uy)<240 and (uy-t4y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t4) )
					point= -75*flag_t4 + 25
					if flag_t4==-1 :
						coin_c+=1
						coinm.play()
					if flag_t4==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t4=0
					t4y=0

			
			

		if abs(flag_t1)==1 :
			if t1y>1000 :
				if (flag_t1)==-1:
					point=-40
					coin_m+=1
				if flag_t1==1 :
					obs_a+=1
				t1y=0
				flag_t1=0
				

		if abs(flag_t2)==1 :
			if t2y>1000 :
				if (flag_t2)==-1:
					point=-40
					coin_m+=1
				if flag_t2==1 :
					obs_a+=1
				t2y=0
				flag_t2=0
				

		if abs(flag_t3)==1 :
			if t3y>1000 :
				if (flag_t3)==-1:
					point=-40
					coin_m+=1
				if flag_t3==1 :
					obs_a+=1
				t3y=0
				flag_t3=0
				

		if abs(flag_t4)==1 :
			if t4y>1000 :
				if (flag_t4)==-1:
					point=-40
					coin_m+=1
				if flag_t4==1 :
					obs_a+=1
				t4y=0
				flag_t4=0
				
		

		if abs(flag_t1)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)

		if abs(flag_t2)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t1==0 and probabilty==1 :
					flag_t1=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)


		if abs(flag_t3)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t1==0 and probabilty==0 :
					flag_t1=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)

		if abs(flag_t4)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t1==0 and probabilty==2 :
					flag_t1=1
					rand_time= A + int(random.random() * K)


		if flag_star==0 :
			prop_star = int(random.random() * 4)
			if prop_star==0:
				flag_star=1
				n = 1 + int(random.random() * 4)
				if n==1 and flag_t1==0:
					flag_t1=-1
					coin+=1
				if n==2 and flag_t2==0:
					flag_t2=-1
					coin+=1
				if n==3 and flag_t3==0:
					flag_t3=-1
					coin+=1
				if n==4 and flag_t4==0:
					flag_t4=-1
					coin+=1

		if flag_t1!=-1 and flag_t2!=-1 and flag_t3!=-1 and  flag_t4!=-1 :
			flag_star=0



		if flag_t1==0 and flag_t2==0 and flag_t3==0 and flag_t4==0 :
			pp=int(random.random() * 4)
			obs+=1
			if pp==1 :
				flag_t1=1
			if pp==2 :
				flag_t2=1
			if pp==3 :
				flag_t3=1
			if pp==0 :
				flag_t4=1
			rand_time= A + int(random.random() * K)




		if rand_time !=0 :
			rand_time-=1
		

		#Y.append(point)
		point_c+=point
		print point
		
		if(abs(point_c)>3000):
			terminate=1

		k=cv2.waitKey(10)
		if k==27:
			break
		elif k== -1 :
			move=0
		elif k== 63235 :
			move=1
		elif k== 63234 :
			move=-1	
		else :
			print k
		


		if terminate==1 :
			break
	cv2.destroyAllWindows()
	if point_c<3000 :
		j=0
		while j<500 :
			frame=PIL_background.copy()
			frame.paste(road, (200,0))
			bug=bug_o.copy()
			if flag_t1==1 :
				frame.paste(trick, (t1x,t1y),trick)

			if flag_t2==1 :
				frame.paste(trick, (t2x,t2y),trick)

			if flag_t3==1 :
				frame.paste(trick, (t3x,t3y),trick)

			if flag_t4==1 :
				frame.paste(trick, (t4x,t4y),trick)

			if flag_t1==-1 :
				frame.paste(gold, (t1x,t1y),gold)

			if flag_t2==-1 :
				frame.paste(gold, (t2x,t2y),gold)

			if flag_t3==-1 :
				frame.paste(gold, (t3x,t3y),gold)

			if flag_t4==-1 :
				frame.paste(gold, (t4x,t4y),gold)


		
			frame.paste(bug, (ux,uy),bug)
		

			frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
			font = cv2.FONT_HERSHEY_SIMPLEX

		
			cv2.putText(frame,'Time:' +str(i) ,(10,30), font, 1,(255,255,255),2)
			cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
			cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
			cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
			cv2.putText(frame,'Toatled' ,(100,500), font, 6,(0,0,255),8)
			j+=1
			cv2.imshow('Gold Rush',frame)

			k=cv2.waitKey(50)
			if k==27:
				break
			cv2.destroyAllWindows()
	else :
		j=0
		while j<200 :
			frame=PIL_background.copy()
			frame.paste(road, (200,0))
			bug=bug_o.copy()
			if flag_t1==1 :
				frame.paste(trick, (t1x,t1y),trick)

			if flag_t2==1 :
				frame.paste(trick, (t2x,t2y),trick)

			if flag_t3==1 :
				frame.paste(trick, (t3x,t3y),trick)

			if flag_t4==1 :
				frame.paste(trick, (t4x,t4y),trick)

			if flag_t1==-1 :
				frame.paste(gold, (t1x,t1y),gold)

			if flag_t2==-1 :
				frame.paste(gold, (t2x,t2y),gold)

			if flag_t3==-1 :
				frame.paste(gold, (t3x,t3y),gold)

			if flag_t4==-1 :
				frame.paste(gold, (t4x,t4y),gold)


		
			frame.paste(bug, (ux,uy),bug)
		

			frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
			font = cv2.FONT_HERSHEY_SIMPLEX

		
			cv2.putText(frame,'Time:' +str(i) ,(10,30), font, 1,(255,255,255),2)
			cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
			cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
			cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
			cv2.putText(frame,'Victory' ,(100,500), font, 6,(0,255,0),8)
			j+=1
			cv2.imshow('Gold Rush',frame)
			k=cv2.waitKey(50)
			if k==27:
				break
			cv2.destroyAllWindows()


	return 0


def play(model) :
	terminate_1=0
	terminate=0
	#move_s=[]
	point_c=0
	#Y=[]
	move=0
	obs_h=int(0)
	
	obs_a=0
	coin_c=0
	coin=0
	coin_m=0
	
	#coinm=pygame.mixer.music.load('coin.mp3')




	flag_t1=0
	flag_t2=0
	flag_t3=0
	flag_t4=0
	flag_star=0
	ft=40
	fire_timer=0

	K=4
	A=21

	ux=200 + 100*int(random.random() * 4)
	uy=760
	pp=int(random.random() * 4)
	if pp==1 :
		flag_t1=1
	if pp==2 :
		flag_t2=1
	if pp==3 :
		flag_t3=1
	if pp==0 :
		flag_t4=1



	t1x=200 
	t1y=0

	t2x=300 
	t2y=0

	t3x=400 
	t3y=0

	t4x=500 
	t4y=0

	rand_time= A + int(random.random() * K)
	#X=np.zeros((1,1,y_v,x_v))
	#move_s.append(0)
	#Y.append(0.1)

	i=0
	while True:

		i+=1
		point=0.1

		frame=PIL_background.copy()
		if i%2 == 1 :
			frame.paste(road, (200,0))
		else :
			frame.paste(road2, (200,0))

		bug=bug_o.copy()
		if flag_t1==1 :
			frame.paste(trick, (t1x,t1y),trick)

		if flag_t2==1 :
			frame.paste(trick, (t2x,t2y),trick)

		if flag_t3==1 :
			frame.paste(trick, (t3x,t3y),trick)

		if flag_t4==1 :
			frame.paste(trick, (t4x,t4y),trick)

		if flag_t1==-1 :
			frame.paste(gold, (t1x,t1y),gold)

		if flag_t2==-1 :
			frame.paste(gold, (t2x,t2y),gold)

		if flag_t3==-1 :
			frame.paste(gold, (t3x,t3y),gold)

		if flag_t4==-1 :
			frame.paste(gold, (t4x,t4y),gold)


		
		frame.paste(bug, (ux,uy),bug)
		x2i=frame.resize((y_v,x_v),Image.ANTIALIAS)
		frame.paste(x2i, (600,0))
		if fire_timer!=0 :
			if (i/2)%2 == 1 :
				frame.paste(fire1, (ux,uy-40),fire1)
			else :
				frame.paste(fire2, (ux,uy-40),fire2)

		frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
		x2i= cv2.cvtColor(np.array(x2i), cv2.COLOR_BGR2GRAY)
		#print x2i.shape
		xi=np.reshape(x2i,(1,1,y_v,x_v))
		#val=int(point)
		font = cv2.FONT_HERSHEY_SIMPLEX

		qval=model.predict_on_batch(xi)
		move=np.argmax(qval)-1
		
		#X=np.concatenate((X,xi),axis=0)
		#move_s.append(move)
		cv2.putText(frame,'Time:' +str(i) ,(10,30), font, 1,(255,255,255),2)
		cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
		cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
		cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
		#cv2.putText(frame,'Current Reward: ' + str(point) ,(10,150), font, 1,(255,0,0),2)
		#cv2.putText(frame,'Toatled' ,(100,500), font, 6,(0,0,255),8)

		cv2.imshow('Gold Rush',frame)
		


		print qval, move, 
		if move==1 :
			ux+=100
		if move==-1 :
			ux-=100
			

		if ux<200 :
			terminate=1
			point=-100
		elif ux>500 :
			terminate=1
			point=-100
			
	
		if abs(flag_t1)==1 :
			t1y=t1y+20

		if abs(flag_t2)==1 :
			t2y=t2y+20

		if abs(flag_t3)==1 :
			t3y=t3y+20

		if abs(flag_t4)==1 :
			t4y=t4y+20


		if abs(flag_t1)==1 :
			if abs(ux-t1x)<100 :
				if (uy-t1y)<100 and (t1y-uy)<=0 :
					#print '21'
					#terminate=int( 0.5 + 0.5*(flag_t1) )
					point= -75*flag_t1 + 25
					if flag_t1==-1 :
						coin_c+=1
						coinm.play()
					if flag_t1==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t1=0
					t1y=0
					
				

				if (t1y-uy)<240 and (uy-t1y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t1) )
					point= -75*flag_t1 + 25
					if flag_t1==-1 :
						coin_c+=1
						coinm.play()
					if flag_t1==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t1=0
					t1y=0



		if abs(flag_t2)==1 :
			if abs(ux-t2x)<100 :
				if (uy-t2y)<100 and (t2y-uy)<=0 :
					#print '21'
					#terminate=int( 0.5 + 0.5*(flag_t2) )
					point= -75*flag_t2 + 25
					if flag_t2==-1 :
						coin_c+=1
						coinm.play()
					if flag_t2==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t2=0
					t2y=0

				if (t2y-uy)<240 and (uy-t2y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t2) )
					point= -75*flag_t2 + 25
					if flag_t2==-1 :
						coin_c+=1
						coinm.play()
					if flag_t2==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t2=0
					t2y=0


		if abs(flag_t3)==1 :
			if abs(ux-t3x)<100 :
				if (uy-t3y)<100 and (t3y-uy)<=0 :
					#print '21'
					#terminate= int( 0.5 + 0.5*(flag_t3) )
					point= -75*flag_t3 + 25	
					if flag_t3==-1 :
						coin_c+=1
						coinm.play()
					if flag_t3==1 :
						obs_h+=1
						fire_timer=14
						crash.play()
					flag_t3=0
					t3y=0


				if (t3y-uy)<240 and (uy-t3y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t3) )
					point= -75*flag_t3 + 25
					if flag_t3==-1 :
						coin_c+=1
						coinm.play()
					if flag_t3==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t3=0
					t3y=0


		if abs(flag_t4)==1 :
			if abs(ux-t4x)<100 :
				if (uy-t4y)<100 and (t4y-uy)<=0 :
					#print '21'
					#terminate=int( 0.5 + 0.5*(flag_t4) )
					point= -75*flag_t4 + 25
					if flag_t4==-1 :
						coin_c+=1
						coinm.play()
					if flag_t4==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t4=0
					t4y=0


				if (t4y-uy)<240 and (uy-t4y)<=0 :
					#print '22'
					#terminate=int( 0.5 + 0.5*(flag_t4) )
					point= -75*flag_t4 + 25
					if flag_t4==-1 :
						coin_c+=1
						coinm.play()
					if flag_t4==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t4=0
					t4y=0

			

		if abs(flag_t1)==1 :
			if t1y>1000 :
				if (flag_t1)==-1:
					point=-40
					coin_m+=1
				if flag_t1==1 :
					obs_a+=1
				t1y=0
				flag_t1=0
				

		if abs(flag_t2)==1 :
			if t2y>1000 :
				if (flag_t2)==-1:
					point=-40
					coin_m+=1
				if flag_t2==1 :
					obs_a+=1
				t2y=0
				flag_t2=0
				

		if abs(flag_t3)==1 :
			if t3y>1000 :
				if (flag_t3)==-1:
					point=-40
					coin_m+=1
				if flag_t3==1 :
					obs_a+=1
				t3y=0
				flag_t3=0
				

		if abs(flag_t4)==1 :
			if t4y>1000 :
				if (flag_t4)==-1:
					point=-40
					coin_m+=1
				if flag_t4==1 :
					obs_a+=1
				t4y=0
				flag_t4=0
				
		

		if abs(flag_t1)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)

		if abs(flag_t2)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t1==0 and probabilty==1 :
					flag_t1=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)


		if abs(flag_t3)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t1==0 and probabilty==0 :
					flag_t1=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)

		if abs(flag_t4)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t1==0 and probabilty==2 :
					flag_t1=1
					rand_time= A + int(random.random() * K)


		if flag_star==0 :
			prop_star = int(random.random() * 4)
			if prop_star==0:
				flag_star=1
				n = 1 + int(random.random() * 4)
				if n==1 and flag_t1==0:
					flag_t1=-1
					coin+=1
				if n==2 and flag_t2==0:
					flag_t2=-1
					coin+=1
				if n==3 and flag_t3==0:
					flag_t3=-1
					coin+=1
				if n==4 and flag_t4==0:
					flag_t4=-1
					coin+=1

		if flag_t1!=-1 and flag_t2!=-1 and flag_t3!=-1 and  flag_t4!=-1 :
			flag_star=0



		if flag_t1==0 and flag_t2==0 and flag_t3==0 and flag_t4==0 :
			pp=int(random.random() * 4)
			obs+=1
			if pp==1 :
				flag_t1=1
			if pp==2 :
				flag_t2=1
			if pp==3 :
				flag_t3=1
			if pp==0 :
				flag_t4=1
			rand_time= A + int(random.random() * K)




		if rand_time !=0 :
			rand_time-=1
		
		if fire_timer !=0 :
			fire_timer-=1

		#Y.append(point)
		point_c+=point
		print point
		if point_c>3000 :
			terminate=1
		
		
		k=cv2.waitKey(20)
		if k==27:
			break
		#elif k== -1 :
		#	move=0
		#elif k== 63235 :
		#	move=1
		#elif k== 63234 :
		#	move=-1	
		#else :
		#	print k
		


		if terminate==1 :
			break
	cv2.destroyAllWindows()
	if point_c<3000 :
		j=0
		while j<500 :
			frame=PIL_background.copy()
			frame.paste(road, (200,0))
			bug=bug_o.copy()
			if flag_t1==1 :
				frame.paste(trick, (t1x,t1y),trick)

			if flag_t2==1 :
				frame.paste(trick, (t2x,t2y),trick)

			if flag_t3==1 :
				frame.paste(trick, (t3x,t3y),trick)

			if flag_t4==1 :
				frame.paste(trick, (t4x,t4y),trick)

			if flag_t1==-1 :
				frame.paste(gold, (t1x,t1y),gold)

			if flag_t2==-1 :
				frame.paste(gold, (t2x,t2y),gold)

			if flag_t3==-1 :
				frame.paste(gold, (t3x,t3y),gold)

			if flag_t4==-1 :
				frame.paste(gold, (t4x,t4y),gold)


		
			frame.paste(bug, (ux,uy),bug)
		

			frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
			font = cv2.FONT_HERSHEY_SIMPLEX

		
			cv2.putText(frame,'Time:' +str(i) ,(10,30), font, 1,(255,255,255),2)
			cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
			cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
			cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
			cv2.putText(frame,'Toatled' ,(100,500), font, 6,(0,0,255),8)
			j+=1
			cv2.imshow('Gold Rush',frame)

			k=cv2.waitKey(10)
			if k==27:
				break
			cv2.destroyAllWindows()
	else :
		j=0
		while j<200 :
			frame=PIL_background.copy()
			frame.paste(road, (200,0))
			bug=bug_o.copy()
			if flag_t1==1 :
				frame.paste(trick, (t1x,t1y),trick)

			if flag_t2==1 :
				frame.paste(trick, (t2x,t2y),trick)

			if flag_t3==1 :
				frame.paste(trick, (t3x,t3y),trick)

			if flag_t4==1 :
				frame.paste(trick, (t4x,t4y),trick)

			if flag_t1==-1 :
				frame.paste(gold, (t1x,t1y),gold)

			if flag_t2==-1 :
				frame.paste(gold, (t2x,t2y),gold)

			if flag_t3==-1 :
				frame.paste(gold, (t3x,t3y),gold)

			if flag_t4==-1 :
				frame.paste(gold, (t4x,t4y),gold)


		
			frame.paste(bug, (ux,uy),bug)
		

			frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
			font = cv2.FONT_HERSHEY_SIMPLEX

		
			cv2.putText(frame,'Time:' +str(i)  ,(10,30), font, 1,(255,255,255),2)
			cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
			cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
			cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
			cv2.putText(frame,'Victory' ,(100,500), font, 6,(0,255,0),8)
			j+=1
			cv2.imshow('Gold Rush',frame)
			k=cv2.waitKey(50)
			if k==27:
				break
			cv2.destroyAllWindows()
	
	return 0





def state(Display,model,iterations,species) :
	#fourcc = cv2.cv.CV_FOURCC(*'XVID')
	#out = cv2.VideoWriter('Video/' + str(species) + '.avi', -1, 20.0, (1000,800))
	terminate_1=0
	terminate=0
	move_s=[]
	point_c=0
	Y=[]
	move=0
	ft=40
	fire_timer=0
	obs_h=int(0)
	obs_a=0
	coin_c=0
	coin=0
	coin_m=0
	pygame.init()
	pygame.mixer.init()
	#coinm=pygame.mixer.music.load('coin.mp3')
	#coinm = pygame.mixer.Sound('sounds/coin.wav')



	flag_t1=0
	flag_t2=0
	flag_t3=0
	flag_t4=0
	flag_star=0

	K=4
	A=21

	ux=200 + 100*int(random.random() * 4)
	uy=760
	pp=int(random.random() * 4)
	if pp==1 :
		flag_t1=1
	if pp==2 :
		flag_t2=1
	if pp==3 :
		flag_t3=1
	if pp==0 :
		flag_t4=1



	t1x=200 
	t1y=0

	t2x=300 
	t2y=0

	t3x=400 
	t3y=0

	t4x=500 
	t4y=0

	rand_time= A + int(random.random() * K)
	X=np.zeros((1,1,y_v,x_v))
	move_s.append(0)
	Y.append(0.1)

	i=0
	while True:

		i+=1
		point=0.1

		frame=PIL_background.copy()
		if i%2 == 1 :
			frame.paste(road, (200,0))
		else :
			frame.paste(road2, (200,0))

		bug=bug_o.copy()
		if flag_t1==1 :
			frame.paste(trick, (t1x,t1y),trick)

		if flag_t2==1 :
			frame.paste(trick, (t2x,t2y),trick)

		if flag_t3==1 :
			frame.paste(trick, (t3x,t3y),trick)

		if flag_t4==1 :
			frame.paste(trick, (t4x,t4y),trick)

		if flag_t1==-1 :
			frame.paste(gold, (t1x,t1y),gold)

		if flag_t2==-1 :
			frame.paste(gold, (t2x,t2y),gold)

		if flag_t3==-1 :
			frame.paste(gold, (t3x,t3y),gold)

		if flag_t4==-1 :
			frame.paste(gold, (t4x,t4y),gold)


		
		frame.paste(bug, (ux,uy),bug)
		x2i=frame.resize((y_v,x_v),Image.ANTIALIAS)
		frame.paste(x2i, (600,0))
		if fire_timer!=0 :
			if (i/2)%2 == 1 :
				frame.paste(fire1, (ux,uy-40),fire1)
			else :
				frame.paste(fire2, (ux,uy-40),fire2)



		frame= cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)
		x2i= cv2.cvtColor(np.array(x2i), cv2.COLOR_BGR2GRAY)
		#print x2i.shape
		xi=np.reshape(x2i,(1,1,y_v,x_v))
		val=int(point)
		font = cv2.FONT_HERSHEY_SIMPLEX

		qval=model.predict_on_batch(xi)
		move=np.argmax(qval)-1
		
		X=np.concatenate((X,xi),axis=0)
		move_s.append(move)
		cv2.putText(frame,'Time:' +str(i) + ' Generation :' + str(species),(10,30), font, 1,(255,255,255),2)
		cv2.putText(frame,'Score : '+ str(point_c) +' Move:' +str(move) ,(10,60), font, 1,(0,255,255),2)
		cv2.putText(frame,'Obstacle avoided :'+ str(obs_a) + '/' + str(obs_a+obs_h) + ' Obstacle Hitted :' + str(obs_h) + '/' + str(obs_a+obs_h) ,(10,90), font, 1,(255,0,255),2)
		cv2.putText(frame,'Coin collected :'+ str(coin_c) + '/' + str(coin)  +' Coin Missed :'+ str(coin_m) + '/' + str(coin) ,(10,120), font, 1,(255,255,0),2)
		#cv2.putText(frame,'Current Reward: ' + str(point) ,(10,150), font, 1,(255,0,0),2)


		if Display==True :
			cv2.imshow('Gold Rush',frame)
		


		print qval, move, 
		if move==1 :
			ux+=100
		if move==-1 :
			ux-=100
			

		if ux<200 :
			terminate=1
			point=-100
		elif ux>500 :
			terminate=1
			point=-100
			
	
		if abs(flag_t1)==1 :
			t1y=t1y+20

		if abs(flag_t2)==1 :
			t2y=t2y+20

		if abs(flag_t3)==1 :
			t3y=t3y+20

		if abs(flag_t4)==1 :
			t4y=t4y+20


		if abs(flag_t1)==1 :
			if abs(ux-t1x)<100 :
				if (uy-t1y)<100 and (t1y-uy)<=0 :
					#print '21'
					terminate=int( 0.5 + 0.5*(flag_t1) )
					point= -75*flag_t1 + 25
					if flag_t1==-1 :
						coin_c+=1
						coinm.play()
					if flag_t1==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t1=0
					t1y=0
					
				

				if (t1y-uy)<240 and (uy-t1y)<=0 :
					#print '22'
					terminate=int( 0.5 + 0.5*(flag_t1) )
					point= -75*flag_t1 + 25
					if flag_t1==-1 :
						coin_c+=1
						coinm.play()
					if flag_t1==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t1=0
					t1y=0



		if abs(flag_t2)==1 :
			if abs(ux-t2x)<100 :
				if (uy-t2y)<100 and (t2y-uy)<=0 :
					#print '21'
					terminate=int( 0.5 + 0.5*(flag_t2) )
					point= -75*flag_t2 + 25
					if flag_t2==-1 :
						coin_c+=1
						coinm.play()
					if flag_t2==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t2=0
					t2y=0

				if (t2y-uy)<240 and (uy-t2y)<=0 :
					#print '22'
					terminate=int( 0.5 + 0.5*(flag_t2) )
					point= -75*flag_t2 + 25
					if flag_t2==-1 :
						coin_c+=1
						coinm.play()
					if flag_t2==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t2=0
					t2y=0


		if abs(flag_t3)==1 :
			if abs(ux-t3x)<100 :
				if (uy-t3y)<100 and (t3y-uy)<=0 :
					#print '21'
					terminate= int( 0.5 + 0.5*(flag_t3) )
					point= -75*flag_t3 + 25	
					if flag_t3==-1 :
						coin_c+=1
						coinm.play()
					if flag_t3==1 :
						obs_h+=1
						fire_timer=14
						crash.play()
					flag_t3=0
					t3y=0


				if (t3y-uy)<240 and (uy-t3y)<=0 :
					#print '22'
					terminate=int( 0.5 + 0.5*(flag_t3) )
					point= -75*flag_t3 + 25
					if flag_t3==-1 :
						coin_c+=1
						coinm.play()
					if flag_t3==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t3=0
					t3y=0


		if abs(flag_t4)==1 :
			if abs(ux-t4x)<100 :
				if (uy-t4y)<100 and (t4y-uy)<=0 :
					#print '21'
					terminate=int( 0.5 + 0.5*(flag_t4) )
					point= -75*flag_t4 + 25
					if flag_t4==-1 :
						coin_c+=1
						coinm.play()
					if flag_t4==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t4=0
					t4y=0


				if (t4y-uy)<240 and (uy-t4y)<=0 :
					#print '22'
					terminate=int( 0.5 + 0.5*(flag_t4) )
					point= -75*flag_t4 + 25
					if flag_t4==-1 :
						coin_c+=1
						coinm.play()
					if flag_t4==1 :
						obs_h+=1
						fire_timer=ft
						crash.play()
					flag_t4=0
					t4y=0

			
			

		if abs(flag_t1)==1 :
			if t1y>1000 :
				if (flag_t1)==-1:
					point=-40
					coin_m+=1
				if flag_t1==1 :
					obs_a+=1
				t1y=0
				flag_t1=0
				

		if abs(flag_t2)==1 :
			if t2y>1000 :
				if (flag_t2)==-1:
					point=-40
					coin_m+=1
				if flag_t2==1 :
					obs_a+=1
				t2y=0
				flag_t2=0
				

		if abs(flag_t3)==1 :
			if t3y>1000 :
				if (flag_t3)==-1:
					point=-40
					coin_m+=1
				if flag_t3==1 :
					obs_a+=1
				t3y=0
				flag_t3=0
				

		if abs(flag_t4)==1 :
			if t4y>1000 :
				if (flag_t4)==-1:
					point=-40
					coin_m+=1
				if flag_t4==1 :
					obs_a+=1
				t4y=0
				flag_t4=0
				
		

		if abs(flag_t1)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)

		if abs(flag_t2)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t1==0 and probabilty==1 :
					flag_t1=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)


		if abs(flag_t3)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t1==0 and probabilty==0 :
					flag_t1=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t4==0 and probabilty==2 :
					flag_t4=1
					rand_time= A + int(random.random() * K)

		if abs(flag_t4)==1 :
			if rand_time==0 :
				probabilty=int(random.random()*3)
				if flag_t3==0 and probabilty==0 :
					flag_t3=1
					rand_time= A + int(random.random() * K)
				if flag_t2==0 and probabilty==1 :
					flag_t2=1
					rand_time= A + int(random.random() * K)
				if flag_t1==0 and probabilty==2 :
					flag_t1=1
					rand_time= A + int(random.random() * K)


		if flag_star==0 :
			prop_star = int(random.random() * 4)
			if prop_star==0:
				flag_star=1
				n = 1 + int(random.random() * 4)
				if n==1 and flag_t1==0:
					flag_t1=-1
					coin+=1
				if n==2 and flag_t2==0:
					flag_t2=-1
					coin+=1
				if n==3 and flag_t3==0:
					flag_t3=-1
					coin+=1
				if n==4 and flag_t4==0:
					flag_t4=-1
					coin+=1

		if flag_t1!=-1 and flag_t2!=-1 and flag_t3!=-1 and  flag_t4!=-1 :
			flag_star=0



		if flag_t1==0 and flag_t2==0 and flag_t3==0 and flag_t4==0 :
			pp=int(random.random() * 4)
			obs+=1
			if pp==1 :
				flag_t1=1
			if pp==2 :
				flag_t2=1
			if pp==3 :
				flag_t3=1
			if pp==0 :
				flag_t4=1
			rand_time= A + int(random.random() * K)




		if rand_time !=0 :
			rand_time-=1
		

		Y.append(point)
		point_c+=point
		print point
		
		if(abs(point_c)>1000):
			terminate=1

		k=cv2.waitKey(20)
		if k==27:
			break
		#elif k== -1 :
		#	move=0
		#elif k== 63235 :
		#	move=1
		#elif k== 63234 :
		#	move=-1	
		#else :
		#	print k
		


		if terminate==1 :
			break
	cv2.destroyAllWindows()

	return X,Y,move_s,terminate_1


