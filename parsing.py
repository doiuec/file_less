import os.path
import argparse
import xml.etree.ElementTree as ET
import re

# Windows Command to generate the XML file
# wevtutil query-events "Windows Powershell" /uni:true /f:XML > winps.xml

parser=argparse.ArgumentParser(description='A parser for the Windows Powershell event log XML generated by wevutil command.')
parser.add_argument('xml', help='Path of the XML File')
args=parser.parse_args()
filename=args.xml
if not os.path.isfile(filename):
  print('Not found:%s' % filename)
  exit(1)
ns='{http://schemas.microsoft.com/win/2004/08/events/event}'  #namespace
comment_out = r'^\s*(#.*|)$'
Invoke = r'Invoke-WebEwquest'
f = open(filename, 'r', encoding='utf-16')
xml=f.read()
#print(xml)
xml= "<eventlog>" + xml + "</eventlog>"
root = ET.fromstring(xml)
alert_command = '(Get-Host).UI.RawUI.ForegroundColor = \'red\''
reposit_command = '(Get-Host).UI.RawUI.ForegroundColor = \'white\''
for event in root:
  for e in event:
    for f in e:
      pass
  eventid=event.find(ns + 'System').find(ns + 'EventID').text
  eventrecid=event.find(ns + 'System').find(ns + 'EventRecordID').text
  time=event.find(ns + 'System').find(ns + 'TimeCreated').attrib
  ps=event.find(ns + 'EventData').findall(ns + 'Data')
  if eventid=="800":
    if(ps[0].text):
      split = ps[0].text.splitlines()
      for column in split:
        match_1 = re.search(comment_out, column)
        match_2 = re.search('Invoke-WebRequest', column)
        if not match_1:
          if match_2:
            os.system('powershell -Command' + ' ' + alert_command)
            print(column, end="\n")
            print("Time:    \t%s" % (time,))
            os.system('powershell -Command' + ' ' + reposit_command)
            continue
          print(column, end="\n")
      #print("ID:     \t%s" % (eventrecid,))
      #print("EID:      \t%s" % (eventid,))
      #print("Time:    \t%s" % (time,))
      #print("PS:      \t%s" % (ps[0].text))
      #print((ps[2].text))
      #print("\x1b[31mRed, \x1b[34mBlue\x1b[0m")