
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np

def predict(request):
    if request.method == 'POST':
        temperature = int(request.POST.get('Temperature'))
        oxygen = int(request.POST.get('Oxygen'))
        humidity = int(request.POST.get('Humidity'))

        input_data = np.array([[temperature, oxygen, humidity]])
        model = pickle.load(open('fire_app/model.pkl', 'rb'))
        prediction = model.predict_proba(input_data)
        output = '{0:.{1}f}'.format(prediction[0][1], 2)

        if float(output) > 0.5:
            return render(request, 'forest_fire.html', {'pred': 'Your Forest is in Danger.', 'output': output})
        else:
            return render(request, 'forest_fire.html', {'pred': 'Your Forest is safe.', 'output': output})
    else:
        return render(request, 'forest_fire.html')
