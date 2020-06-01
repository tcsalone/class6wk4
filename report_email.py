#!/usr/bin/env python3

import os
import datetime
import sys
import emails
#import reports

print("hello world, call the report py script here")


#define a main method, call the generate_email and send email under the Main


def main(argv):

  #styles = getSampleStyleSheet()
  #report = SimpleDocTemplate("/tmp/cars.pdf")
  #report_title = Paragraph("Sales summary for last month", styles["h1"])
  #table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
  #report_summary = Paragraph("<br/>".join(summary), styles["Normal"])
  #report_table = Table(data=cars_dict_to_table(data), style=table_style)
  #report.build([report_title, report_summary, report_table])

  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "student-01-3376cba60dbf@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, body) 
  emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
