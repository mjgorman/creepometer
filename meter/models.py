from __future__ import unicode_literals

from django.db import models
from redis import Redis

def nominate_post(name):
    con = Redis('localhost')
    con.sadd('coworkers', name)
    add_creepy(name.lower)

def list_nominees():
    con = Redis('localhost') 
    return con.smembers('coworkers')

def get_creepy(name):
    con = Redis('localhost') 
    creepy = con.get('coworker{0}'.format(name.lower()))
    if creepy != None:
        return creepy
    else:
        return 0

def add_creepy(name):
    con = Redis('localhost') 
    con.incr('coworker{0}'.format(name.lower()))

def reduce_creepy(name):
    con = Redis('localhost') 
    con.decr('coworker{0}'.format(name.lower()))
