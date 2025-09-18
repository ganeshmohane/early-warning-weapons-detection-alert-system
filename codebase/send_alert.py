import datetime

time = datetime.time() 

def send_alert(image, location, threat_level):
    return f"Alert Sent to Police Authorities with {image}, location: {location} and threat level is {threat_level} at {time}"