import sys
sys.path.insert(0, r'C:\Users\mromankiewic\AppData\Local\Programs\Python\Python37\Lib\site-packages')
sys.path.insert(0, r'C:\Users\mromankiewic\AppData\Local\Programs\Python\Python37')
import xlwings as xw
from datetime import date
from dateutil.relativedelta import relativedelta

####Scrape values from excel files

# today = date.today()
# week= "CW"+ str(today.isocalendar()[1])
# monday = date.today() + relativedelta(days=-4)
monday = date.today() + relativedelta(days=-2)
year, week_num, day_of_week = monday.isocalendar()
thisweek = "CW"+ str(week_num)
a = ""

path1 = "C:/Users/mromankiewic/Desktop/wffc" + \
        "2020" + a + str(thisweek) + \
        str(monday.strftime("%Y%m%d")) + a + "Weekly Financial Forecast" + a + str(thisweek) + a

path0 = "C:/Users/mromankiewic/Desktop/wffc" + \
        "2020" + a + str(thisweek) + \
        "2020" + a + "Master Case" + a + str(thisweek) + ".xlsx"

#OPEN WORKBOOKS
wb0 = xw.Book(path0)
wb1 = xw.Book(path1 + "AT" + ".xlsx")
wb2 = xw.Book(path1 + "SE" + ".xlsx")
wb3 = xw.Book(path1 + "UK" + ".xlsx")
wb4 = xw.Book(path1 + "ES" + ".xlsx")
wb5 = xw.Book(path1 + "FR" + ".xlsx")
wb6 = xw.Book(path1 + "IT" + ".xlsx")
wb7 = xw.Book(path1 + "BE" + ".xlsx")
wb8 = xw.Book(path1 + "DE" + ".xlsx")
wb9 = xw.Book(path1 + "PL" + ".xlsx")
wb10 = xw.Book(path1 + "CZ" + ".xlsx")

#COPY sheets
ws1 = wb1.sheets("AT", "CH")
ws1.api.Copy(Before=wb0.sheets("AT", "CH").api)

ws2 = wb2.sheets("SE", "FI", "DK", "NO")
ws2.api.Copy(Before=wb0).sheets("SE", "FI", "DK", "NO")

ws3 = wb3.sheets("UK", "IE")
ws3.api.Copy(Before=wb0).sheets("UK", "IE")

ws4 = wb4.sheets("ES")
ws4.api.Copy(Before=wb0).sheets("ES")

ws5 = wb5.sheets("FR")
ws5.api.Copy(Before=wb0).sheets("FR")

ws6 = wb6.sheets("IT")
ws6.api.Copy(Before=wb0).sheets("IT")

ws7 = wb7.sheets("BE", "NL")
ws7.api.Copy(Before=wb0).sheets("BE", "NL")

ws8 = wb8.sheets("DE")
ws8.api.Copy(Before=wb0).sheets("DE")

ws9 = wb8.sheets("PL")
ws9.api.Copy(Before=wb0).sheets("PL")

ws10 = wb10.sheets("CZ")
ws10.api.Copy(Before=wb0).sheets("CZ")

wb0.save()
wb0.app.quit()