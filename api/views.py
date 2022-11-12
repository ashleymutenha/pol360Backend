from rest_framework.response import Response 
from rest_framework.decorators import api_view,authentication_classes,permission_classes
import csv
from django.http import HttpResponse
import urllib.parse

from rest_framework.response import Response
from . import file
from .models import Details,Brokers
from .serialiser import DetailsSerialiser
import json
from django.core import serializers




 

@api_view(['POST','GET'])

# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])

def postData(request):
    if request.method =="POST":
        __data = request.data
        
        __details = Details.objects.all()
        __details.delete()
        
        __details =  Details.objects.all()

        request.session['data'] = request.data

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # return ip

        __data['ip'] = ip
        details = Details.objects.create(details=request.data)
        details.save()


        print("for post IP is",ip)
       
        return Response(None)



   
    # if request.method =="POST":
    #     __data = json.dumps(request.data)
        
    #     serializer = DetailsSerialiser(data = __data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)
       
    if request.method =="GET":
        items = Details.objects.all()
        serialiser = DetailsSerialiser(items , many =True)

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        print("for get IP is")

        # return ip
        
        return Response(serialiser.data)
   
        
        
        # values = request.session.get('data').values()
        # extractedValues =[]
        # keys =[]

        # for i in  request.session.get('data').keys():
        #     keys.append(i)

        # if keys.count('clientFirstName') ==1:
        #     name =request.session.get('data')['clientFirstName'] +' ' + request.session.get('data')['clientLastName'] + '.csv'
        #     print(name)

        #     for i in values:
        #         extractedValues.append(i)
        #     response = HttpResponse(
        #     content_type='text/csv',
        #     headers={'Content-Disposition': 'attachment; filename={}'.format(urllib.parse.quote(name))},
        #     )

        #     writer = csv.writer(response)
        #     writer.writerow(['FirstName', 'LastName', 'DOB','ID','Gender' ,'Address'
        #         ,'Productdescription' ,'memberType','ProductPremium','ProductType','accountNo','idNo','deductionDate'])
        #     writer.writerow(extractedValues)

        #     return response
           
        # else:
        #     return HttpResponse({'Server Error ! Click on Generate CSV again'})
           
@api_view(['GET'])
def checkPostedData(request):
    # # __data = request.session['data']
    # print(__data)
    return Response()
    # if request.method =="GET":
    #     keys =[]
    #     for i in  __data.keys():
    #         keys.append(i)

    #     if keys.count('clientFirstName') ==1:
    #         return Response({'Data Available'})
            
    #     else:
    #         return Response({'Server Error ! Click on Generate CSV again'})


@api_view(['POST'])
def addBroker(request):
    if request.method =="POST":
        try:
            filteredData =[]
            data = request.data
            if data != None:
                broker = Brokers.objects.create(brokers=request.data, status =request.data['status'])
                broker.save()
            brokers = serializers.serialize('json', Brokers.objects.all())
            print(request.data['status'])

            
            b = json.loads(brokers)
            for i in b :
                filteredData.append(i['fields']['brokers'])


            __response = {
                'response':'success',
                'data':filteredData
            }
            
            


            
            return Response(__response)
        except:
            __response = {
                'response':'Server failed',}
            return Response(__response)
            


@api_view(['GET'])
def getBrokers(request):
    if request.data!=None:
        brokers = serializers.serialize('json', Brokers.objects.all())
        filteredData =[]
        brokersList  =json.loads(brokers)

        print(brokersList)

        for i in brokersList:
            if i['fields']['status'] =='active':
                i['fields']['brokers']['status'] ='active'

            filteredData.append(i['fields']['brokers'])

        
        __response ={
            'response':'success',
            'data':filteredData
        }


        
        return Response(__response)


@api_view(['POST'])
def deleteBroker(request):
    if request.method =="POST":
        data = request.data
        if data != None:
            try:
                
                brokers = serializers.serialize('json', Brokers.objects.all())

                brokerList = json.loads(brokers)
                for i in brokerList:
                    if i['fields']['brokers']['brokerName'] ==data['brokerName']:
                        _id = i['pk']
                
                Brokers.objects.filter(id=_id).delete()

                __response ={
                    'response':'success',
                    
                }
                    
                
                return Response(__response)
            except:
                __response ={
                    'response':'failure',
                    
                }
                return Response(__response)

@api_view(['POST'])
def setAsDefault(request):
    if request.method =="POST":
        data = request.data
        if data != None:
            try:
                brokers = serializers.serialize('json', Brokers.objects.all())

                brokerList = json.loads(brokers)

                for i in brokerList:
                    if i['fields']['status'] =='active':
                        key = i['pk']
                        if key != None:
                            Brokers.objects.filter(id =key).update(status ='inactive')
                    if i['fields']['brokers']['brokerName'] ==data['brokerName']:
                        __key = i['pk']
                        Brokers.objects.filter(id=__key).update(status ='active')

                    
            


                __response ={
                    'response':'success'
                }

                return Response(__response)

            except:

                __response ={
                    'response':'failure'
                }

                return Response(__response)

                







           


        
        


       
 