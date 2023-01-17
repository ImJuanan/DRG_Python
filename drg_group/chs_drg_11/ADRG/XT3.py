from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCX_DRG

def group(record):
  adrg_zd=["B90.000","B90.100","B90.101","B90.200","B90.200x002","B90.200x003","B90.201","B90.202","B90.800x004","B90.800x005","B90.800x006","B90.801","B90.802","B90.803","B90.804","B90.901","B90.903","B90.904","B91.x00","B92.x00","B94.000","B94.200","B94.201","B94.800x001","B94.801","B94.802","B94.900","E89.900","Q85.914","Q90.200","Q93.300","R46.300","R46.500","R46.800x001","R46.801","R58.x00x002","R58.x00x004","R58.x00x005","R58.x00x006","R58.x00x007","R59.901","R96.100x001","R98.x00x002","R99.x00x002","R99.x01","T73.200","T73.300","T75.200","T80.202","T80.203","T80.800","T80.801","T81.601","T82.812","T84.400","T84.700","T84.700x001","T84.900","T84.901","T85.800","T85.801","T85.802","T85.806","T85.902","T86.900","T87.200","T88.901","T96.x00x001","T96.x00x002","T96.x00x003","T98.000","T98.200","T98.200x031","T98.200x032","Z00.001","Z00.100","Z00.200","Z00.300","Z00.300x001","Z01.600x002","Z01.800x002","Z03.100","Z03.101","Z03.102","Z03.103","Z03.300","Z03.600x001","Z03.800","Z03.800x701","Z03.800x711","Z03.800x721","Z03.800x731","Z03.802","Z03.803","Z03.900","Z03.900x001","Z09.001","Z10.000","Z11.000","Z11.200","Z11.300","Z11.400","Z11.500","Z11.600","Z11.800x001","Z11.801","Z11.802","Z11.803","Z11.901","Z11.902","Z12.000","Z12.100","Z12.300","Z12.400","Z12.500","Z12.600","Z12.800","Z12.900x001","Z12.901","Z13.000x001","Z13.001","Z13.100","Z13.200","Z13.300","Z13.300x002","Z13.300x003","Z13.400x001","Z13.500","Z13.500x001","Z13.501","Z13.600","Z13.700","Z13.800x011","Z13.800x031","Z13.800x032","Z13.800x041","Z13.800x051","Z13.800x061","Z13.801","Z13.900","Z20.000","Z20.001","Z20.100","Z20.200","Z20.300","Z20.400","Z20.500","Z20.600","Z20.701","Z20.702","Z20.801","Z20.802","Z20.900","Z22.000","Z22.100","Z22.101","Z22.102","Z22.103","Z22.200","Z22.300","Z22.301","Z22.303","Z22.400","Z22.401","Z22.402","Z22.600","Z22.700","Z22.801","Z22.900x001","Z23.000","Z23.100","Z23.200","Z23.300","Z23.400","Z23.500","Z23.600","Z23.700","Z23.800x001","Z24.001","Z24.200","Z24.300","Z24.400","Z24.500","Z24.600","Z24.601","Z25.000","Z25.100","Z25.800x001","Z26.000","Z26.800","Z26.900","Z27.000","Z27.100","Z27.200","Z27.300","Z27.400x001","Z27.800","Z27.900","Z28.000","Z28.100","Z28.101","Z28.201","Z28.800","Z28.900","Z29.000","Z29.100","Z30.000x001","Z30.000x002","Z30.000x003","Z30.101","Z30.102","Z30.103","Z30.201","Z30.202","Z30.203","Z30.301","Z30.302","Z30.400x001","Z30.400x003","Z30.400x004","Z30.500x011","Z30.501","Z30.503","Z30.504","Z30.505","Z30.800x001","Z30.800x002","Z30.800x003","Z30.800x004","Z30.800x005","Z30.900","Z31.202","Z31.203","Z31.400x003","Z31.400x004","Z31.401","Z31.402","Z31.500","Z31.600x001","Z31.800","Z31.900","Z32.000x001","Z32.100","Z39.100x001","Z39.100x002","Z39.100x003","Z39.200x001","Z40.000x001","Z40.800","Z40.900x001","Z41.300","Z41.800x002","Z41.801","Z41.900","Z51.300","Z51.400x001","Z51.400x002","Z51.400x003","Z51.401","Z51.800","Z52.000","Z52.001","Z52.300x002","Z52.900","Z54.000","Z54.000x002","Z54.000x003","Z54.000x004","Z54.000x005","Z54.000x006","Z54.000x007","Z54.000x008","Z54.000x009","Z54.000x010","Z54.000x012","Z54.000x013","Z54.000x014","Z54.000x015","Z54.000x016","Z54.000x017","Z54.000x018","Z54.000x019","Z54.000x020","Z54.000x021","Z54.000x022","Z54.100","Z54.200x001","Z54.300","Z54.400","Z54.700","Z54.800x001","Z54.800x002","Z54.800x003","Z54.800x006","Z54.800x007","Z54.800x008","Z55.000","Z55.100","Z55.200","Z55.300","Z55.400","Z55.800","Z55.900","Z56.000","Z56.100","Z56.200","Z56.300","Z56.400","Z56.500","Z56.600","Z56.700","Z57.000","Z57.100","Z57.201","Z57.300","Z57.400","Z57.501","Z57.502","Z57.503","Z57.504","Z57.505","Z57.506","Z57.507","Z57.508","Z57.600","Z57.700","Z57.800","Z57.900","Z58.000","Z58.100","Z58.200","Z58.300","Z58.400","Z58.500","Z58.600","Z58.700","Z58.800","Z58.900","Z59.000x001","Z59.100","Z59.200","Z59.300","Z59.400","Z59.500","Z59.600","Z59.700","Z59.800","Z59.900","Z60.000x001","Z60.100x001","Z60.200x001","Z60.300x002","Z60.400","Z60.500","Z60.800","Z60.900","Z61.000x001","Z61.100x001","Z61.200x001","Z61.300x001","Z61.400x001","Z61.500x001","Z61.600x001","Z61.700x001","Z61.800","Z61.900x001","Z62.000x001","Z62.100x001","Z62.200x001","Z62.300x001","Z62.400x001","Z62.500x001","Z62.600x001","Z62.800","Z62.900","Z63.000","Z63.100x001","Z63.200x001","Z63.300x001","Z63.400x001","Z63.400x002","Z63.400x003","Z63.500x001","Z63.500x002","Z63.500x003","Z63.600","Z63.700x001","Z63.700x011","Z63.700x021","Z63.700x091","Z63.700x092","Z63.700x093","Z63.800x001","Z63.800x002","Z63.800x003","Z63.800x004","Z63.900","Z64.100x001","Z64.200","Z64.300","Z64.400x001","Z64.400x002","Z64.400x003","Z65.000","Z65.100x001","Z65.200","Z65.300x001","Z65.300x002","Z65.300x003","Z65.300x004","Z65.300x005","Z65.400x001","Z65.400x002","Z65.400x003","Z65.500x001","Z65.500x002","Z65.500x003","Z65.800","Z65.900","Z70.000","Z70.100","Z70.200","Z70.300","Z70.800","Z70.900","Z71.000","Z71.100","Z71.200","Z71.300","Z71.400","Z71.500","Z71.600","Z71.700","Z71.800","Z71.900","Z72.000","Z72.100","Z72.200","Z72.300","Z72.400","Z72.500","Z72.600","Z72.800","Z72.900","Z73.000","Z73.100x001","Z73.200","Z73.300","Z73.400","Z73.500","Z73.600","Z73.800","Z73.900","Z74.000","Z74.100x001","Z74.200","Z74.300","Z74.800","Z74.900","Z75.000","Z75.100","Z75.200","Z75.300","Z75.400","Z75.500","Z75.800x001","Z75.900x001","Z76.000","Z76.100","Z76.201","Z76.300","Z76.400","Z76.500","Z76.800x001","Z76.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合XT3入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XT33_group(record):
      return 'XT33'

    if MDCX_DRG.XT35_group(record):
      return 'XT35'

    return 'XT3'
  else:
    return ''

