from __future__ import print_function
# coding=utf-8
import sys
CURRENT_USER = None

def getCurrentUser(session):
    try:
        return session.get("user_id")
    except Exception as e:
        print(' gerCurrentUser() -> ' + e.message, file=sys.stdout)
        return None

def updateCurrentUser(session):
    global CURRENT_USER
    CURRENT_USER = getCurrentUser(session)
    print(' updateCurrentUser() : user -> ' + CURRENT_USER, file=sys.stdout)