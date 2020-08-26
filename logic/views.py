from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import EntriesModel, SaveRecords
from django.http import HttpResponse
from .serializer import EntriesSerializer
from django.conf import settings
import os




def index(request):
	with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
		return HttpResponse(f.read())






@api_view(['GET', 'POST'])
def EntriesAPIView(request):
	if request.method == 'POST':
		serializer = EntriesSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	serializer = EntriesSerializer(data=EntriesModel.objects.all(), many=True)


	serializer.is_valid()
	if len(serializer.data)==0:
		return Response([[{'id':0}]])
	res = []
	if serializer.data[0]['clr'] == 'red':
		first='red'
	else:
		first='black'
	start=0
	count=0
	dataS = serializer.data
	end=len(dataS)
	while(start<end):
		k = 0
		paas = []
		for data in dataS[start:]:
			print(first, data['clr'])
			if data['clr'] == first and k<=1:
				
				paas.append(data)
			else:
				k+=1
				if(k==1):
					paas.append(data)
				if first=="red":
					first="black"
				else:
					first="red"
			if k==2:
				break
			start+=1
		print(start-1)
		print([(i['id'], i['clr']) for i in paas])
		res.append(paas)

	return Response(res)








@api_view(['PUT'])
def updateEntryAPIView(request, id, num):
	pick = EntriesModel.objects.get(id=id)
	pick.number = num
	pick.save()
	return Response(status=status.HTTP_201_CREATED)






@api_view(['GET', 'DELETE'])
def new(request):
	new = EntriesModel.objects.all()
	for i in new:
		SaveRecords.objects.create(number=i.number, clr=i.clr, gametype=i.gametype, playedTime=i.playedTime)
		i.delete()

	return Response(status=status.HTTP_201_CREATED)
