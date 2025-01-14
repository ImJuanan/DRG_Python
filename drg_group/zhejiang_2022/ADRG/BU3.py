from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["G11.000","G11.000x002","G11.000x003","G11.000x004","G11.000x005","G11.000x006","G11.000x007","G11.000x008","G11.100","G11.100x002","G11.100x003","G11.100x004","G11.100x005","G11.100x006","G11.101","G11.102","G11.200","G11.200x002","G11.200x003","G11.200x004","G11.201","G11.300","G11.300x001","G11.300x002","G11.301","G11.400","G11.400x001","G11.800","G11.801","G11.900","G11.900x001","G11.900x005","G11.900x006","G11.901","G11.902","G35.x00","G35.x00x002","G35.x00x003","G35.x01","G35.x02","G35.x03","G35.x04","G35.x05","G35.x06+F02.8*","G36.000","G36.000x002","G36.100","G36.101","G36.800","G36.900","G36.901","G37.000","G37.000x002","G37.100","G37.100x002","G37.200","G37.200x001","G37.200x002","G37.300","G37.301","G37.400","G37.500","G37.800","G37.800x006","G37.801","G37.802","G37.803","G37.804","G37.805","G37.900","G37.901","R27.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BU3入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BU31_group(record):
      return 'BU31'

    if MDCB_DRG.BU33_group(record):
      return 'BU33'

    if MDCB_DRG.BU35_group(record):
      return 'BU35'

    return 'BU3'
  else:
    return ''

