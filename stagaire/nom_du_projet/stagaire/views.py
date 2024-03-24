from django.shortcuts import render,redirect
from pymongo import MongoClient
from bson import ObjectId
def home(request):
    with MongoClient('mongodb://localhost:27017/') as client:
        db = client['db_student']
        collection = db['students']

        students = list(collection.find())

        for student in students:
            student['id_str'] = str(student['_id'])

        context = {'students': students}

    return render(request, "stagaire/home.html", context)

def student_add(request):
    if request.method == 'POST':

        student_roll = request.POST.get("student_roll")
        student_name = request.POST.get("student_name")
        student_email = request.POST.get("student_email")
        student_address = request.POST.get("student_adress")
        student_phone = request.POST.get("student_phone")

        client = MongoClient('mongodb://localhost:27017/')
        db = client['db_student']  
        collection = db['students'] 
        student_data = {
            'roll': student_roll,
            'name': student_name,
            'email': student_email,
            'address': student_address,
            'phone': student_phone
        }
        collection.insert_one(student_data)
        client.close()
        return render(request, "stagaire/add_student.html", {})
    return render(request, "stagaire/add_student.html", {})

def delete_student(request, student_id):
    with MongoClient('mongodb://localhost:27017/') as client:
        db = client['db_student']
        collection = db['students']

        result = collection.delete_one({'_id': ObjectId(student_id)})
        
        if result.deleted_count == 1:
            return redirect('home') 
        return render(request, "stagaire/add_student.html", {})

from django.shortcuts import render, redirect
from pymongo import MongoClient
from bson import ObjectId

def update_student(request, student_id):
    with MongoClient('mongodb://localhost:27017/') as client:
        db = client['db_student']
        collection = db['students']
        student = collection.find_one({'_id': ObjectId(student_id)})
    
    if request.method == 'POST':
        student_roll = request.POST.get('student_roll')
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')
        student_address = request.POST.get('student_address')
        student_phone = request.POST.get('student_phone')
        

        with MongoClient('mongodb://localhost:27017/') as client:
            db = client['db_student']
            collection = db['students']

            result = collection.update_one(
                {'_id': ObjectId(student_id)},
                {'$set': {
                    'roll': student_roll,
                    'name': student_name,
                    'email': student_email,
                    'address': student_address,
                    'phone': student_phone
                }}
            )
            
            if result.modified_count == 1:
                return redirect('home') 

    return render(request, 'stagaire/update_student.html', {'student': student, 'student_id': student_id})
