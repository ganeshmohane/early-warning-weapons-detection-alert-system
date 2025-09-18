def threat_analysis(frame, weapon, accuracy):
    print('data received', frame, weapon, accuracy)

    if weapon == 'gun':
        print('inside')
        data =  {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Critical/High Threat Level'
        }
        print(type(data), data)
        return data
    elif weapon == 'knife':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Mild Threat Level'
        }
        return data
    elif weapon == 'improvised_weapon':
        data = {
            'image': frame,
            'weapon': weapon,
            'accuracy': accuracy,
            'threat_level': 'Mild Threat Level'
        }
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
        return f"Unkown Weapon & Threat Level"