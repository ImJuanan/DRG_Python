from drg_group.wuhan_2022.Base import messages,has_mcc,has_cc,intersect
def KE19_group(record):
  return True
def KD19_group(record):
  return True
def KF19_group(record):
  return True
def KR19_group(record):
  return True
def KS19_group(record):
  return True
def KD29_group(record):
  return True
def KC19_group(record):
  return True
def KB19_group(record):
  return True
def KT11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KJ1A_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KU13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KZ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KV1B_group(record):
  return True
def KU15_group(record):
  return True
def KT15_group(record):
  return True
def KZ15_group(record):
  return True
def KJ15_group(record):
  return True

