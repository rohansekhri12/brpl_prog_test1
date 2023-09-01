from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from pymongo import MongoClient
import os , random ,string
from datetime import datetime
from bson import ObjectId  # Import the ObjectId type from pymongo
# Create your views here.
client = MongoClient("mongodb://localhost:27017/")
db = client["WebSite"]
def homepage_view(request):   
    if request.method == 'POST':
        # Access uploaded file
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            # ... process the uploaded file ...
            # Determine the path to the desktop directory
            desktop_path = os.path.join(os.path.expanduser("~"), 'Downloads')


            # Define the destination path for the uploaded file
            destination_path = os.path.join(desktop_path, uploaded_file.name)

            # Save the uploaded file to the desktop
            with open(destination_path, 'wb') as destination_file:
                for chunk in uploaded_file.chunks():
                    destination_file.write(chunk)

        # Access form data
        
        emp_id = request.POST.get('empname')
        print(emp_id)
        circle_id = request.POST.get('circleId')
        division_id = request.POST.get('divisionId')
        ward_no = request.POST.get('wardNo')
        meeting_host = request.POST.get('meetingHost')
        issue_type = request.POST.get('issueType')
        brpl_view = request.POST.get('brplView')
        target_date = request.POST.get('targetDate')
        sub_division = request.POST.get('subDivision')
        issue_raised_by = request.POST.get('issueRaisedBy')
        counselor = request.POST.get('counselor')
        meeting_date = request.POST.get('meetingDate')
        meeting_attendees = request.POST.get('meetingAttendees')
        description = request.POST.get('description')
        action_plan = request.POST.get('actionplan')
        attachment = request.FILES.get('attachment', '')  # Get the attached file
        collection_nam=db['WebPage']
        #------------------------------------------ unique id generation!!
        current_date = datetime.now().strftime("%d/%m/%y")
        for_current_date=current_date.split('/')
        date_reeltime=""
        for i in for_current_date:
            date_reeltime+=i
        str1=str(division_id)
        ftr=""
        for i in range(0,3):
            ftr+=str1[i]
        print(ftr)
        letters_and_digits=string.ascii_letters +string.digits
        uni_id = ftr+date_reeltime+''.join(random.choice(letters_and_digits) for _ in range(3))
        print("unique id ---------->",uni_id)
        collection_nam=db['WebPage']
        






     #----------------------------------------
        
        data = {
            'ticket_id':uni_id,
            'empId': emp_id ,
                'circleid': circle_id , 
                'divisionId' :division_id ,
                'wardno': ward_no ,
                'meetinghost': meeting_host ,
                'issuetype':issue_type ,
                'brplview': brpl_view ,
                'targetdate':target_date ,
                'subdivision':sub_division ,
                'issueraisedby':issue_raised_by ,
                'counselor':counselor ,
                'meetingdate': meeting_date ,
                'meetingattendee':meeting_attendees ,
                'description':description ,
                'action':action_plan,
        }
        collection_nam.insert_one(data)

        client.close()

        return HttpResponse(f'''YOUR REQUEST IS SUBMITTED WITH 
                            TICKET_ID:{uni_id}''')
    return render(request, 'home.html')


users_collection = db["login"]
collection = db["circle"]
issue_raised_collection=db["ISSUES_RAISED_BY"]
issue_type_collection=db["ISSUE_TYPE"]
# Check if the user exists and verify the password



def login(request):

    if request.method == 'POST':
        global username
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("----------------",username)
        # print("Entered_password",password)
        # print(request)

            # Connect to MongoDB
        user = users_collection.find_one({"username": username})
        issues_raised=issue_raised_collection.find({}, {"ISSUE_RAISED_NAME": 1, "ISSUE_RAISED_ID": 1})
        issues_type=issue_type_collection.find({},{"ISSUE_ID":1 ,"ISSUE_NAME":1})
        # print(issues_raised)
        data = collection.find({},{"CIRCLENAME":1,"CIRCLEID":1})

       

      #  if user and check_password(password, user['password']):
        if user['password']==password:    
            return render(request, '2nd_page.html',{'data':data ,'username':username,'issues_raised':issues_raised ,'issues_type':issues_type})
            
        else:
            return HttpResponse('failure.html')
    return render(request, 'test.html')












def get_data(request):
    if request.method == 'GET':
        emp_id = request.GET.get('emp_id')
        website_collection = db['WebPage']
        user_data_list = list(website_collection.find({"empId": emp_id}))

        # Convert ObjectId to string and exclude _id field for each entry
        formatted_data_list = []
        for user_data in user_data_list:
            user_data['_id'] = str(user_data['_id'])
            del user_data['_id']
            formatted_data_list.append(user_data)

        return JsonResponse(formatted_data_list, safe=False)
    return JsonResponse({}, safe=False)


def test_3_page(request):
     # Connect to MongoDB
        user = users_collection.find_one({"username": username})
        issues_raised=issue_raised_collection.find({}, {"ISSUE_RAISED_NAME": 1, "ISSUE_RAISED_ID": 1})
        issues_type=issue_type_collection.find({},{"ISSUE_ID":1 ,"ISSUE_NAME":1})
        # print(issues_raised)
        data = collection.find({},{"CIRCLENAME":1,"CIRCLEID":1})
        return render(request, 'test_3.html',{'data':data ,'username':username,'issues_raised':issues_raised ,'issues_type':issues_type})


def get_divisions(request):
    circle_id = request.GET.get('circle_id')
    # print("THIS IS CIRCLE ID:",type(circle_id))
    # Fetch division data
    division_collection = db["division"]
    
    query = {"CIRCLEID": int(circle_id)}
    # print(query)
    divisions = list(division_collection.find(query,{"_id": 0, "DIVISIONNAME": 1}))
    
    # print("DATA FROM THE DATABASE:",divisions)

    return JsonResponse(divisions, safe=False)
def get_subdivisions(request):
    division_name = request.GET.get('division_name')
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["WebSite"]  # Replace 'your_database_name' with 'WebSite'
    
    # Fetch the CIRCLEID for the selected division
    division_collection = db["division"]
    circle_id_query = {"DIVISIONNAME": division_name}
    division = division_collection.find_one(circle_id_query, {"CIRCLEID": 1})
    
    # Check if the division and CIRCLEID are found
    if division and "CIRCLEID" in division:
        circle_id = division["CIRCLEID"]
        
        # Execute the MongoDB query based on CIRCLEID
        if circle_id == 1:
            query_result = db.division.aggregate([
                {
                    "$match": {
                        "DIVISIONNAME": division_name
                    }
                },
                {
                    "$lookup": {
                        "from": "subdivision",
                        "localField": "DIVISIONCODE",
                        "foreignField": "DIVISION",
                        "as": "subdivisions"
                    }
                },
                {
                    "$unwind": "$subdivisions"
                },
                {
                    "$project": {
                        "_id": 0,
                        "DIVISIONNAME": 1,
                        "SUB_DIVISION_DESC": "$subdivisions.SUB_DIVISION_DESC"
                    }
                }
            ])
        elif circle_id == 2:
            query_result = db.division.aggregate([
                {
                    "$match": {
                        "DIVISIONNAME": division_name
                    }
                },
                {
                    "$lookup": {
                        "from": "subdivision",
                        "localField": "DIVISIONCODE",
                        "foreignField": "DIVISION",
                        "as": "subdivisions"
                    }
                },
                {
                    "$unwind": "$subdivisions"
                },
                {
                    "$project": {
                        "_id": 0,
                        "DIVISIONNAME": 1,
                        "SUB_DIVISION_DESC": "$subdivisions.DIVISION_DESC"  # Use DIVISION_DESC for CIRCLEID 2
                    }
                }
            ])
        
        # Extract Subdivision descriptions from the query result
        subdivisions = [{'SUB_DIVISION_DESC': item['SUB_DIVISION_DESC']} for item in query_result]
        
        client.close()
        
        return JsonResponse(subdivisions, safe=False)
    else:
        client.close()
        return JsonResponse({'error': 'Division or CIRCLEID not found'}, status=400)

# def test_3_view(request):
#     # Your view logic here
#     return render(request, 'test_3.html') 
    