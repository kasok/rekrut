from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, Http404

from django.shortcuts import render
from django.utils import timezone

from .models import Message
from .serializers import MessageSerializer

from rest_framework import viewsets, permissions, generics

class MessageViewSet(viewsets.ModelViewSet): 
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all()
#    recipient = request.query_params.get('recipient', None)
#    if username is not None:
#        queryset = queryset.filter(recipient=recipient)
    serializer_class = MessageSerializer
    def get_queryset(self):
        if 'recipient' in self.request.GET:
            recipient = self.request.GET['recipient']
            return Message.objects.filter(recipient=recipient)
        else:
            return Message.objects.all()


def index(request):    
    return render(request,'messages/index.html', {})
    
def list(request):
    recipient = request.POST['recipient']
    messages = Message.objects.filter(recipient = recipient).filter(read_date__isnull=True)
    context = {'messages_list': messages,}
    return render(request, 'messages/list.html', context)
    
def read(request, id):
    try:
        message = Message.objects.get(pk=id)
    except Message.DoesNotExist:
        raise Http404('Wiadomosc nie istnieje.')    
        
    if not message.read_date:    
        message.read_date = timezone.now()
        message.save()
    else:
        return HttpResponse('Wiadomosc zostala juz odczytana.<br /><a href="../" >Powrót</a>')
    
    return render(request, 'messages/read.html',  {'message': message})
    
def send(request):
    m = Message (text = request.POST['text'], recipient = request.POST['recipient'])
    m.save()
    return HttpResponse('<h1>Wysłano pomyślnie</h1><br /><a href="./" >Powrót</a>');
    