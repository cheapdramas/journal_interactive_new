from fastapi import APIRouter,Request
import requests
from fastapi.templating import Jinja2Templates
from pathlib import Path
import ast

path_templates = f'{Path(__file__).parent}' + '/templates'

templates = Jinja2Templates(path_templates)

MAIN_PAGE = 'http://127.0.0.1:8000'




router = APIRouter()

def get_namescname():
    url = 'https://16.16.198.178.nip.io/0986525956Ee/id_name_secname'
    req = requests.get(url)
    return ast.literal_eval(req.text)

def get_all_subjects():
    url = 'https://16.16.198.178.nip.io/0986525956Ee/all_subjects'
    req = requests.get(url)
    return ast.literal_eval(req.text)

def get_dates_represent():
    url = 'https://16.16.198.178.nip.io/get_dates_represent'
    req= requests.get(url)
    return ast.literal_eval(req.text)
def get_schedule(day_index:int):
    url = f'https://16.16.198.178.nip.io/get_schedule?day_index={day_index}'
    req= requests.get(url)
    return ast.literal_eval(req.text)






@router.get('/test')
async def test():
    return get_schedule(1)

@router.get('/')
async def main_page_url(request:Request):
    global MAIN_PAGE
    return templates.TemplateResponse('main.html',{'request':request,'main_page':MAIN_PAGE})

@router.get('/add_marks')
async def add_marks(request:Request):
    global MAIN_PAGE
    students = get_namescname()
    students_list  =[]
    for i in students:
        students_list.append([i[0],i[1] +' ' + i[2]])
    marks_list = [i for i in range(1,13)]

    return templates.TemplateResponse('add_mark.html',{'request':request,'marks_list' : marks_list,'student_list' : students_list,'subj_list': get_all_subjects(),'name':'idk','main_page':MAIN_PAGE})


@router.get('/add_hw')
async def add_homework(request:Request):
    global MAIN_PAGE
    dates_represent = get_dates_represent()
    
    return templates.TemplateResponse('add_homework.html',{'request': request,'date_list':dates_represent,'name':'homework','main_page':MAIN_PAGE})


@router.get('/schedule')
async def schedule_lobby(request:Request):
    global MAIN_PAGE
    return templates.TemplateResponse('schedule_main.html',{'request':request,'main_page':MAIN_PAGE})

@router.get('/schedule/monday')
async def change_schedule_monday_url(request:Request):
    global MAIN_PAGE
    schedule = get_schedule(0)
    title = 'Розклад на понеділок'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=1'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route,'main_page':MAIN_PAGE})


@router.get('/schedule/tuesday')
async def change_schedule_monday_url(request:Request):
    global MAIN_PAGE
    schedule = get_schedule(1)
    title = 'Розклад на вівторок'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=2'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route,'main_page':MAIN_PAGE})

@router.get('/schedule/wednesday')
async def change_schedule_monday_url(request:Request):
    global MAIN_PAGE
    schedule = get_schedule(2)
    title = 'Розклад на середу'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=3'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route,'main_page':MAIN_PAGE})


@router.get('/schedule/thursday')
async def change_schedule_monday_url(request:Request):
    global MAIN_PAGE
    schedule = get_schedule(3)
    title = 'Розклад на четвер'
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=4'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route,'main_page':MAIN_PAGE})


@router.get('/schedule/friday')
async def change_schedule_monday_url(request:Request):
    global MAIN_PAGE
    schedule = get_schedule(4)
    title = "Розклад на п'ятницю"
    route = 'https://16.16.198.178.nip.io/change_schedule?day_index=5'
    all_subjects = get_all_subjects()

    return templates.TemplateResponse('schedule.html',{'request':request,'title':title,'schedule':schedule,'all_subjects':all_subjects,'name':'schedule','route':route,'main_page':MAIN_PAGE})
