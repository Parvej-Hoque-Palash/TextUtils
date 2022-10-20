from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #Check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()

        params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed+ char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (charcounter == "on"):
        #analyzed = "Number of Character count is : "
        charcount=0
        for char in djtext:
            if char:
                charcount = charcount + 1

        analyzed=djtext + "\n Number of Character count is : "
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed, 'char_count': charcount}
        #return render(request, 'analyze.html', params)
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select any option.")

    return render(request, 'analyze.html', params)

