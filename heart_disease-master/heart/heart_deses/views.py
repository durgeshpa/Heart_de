from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
#import sys 
#no commond line argument hence no need sys library
#from sklearn.ensemble import RandomForestClassifier
##import numpy as np


#from heart import Slides

x=1
def heartdeses_prediction(lis):
	import numpy as np
	x=1
	if x!=0:
		from sklearn.ensemble import RandomForestClassifier
		import pandas as pd
		import numpy as np
		#from sklearn.metrics import confusion_matrix
		from sklearn.metrics import accuracy_score
		df=pd.read_csv(r"heart.csv")
		df.dropna(axis=0,how="all")
		df.dropna(axis=0,how="any")
		independent_variables=list(df.columns.values)
		independent_variables.remove("num")
		x= df[independent_variables]
		y=df["num"]
		from sklearn.model_selection import train_test_split
		x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=.80,random_state=1)
		ex= RandomForestClassifier()
		lm = ex.fit(x_train, y_train)
		#print(lm)
		y_train_pred = lm.predict(x_train)
		y_test_pred = (lm.predict(x_test))
		print(accuracy_score(y_test,y_test_pred))
		#y_test_pred[y_test_pred>0.5]=1
		#y_test_pred[y_test_pred<=.5]=0
		#print(len(independent_variables))
		#i=0
		#x_arg=(x_arg[0].split(","))
		#print(type(x_arg[0]))
		#print(float(x_arg[0]))
		'''for index in range(len(lis)):
        	t=float(lis[index])
        	dic[index]=lis[i]
        	dic[index]=t
        	i+=1'''
    	#x=x+1
	
	
	df=pd.DataFrame(lis,index=[0])	
	return np.round(lm.predict(df))



def hearts(request):
	res=render(request,"Slides/index.html")
	return res
def pridict(request):
	lis=request
	if request.method=='POST':
		#print(lis)
		lis={'age':request.POST['age'],'sex':request.POST['sex'],'cp':request.POST['cp'],'trestbps':request.POST['trestbps'],'chol':request.POST['chol'],'fbs':request.POST['fbs'],'restecg':request.POST['restecg'],'thalach':request.POST['thalach'],'exang':request.POST['exang'],'oldpeak':request.POST['oldpeak'],'slope':request.POST['slope'],'ca':request.POST['ca'],'thal':request.POST['thal']}
		
	#lis=lis[1:len(lis):]
	#print(lis)
	lis=heartdeses_prediction(lis)
	print(lis)
	print(lis[0])
	if lis[0]<=.5:
		lis='no'
	else:
		lis='yes'
	
	
	#lis.append("hari")
	#eturn render(request,"Slides/index.html",{'lis':lis})
	return JsonResponse(json.dumps(lis),safe=False)

		

	