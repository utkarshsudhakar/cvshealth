import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromemail="noreply-ain@cvshealth.com"
password="CVS53438@"
toemail="sudhakar.utkarsh9@gmail.com"
component = {"activeMQ","bladeBatch","devices","stores","patients","cmhub","tools","sales","deliveries","inv-messages","rx-connect","compliance","messagehub","messages","redeploy","bsl","orders","customers","scripts","items","notifications"}


msg = MIMEMultipart()
msg['From'] = fromemail
msg['To'] = toemail
msg['Subject'] = "Alert!!"

template="Status is DOWN for Following components: \n"

list =""


def sendmail(list):

  s = smtplib.SMTP(host='cvsmail.cvs.com', port=587)

  s.starttls()

  s.login(fromemail, password)

  body=template+list

  msg.attach(MIMEText(body, 'plain'))

  text= msg.as_string()

  s.sendmail(fromemail,toemail,text)


elastic ='{ "_index" : "store_healthstatus-2018-10-04", "_type" : "healthlog", "_id" : "76ncPGYB05j4jx-0BfLA", "_score" : 1.0, "_source" : { "store_stat" : "DOWN", "@timestamp" : "2018-10-04T02:15:44.269Z", "store_num" : "68932", "@version" : "1", "host" : "192.168.200.11", "type" : "healthlog", "store_msg" : { "code" : 200, "storeInfo" : { "activeMQ" : { "component" : "activeMQ", "serverStatus" : { "status" : "DOWN" } }, "bladeBatch" : { "component" : "bladeBatch", "serverStatus" : { "status" : "DOWN" } }, "devices" : { "component" : "devices", "serverStatus" : { "status" : "DOWN" } }, "stores" : { "component" : "stores", "serverStatus" : { "status" : "DOWN" } }, "patients" : { "component" : "patients", "serverStatus" : { "status" : "DOWN" } }, "cmhub" : { "component" : "cmhub", "serverStatus" : { "status" : "DOWN" } }, "tools" : { "component" : "tools", "serverStatus" : { "status" : "DOWN" } }, "sales" : { "component" : "sales", "serverStatus" : { "status" : "DOWN" } }, "deliveries" : { "component" : "deliveries", "serverStatus" : { "status" : "DOWN" } }, "inv-messages" : { "component" : "inv-messages", "serverStatus" : { "status" : "DOWN" } }, "rx-connect" : { "component" : "rx-connect", "serverStatus" : { "status" : "DOWN" } }, "compliance" : { "component" : "compliance", "serverStatus" : { "status" : "DOWN" } }, "messagehub" : { "component" : "messagehub", "serverStatus" : { "status" : "DOWN" } }, "messages" : { "component" : "messages", "serverStatus" : { "status" : "DOWN" } }, "redeploy" : { "component" : "redeploy", "serverStatus" : { "status" : "DOWN" } }, "bsl" : { "component" : "bsl", "serverStatus" : { "status" : "DOWN" } }, "orders" : { "component" : "orders", "serverStatus" : { "status" : "DOWN" } }, "customers" : { "component" : "customers", "serverStatus" : { "status" : "DOWN" } }, "scripts" : { "component" : "scripts", "serverStatus" : { "status" : "DOWN" } }, "items" : { "component" : "items", "serverStatus" : { "status" : "DOWN" } }, "notifications" : { "component" : "notifications", "serverStatus" : { "status" : "DOWN" } } }, "status" : "DOWN" } } }  '

json_data = json.loads(elastic)


for i in component:

  status=json_data["_source"]["store_msg"]["storeInfo"][i]["serverStatus"]["status"]
  print i ,": ",status

  if status=="DOWN":
    list+=i+"\n"

if list!="":
  sendmail(list)


