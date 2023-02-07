from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.ADRG import EB1,EB2,EC1,EC2,ED1,EJ1,ER1,ER2,ER3,ES1,ES2,ES3,ET1,ET2,EU1,EV1,EW1,EX1,EX2,EZ1

def group(record):
  mdc_zd=["A06.502+J17.3*","A19.000x004","J85.200","Q85.900x015","J86.006","A16.406","A15.500x003","R06.804","B05.200+J17.1*","J95.800x016","J40.x00x002","J63.800x018","J67.600","C34.802","D17.400x005","J98.501","R84.100","J45.000x003","J60.x00x004","A15.603","J98.503","Q33.800x001","J98.400x013","R06.400","B33.400x001+J17.1*","J86.901","J68.301","C34.100x004","S27.801","A16.035","J69.001","J86.016","R59.009","J15.600x005","S27.800x013","T17.500","A01.000x005+J17.0*","J86.000x006","J98.507","B42.000+J99.8*","B06.801+J17.1*","J15.300","J43.001","D15.200","A19.001","J15.800x002","J98.800x004","A15.812","C34.000x002","D36.706","A16.029","C49.300x003","J69.000","A15.500x010","J95.800x004","J66.200","D38.200x001","A15.100x002","J98.800x001","J86.902","J81.x00x002","J95.811","A16.021","D18.000x857","J86.019","A16.500x010","J46.x00x010","A15.100x010","J98.008","A15.810","J42.x00x004","J18.200","J44.801","A15.500x016","I88.106","J86.020","Q34.100","J65.x00","A15.800x001","R84.903","A15.701","J12.100","I26.900x013","A16.800x003","A15.404","D17.400x002","J42.x00","A16.008","A15.103","A15.500x027","J15.101","D17.700x023","A15.500x002","J10.000","B48.501+J17.2*","A19.802","A15.406","Q79.101","A15.401","S27.806","M33.901+J99.1*","J60.x00x002","S27.700","J18.801","S27.303","D48.700x019","J18.903","C78.002","I89.000x027","A16.100x001","J86.017","J98.007","A06.500+J99.8*","B40.100","I26.900x006","J18.002","S27.301","J45.002","J86.007","J93.100x002","R09.000","B37.100","J18.803","J94.800x010","Q33.500","J70.001","A15.100x005","J70.101","I89.800x002","J18.802","J63.000x002","J63.800x025","J84.002","A16.016","Z03.800x001","D17.400x004","J86.000x012","A19.000x008","A16.401","J20.500","J86.903","A15.500x026","T17.802","J63.001","A16.803","J63.800x009","S27.302","A15.000x028","J20.000","J62.000x002","J96.900x003","J84.104","C45.700","J94.800x004","A06.501+J99.8*","R84.500","C79.810","J41.100","C76.100x003","J62.802","I26.900x002","J45.000","A15.101","J43.000","A16.900x023","J61.x00x002","J10.100x005","J94.901","R09.100","I89.800x007","R09.801","B40.000","C49.300x001","S29.800","D36.700x008","T81.400x009","T17.801","A16.038","D38.601","I26.900x009","J15.200","R04.800x004","J84.102","J69.100x001","A16.033","J10.001","J09.x02","A37.900","A16.504","J98.800x007","B38.000","A16.106","J15.602","D15.200x001","A15.007","A16.009","A19.000x020","A15.609","D38.102","J82.x00x002","J15.500","J43.901","Q34.000","J18.000x002","A19.000x002","J40.x01","A16.304","J15.800x001","J12.800","C76.100","A15.503","A15.900","A19.000x003","C34.001","J11.100x005","J15.901","J22.x00","J67.900","A16.101","I26.901","Q33.200","Q85.901","R91.x03","S28.000","J63.803","J85.001","U07.100x001","C37.x00","J11.000x001","J98.800x018","J62.800x007","J98.901","J67.800x002","J15.600x003","D38.103","I26.900x012","J63.301","J68.000x001","A15.305","J18.001","R94.202","J43.902","J39.804","J80.x01","J60.x00x005","A16.027","J90.x00x003","A15.703","D48.709","J44.800x001","J70.800","A36.201","A16.303","A15.100x009","R06.000","A15.306","A19.000x005","A16.200x002","C77.101","J95.200","J86.002","B38.100x001+J17.2*","J94.200","S27.802","D38.300x003","C34.900x006","R06.301","S27.312","J15.400","J44.807","J67.300","A06.500x002+J99.8*","A15.003","J95.804","A16.200x012","R91.x04","C34.800","A22.102+J17.0*","J93.003","Q32.102","J98.417","J94.800x003","I26.900x016","A15.000x012","R04.800x002","J82.x00x001","A15.100x011","A15.301","E32.800x001","J09.x00","J15.700","J98.010","J12.300","J90.x00","A19.000x016","B39.000x001+J17.2*","R93.805","D18.011","J43.101","R09.100x002","J84.800x003","S27.210","T27.700","J96.900x001","A19.801","J85.000x002","J98.602","A16.001","J63.800x014","T86.803","A16.501","J63.800x022","C34.803","J98.006","J84.800x004","J98.800x009","Q89.209","A15.106","A16.036","R93.801","J47.x02","A16.301","J84.110","B77.801+J17.3*","T84.200x004","J45.000x001","A15.300x001","A16.200x007","J67.200x002","J20.902","A16.805","J98.000x009","J44.900x002","C77.105","S27.804","C49.302","I26.900x017","J21.801","D36.700x013","J63.400","R09.200","A16.302","J18.800x001","D15.000","B38.200","J98.009","B45.000x002+J99.8*","B67.100x001+J99.8*","A15.504","J44.000","J98.800x003","A15.400x001","J45.004","A16.900x002","I26.900x001","J84.100x006","Q79.102","J63.801","J98.404","A16.032","C38.100","E32.000","J68.400","J68.900","J98.500x007","A15.201","Q79.103","A16.005","J44.900x004","I89.800x023","J86.013","J86.012","J61.x01","A15.901","I89.000x016","J82.x00x005","T17.900","B65.907+I52.1*","J18.901","J98.400x016","A19.000","B38.000x001+J17.2*","D02.201","D86.000","S27.311","D38.401","A16.017","B25.000+J17.1*","R94.204","J95.808","A15.006","C34.201","J94.801","B66.401+J99.8*","R06.600","J94.804","Q85.904","C78.200","J62.000x003","J80.x00","J44.805","J98.800x006","J84.804","R06.803","J44.900x005","E85.412+J99.8*","J98.000x012","J63.800x016","J63.800x012","Q33.400","A16.004","J44.802","C34.800x003","J60.x01","J62.801","A16.104","J98.409","A16.505","J98.004","A15.000x001","J45.900x012","A16.300x007","A16.003","A15.102","J82.x01","R05.x00","A15.307","A15.000x010","J20.800","J62.800x002","J39.806","A16.026","R04.200","T27.200x001","J14.x00","J46.x00x003","A15.002","J86.004","A21.201+J17.0*","J94.805","J86.018","J45.900x023","A16.018","I26.902","J94.900x001","A16.807","Q33.100","Q79.000","A15.805","A15.000x020","A16.030","A16.800x002","J16.000","I26.900x003","T27.500x001","J85.002","T17.804","J45.902","B06.800","R05.x01","A16.107","A15.000x016","A16.400x011","I00.x00x007+J17.8*","A16.200x014","A16.000x002","J98.416","A16.210","J86.011","E84.001","Q33.000","A16.200x013","J39.808","J63.800x023","S27.000","A15.507","A15.000x018","A15.500x022","A16.205","B38.100","A15.804","C34.300x004","B41.000","D14.400","J64.x00","J98.508","J84.103","R06.000x003","J86.008","J63.800x011","J98.401","E32.002","J45.900","J67.800x003","B01.200+J17.1*","M31.304+J99.1*","S27.812","Q89.800x910","U07.100x002","S27.811","A15.806","J98.400x005","C39.900x001","J15.900","J62.800x003","C78.304","J63.200","S27.807","J98.200","J92.901","J84.801","A15.000x003","A15.100x006","I26.900x018","R09.300","J42.x00x006","A15.000x026","C34.801","A15.500x025","J62.001","J69.000x002","E85.404","A15.206","J63.300x003","A15.500x011","D36.717","J45.100","J60.x00","B48.502+J17.2*","C77.103","D38.101","C79.800x809","J39.803","J45.901","J63.800x020","Q85.908","J40.x00","J98.100","R05.x02","J67.800x004","M05.101+J99.0*","J47.x01","J67.200x003","J95.800x010","C79.800x829","M32.103+J99.1*","J20.600","D14.302","E32.800x005","A15.607","A16.300x003","C38.300","C79.807","D18.000x814","U07.000","A15.302","J90.x02","J98.000x011","S27.610","T79.800x007","J93.100x001","A15.205","J95.300","E32.900","Q33.301","A15.604","A16.102","J63.800x003","A16.200x015","E89.802","A37.901+J17.0*","J98.414","D38.400x001","A37.000","R09.201","J95.801","J43.800x001","J41.000","R84.600","A19.000x009","J63.800x013","R84.904","J68.001","A16.023","R91.x00x001","A16.400x005","B39.000","B45.000","B65.902+J99.8*","J90.x01","D38.105","A15.107","B38.200x001+J17.2*","J63.100","J63.800x021","A15.500x012","Q32.402","S27.805","U07.100x003","A16.900x001","J94.201","A16.000x001","J45.900x031","S27.100","A16.105","J84.109","D15.900","D18.100x025","J63.800x019","J21.900","M35.904+J99.1*","J98.400x012","J98.000x013","T85.700x804","J67.400","J93.800x001","A15.809","B44.101+J99.8*","C34.300x003","B37.800x083","B48.500+J17.2*","J70.900","C34.101","J84.101","J98.800x016","J45.100x003","D38.600x001","C34.900x001","J18.000","A15.814","A16.700x001","J45.900x041","A43.000x001+J99.8*","A37.900x004","A54.806+J17.0*","C77.100x004","J61.x00x003","E32.001","J63.800x017","M05.102+J99.0*","J98.801","S29.700","R84.700","D02.200x002","J92.900x002","J98.102","E83.104+J99.8*","Q32.400x002","S27.400","J47.x03","J66.100","M33.103+J99.1*","A15.702","A16.802","J67.000","J98.002","J95.800x012","A15.100x003","J45.100x002","A15.506","C33.x00","D19.000","I89.800x016","A19.000x018","J39.801","S27.510","J95.802","C34.000","A15.500x004","J44.900x003","A15.408","C34.900x008","J86.001","I28.800x010","J45.900x001","J63.800x024","I89.800x018","A16.020","J86.000","A16.024","J63.000x001","A16.103","J41.800","J46.x02","J98.412","J69.000x004","J98.011","A16.002","Q33.002","J45.900x013","A15.004","J67.700x001","J98.400x008","J68.201","C38.400","D14.200","A16.402","R06.801","R09.800x093","R84.400","S27.600","J98.418","J62.800x006","J98.101","T86.800x011","A16.207","C34.901","D38.300x001","J66.800","A15.606","J84.800x007","C34.301","J96.000","M33.201+J99.1*","S27.110","M35.002+J99.1*","C34.900x005","J95.900","J98.502","I26.900x008","B46.000x001+J99.8*","I89.807","R94.201","A15.200x002","A15.807","J82.x00x004","J69.101","J15.402","R84.800","Q34.900","D15.701","A15.500x023","A19.000x017","J43.900x001","I89.003","D38.100x003","I89.000x028","A15.811","J21.901","J67.800x001","M34.800x001+J99.1*","Q33.600","A15.500x020","R06.000x002","J45.800","J98.201","T85.608","A15.402","A15.500x029","D17.400x003","R06.800x005","M34.801+J99.1*","J84.803","A15.803","J68.101","J18.800x012","J96.100","E32.800x004","J67.800x005","J81.x00","C45.000","C78.100","J63.802","J15.600x006","J98.410","B37.803","R06.806","A16.010","J39.810","A15.500x019","J43.000x003","A37.800x001","A15.500x017","J90.x00x002","Q33.800x002","J98.407","J20.100","J94.101","D48.115","J43.200","S27.300x012","J45.903","J84.800x005","D38.201","C34.902","J95.800x009","J21.900x002","A15.100x008","J61.x00x001","J63.800x015","J63.300x001","A15.601","A16.014","D38.100x002","J44.803","J86.014","A15.207","J21.100","J94.806","J98.003","J98.505","J62.800x005","J98.601","A19.803","J86.010","J98.001","A15.000x014","J39.802","J90.x00x005","T17.803","I26.900x005","S24.200","I88.900x008","T17.501","J67.100","J44.900","J20.200","C77.104","I89.000x029","A16.013","A15.500x015","A52.704+J99.8*","A16.203","A16.015","C77.100","A15.500x013","E32.801","J98.402","E32.000x003","J86.009","J10.000x001","D38.104","D17.700x019","A16.206","E85.400x005","J84.100x008","A37.900x003","B39.200","J84.000x003","M33.001+J99.1*","C77.102","J45.006","J67.600x001","A16.405","A15.203","A16.500x004","D38.301","J62.000x001","J68.002","A15.405","J85.100","D02.100","I89.804","J67.400x002","A16.804","J98.415","A15.001","J18.000x001","J46.x00x009","J43.904","J98.300","A15.200x001","R84.200","T27.300","A15.500x028","J43.903","J84.900","J84.105","J98.400x001","J63.500","J94.807","A15.000x022","J63.800x026","J93.900","C34.800x001","J70.200x002","J68.000x002","T17.400","A16.007","Q33.900","D48.710","A19.000x015","J63.800x005","J85.300","J84.100x007","R06.100","J12.900","B37.101+J17.2*","J15.601","J63.800","J84.001","C79.800x838","J84.805","J42.x00x005","A16.201","J98.600x001","B44.000x001+J99.8*","J45.003","M05.100+J99.0*","R09.800x092","J62.800x004","A15.808","T27.600x001","C38.400x003","J18.800x004","J43.900","A15.508","J42.x01","A16.028","J63.300x002","J86.015","S29.900","R06.200","A16.400x010","S28.100","R84.300","J20.700","J95.401","Q32.400x005","A16.006","J66.000","J62.804","J15.902","J21.000","S27.010","A16.900x003","G47.300x034","J42.x00x003","J63.000x003","A15.500x014","C34.900x004","J90.x00x004","S27.500","I26.900x015","S27.808","A16.202","J95.100","J98.400x019","C78.001","J15.000x002","J67.200","B39.200x001+J17.2*","B44.102+J17.2*","J70.300","J13.x00","B49.x13","A16.204","S27.810","R06.300","A16.019","A16.300x002","A16.500x009","A16.037","D15.200x002","A16.500x001","J45.900x011","J67.500","A37.100","J84.800x008","Q32.400x004","I89.800x017","R91.x00x005","J15.100","Q32.200","J86.000x013","J67.700x002","J98.500x001","C38.800","E32.100","A15.505","D14.301","J46.x01","Q32.401","J98.802","A16.500x008","D18.000x800","A15.813","B49.x14+J99.8*","A15.608","D21.302","J12.200","J98.411","S27.501","J84.800x006","A16.108","R09.800x091","Q32.300","J18.902","J86.003","M31.300x002","R91.x01","J45.007","D14.300x001","J94.802","S27.401","J46.x00x002","J98.408","S27.313","A19.000x007","J95.800x021","J68.800","J62.803","J86.005","C78.000","A02.201+J17.0*","A15.501","D18.100x015","E85.407","J18.800x002","J20.901","J96.900x002","J15.600x002","A16.011","J84.108","A15.303","A15.104","R94.200","J45.900x002","A15.407","A16.022","C38.401","J95.810","A16.109","J98.504","S27.410","J39.805","A15.304","J63.800x010","J98.403","J70.200","J98.800x014","J18.100","A15.204","J43.100","R04.802","J12.000","D17.400x001","J84.802","J62.800x008","R06.802","A19.000x019","C46.701","C34.100x003","A15.500x001","A15.100x001","C34.102","A15.100x007","J45.005","R84.000","A15.605","R09.800x095","U04.900","I88.107","M31.302+J99.1*","C78.000x003","C38.200","A15.105","I26.900x010","A15.801","A16.025","B39.100","B40.200","J15.000","R09.800x094","S27.310","J63.201","S27.710","J09.x01","A15.500x021","A16.700x002","I97.800x018","J42.x00x001","D18.100x026","J60.x00x003","A15.202","A19.000x014","C34.000x003","C78.306","C78.003","D86.200","A16.801","A16.012","B58.300+J17.3*","D15.700","J45.900x021","J63.800x001","R93.804","J16.800x001","A16.305","B39.100x001+J17.2*","J18.900","A15.502","A15.000x002","A15.409","J69.800x001","A15.403","A19.000x006","S25.401","A19.000x001","J46.x00x008","A15.509","A15.802","A16.031","A15.602","C39.800","R09.101","S27.200","C34.800x002","A15.000x024","S27.900","I26.900x011","A19.000x011","A15.005","I26.900x007","J70.400","R04.900","J98.405","R06.805","J98.005","A19.000x010","D38.300x002","C45.702","J47.x00","D38.100x001","J44.806","J98.506","D02.400","J46.x00x006","J98.700","J39.807","A19.000x013","C45.701","A15.500x024","A15.500x018","J63.000","J98.413","M05.103+J99.0*","J18.800x006","I89.800x021","A16.503","A15.100x004","A16.403","J44.100","J92.000","T17.901","A16.806","C78.201","J20.300","J20.400","J20.900","E32.802","Q33.003","S27.910","J15.903","A16.034","S27.803","B49.x00x011","J98.500x008","A19.000x012"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCE入组条件，匹配规则：主诊断匹配')

  result=EB1.group(record)
  if result:
    return result
  result=EB2.group(record)
  if result:
    return result
  result=EC1.group(record)
  if result:
    return result
  result=EC2.group(record)
  if result:
    return result
  result=ED1.group(record)
  if result:
    return result
  result=EJ1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合EQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'EQY'

  result=ER1.group(record)
  if result:
    return result

  result=ER2.group(record)
  if result:
    return result

  result=ER3.group(record)
  if result:
    return result

  result=ES1.group(record)
  if result:
    return result

  result=ES2.group(record)
  if result:
    return result

  result=ES3.group(record)
  if result:
    return result

  result=ET1.group(record)
  if result:
    return result

  result=ET2.group(record)
  if result:
    return result

  result=EU1.group(record)
  if result:
    return result

  result=EV1.group(record)
  if result:
    return result

  result=EW1.group(record)
  if result:
    return result

  result=EX1.group(record)
  if result:
    return result

  result=EX2.group(record)
  if result:
    return result

  result=EZ1.group(record)
  if result:
    return result

  message('不符合MDCE的ADRG入组条件')
