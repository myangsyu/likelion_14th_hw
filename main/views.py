from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 14,                   
        'info': {                           
            'weather': '비 조금',
            'feeling': '과제가 많아서 힘들다 ㅠㅠ',
            'note': '멋사 과제 파이팅해서 끝내기!'
        },
        'shortcuts': [
            '들여쓰기: Tab',
            '내어쓰기: Shift + Tab',
            '주석 처리: 윈도우- Ctrl + /, 맥- command + /',
            '자동 정렬: 윈도우- Shift + Alt + F, 맥- Shift + Option + F',
            '한 줄 이동: 윈도우- Alt + 방향키, 맥- Option + 방향키',     
            '한 줄 잘라내기: 윈도우- Ctrl + X, 맥- command + X',          
            '같은 단어 전체 선택: Ctrl + Shift + L'
        ]
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')