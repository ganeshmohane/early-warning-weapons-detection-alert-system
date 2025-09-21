from core import send_alert as sa

def detect_threat_level(frame, weapon, accuracy):
    print('data received in threat_analysis:', weapon, accuracy)
    '''In future use accuracy to prevent False Reports set threshold'''

    if weapon in ['Bazooka', 'Grenade Launcher', 'Explosives']:
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Critical Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['Automatic Rifle', 'Sniper']:
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'High Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['Handgun', 'Shotgun', 'SMG']:
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Medium Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['Knife', 'Sword']:
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Low Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon == 'improvised_weapon':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Improvised Weapon'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon == 'No_Weapon':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Safe - No Threat'
        }
        return data
    else :
        data = {
            'image': None,
            'weapon': None,
            'accuracy': None,
            'threat_level': 'Unknown as parameters passed are wrong/insufficeint'
        }
        return data