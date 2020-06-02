#!/usr/bin/env python3

import os
import datetime
import sys
import emails
import reports

print("Running Script")


def main(argv):
  date = datetime.datetime.now()
  date2 = "Processed Update on " + date.strftime("%B %d, %Y")
  print(date2)
  srcDir = "/home/student-01-c4b067d66a1f/supplier-data/descriptions/"
  table_data = []


  for (dirname, dirpath, filename) in os.walk(srcDir):
      for file in filename:
          temp={}
          name = ['name', 'weight']
          with  open(os.path.join(dirname, file), 'r') as opened:
              lines = opened.readlines()
          for i in range(len(name)):
              temp[name[i]]=lines[i].rstrip("\n")

          weight_conv=temp.get("weight")
          temp['weight']=(int(weight_conv.replace('lbs', '')))
          print("temp var:", temp)
          if table_data == "":
              table_data = "<br />".join([str("name: " + temp["name"]), str("weight: " + temp["weight"])]) 
          else:
              table_data = "<br />".join([table_data, str("name: " + table_data["name"]), str("weight: " + table_data["weight"])])
  print("Table Data: ", table_data)
  reports.generate_report("/tmp/processed.pdf", date2, table_data)


  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student-01-c4b067d66a1f@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body) 
  emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
