from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def loki(request):
    return HttpResponse("loki is a good guy")

def salaar(request):
    return HttpResponse('''<h1><img src="https://imgs.search.brave.com/ZShadkv21VuVGjM-2rn4fmw2ancFTj9Cn6oigPsVXl8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMxLnNyY2RuLmNv/bS93b3JkcHJlc3Mv/d3AtY29udGVudC91/cGxvYWRzLzIwMjQv/MDQvc2FsYWFyLXBy/YWJoYXMtaG9sZGlu/Zy10d28tc3dvcmRz/LWFuZC1mbGV4aW5n/LWluLXNhbGFhci1w/YXJ0LTEtY2Vhc2Vm/aXJlLmpwZw" width:100% height:100% object-fit:cover>
                        <text align="center">Daily Dosage of salaar</h1>''')
