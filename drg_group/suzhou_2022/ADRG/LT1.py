from drg_group.suzhou_2022.Base import message,intersect,SS_VALID
from drg_group.suzhou_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C48.001","C64.x00x001","C64.x00x003","C64.x00x004","C65.x00","C65.x01","C65.x02","C66.x00","C66.x00x002","C66.x00x003","C67.000","C67.100","C67.200","C67.300","C67.400","C67.500","C67.501","C67.600","C67.700","C67.800","C67.900","C67.900x002","C68.000","C68.100","C68.800x003","C68.801","C68.802","C68.803","C68.804","C68.805","C68.900","C76.301","C76.303","C79.000x001","C79.001","C79.100x002","C79.101","C79.102","C79.103","D09.000","D09.100x001","D09.101","D09.102","D09.103","D09.104","D18.000x806","D18.000x811","D18.000x819","D21.506","D30.000","D30.100","D30.200","D30.300","D30.301","D30.302","D30.400","D30.701","D30.900","D41.000x001","D41.001","D41.100x001","D41.101","D41.200x001","D41.201","D41.300x001","D41.301","D41.400x001","D41.400x004","D41.401","D41.700","D41.900x001","D41.901","Q85.900x013","Q85.900x029","Q85.903"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合LT1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LT11_group(record):
      return 'LT11'

    if MDCL_DRG.LT13_group(record):
      return 'LT13'

    if MDCL_DRG.LT15_group(record):
      return 'LT15'

  return ''

