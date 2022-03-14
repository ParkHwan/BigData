from django.shortcuts import render, redirect
from django.http import HttpResponse
# from todaysPlay.models import Subway
from django.contrib.auth.models import User
# from todaysPlay.models import Cultureplace
from django.contrib import auth
import random
import json

def main(request):
    print(request.user.is_authenticated)
    print(request.user)
    j = random.randrange(1, 7)
    context = {
        'j': j,
        'link': ['미술관', '공연·전시장', '문화예술회관', '박물·기념관', '유적지', '문화원', '기타'],
        'link2': ['국악', '독주·독창회', '무용', '문화교양·강좌', '뮤지컬·오페라', '연극', '전시·미술', '콘서트', '클래식', '기타'],
    }
    return render(request, 'main.html', context)

def randomslot(request):
    randint = random.randrange(1, 16)
    if randint == 1:
        subwayNo = '1호선'
    elif randint == 2:
        subwayNo = '2호선'
    elif randint == 3:
        subwayNo = '3호선'
    elif randint == 4:
        subwayNo = '4호선'
    elif randint == 5:
        subwayNo = '5호선'
    elif randint == 6:
        subwayNo = '6호선'
    elif randint == 7:
        subwayNo = '7호선'
    elif randint == 8:
        subwayNo = '8호선'
    elif randint == 9:
        subwayNo = '9호선'
    elif randint == 10:
        subwayNo = '수인분당선'
    elif randint == 11:
        subwayNo = '신분당선'
    elif randint == 12:
        subwayNo = '경의선'
    elif randint == 13:
        subwayNo = '경춘선'
    elif randint == 14:
        subwayNo = '우이신설경전철'
    elif randint == 15:
        subwayNo = '공항철도'
    return HttpResponse(subwayNo)

def map(request):
    line = request.GET.get("line")
    if "1호선" in line:
        color = "#000099"
    elif "2호선" in line:
        color = "#008000"
    elif "3호선" in line:
        color = "#ff6600"
    elif "4호선" in line:
        color = "#0099ff"
    elif "5호선" in line:
        color = "#9900cc"
    elif "6호선" in line:
        color = "#993333"
    elif "7호선" in line:
        color = "#666633"
    elif "8호선" in line:
        color = "#e6005c"
    elif "9호선" in line:
        color = "#cc9900"
    elif "수인분당선" in line:
        color = "#ffcc00"
    elif "신분당선" in line:
        color = "#cc0000"
    elif "경의선" in line:
        color = "#00cc99"
    elif "경춘선" in line:
        color = "#00cc66"
    elif "우이신설경전철" in line:
        color = "#993333"
    else:
        color = "#33ccff"
    subwaylist = Subway.objects.filter(hosun__contains=line)
    hosunno, hosunno_1, hosunno_2, hosunno_3  = [], [], [], []
    for data in subwaylist:
        if line+"_1" in data.hosun:
            hosunno_1.append({"lat": data.lat, "lng": data.lng})
        elif line+"_2" in data.hosun:
            hosunno_2.append({"lat": data.lat, "lng": data.lng})
        elif line+"_3" in data.hosun:
            hosunno_3.append({"lat": data.lat, "lng": data.lng})
        else:
            hosunno.append({"lat": data.lat, "lng": data.lng})
    placelist = Cultureplace.objects.filter(lineNumber__contains=line)
    print(placelist)
    xy = []
    for coordinate in placelist:
        xy.append({"name": coordinate.placeName, "lat": coordinate.lat, "lng": coordinate.lng})
    context = {
        "line": line,
        "color": color,
        "hosun": hosunno,
        "hosun_1": hosunno_1,
        "hosun_2": hosunno_2,
        "hosun_3": hosunno_3,
        "xy": xy,
    }
    return render(request, 'googlemap.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect("main:main")
        else :
            return render(request, 'loginpage.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else :
        return render(request, 'loginpage.html')

def signInPage(request):
    res_data = None
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('pw1')
        repassword = request.POST.get('pw2')
        res_data = {}
        if User.objects.filter(username=id):
            res_data['error'] = '이미 가입된 아이디입니다.'
        elif password != repassword:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username=id, password=password)
            auth.login(request, user)
            return redirect("main:main")
    return render(request, 'signInPage.html', res_data)

def location1(request):
    i = request.GET.get("pid")
    with open('D:\lee\study\BigData\project\Data\place3.json','r',encoding='utf-8') as f:
        place1 = json.load(f)
    name = list(place1.keys())
    # Address =
    context = {
        'title': i,
        '미술관': {'ADM 갤러리':'미술관1 내용'},
        '공연장': {'공연장1': "공연장1 내용",
            '공연장2': "공연장2 내용",
            '공연장3': "공연장3 내용",},
        '문화예술회관': {'문화예술회관1': "공연장1 내용",
            '공연장2': "공연장2 내용",
            '공연장3': "공연장3 내용",},
        '박물관': {'박물·기념관1': "박물·기념관1 내용",
            '박물·기념관2': "박물·기념관2 내용",
            '박물·기념관': "박물·기념관3 내용",},
        '유적지': {'공연장1': "공연장1 내용",
            '공연장2': "공연장2 내용",
            '공연장3': "공연장3 내용",},
        '문화원': {'공연장1': "공연장1 내용",
            '공연장2': "공연장2 내용",
            '공연장3': "공연장3 내용",},
        '기타': {'공연장1': "공연장1 내용",
            '공연장2': "공연장2 내용",
            '공연장3': "공연장3 내용",},
    }
    return render(request, 'location1.html',context)

def location2(request):
    i = request.GET.get("pid")
    context = {
        'title': i,
        '국악': {'판소리 레미제라블 ＜구구선 사람들＞':'국악2'},
        '독창회': {'독주1' : '독주2'},
        '무용': {'무용1': '무용2'},
        '문화교양강좌': {'강좌1':'강좌2'},
        '뮤지컬·오페라': {'뮤지컬1':'뮤지컬2'},
        '연극': {'연극1':'연극2'},
        '전시미술': {'전시1':'전시2'},
        '콘서트': {'콘서트1':'콘서트2'},
        '클래식': {'클래식1':'클래식2'},
        '기타': {'기타1':'기타2'},
    }
    return render(request, 'location2.html',context)

def info1(request):
    with open('D:\lee\study\BigData\project\Data\place3.json','r',encoding='utf-8') as f:
        place1 = json.load(f)
    Name = request.GET.get("pid")
    LineNumber = place1[Name]['LineNumber']
    Station = place1[Name]['Station']
    Address = place1[Name]['Address']
    Telephone = place1[Name]['Telephone']
    Image = place1[Name]['Image']
    Website = place1[Name]['Website']
    OpeningHours = place1[Name]['OpeningHours']
    Fee = place1[Name]['Fee']
    Closed = place1[Name]['Closed']
    PayFree = place1[Name]['PayFree']
    Class = place1[Name]['Class']
    context = {
        'info1' : {
            'Name' : Name,
            'LineNumber' : LineNumber,
            'Station' : Station,
            "Address" : Address,
            "Telephone" : Telephone,
            "Image" : Image,
            "Website" : Website,
            "OpeningHours" : OpeningHours,
            "Fee" : Fee,
            "Closed" : Closed,
            "PayFree" : PayFree,
            "Class" : Class,
        },
    }
    return render(request, 'info1.html', context)

def info2(request):
    with open('D:\lee\study\BigData\project\Data\program3.json','r',encoding='utf-8') as f:
        program1 = json.load(f)
    Name = request.GET.get("pid")
    Fee = program1[Name]['Fee']
    Image = program1[Name]['Image']
    Category = program1[Name]['Category']
    PlaceName = program1[Name]['PlaceName']
    StartDay = program1[Name]['StartDay'][0:10]
    EndDay = program1[Name]['EndDay'][0:10]
    TargetAudience = program1[Name]['TargetAudience']
    context = {
        'info2' : {
            'Category' : Category,
            'Name' : Name,
            "Image": Image,
            "Fee" : Fee,
            "PlaceName" : PlaceName,
            "StartDay" : StartDay,
            "EndDay" : EndDay,
            "TargetAudience" : TargetAudience,
        },
    }
    return render(request, 'info2.html', context)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("main:loginPage")

