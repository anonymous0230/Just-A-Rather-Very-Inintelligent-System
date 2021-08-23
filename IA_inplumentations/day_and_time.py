from datetime import date, time
from datetime import datetime
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
I_time = (dt_string)	
