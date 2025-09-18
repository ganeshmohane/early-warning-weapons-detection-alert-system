import datetime

time = datetime.time() 

def alert_police(image, location, threat_level):
    return f"Alert Sent to Police Authorities with {image}, location: {location} and threat level is {threat_level} at {time}"

def alert_locals():
    pass

def alert_army():
    pass