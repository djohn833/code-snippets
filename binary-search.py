a = [2, 3, 3, 5, 5, 5, 6, 6]

def template(a, key):
  ans = -1
  lo, hi = 0, len(a) - 1

  while lo <= hi:
    mid = (lo + hi) / 2
    val = a[mid]

    print(lo, mid, hi, val)

    if key < val:
      hi = mid - 1
    elif val < key:
      lo = mid + 1
    else:
      pass
  
  return ans

def contains(a, key):
  ans = False
  lo, hi = 0, len(a) - 1

  while lo <= hi:
    mid = (lo + hi) / 2
    val = a[mid]

    print(lo, mid, hi, val)

    if key < val:
      hi = mid - 1
    elif val < key:
      lo = mid + 1
    else:
      ans = True
      break
  
  return ans

def first(a, key):
  ans = -1
  lo, hi = 0, len(a) - 1

  while lo <= hi:
    mid = (lo + hi) / 2
    val = a[mid]

    print(lo, mid, hi, val)

    if key < val:
      hi = mid - 1
    elif val < key:
      lo = mid + 1
    else:
      ans = mid
      hi = mid - 1
  
  return ans

def last(a, key):
  ans = -1
  lo, hi = 0, len(a) - 1

  while lo <= hi:
    mid = (lo + hi) / 2
    val = a[mid]

    print(lo, mid, hi, val)

    if key < val:
      hi = mid - 1
    elif val < key:
      lo = mid + 1
    else:
      ans = mid
      lo = mid + 1
  
  return ans


def lowerBound(a, key):
  ans = -1
  lo, hi = 0, len(a) - 1

  while lo <= hi:
    mid = (lo + hi) / 2
    val = a[mid]

    print(lo, mid, hi, val)

    if key < val:
      hi = mid - 1
    elif val < key:
      ans = mid
      lo = mid + 1
    else:
      hi = mid - 1
  
  return ans

def upperBound(a, key):
  ans = -1
  lo, hi = 0, len(a) - 1

  while lo <= hi:
    mid = (lo + hi) / 2
    val = a[mid]

    print(lo, mid, hi, val)

    if key < val:
      ans = mid
      hi = mid - 1
    elif val < key:
      lo = mid + 1
    else:
      lo = mid + 1
  
  return ans
