from django.shortcuts import render,HttpResponse
import openai 
openai.api_key="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"




def index(request):
    return render(request,'index.html')




def generate(up):
    
    Completion=openai.Completion.create(
        engine="text-davinci-003",
        prompt=up,
        max_tokens=1000
    )
    return Completion.choices[0]['text']

def aboutme(request):
    return render(request,'AboutME.html')

def abtp(request):
    return render(request,'aboutthisproject.html')

# response=generate()

def search(request):
    
    try:
        up=request.GET['val']
        response=generate(up)
        return HttpResponse(response)
        
    except:
        return HttpResponse('INVALID QUESTION')
    

def generateimg(up):
    response = openai.Image.create(
    prompt=up,
    n=1,
    size="1024x1024"
    )
    return response['data'][0]['url']
    
def img(request):
    
    try:
        up=request.GET['val']
        print(up)
        response=generateimg(up)
        return HttpResponse(response)
        
    except:
        return HttpResponse('INVALID QUESTION')
    