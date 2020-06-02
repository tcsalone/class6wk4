#!/usr/bin/env python3

import os
import datetime
import sys
import emails
import reports

print("Running Script")


def main(argv):

  #styles = getSampleStyleSheet()
  #report = SimpleDocTemplate("/tmp/cars.pdf")
  #report_title = Paragraph("Sales summary for last month", styles["h1"])
  #table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
  #report_summary = Paragraph("<br/>".join(summary), styles["Normal"])
  #report_table = Table(data=cars_dict_to_table(data), style=table_style)
  #report.build([report_title, report_summary, report_table])

  date = datetime.datetime.now()
  date2 = "Processed Update on " + date.strftime("%B %d, %Y")
  print(date2)
  srcDir = "/home/student-04-926dcec39a73/supplier-data/descriptions/"
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
          #print(temp)
          for key, value in temp.items():
              print("value: ", value)
              print("key: ", key)
              table_data.append((key, value))
              if(key == "weight"):
                  table_data.append([])
  #print("Table Data: ", table_data)
  reports.generate_report("/tmp/processed.pdf", date2, table_data)


  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student-04-926dcec39a73@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body) 
  emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
