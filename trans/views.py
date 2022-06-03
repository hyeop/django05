from django.shortcuts import render
from googletrans import Translator
from googletrans import LANGUAGES
# Create your views here.
def index(request):
    # print(LANGUAGES)
    context = {
        "ndict" : LANGUAGES
    }
    if request.method == "POST":
        b = request.POST.get("bf")
        s = request.POST.get("fr")
        d = request.POST.get("to")
        
        tra = Translator()
        after = tra.translate(b, src=s, dest=d)
        context.update({
            "af" : after.text,
            "bf" : b,
            "fr" : s,
            "to" : d
        })
    return render(request, "trans/index.html", context)