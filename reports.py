#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
import os

def generate_report(filename, title, data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    document = [report_title, empty_line]
    for entry in data:
        entry_line1 = Paragraph('name: '+entry['name'], styles['BodyText'])
        entry_line2 = Paragraph('weight: '+entry['weight'], styles['BodyText'])
        document.append(entry_line1)
        document.append(entry_line2)
        document.append(empty_line)
    report.build(document)

def gather_data(files):
    data = []
    for file in files:
        entry = {}
        with open(file) as f:
            entry['name'] = f.readline().replace('\n','')
            entry['weight'] = f.readline().replace('\n','')
        data.append(entry)
    return data

if __name__ == "__main__":
    files = os.listdir('supplier-data/descriptions/')
    files = ['supplier-data/descriptions/'+fname for fname in files]
    data = gather_data(files)
    today = date.today()
    title = "Processed Update on {}".format(today)
    generate_report('/tmp/processed.pdf', title, data)
