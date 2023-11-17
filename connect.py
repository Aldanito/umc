import psycopg2
import paramiko
from sshtunnel import SSHTunnelForwarder

mypkey = paramiko.RSAKey.from_private_key_file('pyapp')
pkey='pyapp'
key=paramiko.RSAKey.from_private_key_file(pkey)
tunnel =  SSHTunnelForwarder(
        ( '172.16.1.13', 22),
        ssh_username='',
        ssh_password='.',
        ssh_pkey=pkey,
        remote_bind_address=('localhost', ))

tunnel.start()
conn = psycopg2.connect(dbname='', user='' , password='.', host='', port=tunnel.local_bind_port)
