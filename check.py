from flask import Flask, render_template,session, abort, redirect, request, url_for, send_from_directory,g

import psycopg2

# #establishing the connection for deleting data
conn = psycopg2.connect(
   database="postgres", user='postgres', password='', host='..', port= ''
)
cursor = conn.cursor()
sql = '''SET search_path TO public;'''
cursor.execute('SHOW search_path')
for record in cursor:
    print(record)
conn.commit()
