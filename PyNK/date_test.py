from datetime import datetime

now = datetime.utcnow()
print(now.strftime("%a, %d %b %Y %H:%M:%S GMT"))