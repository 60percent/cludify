#!/usr/bin/env bash

kill $(<app.py.pid)
rm app.py.pid
rm app.pyc
rm app.py
