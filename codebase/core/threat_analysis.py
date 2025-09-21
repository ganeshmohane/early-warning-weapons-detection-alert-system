from core import send_alert as sa

def detect_threat_level(frame, weapon, accuracy):
    print('data received in threat_analysis:', weapon, accuracy)
    '''In future use accuracy to prevent False Reports set threshold'''

    if weapon in ['bazooka', 'grenade_launcher', 'explosives']:
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Critical Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['rifle', 'sniper']:
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'High Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['handgun', 'shotgun', 'smg']:
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Medium Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['knife', 'sword']:
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Low Threat'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon in ['metal_rod', 'broken_bottle']:
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Improvised Weapon'
        }
        sa.send_alert(frame, data['threat_level'], weapon)
        return data
    elif weapon == 'no_weapon':
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