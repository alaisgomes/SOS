# Lib.py
# Holds standard tools.
# ___________________________________________________
# Standard headers

from __future__ import division,print_function
import sys,random,re,copy
sys.dont_write_bytecode=True # don't write irritating .pyc files

# ___________________________________________________
# Standard short cuts

rseed=random.seed
r=random.random
copy=copy.deepcopy

# ___________________________________________________
# Generic container (fields, but no methods).

class o:
  def __init__(i, **entries): i.__dict__.update(entries)
  def __repr__(i):  return str(kv(i.__dict__))

# ___________________________________________________
# Dictionary tricks

def kv(d, private="_", places=4):
  "Print dicts, keys sorted (ignoring 'private' keys"
  def _private(key):
    return key[0] == private
  def pretty(x):
    return round(x,places) if isa(x,float) else x
  return ['%s: %s' % (k,pretty(d[k]))
          for k in sorted(d.keys())
          if not _private(k)]

# ___________________________________________________
# Printing tricks

def dot(x='.'):
  "Write without new line"
  sys.stdout.write(x)
  sys.stdout.flush()

# ___________________________________________________
# Type tricks

def isa(x,y): return isinstance(x,y)
def isSym(x): return isa(x,str)

def thing(x):
  "Coerce to a float or an int or a string"
  try: return int(x)
  except ValueError:
    try: return float(x)
    except ValueError:
      return x

# ___________________________________________________
# Meta tricks

def same(z): return z

# ___________________________________________________
# 'The' is the place to hold global options

The=o()