from django.shortcuts import render
from django.http import HttpResponse
from .cryptogr import Encry, Decry
def home(request):
	return HttpResponse('<h1>Главная</h1>')
 
def crypto(request):
	return HttpResponse('Криптография')

def encode_message(request):
    if request.method == 'POST':
        ls = list(request.POST)
        if "encode" in ls:
            message = request.POST.get('message')
            key = request.POST.get('key')
            result = Encry(message,key)
            return render(request, 'C:/vscode/cryptograph/crypto/temptates/crypto1.html', {'result': result})
        elif "decode" in ls:
            message = request.POST.get('message')
            key = request.POST.get('key')
            result = Decry(message,key)
            return render(request, 'C:/vscode/cryptograph/crypto/temptates/crypto1.html', {'result': result})
    else:
        return render(request, 'C:/vscode/cryptograph/crypto/temptates/crypto1.html')