from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.ADRG import GB1,GB2,GC1,GC2,GD1,GD2,GE1,GE2,GF1,GF2,GG1,GJ1,GK1,GK2,GK3,GR1,GS1,GT1,GU1,GU2,GV1,GW1,GZ1

def group(record):
  mdc_zd=["K25.200x001","Q40.209","K28.500x001","K52.104","C16.401","K63.401","A03.900x009","K57.102","K26.600","K51.400","C78.504","I72.802","K40.307","D37.204","K31.300","Q40.100","K64.401","Q43.804","K22.808","K22.802","E16.402","K57.104","K26.500x001","A18.303+K93.0*","E14.400x370+G99.0*","K90.000","A18.311+K93.0*","C26.900","K91.801","D48.401","A49.809","S36.403","K25.100x001","K55.106","K20.x00x003","K56.200x011","K66.008","K91.800x601","K59.401","K28.700","K91.837","K56.400x001","I72.800x142","K91.813","K66.812","C15.500","Q41.800","C26.800x001","K40.401","D37.206","R10.102","K90.300x001","S36.801","B37.806","K27.501","K62.300x003","K62.401","K31.808","K63.504","R19.000x005","C16.000x004","K27.900x001","K63.810","D18.000x825","K51.903","K65.906","K65.800x002","K51.202","M34.800x006+K23.8*","Q39.000x001","K52.907","Q43.403","K64.801","C17.200","K61.001","C45.700x002","K64.400","A07.200","C19.x01","A09.000x001","K64.809","K57.200x001","D48.117","T18.100","K29.000","A09.000x003","S36.814","K92.204","D12.700","D37.901","K51.902","Q43.102","D48.713","K59.900x002","D37.409","K45.100","K40.300","K27.000","Q43.800x009","K64.810","K91.102","C78.801","K36.x01","K62.100","K63.805","T18.400","K50.800","K65.013","C78.603","K36.x00x003","D37.101","C21.801","K59.101","K90.404","Q42.803","K63.307","D01.300x001","K38.200","K31.000","K63.500x084","K63.200x003","K55.013","D17.500x003","K56.501","I89.803","S36.500x041","K22.203","K91.800x103","K63.210","A09.904","C15.801","K63.814","Q79.400","A04.803","C15.800x004","Q43.601","K52.910","K62.815","Q43.200x003","K65.800x001","K40.313","K56.603","C48.103","K55.800x004","K90.801","K63.900x001","R85.100","K51.003","K55.002","K52.917","C15.900x003","K63.216","K43.602","D17.500x009","C26.800x003","K31.703","A09.900x007","Q40.300","C16.100","K62.402","Q45.300x102","C16.301","K60.300","K58.800","K22.812","C26.901","B82.000","K40.311","R19.400","K29.800","K46.000x002","E10.400x330+G99.0*","Q43.809","K62.818","K27.503","I86.812","K62.808","K59.000","C16.903","T28.200x001","K63.205","K55.003","K64.805","K56.000","A08.300","K63.817","K52.918","A74.801+K67.0*","K91.821","K90.405","Q42.901","K57.300x006","K63.809","K52.000x001","K40.903","K40.301","K62.822","K64.811","K31.812","R19.200","K52.201","K38.000","Q43.003","A18.300x016","E11.400x340+G99.0*","K55.801","Q42.001","K44.901","K22.206","K22.800x011","K25.000x001","K31.802","C18.901","K63.303","K36.x00x004","A09.902","K57.303","K56.400x003","K92.800x005","K65.807","C45.705","K59.200x002","D00.100","K65.802","K40.203","C16.000","K57.800","Q43.602","K22.600x001","K57.103","S36.500x011","A18.300x015+K93.0*","K20.x01","K46.903","Q42.202","K22.200","K26.001","Q43.002","D13.900x003","D00.200x002","K22.209","C16.804","K40.309","Q42.102","K90.901","K63.211","A18.316+K93.0*","C78.401","D36.708","C16.800","K27.600x001","K63.200","K66.809","R19.500x002","K63.902","K66.004","K62.805","D48.714","K57.108","B37.800x091","K92.208","K66.800x008","A04.401","Q42.000x301","K65.000x014","B77.001+K93.8*","E11.406+G99.0*","A08.400x003","K40.900x002","K41.900x001","C21.100","K59.200x003","K63.503","K27.500","K64.806","D18.000x838","K56.401","R14.x00x007","K66.007","A60.102+K93.8*","A08.100x001","K61.002","D37.707","E14.400x340+G99.0*","K31.603","R85.800","D18.000x859","K31.605","K63.901","K31.100","D37.700x001","K50.103","C77.208","K66.002","J11.800x002","C16.600","C18.802","D36.901","K35.800x001","K42.901","Q41.001","K64.402","K45.806","D37.403","K25.700","A04.800x010","R93.300x003","K41.300x003","Q39.400","K45.805","A18.300x014+K93.0*","K92.000","K91.831","K91.402","C17.900x002","K40.900x004","A05.200x002","Q43.811","D37.708","K22.815","R10.402","Q43.300x201","D19.100","I86.400","K26.300","S36.400x093","K91.832","K25.400x001","K43.000","K55.300x001","D37.100x001","K43.902","D37.200x003","K65.801","K52.800x003","K38.000x002","K65.804","K55.300","K51.201","K45.000","K38.800x001","K63.306","A07.000","E16.401","K43.302","K56.201","Q41.201","T18.301","Q39.800x201","K62.902","K55.008","R85.400","K29.608","K44.000x002","K27.400x001","D37.401","K56.200","K51.901","D12.800","K60.302","E73.800","K21.001","S36.300","E84.102","K91.800x102","D36.707","K22.806","D48.402","K62.601","K66.005","D18.000x801","K27.902","Q89.301","Q40.200x004","S36.500x031","Q79.200","K40.402","K56.203","K62.821","K63.900x005","Q40.202","K66.006","K66.800","K66.800x009","Q42.200x901","K42.100x001","K27.700x001","D17.500x001","K31.815","R58.x01","Q42.802","Q39.803","D37.606","A09.000x006","C48.000","K52.001","I88.001","C16.200","C17.100","K55.004","C18.800x002","Q40.201","K92.203","Q41.101","K52.300","K51.002","Q39.300","Q85.900x002","A09.900x004","K51.300","Q39.800x903","K40.305","D01.100","D12.600","K91.802","R93.500x001","K52.912","D12.301","Q42.200x904","K52.804","K22.100","D37.502","R85.600","K66.901","R19.600","S36.310","K42.001","S36.412","C15.100x002","A18.315+K93.0*","C78.802","K62.001","C16.402","K66.811","K57.106","K91.305","A18.305+K93.0*","K42.900","A07.100","K31.200","K63.500x002","K26.000","D12.400","D12.000x002","R19.501","K31.601","K91.842","K64.900","R14.x00x006","K61.100","S36.511","K25.500x001","K52.911","K58.300","A18.300x013+K93.0*","K31.800x806","A03.902","D12.001","K55.000x010","R93.300x004","K62.800x010","K62.803","K62.800x005","K63.209","K26.400x003","A03.903","K25.000","K28.600","K62.901","K31.606","K57.003","K65.805","K91.800x702","D48.301","D13.303","K65.001","Q41.203","C15.200","K65.000","K55.902","K91.833","C79.800x834","S36.405","B66.501","D37.700x007","C45.101","K91.814","C26.800x002","K25.600","K42.000x001","K46.900x003","K55.000x005","K62.810","C45.100","C16.803","K29.600","K25.901","K63.806","Q43.807","K51.302","K55.101","K65.903","S39.909","R14.x00x001","K62.800x001","Q39.800x905","D01.401","A05.900","Q42.201","K29.500","K52.200x004","K31.102","D48.121","K62.800x009","D17.500x005","K56.601","Q39.900","C17.300","K56.503","D01.402","A00.000x001","K90.100x002","K66.806","I72.800x063","A05.000","K60.303","A18.310","K63.104","Q43.800x015","C78.800x013","C48.200","S36.900","K92.800x007","Q42.000x101","K62.802","D37.201","K41.000","K55.900","K35.201","Q42.902","T28.100","A09.901","D17.701","I85.000x001","K51.001","K50.101","Q45.300x104","K22.805","K31.501","K62.201","Q41.003","K64.000","K22.202","E10.400x350+G99.0*","A00.900x005","K59.800x002","K31.816","Q40.900","D37.400x002","K40.904","K58.200","E10.400x340+G99.0*","K91.000","Q43.401","K27.200","Q40.200x005","D37.103","Q43.105","C16.902","K91.815","K63.208","K40.314","S30.102","D37.900x001","C45.703","K62.500x001","K64.200","K25.903","D12.901","K22.803","K62.200x001","R10.400x004","A04.000x002","K90.001","K92.800x001","D37.411","K52.901","K62.700","C18.200","C21.000","K62.000","C16.500","K64.804","K31.904","K63.302","K63.812","D13.301","Q43.404","Q43.500","K59.200","K57.302","K55.200","K61.300","K57.801","K57.400","K91.829","C15.400","B82.900","Q42.000x201","C78.600x004","K55.800x003","K59.400","K52.803","K29.600x006","A00.100x001","K40.002","K66.003","K91.302","K40.102","K91.406","K45.002","D37.402","K41.300x002","K90.200x001","K91.405","I86.800x014","C15.800x002","K65.900","K92.901","K40.900x003","K55.102","S36.901","K40.400x001","D13.902","E16.400x003","Q39.802","D18.000x041","Q42.800x003","K22.000x001","E14.400x350+G99.0*","B77.000x001+K93.8*","Q43.810","K91.800x602","K29.601","C18.803","A08.500","Q43.808","K50.801","K35.300","K40.204","T18.502","K29.606","K52.802","K55.012","D00.200","K61.200","D20.102","K22.301","M32.112+K93.8*","B87.800x002+K93.8*","S39.905","K31.600x005","K63.213","K56.200x003","Q43.100","K90.002","K65.004","K90.100x001","Q43.800x012","K31.604","K51.800x001","K55.100x008","C18.801","K41.301","K92.800x004","Q42.800x002","K65.012","K31.807","C48.800","A03.901","K59.400x002","K63.819","K90.400","K90.403","Q85.902","T28.200x002","R19.100","I86.800x022","D36.700x018","D37.207","K29.001","M32.115+K67.8*","Q41.104","K44.100x001","K45.807","R85.000","K31.800x801","K63.801","K92.206","K40.304","K35.200","K40.902","K52.909","Q43.800x019","K31.809","K91.800x111","C21.200","K56.202","K91.404","R12.x00","K22.000x002","K59.800x005","K31.813","D18.000x045","C15.100","D13.302","Q43.812","C78.500x008","K63.204","K27.600","D01.900","A04.702","S36.301","I72.816","Q45.900","K91.900","K51.203","K22.809","K61.101","K62.501","A04.700x002","K63.000","T18.501","K57.900","K55.100x001","K28.200","K55.104","K56.001","K60.402","C26.000","K59.801","K65.904","C16.002","R19.100x001","K43.002","C76.200","Q43.800x014","A09.006","K63.103","R93.303","K50.001","K52.103","K55.005","K52.903","K92.200x001","Q42.000x401","A04.700","D37.410","A18.318","R19.500x003","K38.802","I72.800x132","D37.203","A04.300x001","K63.101","Q41.901","C17.800","A08.400","K55.901","T28.700x002","K40.308","D12.100","K55.000x011","K52.000","K56.600x005","D37.503","K46.100x001","K31.902","K27.500x002","K55.900x004","A03.900x002","K25.400x002","K27.500x001","K46.900x002","C16.900x003","A18.309","K91.103","A03.100x001","K55.010","D18.000x043","I85.900x001","D37.406","K65.803","K51.200x001","Q43.104","K22.804","A08.401","A18.317","K65.008","K28.901","A18.304+K93.0*","I78.802","K63.108","K42.902","K91.812","K56.700x003","K62.400x002","R14.x00x003","K62.820","K50.800x001","K25.300x001","K29.802","K45.003","K91.800x007","D12.601","K56.600x008","A04.600","K92.100x001","K57.401","K26.900x002","K27.400x004","Q42.200x905","K43.304","K51.301","K62.804","S11.202","K31.811","K44.000x001","K91.811","K60.500","D09.700x002","A04.800x003","K37.x00","C16.900","A04.500","D20.101","K91.408","B46.200x001+K93.8*","K22.300","K66.001","K62.806","K63.304","K40.312","A09.900x003","K27.502","C78.601","S36.500x021","D37.607","K57.100x005","K37.x00x002","K28.500","K29.602","K57.202","K43.603","A05.000x001","K31.814","D48.400x002","K65.006","K63.813","K40.201","Q43.101","I89.801","S36.803","D01.404","I88.105","S36.813","K40.900x006","K22.500","Q43.801","K63.500","K91.808","R85.700","A08.301","A04.900","C15.100x003","K40.905","K62.100x002","K66.200","A05.400x001","K50.102","K27.900x005","C78.500x006","K26.900x001","A07.801","K28.900x001","K40.900x001","K43.400","A18.302+K93.0*","K29.400","R85.200","R85.500","K22.813","K62.600x002","D01.405","Q43.103","D17.700x027","C78.403","C78.800x010","K52.202","A05.300","K66.000","C18.000","K57.001","R10.103","K56.102","K51.401","K43.200","K51.900","D18.000x046","Q43.201","K91.820","K62.202","K64.100","Q42.301","K22.901","S36.411","K31.101","K91.830","K22.205","K50.104","D18.000x042","A03.800x002","S36.413","K31.800x802","Q27.810","K91.809","K92.800x002","K60.200","Q40.002","K26.200x002","K91.800x206","K63.804","D18.000x040","A18.300x006+K67.3*","I72.801","K29.604","I77.400","D17.500x008","K31.400","C18.500","A05.300x001","K60.403","C48.100","K66.201","K38.800x003","S36.812","K64.500","K62.813","S36.501","D13.000","Q40.208","C15.100x004","K57.305","D37.200x004","K31.702","D12.200","K92.800x011","A07.300","K55.000","A08.402","A18.313+K93.0*","K30.x00x001","K63.402","K38.801","A04.800x007","K63.403","K40.302","K64.803","K63.201","C78.809","K57.105","D37.710","Q42.302","Q43.106","K63.206","K64.300","K22.400","C20.x01","K29.101","Q89.300x001","Q45.300x103","A18.306+K93.0*","K43.301","D20.000","D48.300x001","C16.800x003","K28.401","S36.810","T18.900","K43.700","Q43.800x017","K66.805","K40.202","K60.301","Q39.602","A00.900x004","K63.400","K66.807","D37.100x002","C48.201","T28.600","Q79.201","K40.310","T28.701","E11.400x330+G99.0*","K56.600x001","K66.102","D36.700x014","K31.901","K90.406","S36.401","K45.804","K65.011","A03.900x008","K91.828","K43.900x001","Q43.803","K91.800x117","I85.901","D13.100","K43.605","K90.100x003","C15.800x003","K31.805","K36.x02","K56.500x003","K92.800x003","A09.005","Q43.200","K43.604","S36.601","I72.800x131","K52.102","K91.301","K91.805","Q85.900x036","K51.303","S36.910","A09.004","R93.300x001","K59.302","Q43.805","K31.803","A03.900x007","K58.100","K92.207","K63.215","B49.x17","Q45.801","A08.101","E11.400x350+G99.0*","K65.017","K66.810","D37.100x003","R19.300","C78.602","K31.609","A09.003","K91.835","R12.x00x002","K62.800x017","Q41.903","K65.901","Q51.702","K52.914","K57.101","A03.300x001","K40.100x001","S36.500x092","A05.202","K59.002","K66.101","K59.301","C18.100","K25.000x002","K91.817","Q40.206","K50.000","Q39.800x904","K55.011","K65.902","K40.101","Q43.001","S36.414","K21.900x003","K63.502","Q43.800x006","K92.200x005","A07.300x002","K22.400x003","K43.303","K22.811","C78.500x004","A52.710+K67.2*","K55.001","K65.016","K56.100","K21.903","C78.501","K65.002","R10.101","K66.802","Q42.200x902","Q42.000x501","K65.003","Q43.200x002","K91.839","K91.300x002","A00.900","K63.100x001","Q40.003","K40.200x001","C16.800x002","Q41.002","K22.807","K60.000","K29.605","K66.103","A07.800x002","D48.129","K58.801","K57.800x001","Q39.501","B82.901","K26.501","A04.100x001","K90.900x002","B37.805","I86.400x004","R15.x00","K22.204","K91.401","K91.200x002","A03.200x001","C15.300","K52.902","D12.300","D37.102","K57.201","K21.902","K27.100x001","K41.100x001","C78.503","B49.x16","C48.105","K20.x02","D37.400x001","C45.102","K55.100x006","K91.819","K57.500","K40.000x001","C20.x00","I74.800x011","K46.002","T18.300","D37.709","C76.304","K63.818","S36.802","K65.806","K29.701","K66.808","Q39.600","K22.814","A09.002","A18.812+K93.8*","D12.302","A04.801","K38.100","D37.200x001","D12.602","S36.611","K20.x00x006","K91.800x412","C16.001","C48.104","D48.400x003","R19.200x002","K63.203","K62.811","Q42.200x903","K57.002","D48.403","R19.500x004","K63.305","K46.900","A04.800x001","S36.400","K41.200x001","E85.417+K93.8*","Q41.202","A04.701","Q43.402","K92.205","K62.602","K22.801","Q43.300x901","K55.200x013","C77.106","C18.900","K20.x00","K90.200","K40.907","K22.401","K27.401","A09.007","C77.200x001","K31.903","K57.301","C15.000","C21.802","K25.401","Q40.207","D37.205","I89.800x019","K55.100","C79.809","K62.200","K56.604","A18.807+K23.0*","Q79.300","K52.101","A18.314+K67.3*","K43.601","K57.304","K55.000x015","Q85.906","C18.700","D12.000","K41.302","K50.900","Q39.100","K43.003","K46.901","K60.400","C15.802","Q43.800x008","C17.801","D37.404","T80.200x001","S36.404","K55.100x005","K63.815","K22.208","A18.307+K93.0*","K27.400","K63.501","K64.901","K50.000x001","Q42.002","D37.500x002","Q40.800","B49.x00x002","K62.816","Q39.100x021","C78.800x014","C21.800","K91.100x001","K31.821","K51.500","K91.816","R10.301","Q89.302","K91.803","K62.903","K62.817","K63.301","A08.000","A03.904","K91.810","K40.303","K29.501","Q43.900","R10.000x004","K29.300","D37.701","K46.001","S36.400x091","K62.814","D12.500","K46.900x004","K62.809","K92.209","C15.900","A09.900x006","Q39.100x011","Q42.903","K31.103","K63.200x008","C77.201","A04.802","K65.905","K22.102","K27.900x002","A09.903","K64.808","K65.015","K61.000","K25.902","K91.201","K45.808","A04.200x001","K31.100x002","K63.107","K60.100","K62.807","K62.800x021","Q40.203","I86.400x002","E73.900","K20.x03","T98.300x001","K52.904","C18.400","T18.500x004","Q43.301","K22.201","K56.101","S36.402","D37.407","K31.800x808","K28.100","K55.105","A18.300x009+K93.0*","E10.400x370+G99.0*","K22.800x003","K55.006","K31.600x004","K55.201","K28.600x001","K57.900x001","K91.303","K91.824","C78.804","D37.702","K22.900x001","S36.811","Q40.200x010","T18.801","A03.000x001","K92.210","K28.900x002","R19.100x002","K92.202","K31.806","A08.200","K27.500x005","K25.501","K28.000","K55.103","K66.100","K62.400x004","D01.301","K41.400x001","K60.400x003","E14.400x330+G99.0*","K57.000","D17.500","D48.700x005","D37.408","K38.900","S36.701","K29.603","K31.502","K90.400x003","Q43.802","K91.101","K52.919","K57.107","C18.900x001","K43.500","K64.807","C16.802","K52.203","B37.804","K29.100x001","K46.905","I72.815","C16.801","K90.802+M14.8*","K64.501","C15.800x001","K26.701","K91.800x501","K46.000","K46.900x012","K40.001","K22.700x001","K92.201","K59.100","K55.202","K51.000","K91.202","K40.900x005","K43.001","K55.009","D01.000","K43.004","K29.801","K31.602","K31.701","Q45.300x105","K46.101","C21.101","K62.301","S36.500","K63.207","K59.900x001","K63.816","A03.800x001","C78.400","K66.801","Q41.902","D18.012","D37.301","K22.207","C45.700x005","K43.900","K31.804","K31.819","K31.820","D37.300x001","A07.900x001","C20.x00x003","R14.x00x002","K56.701","K26.100","K63.803","K22.103","Q43.700","K65.014","C16.000x003","K45.801","C78.505","K45.800","D37.202","K55.007","Q43.901","D37.200x002","R10.400x002","K63.900x002","K91.800x106","K62.800x012","K44.900x001","Q39.200x011","D13.304","K65.009","R10.401","D18.100x001","A05.800","K60.401","A04.600x001","K59.303","K66.803","Q79.301","K50.000x005","K31.810","K52.908","T18.200","A54.807+K67.1*","S36.600x003","D01.200","C19.x00","K64.802","Q40.204","A00.900x003","Q39.801","K35.301","I89.800x006","D12.603","Q44.500x008","A18.308","Q79.501","Q42.101","D37.500x001","K31.607","K38.800x004","T28.702","I72.807","Q39.601","K91.804","A04.902","Q43.806","K29.600x007","K46.902","C78.502","C17.000","K63.102","C78.402","S36.700","K25.001","K90.000x001","K29.200","K90.402","K63.212","I89.005","K91.800x116","D00.200x003","A18.312+K93.0*","C17.900","D17.500x007","D37.501","I86.401","K62.300","K40.901","E16.400","K40.906","K62.801","K45.802","K22.101","I88.000x003","A04.800x006","K56.602","K25.900x001","K31.818","A04.400x004","K31.104","K40.315","D17.702","K91.300","I89.006","K43.100","D01.403","K59.003","K40.306","K63.105","K63.900x003","K56.300","K27.901","K63.308","S36.400x095","Q42.801","K27.400x002","K29.900","K90.401","K63.802","D13.200","A03.900x005","C18.001","A09.001","C26.800","K27.300","K62.400x003","K29.700","K30.x00","K31.500","D12.900x001","K63.807","K63.214","A04.901","K91.818","S36.600","K20.x00x001","D17.700x022","K29.700x002","Q41.103","K31.608","A05.100","R19.800x001","D37.405","K28.400x002","K52.204","R10.000","A05.200","K31.905","K91.100","S36.500x091","K62.812","K63.001","E73.000","Q43.000","K91.836","K56.700","Q89.300","C77.207","D17.700x017","K50.002","A18.800x014+K23.0*","K65.005","Q40.205","Q40.000","D20.100","Q43.800x018","R85.300","D36.700x019","D37.700x002","S36.800x022","C18.600","D13.900","K63.202","Q43.004","Q85.913","I86.400x001","D17.500x004","A05.400","D48.700x004","T18.300x003","K38.300","D13.101","Q79.500","A00.900x002","K31.801","A03.900","K91.834","C78.803","K28.300x001","K21.901","C78.800x005","K26.200x001","Q41.102","B49.x12","K52.801","C16.400","K62.819","K26.401","K61.400","K22.601","K66.000x007","C18.300","K46.100","S36.500x093","K65.010"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCG入组条件，匹配规则：主诊断匹配')

  result=GB1.group(record)
  if result:
    return result
  result=GB2.group(record)
  if result:
    return result
  result=GC1.group(record)
  if result:
    return result
  result=GC2.group(record)
  if result:
    return result
  result=GD1.group(record)
  if result:
    return result
  result=GD2.group(record)
  if result:
    return result
  result=GE1.group(record)
  if result:
    return result
  result=GE2.group(record)
  if result:
    return result
  result=GF1.group(record)
  if result:
    return result
  result=GF2.group(record)
  if result:
    return result
  result=GG1.group(record)
  if result:
    return result
  result=GJ1.group(record)
  if result:
    return result
  result=GK1.group(record)
  if result:
    return result
  result=GK2.group(record)
  if result:
    return result
  result=GK3.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合GQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'GQY'

  result=GR1.group(record)
  if result:
    return result

  result=GS1.group(record)
  if result:
    return result

  result=GT1.group(record)
  if result:
    return result

  result=GU1.group(record)
  if result:
    return result

  result=GU2.group(record)
  if result:
    return result

  result=GV1.group(record)
  if result:
    return result

  result=GW1.group(record)
  if result:
    return result

  result=GZ1.group(record)
  if result:
    return result

  message('不符合MDCG的ADRG入组条件')

