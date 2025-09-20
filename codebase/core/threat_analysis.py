from core import send_alert as sa

def detect_threat_level(frame, weapon, accuracy):
    # print('data received', frame, weapon, accuracy)

    if weapon == 'gun':
        print('inside')
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Critical/High Threat Level'
        }
        sa.alert_police(image, location, threat_level)
        return data
    elif weapon == 'knife':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Mild Threat Level'
        }
        sa.alert_police(image, location, threat_level)
        return data
    elif weapon == 'improvised_weapon':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Mild Threat Level'
        }
        sa.alert_police(image, location, threat_level)
        return data
    elif weapon == 'no_weapon':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'No Threat'
        }
        return data
    else :
        return {'Error':"Unkown Weapon & Threat Level"}