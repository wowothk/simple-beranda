import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder


# local config
# import os

# from dotenv import load_dotenv
# load_dotenv()


# ssh_host = os.environ.get('SSH_HOST')
# ssh_username = os.environ.get('SSH_USERNAME')
# ssh_password = os.environ.get('SSH_PASSWORD')
# ssh_port = os.environ.get('SSH_PORT')
# database_username = os.environ.get('DB_USERNAME')
# database_password = os.environ.get('DB_PASSWORD')
# database_name = os.environ.get('DB_NAME')
# database_host = os.environ.get('DB_HOST')
# localhost = os.environ['SSH_HOST']

# deploy
import streamlit as st

ssh_host = st.secrets['SSH_HOST']
ssh_username = st.secrets['SSH_USERNAME']
ssh_password =st.secrets['SSH_PASSWORD']
ssh_port = st.secrets['SSH_PORT']
database_username = st.secrets['DB_USERNAME']
database_password = st.secrets['DB_PASSWORD']
database_name = st.secrets['DB_NAME']
database_host = st.secrets['DB_HOST']


def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, int(ssh_port)),
        ssh_username = ssh_username,
        ssh_password = ssh_password,
        remote_bind_address = (database_host, 3306)
    )
    
    tunnel.start()

def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection
    
    :return connection: Global MySQL database connection
    """
    
    global connection
    
    connection = pymysql.connect(
        host=database_host,
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port
    )

def run_query(sql):
    """Runs a given SQL query via the global database connection.
    
    :param sql: MySQL query
    :return: Pandas dataframe containing results
    """
    
    return pd.read_sql_query(sql, connection)

def mysql_disconnect():
    """Closes the MySQL database connection.
    """
    
    connection.close()