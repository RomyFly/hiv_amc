#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                   STOCKOUT RATE
#___________________________________________________________________________________________________________________________________________________________________________________

#                                                   This app allow to calculate the stockout rate of PEPFAR health facilities

#                                                   import libraries
import pandas as pd
import matplotlib.pyplot as plt 

ad=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Adamawa.xls')
ce=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Centre.xls')
es=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Est.xls')
en=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Extrême-Nord.xls')
lt=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Littoral.xls')
no=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Nord.xls')
nw=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Nord-Ouest.xls')
ou=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Ouest.xls')
su=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Sud.xls')
sw=pd.read_excel('C:/Users/rndzana/Documents/my_git_repositories/HIV analysis/stockout rate/Sud-Ouest.xls')

lst=ad.columns.tolist()
print(ad)
