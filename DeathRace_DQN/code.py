from game import *
from keras.models import Sequential
from keras.layers import Dense
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.optimizers import Adam
from keras.layers.convolutional import Convolution2D, MaxPooling2D
import numpy as np
from keras.models import model_from_yaml
import os
import sys



to_do=int(sys.argv[1])


x_v=80
y_v=120

model = Sequential()
model.add(Convolution2D(32, 2, 2, border_mode='same', input_shape=(1,y_v,x_v)))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(512*2))
model.add(Activation('tanh'))
model.add(Dense(512))
model.add(Activation('tanh'))
model.add(Dense(3))
model.add(Activation('linear'))


species=1
Xi=np.zeros((1,1,y_v,x_v))
Y=np.zeros((1,3))

try :
	model.load_weights("model/model.h5")
	print 'Model loded'
except :
	print 'No weight found'

adam = Adam(lr=1e-5)
model.compile(loss='mse',optimizer=adam)
model.summary()

if to_do==0 :
	while True :
		iteration=1000
		X,point,move_s,terminate =state(int(sys.argv[2]),model,iteration,species)
		print X.shape
		gamma=0.99
		X=np.array(X)
		#print X.shape
		[ux,img_ch,x,y] = X.shape

		Xi=np.zeros((1,1,y_v,x_v))
		Y=np.zeros((1,3))
		


		move_s=np.array(move_s)
		move_s=np.reshape(move_s,(1,ux))
	
		point=np.array(point)
		point=np.reshape(point,(1,ux))
		loss=0

		for j in range(0,ux) :
			i=ux-j-1
			xold=X[i,:,:,:]
			xold=np.reshape(xold,(1,1,y_v,x_v))
			y=model.predict(xold)

			if i==ux-1 :
				y[0,move_s[0,i]+1]= point[0,i] 
			else :
				x=X[i+1,:,:,:]
				x=np.reshape(x,(1,1,y_v,x_v))
				Q=model.predict(x)

				y[0,move_s[0,i]+1]= point[0,i] + gamma*np.max(Q)


			#print Xi.shape
			#print xold.shape
			Xi=np.concatenate((Xi,xold),axis=0)
			Y=np.vstack((Y,y))
		loss=model.train_on_batch(Xi,Y)



	
		species+=1
		model.save_weights("model/model.h5")
		print loss
		if terminate==1 :
			break

if to_do==1 :
	while  True:
		play(model)

if to_do==2 :
	userplay()
	
	


	