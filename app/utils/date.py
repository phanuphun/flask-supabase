from datetime import datetime, timedelta, timezone

def jwt_exp(remember:bool):
    if remember == True :
        exp_duration = timedelta(days=99)  
    else :
        exp_duration = timedelta(hours=8)
    
    # Calculate expiration time using timezone-aware UTC datetime
    exp_time = datetime.now(timezone.utc) + exp_duration
    exp_timestamp = int(exp_time.timestamp())  # Convert to UNIX Timestamp
    return exp_timestamp

def check_exp_date(exp):
    try:
        exp_date = datetime.fromtimestamp(exp, tz=timezone.utc) # Convert Unix Timestamp to datetime
        readable_date = exp_date.strftime('%Y-%m-%d %H:%M:%S UTC') # Convert datetime to string  
        now = datetime.now(timezone.utc)  # Compare 
        
        if exp_date < now:
            return {"expired": True, "expires_at": readable_date}
        else:
            return {"expired": False, "expires_at": readable_date}
    except Exception as e:
        return {"error": str(e)}