from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=["A27.900x005","E10.200x031+N29.8*","E10.200x214+N08.3*","E10.200x215+N08.3*","E11.200x031+N29.8*","E11.200x214+N08.3*","E11.200x215+N08.3*","E14.200x031+N29.8*","E14.200x214+N08.3*","E14.200x215+N08.3*","I12.000x001","N17.000","N17.001","N17.100","N17.101","N17.200","N17.200x002","N17.200x003","N17.800","N17.900","N17.900x002","N17.900x003","N17.900x004","N17.901","N18.400","N18.500","N18.501","N18.505+I68.8*","N18.506+I32.8*","N18.902","N19.x00","N19.x01","N19.x02","N99.000","N99.001","R39.200","R39.200x001","T79.500","T79.500x002","T86.100x003","T86.102","T86.106"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合LR1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LR11_group(record):
      return 'LR11'

    if MDCL_DRG.LR13_group(record):
      return 'LR13'

    if MDCL_DRG.LR15_group(record):
      return 'LR15'

    return 'LR1'
  else:
    return ''

