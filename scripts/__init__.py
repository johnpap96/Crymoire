#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os.path
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
