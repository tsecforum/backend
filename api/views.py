from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Organisation, Scholarship, Application
import json
from json import JSONDecodeError
from django.forms.models import model_to_dict
from django.db.models import Q


@csrf_exempt
def post_organisation(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid JSON")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) > 0:
        try:
            existing.update(**content)
        except Exception:
            print("Invalid update")
            return JsonResponse({'success': False})
    else:
        try:
            new_org = Organisation(**content)
        except Exception:
            print("Invalid create")
            return JsonResponse({'success': False})
        new_org.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_organisation(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': True, 'exists': False})
    else:
        organisation_dict = model_to_dict(existing[0])
        organisation_dict['exists'] = True
        organisation_dict['success'] = True
        return JsonResponse(organisation_dict)


@csrf_exempt
def post_student(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid JSON")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) > 0:
        try:
            existing.update(**content)
        except Exception:
            print("Invalid update")
            return JsonResponse({'success': False})
    else:
        try:
            new_org = Student(**content)
        except Exception:
            print("Invalid create")
            return JsonResponse({'success': False})
        new_org.save()
    return JsonResponse({'success': True})


@csrf_exempt
def post_scholarship(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid JSON")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    # existing = Scholarship.objects.filter(uid=uid)
    # if len(existing) > 0:
    #     try:
    #         existing.update(**content)
    #     except Exception:
    #         print("Invalid update")
    #         return JsonResponse({'success': False})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) == 0:
        print("Invalid UID")
        return JsonResponse({'success': False})
    else:
        del content['uid']
        try:
            new_shp = Scholarship(**content)
        except Exception:
            print("Invalid create")
            return JsonResponse({'success': False})
        new_shp.organisation = existing[0]
        new_shp.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_student(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': True, 'exists': False})
    else:
        student_dict = model_to_dict(existing[0])
        student_dict['exists'] = True
        student_dict['success'] = True
        return JsonResponse(student_dict)


@csrf_exempt
def get_type(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) > 0:
        return JsonResponse({'success': True, 'type': 'student'})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) > 0:
        return JsonResponse({'success': True, 'type': 'organisation'})
    return JsonResponse({'success': True, 'type': 'none'})


@csrf_exempt
def get_scholarship(request):
    all_scholarships = Scholarship.objects.all()
    scholarships = []
    for scholarship in all_scholarships:
        scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
                             scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
        scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarships': scholarships, 'success': True}
    return JsonResponse(scholarship_dict)


@csrf_exempt
def get_scholarship_details(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        sid = content['sid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Scholarship.objects.filter(id=sid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    # scholarships = []
    # for scholarship in all_scholarships:
    #     scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
    #                          scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
    #     scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarship': model_to_dict(
        existing[0]), 'success': True}
    return JsonResponse(scholarship_dict)


@csrf_exempt
def get_scholarship_organisation(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    organisation = existing[0]
    filtered_scholarships = Scholarship.objects.all()
    scholarships = []
    for scholarship in filtered_scholarships:
        scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
                             scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
        scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarships': scholarships, 'success': True}
    return JsonResponse(scholarship_dict)


@csrf_exempt
def get_scholarship_eligible(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    student = existing[0]
    gender = student.gender
    state = student.state
    religion = student.religion
    max_annual_income = student.annual_income
    category = student.category
    course = student.course_interested_in
    physically_challenged = student.physically_challenged
    filtered_scholarships = Scholarship.objects.filter(Q(gender=gender) | Q(gender='')).filter(Q(state=state) | Q(state='')).filter(Q(religion=religion) | Q(religion='')).filter(Q(max_annual_income=max_annual_income) | Q(
        max_annual_income=None)).filter(Q(category=category) | Q(category='')).filter(Q(course=course)).filter(Q(physically_challenged=physically_challenged) | Q(physically_challenged=''))
    scholarships = []
    for scholarship in filtered_scholarships:
        scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
                             scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
        scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarships': scholarships, 'success': True}
    return JsonResponse(scholarship_dict)


@csrf_exempt
def post_scholarship_apply(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    student = existing[0]
    try:
        sid = content['sid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Scholarship.objects.filter(id=sid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    scholarship = existing[0]
    application = Application(
        student=student, scholarship=scholarship, application_status='Pending')
    application.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_scholarship_application(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        sid = content['sid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Scholarship.objects.filter(id=sid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    applications = Application.objects.filter(scholarship=existing[0])
    application_list = []
    for application in applications:
        application_entry = {
            'student_id': application.student.id, 'status': application.application_status}
        application_list.append(application_entry)
    application_dict = {'applications': application_list, 'success': True}
    return JsonResponse(application_dict)


@csrf_exempt
def post_application_status(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        aid = content['aid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Application.objects.filter(id=aid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    application = existing[0]
    try:
        new_status = content['new_status']
    except KeyError:
        return JsonResponse({'success': False})
    if new_status == 'Accepted' or new_status == 'Rejected':
        application.application_status = new_status
        application.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_scholarship_filter(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    filtered_scholarships = Scholarship.objects.all()
    params = ['gender',
              'state',
              'religion',
              'category',
              'course',
              'physically_challenged', ]
    for key in params:
        try:
            value = content[key]
            kwarg1 = {key: value}
            kwarg2 = {key: ''}
            filtered_scholarships = filtered_scholarships.filter(Q(**kwarg1) | Q(**kwarg2))
        except KeyError:
            pass
    try:
        value = content['max_annual_income']
        kwarg1 = {'max_annual_income__gte': value}
        kwarg2 = {'max_annual_income': None}
        filtered_scholarships = filtered_scholarships.filter(Q(**kwarg1) | Q(**kwarg2))
    except KeyError:
        pass
    scholarships = []
    for scholarship in filtered_scholarships:
        scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
                             scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
        scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarships': scholarships, 'success': True}
    return JsonResponse(scholarship_dict)
