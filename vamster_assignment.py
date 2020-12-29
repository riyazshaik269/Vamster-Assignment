import json

js_fil= '''
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
'''

js_file = json.loads(js_fil)

overweight_count = 0

for i in range(0,len(js_file)):
    h = (js_file[i]["HeightCm"])/100
    m = (js_file[i]["WeightKg"])
    js_file[i]["BMI"] = round(m/(h)**2,2)
    if js_file[i]["BMI"] <=18.5:
        js_file[i]["BMI CATEGORY"] = "Underweight"
        js_file[i]["Health Risk"] = "Malnutrition risk"
    elif js_file[i]["BMI"] > 18.5 and js_file[i]["BMI"]< 25:
        js_file[i]["BMI CATEGORY"] = "Normal weight"
        js_file[i]["Health Risk"] = "low risk"
    elif js_file[i]["BMI"] > 25 and js_file[i]["BMI"] <30:
        js_file[i]["BMI CATEGORY"] = "overweight"
        js_file[i]["Health Risk"] = "enhanced risk"
        overweight_count +=1
    elif js_file[i]["BMI"] > 30 and js_file[i]["BMI"] <35:
        js_file[i]["BMI CATEGORY"] = "Moderately obese"
        js_file[i]["Health Risk"] = "Medium risk"
    elif js_file[i]["BMI"] > 35 and js_file[i]["BMI"] <40:
        js_file[i]["BMI CATEGORY"] = "severely obese"
        js_file[i]["Health Risk"] = "High risk"
    else:
        js_file[i]["BMI CATEGORY"] = "very severely obese"
        js_file[i]["Health Risk"] = "very high risk"
        
print(js_file)
print("\nOverweight People are : " + str(overweight_count))

