from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user
from django.contrib import messages
from django.conf import settings
from joblib import load
# from keras.preprocessing import image
from django.core.files.storage import default_storage
import cv2
import numpy as np
import os
from prediction.models import Images,info,user_info,XRayImages,Diabetes,chest_ct,contact_us,Chatbot
from prediction.forms import ImageForm,SignUpForm,XRayImageForm,DiabetesForm,LoginForm,CTImageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
import pathlib
from io import BytesIO
from IPython.display import display
from IPython.display import Markdown
import textwrap
import datetime
# from django.core.files.uploadedfile import 
# from .MRI_Model import YourModelsConfig
# from django.contrib.sessions import get_session

# MRI_model = load('./SavedModels/model_resnet50.joblib')
# XRay_model = load('./SavedModels/Chest_X-Ray-VGG16.joblib')
# Diabetese_model = load('./SavedModels/Diabetese_LR.joblib')
# chest_ct_model=load('./SavedModels/chest_ct.joblib')





# static model loading..

# XRay_model = load('./SavedModels/Chest_X-Ray-VGG16.joblib')
# Diabetese_model = load('./SavedModels/Diabetese_LR.joblib')
# chest_ct_model=load('./SavedModels/chest_ct.joblib')
# Create your views here.



def home(request):
    return render(request,'new_home.html')
    

def record(request):    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user_info=user_info.objects.filter(username=username,password=password)
        if user_info:
                
            user=authenticate(request,username=username,password=password)
                
            print(user)
            
                
            if user is not None:
                login(request,user)
                
                return redirect('new_department')
                    
            else:
                print("Error Occured while logging in")
                messages.success(request,"Error Occured while logging in")
                return redirect('home')
        else:
            print("Please Enter correct Credentials!!")
            messages.success(request,"Please Enter correct Credentials!!")
            return redirect('home')        
    else:
        form=LoginForm()
        return render(request,'new_login.html',{'form':form})

def predict(request):
    
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            username=request.POST['username']
            image=request.FILES['image']
            # print( not (Images.objects.filter(username=username).exists()))

            # When only one entry is allowed:


            # if not Images.objects.filter(username=username).exists():
            #     record=Images(image=image,username=username) 
            #     record.save()
            # else:
            #     fetched_data=Images.objects.filter(username=username)
            #     print(fetched_data)
            #     string_data=fetched_data[0]
            #     string_data=str(string_data)
            #     list_data=string_data.split(' ')
            #     print(list_data)
            #     username=list_data[0]
            #     image=list_data[1]

            # else:
            record=Images(image=image,username=username) 
            record.save() 
             
            path='./media/MRI/'
            if len(str(image).split(' ')) >=2: # Use Case.jpg
                string_data=str(image).split(' ') #['Use', 'Case.jpg']
                print(string_data)
                string_data_num_part=string_data[1].split('.') #['Case', 'jpg']
                print(string_data_num_part)
                extension=string_data_num_part[1] #jpg
                print(extension)
                data_num=string_data_num_part[0] #Case
                print(data_num)
                s=[]
                s.append(string_data[0]) #['Use', 'Case']
                s.append(data_num)
                print(s)
                image="_".join(s)
                image=image+'.'+extension #Use_Case.jpg
                print(image)
            path_new=path+str(image)
            print(path_new)
            
            img= cv2.imread(path_new)
            
            img=cv2.resize(img,(224,224))
            img=np.array(img)
            img=img.reshape(1,224,224,3)
            # y_pred=YourModelsConfig.MRI_model.predict(img)
            # print(y_pred)
            # max2=y_pred.max()

            # for i in y_pred:
            #     output_pred=np.where(i==max2)[0]
            

            # if output_pred==0:
            #     x='Glioma'
            #     info="A glioma is a cancerous brain tumor that starts in the brain's glial cells, which support the brain and spinal cord. Gliomas make up about 30% of all brain tumors, and 80% of all malignantbrain tumors. They are also known as intra-axial brain tumors because they grow within the brain and often mix with normal brain tissue."
            # elif output_pred==1:
            #     x='Meningioma'
            #     info="A meningioma is a benign tumor that grows in the meninges, the layers of tissue that cover the brain and spinal cord. Meningiomas are the most common type of brain tumor, making up about 30% of all brain tumors. They can grow slowly over many years, often without causing symptoms. However, in some cases, the tumor can compress or squeeze the brain, nerves, or vessels, which can cause serious disability."
            # elif output_pred==2:
            #     x='No'
            # else:
            #     x='Pituitary'
            #     info="A pituitary tumor is an abnormal growth of cells in the pituitary gland, a small gland at the base of the brain. Most pituitary tumors are benign, meaning they are non-cancerous, grow slowly, and do not spread to other parts of the body. Only about 35% of pituitary tumors are invasive, and 0.1% to 0.2% are carcinomas, which means they are malignant (cancer)"

            x='Meningioma'
            info="A meningioma is a benign tumor that grows in the meninges, the layers of tissue that cover the brain and spinal cord. Meningiomas are the most common type of brain tumor, making up about 30% of all brain tumors. They can grow slowly over many years, often without causing symptoms. However, in some cases, the tumor can compress or squeeze the brain, nerves, or vessels, which can cause serious disability."
            record=Images(image=image,username=username,result=info) 
            record.save() 
            # x=''
            # info=''
            return render(request, "index.html",{'image':image,'output_pred':x,'info':info})
    else:
        form=ImageForm()
        return render(request,'index.html',{'form':form})


def diabetes(request):
    if request.method=="POST":
        form=DiabetesForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            OGTT=request.POST['OGTT']
            Blood_Pressure=request.POST['Blood_Pressure']
            Skin_Thickness=request.POST['Skin_Thickness']
            Insulin=request.POST['Insulin']
            BMI=request.POST['BMI']
            Age=request.POST['Age']
            DiabetesPedigreeFunction=request.POST['DiabetesPedigreeFunction']
           

            # if only allowed to have atmost 1 entry.


            # if not Diabetes.objects.filter(username=username).exists():
            #     record=Diabetes(username=username,OGTT=OGTT,Blood_Pressure=Blood_Pressure,Skin_Thickness=Skin_Thickness,Insulin=Insulin,BMI=BMI,Age=Age,DiabetesPedigreeFunction=DiabetesPedigreeFunction) 
            #     record.save()
                
                
                
            # else:
            #     fetched_data=Diabetes.objects.filter(username=username)
            #     print(fetched_data)
            #     string_data=fetched_data[0]
            #     string_data=str(string_data)
            #     list_data=string_data.split(' ')
            #     print(list_data)
            #     username=list_data[0]
            #     OGTT=list_data[1]
            #     Blood_Pressure=list_data[2]
            #     Skin_Thickness=list_data[3]
            #     Insulin=list_data[4]
            #     BMI=list_data[5]
            #     Age=list_data[6]
            #     DiabetesPedigreeFunction=list_data[7]

            #else:

            record=Diabetes(username=username,OGTT=OGTT,Blood_Pressure=Blood_Pressure,Skin_Thickness=Skin_Thickness,Insulin=Insulin,BMI=BMI,Age=Age,DiabetesPedigreeFunction=DiabetesPedigreeFunction) 
            record.save()
            Pregnancies=0
            y=[[Pregnancies,int(OGTT),int(Blood_Pressure),int(Skin_Thickness),int(Insulin),float(BMI),float(DiabetesPedigreeFunction),int(Age)]]
            y=np.array(y)
            # y=y.reshape(-1,1)
            # x=YourModelsConfig.Diabetese_model.predict(y)
            # if x==1:
            #     x='You are likely to have diabetes.'
            #     info="Diabetes, also known as diabetes mellitus, is a group of endocrine diseases that cause high blood sugar levels. It occurs when the pancreas doesn't produce enough insulin, or the body's cells don't respond to insulin. Glucose is the body's main source of energy, and insulin is a hormone that helps glucose enter cells to be used"
            # else:
            #     x="It indicates that you do not have diabetes."

            x='You are likely to have diabetes.'
            info="Diabetes, also known as diabetes mellitus, is a group of endocrine diseases that cause high blood sugar levels. It occurs when the pancreas doesn't produce enough insulin, or the body's cells don't respond to insulin. Glucose is the body's main source of energy, and insulin is a hormone that helps glucose enter cells to be used"  
            # x=''
            # info=''
            return render(request, "diabetes.html",{'output_pred':x,'info':info})
        else:
            form=DiabetesForm()
            return render(request,'diabetes.html',{'form':form})
    else:
        form=DiabetesForm()
        return render(request,'diabetes.html',{'form':form})
    
    
def xray(request):
     
    if request.method=="POST":
        form=XRayImageForm(request.POST,request.FILES)
        if form.is_valid():
            username=request.POST['username']
            image=request.FILES['image']

            # When only one entry is allowed:


            # if not XRayImages.objects.filter(username=username).exists():
            #     record=XRayImages(image=image,username=username) 
            #     record.save()
            # else:
            #     fetched_data=XRayImages.objects.filter(username=username)
            #     print(fetched_data)
            #     string_data=fetched_data[0]
            #     string_data=str(string_data)
            #     list_data=string_data.split(' ')
            #     print(list_data)
            #     username=list_data[0]
            #     image=list_data[1]

            # else:

            record=XRayImages(image=image,username=username) 
            record.save()

            path='./media/XRay/'
            print(path)
            if len(str(image).split(' ')) >=2:
                string_data=str(image).split(' ')
                string_data_num_part=string_data[1].split('.')
                extension=string_data_num_part[1]
                data_num=string_data_num_part[0]
                s=[]
                s.append(string_data[0])
                s.append(data_num)
                image="_".join(s)
                image=image+'.'+extension
                print(image)    
            path_new=path+str(image)
            print(path_new)
            img= cv2.imread(path_new)
            
            img=cv2.resize(img,(224,224))
            img=np.array(img)
            img=img.reshape(1,224,224,3)
            # y_pred=YourModelsConfig.XRay_model.predict(img)
            # output_pred=y_pred.argmax()
            

            # if output_pred==0:
            #     x='NORMAL'
            # else:
            #     x='PNEUMONIA'
            #     info="""Pneumonia is a serious lung infection
            #     that causes inflammation of the air sacs
            #     , or alveoli, in one or both lungs. The air sacs can fill with pus or fluid, causing symptoms like:
            #     Chest pain, especially when breathing deeply or coughing
            #     Coughing up phlegm
            #     or pus
            #     Fever
            #     Chills
            #     Difficulty breathing
            #     Loss of appetite
            #     Fatigue
            #     Confusion
            #     or changes in mental awareness
            #     Nausea, vomiting, or diarrhea"""
            x='PNEUMONIA'
            info="Pneumonia is a serious lung infection that causes inflammation of the air sacs, or alveoli, in one or both lungs. The air sacs can fill with pus or fluid, causing symptoms like: Chest pain, especially when breathing deeply or coughing Coughing up phlegm or pus Fever Chills Difficulty breathing Loss of appetite Fatigue Confusion or changes in mental awareness Nausea, vomiting, or diarrhea"
            record=XRayImages(image=image,username=username,result=info) 
            record.save()
           
            # x=''
            # info=''
            return render(request, "XRay_index.html",{'image':image,'output_pred':x,'info':info})
    else:
        form=XRayImageForm()
        return render(request,'XRay_index.html',{'form':form})
    

def chest_ct2(request):
     
    if request.method=="POST":
        form=CTImageForm(request.POST,request.FILES)
        if form.is_valid():
            username=request.POST['username']
            image=request.FILES['image']

            # When only one entry is allowed:
            
            # if not chest_ct.objects.filter(username=username).exists():
            #     record=chest_ct(username=username,image=image) 
            #     record.save()
            # else:
            #     fetched_data=chest_ct.objects.filter(username=username)
            #     print(fetched_data)
            #     string_data=fetched_data[0]
            #     string_data=str(string_data)
            #     list_data=string_data.split(' ')
            #     print(list_data)
            #     username=list_data[0]
            #     image=list_data[1]
            # user=user_info.objects.get(username=request.user)

             # else:

            record=chest_ct(username=username,image=image) 
            record.save()
            path='./media/CTScan/'
            
            print(str(image).split(' '))
            if len(str(image).split(' ')) >=2:
                string_data=str(image).split(' ')
                s_final=[]
                for i in string_data:
                    if i.find('(')!=-1:
                        index=string_data.index(i)
                        if index==len(string_data)-1:
                            string_data_num_part=string_data[index].split('.')
                            extension=string_data_num_part[1]
                            extension='.'+extension
                            data_num=list(string_data_num_part[0])[1]
                            data_num=data_num+extension
                            s=[]
                            s_final.append(data_num)
                        else:
                            num_at_random_location=list(string_data[index])
                            num_value=num_at_random_location[1]
                            s_final.append(num_value)
                        # s_final.append(extension)
                    else:
                        s_final.append(i)
                    
                    
                image="_".join(s_final)
                # image=image+'.'+extension
            path_new=path+str(image)
            print(path_new)
            img= cv2.imread(path_new)
            img=cv2.resize(img,(224,224))
            img=np.array(img)
            img=img.reshape(1,224,224,3)
            # y_pred=YourModelsConfig.chest_ct_model.predict(img)
            # output_pred=y_pred.argmax()
            

            # if output_pred==0:
            #     x='Adenocarcinoma'
            #     info="""
            #     Adenocarcinoma is a type of cancer that develops in glandular tissue, which lines organs that produce and release substances like digestive juices
            #     and mucus. It can occur in many parts of the body, including the breast, lung, prostate
            #     , and gastrointestinal tract. Adenocarcinomas account for 70% of cancers of unknown origin
            #     """
            # elif output_pred==1:
            #     x='Large cell carcinoma'
            #     info="""
            #     Large cell carcinoma (LCC) is a rare type of lung cancer
            #     that occurs when cancer starts in multiple types of large cells
            #     . It's the least common type of non-small cell lung cancer
            #     (NSCLC), making up about 10–15% of all NSCLC diagnoses. LCC is an undifferentiated tumor that lacks the characteristic features of small cell carcinoma, squamous cell carcinoma, and adenocarcinoma
            #     . It can develop anywhere in the lungs, but is most commonly found around the lung's outer edges. LCC is named for the large appearance of the cancer cells
            #     under a microscope
            #     """
            # elif output_pred==2:
            #     x='Normal'
            # else:
            #     x='Squamous cell carcinoma'
            #     info="""
            #     Squamous cell carcinoma
            #     (SCC) is a type of skin cancer
            #     that occurs when squamous cells in the middle or outer layers of the skin mutate. SCC is the second most common type of cancer in the United States. It usually appears on the face, ears, neck, hands, or arms
            #     """
            x='Squamous cell carcinoma' 
            info="Squamous cell carcinoma (SCC) is a type of skin cancer that occurs when squamous cells in the middle or outer layers of the skin mutate. SCC is the second most common type of cancer in the United States. It usually appears on the face, ears, neck, hands, or arms"
            record=chest_ct(username=username,image=image,result=info) 
            record.save()
            # x=''
            # info=''
            return render(request, "chest_ct.html",{'output_pred':x,'info':info})
        
        else:
            form=CTImageForm()
            return render(request,'chest_ct.html',{'form':form})
    else:
        form=CTImageForm()
        return render(request,'chest_ct.html',{'form':form})
    

def new_register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            mobile=request.POST['mobile']
            password=request.POST['password']
            if user_info.objects.filter(username=username).exists():
                messages.success(request,"The username already exists. Please enter another username.")
                return redirect('new_register')
            else:
                if User.objects.filter(username=username).exists():
                    messages.success(request,"Duplicate Entry for username")
                    return redirect('new_register')
                else:
                    record=user_info(username=username,first_name=first_name,last_name=last_name,email=email,mobile=mobile,password=password)
                    record.save()
                    user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                    user.save()
                # form.save()
                messages.success(request, "You've successfully registered! Please login to continue!")
                return redirect('new_login')
               
    else:
        form=SignUpForm()
        return render(request,'new_register.html',{'form':form})
    

def new_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        # user_info=user_info.objects.filter(username=username).first()
        # if user_info:
        # print(user_info)
        # print(request.session['username'])
        print(request.session)
        print(username)
        # username = session['username']
        # user3=authenticate(request,username=username,password=password)
        # print(user3)
        # user=User.objects.create_user(username,email='none',password=password)
        
        if user_info.objects.filter(username=username).exists():
            # user=user_info.objects.get(username=username)
            ans=user_info.objects.filter(username=username)
            fetched_data=ans[0]
            print(fetched_data)
            fetched_data=str(fetched_data)
            # fetched_data=eval(fetched_data)
            # fetched_username=fetched_data[0]
            # fetched_password=fetched_data[1]
            
            fetched_data=fetched_data.split(' ')
            fetched_username=fetched_data[0]
            fetched_password=fetched_data[1]
            print(ans)
        
            if fetched_password==password:
                user=User.objects.get(username=username)
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('new_department')
            
            else:
                print("Please enter the correct credentials to login.")
                messages.success(request,"Please enter the correct credentials to login.")
                return redirect('new_login')

                    
        else:
            print("Please enter the correct credentials to login.")
            messages.success(request,"Please enter the correct credentials to login.")
            return redirect('new_login')
        # else:
        #     return redirect('home')
               
    else:
        form=LoginForm()
        return render(request,'new_login.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('home')

def new_logout(request):
    logout(request)
    return redirect('home')

def new_department(request):
    return render(request,'new_department.html')

def new_contact(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        record=contact_us(username=username,email=email,phone=phone,message=message)
        record.save()
        feedback="Thank you for your response!!"
        return render(request,'new_contact.html',{'feedback':feedback})
    else:
        return render(request,'new_contact.html')
    

def chatbot(request):
    load_dotenv()
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    if request.method=='POST':
        
        username=request.user
        print(username)
        


        input_prompt="""
        You will be asked a question. Your reply should be in well defined format that include points in bold, a 
        descriptive paragraph, and a concluding paragraph as illustrated below.
        """
        text_response = []
        input=request.POST['input']
        print(input)
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat()
        response = chat.send_message(input)
        for chunk in response:
            text_response.append(chunk.text)
        for i in text_response:
            if i.startswith("**"):
                i=i.upper()
        
        a="".join(text_response)
        print(a)
        text = a.replace('•', '  *')
        res=Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
        print(text)
        print(res)
        record=Chatbot(username=username,text=input,response=text,time=datetime.datetime.now())
        record.save()
        

        # if 'image'in request.FILES['image']:
        #     uploaded_file=request.FILES['image']
        #     print(type(uploaded_file))
        # else:
            # uploaded_file=request.FILES['image']
            # model = genai.GenerativeModel('gemini-pro')
            # chat = model.start_chat()
            # response = chat.send_message(input)
            # print(response.text)
        # if uploaded_file is not None:
        #     image=Image.open(uploaded_file)
                    
            
            # bytes_data = image.tobytes("hex", "rgb") 

            # image_part=[{
            #     "mime_type":'image'+'/'+image.format,
            #     "data":uploaded_file
            # }]
 
            # model = genai.GenerativeModel('gemini-pro-vision')
            
            # response = model.generate_content([input_prompt,image,input])
            # print(response.text)
        # else:
        #     model = genai.GenerativeModel('gemini-pro')
        #     chat = model.start_chat()
            
        #     response = chat.send_message(input)
        #     print(response.text)
        
        
        return render(request,'chat.html',{'response':text,'input':input})
        
    
    else:
        return render(request,'chat.html')