import requests, json

browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

def ListOfState():
    url = f'https://cdn-api.co-vin.in/api/v2/admin/location/states'
    response = requests.get(url, headers=browser_header)
    json_data = response.json()
    final_text = ''
    
    for slots in json_data['states']:
        final_text = final_text + "\nName: "+str(slots['state_name']) +' , '+ "State_Id: "+str(slots['state_id']) +'\n'

    return final_text

def District_List(text):
    var = int(text)
    url = f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{var}'
    response = requests.get(url, headers=browser_header)
    json_data = response.json()
    final_text = ''
    if len(json_data['districts'])==0:
           # no = 
           # no = no + pin + "on" + date
        return 'No districts for the given state'
    else:
        for slots in json_data['districts']:
            final_text = final_text + "\nName: "+str(slots['district_name']) +' , '+ "District_Id: "+str(slots['district_id']) +'\n'
            #final_text = final_text + '----------------------------------------'

    return final_text

def myfuc():
    return "Hey There,\nI can help you to book your Cvoid19 Vaccination slot!\nList of my sevices:\n1.Know The Available slots of covid doses in your distric , For steps to follow Enter help"


def sample(input_text):
    f = 1
    for i in input_text:
        if i==':' :
            f = 0

    if(f):
        s = "Invalid Input"
        s+="If you want to know the vaccination slots for your district then the input format is \n District_code:DD-MM-YR , Eg.432:03-05-2001\n If You want to Know your District Code Just Hit \n help"
        return s
    user_message = str(input_text).lower()
    #print(user_message)
    new_data = user_message.split(':')
    pin = new_data[0]
    date = new_data[1]
    try:
        pin = int(pin)
    except Exception as e:
        pass
    if(int(pin)<10000 and int(pin)>0):

        url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
       
        #print(url)
        response = requests.get(url, headers=browser_header)
        #print(response)
        json_data = response.json()
        final_text = ''
        arr =[]
        brr = []
        brr.append('Slots Not Available for the selected District and date')
        if len(json_data['sessions'])==0:

            return brr
        else:
            for slots in json_data['sessions']:
                final_text = final_text + "\nName: "+str(slots['name']) +'\n'+ "Available Capacity: "+str(slots['available_capacity']) +'\n' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n' + "Vaccine: "+str(slots['vaccine'])+ '\n'
                if(slots['available_capacity']>0):
                    final_text = final_text + '----------------------------------------'
                    arr.append(final_text)
                final_text = ''
        #print(final_text)
        return arr
    else:
        return "Invalid input"
