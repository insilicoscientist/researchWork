#!/usr/bin/env python
import csv
import matplotlib.pyplot as plt
from pylab import *
from numpy import *
from matplotlib.font_manager import fontManager, FontProperties
from matplotlib.backends.backend_pdf import PdfPages

#Custom image size | Overrides matplotlibrc default values
import matplotlib as mpl
#mpl.rcParams['figure.figsize'] = '2, 24'
mpl.rcParams['grid.color'] = 'grey'
mpl.rcParams['figure.figsize'] = '1.5,36'
mpl.rcParams['font.size'] = '3.5'
mpl.rcParams['axes.linewidth'] = '0.5'


#####################################Global.Code.Header###############################################

#!/usr/bin/python
################################plot23-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#23, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_2BDW-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_2BDW-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_2BDW-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax23 = plt.subplot(24,1,23)

#Plot x,y as steps with custom mark, color, line width
ax23.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax23.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax23.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax23.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax23.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax23.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax23.get_xticklabels(), visible=False)
#plt.setp(ax23.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '2BDW, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax23.text(0.6, 0.2, textstr, transform=ax23.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot23-ends-here###########################################################

#!/usr/bin/python
################################plot19-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#19, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_2HAK-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_2HAK-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_2HAK-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax19 = plt.subplot(24,1,19)

#Plot x,y as steps with custom mark, color, line width
ax19.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax19.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax19.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax19.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax19.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax19.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax19.get_xticklabels(), visible=False)
#plt.setp(ax19.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '2HAK, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax19.text(0.6, 0.2, textstr, transform=ax19.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot19-ends-here###########################################################

#!/usr/bin/python
################################plot17-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#17, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_2QNJ-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_2QNJ-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_2QNJ-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax17 = plt.subplot(24,1,17)

#Plot x,y as steps with custom mark, color, line width
ax17.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax17.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax17.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax17.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax17.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax17.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax17.get_xticklabels(), visible=False)
#plt.setp(ax17.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '2QNJ, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax17.text(0.6, 0.2, textstr, transform=ax17.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot17-ends-here###########################################################

#!/usr/bin/python
################################plot18-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#18, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_3FE3-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_3FE3-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_3FE3-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax18 = plt.subplot(24,1,18)

#Plot x,y as steps with custom mark, color, line width
ax18.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax18.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax18.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax18.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax18.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax18.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax18.get_xticklabels(), visible=False)
#plt.setp(ax18.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '3FE3, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax18.text(0.6, 0.2, textstr, transform=ax18.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot18-ends-here###########################################################

#!/usr/bin/python
################################plot20-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#20, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_3I79-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_3I79-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_3I79-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax20 = plt.subplot(24,1,20)

#Plot x,y as steps with custom mark, color, line width
ax20.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax20.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax20.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax20.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax20.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax20.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax20.get_xticklabels(), visible=False)
#plt.setp(ax20.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '3I79, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax20.text(0.6, 0.2, textstr, transform=ax20.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot20-ends-here###########################################################

#!/usr/bin/python
################################plot22-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#22, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_3KK8-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_3KK8-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_3KK8-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax22 = plt.subplot(24,1,22)

#Plot x,y as steps with custom mark, color, line width
ax22.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax22.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax22.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax22.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax22.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax22.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax22.get_xticklabels(), visible=False)
#plt.setp(ax22.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '3KK8, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax22.text(0.6, 0.2, textstr, transform=ax22.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot22-ends-here###########################################################

#!/usr/bin/python
################################plot21-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#21, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_3KK9-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_3KK9-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_3KK9-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax21 = plt.subplot(24,1,21)

#Plot x,y as steps with custom mark, color, line width
ax21.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax21.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax21.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax21.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax21.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax21.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax21.get_xticklabels(), visible=False)
#plt.setp(ax21.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '3KK9, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax21.text(0.6, 0.2, textstr, transform=ax21.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot21-ends-here###########################################################

#!/usr/bin/python
################################plot9-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#9, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_537-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_537-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_537-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax9 = plt.subplot(24,1,9)

#Plot x,y as steps with custom mark, color, line width
ax9.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax9.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax9.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax9.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax9.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax9.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax9.get_xticklabels(), visible=False)
#plt.setp(ax9.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = '537, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax9.text(0.6, 0.2, textstr, transform=ax9.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot9-ends-here###########################################################

#!/usr/bin/python
################################plot24-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#24, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_Apo-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_Apo-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_Apo-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax24 = plt.subplot(24,1,24)

#Plot x,y as steps with custom mark, color, line width
ax24.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax24.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax24.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax24.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax24.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax24.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax24.get_xticklabels(), visible=False)
#plt.setp(ax24.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'Apo, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax24.text(0.6, 0.2, textstr, transform=ax24.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot24-ends-here###########################################################

#!/usr/bin/python
################################plot16-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#16, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_ATP-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_ATP-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_ATP-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax16 = plt.subplot(24,1,16)

#Plot x,y as steps with custom mark, color, line width
ax16.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax16.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax16.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax16.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax16.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax16.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax16.get_xticklabels(), visible=False)
#plt.setp(ax16.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'ATP, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax16.text(0.6, 0.2, textstr, transform=ax16.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot16-ends-here###########################################################

#!/usr/bin/python
################################plot12-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#12, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_ATU-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_ATU-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_ATU-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax12 = plt.subplot(24,1,12)

#Plot x,y as steps with custom mark, color, line width
ax12.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax12.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax12.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax12.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax12.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax12.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax12.get_xticklabels(), visible=False)
#plt.setp(ax12.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'ATU, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax12.text(0.6, 0.2, textstr, transform=ax12.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot12-ends-here###########################################################

#!/usr/bin/python
################################plot3-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#3, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_B49-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_B49-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_B49-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax3 = plt.subplot(24,1,3)

#Plot x,y as steps with custom mark, color, line width
ax3.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax3.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax3.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax3.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax3.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax3.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax3.get_xticklabels(), visible=False)
#plt.setp(ax3.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'B49, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax3.text(0.6, 0.2, textstr, transform=ax3.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot3-ends-here###########################################################

#!/usr/bin/python
################################plot5-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#5, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_DRN-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_DRN-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_DRN-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax5 = plt.subplot(24,1,5)

#Plot x,y as steps with custom mark, color, line width
ax5.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax5.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax5.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax5.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax5.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax5.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax5.get_xticklabels(), visible=False)
#plt.setp(ax5.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'DRN, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax5.text(0.6, 0.2, textstr, transform=ax5.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot5-ends-here###########################################################

#!/usr/bin/python
################################plot10-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#10, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_IQB-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_IQB-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_IQB-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax10 = plt.subplot(24,1,10)

#Plot x,y as steps with custom mark, color, line width
ax10.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax10.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax10.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax10.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax10.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax10.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax10.get_xticklabels(), visible=False)
#plt.setp(ax10.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'IQB, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax10.text(0.6, 0.2, textstr, transform=ax10.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot10-ends-here###########################################################

#!/usr/bin/python
################################plot6-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#6, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_L20-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_L20-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_L20-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax6 = plt.subplot(24,1,6)

#Plot x,y as steps with custom mark, color, line width
ax6.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax6.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax6.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax6.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax6.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax6.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax6.get_xticklabels(), visible=False)
#plt.setp(ax6.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'L20, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax6.text(0.6, 0.2, textstr, transform=ax6.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot6-ends-here###########################################################

#!/usr/bin/python
################################plot13-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#13, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_LI8-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_LI8-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_LI8-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax13 = plt.subplot(24,1,13)

#Plot x,y as steps with custom mark, color, line width
ax13.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax13.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax13.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax13.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax13.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax13.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax13.get_xticklabels(), visible=False)
#plt.setp(ax13.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'LI8, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax13.text(0.6, 0.2, textstr, transform=ax13.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot13-ends-here###########################################################

#!/usr/bin/python
################################plot15-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#15, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_PP1-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_PP1-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_PP1-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax15 = plt.subplot(24,1,15)

#Plot x,y as steps with custom mark, color, line width
ax15.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax15.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax15.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax15.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax15.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax15.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax15.get_xticklabels(), visible=False)
#plt.setp(ax15.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'PP1, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax15.text(0.6, 0.2, textstr, transform=ax15.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot15-ends-here###########################################################

#!/usr/bin/python
################################plot14-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#14, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_PP2-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_PP2-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_PP2-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax14 = plt.subplot(24,1,14)

#Plot x,y as steps with custom mark, color, line width
ax14.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax14.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax14.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax14.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax14.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax14.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax14.get_xticklabels(), visible=False)
#plt.setp(ax14.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'PP2, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax14.text(0.6, 0.2, textstr, transform=ax14.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot14-ends-here###########################################################

#!/usr/bin/python
################################plot7-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#7, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_PVB-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_PVB-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_PVB-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax7 = plt.subplot(24,1,7)

#Plot x,y as steps with custom mark, color, line width
ax7.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax7.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax7.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax7.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax7.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax7.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax7.get_xticklabels(), visible=False)
#plt.setp(ax7.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'PVB, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax7.text(0.6, 0.2, textstr, transform=ax7.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot7-ends-here###########################################################

#!/usr/bin/python
################################plot11-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#11, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_STI-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_STI-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_STI-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax11 = plt.subplot(24,1,11)

#Plot x,y as steps with custom mark, color, line width
ax11.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax11.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax11.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax11.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax11.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax11.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax11.get_xticklabels(), visible=False)
#plt.setp(ax11.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'STI, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax11.text(0.6, 0.2, textstr, transform=ax11.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot11-ends-here###########################################################

#!/usr/bin/python
################################plot1-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#1, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_STU-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_STU-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_STU-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax1 = plt.subplot(24,1,1)

#Plot x,y as steps with custom mark, color, line width
ax1.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax1.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax1.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax1.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax1.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax1.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax1.get_xticklabels(), visible=False)
#plt.setp(ax1.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'STU, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax1.text(0.6, 0.2, textstr, transform=ax1.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot1-ends-here###########################################################

#!/usr/bin/python
################################plot8-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#8, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_TAK-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_TAK-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_TAK-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax8 = plt.subplot(24,1,8)

#Plot x,y as steps with custom mark, color, line width
ax8.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax8.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax8.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax8.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax8.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax8.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax8.get_xticklabels(), visible=False)
#plt.setp(ax8.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'TAK, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax8.text(0.6, 0.2, textstr, transform=ax8.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot8-ends-here###########################################################

#!/usr/bin/python
################################plot4-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#4, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_UCN-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_UCN-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_UCN-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax4 = plt.subplot(24,1,4)

#Plot x,y as steps with custom mark, color, line width
ax4.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax4.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax4.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax4.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax4.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax4.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax4.get_xticklabels(), visible=False)
#plt.setp(ax4.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'UCN, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax4.text(0.6, 0.2, textstr, transform=ax4.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot4-ends-here###########################################################

#!/usr/bin/python
################################plot2-begins-here################################################ 
#Dynamic Code variables: Will be assigned dynamically during the 'for' loop;
#VAR_CODE, 
#2, 

##Variables to be assigned here
#INA='SCH'
#1=1
#24=24

##VS job identification
#en_r_vsw-01='en_r_vsw-01-02'


#Data for the plot is read from several CSV files, x and y axex are read from first and 2nd column
x1,x2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_XP_VX6-data-ROC.csv'))
for line in csv_reader:
  x1.append(float(line[0]))
  x2.append(float(line[1]))

s1,s2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_SP_VX6-data-ROC.csv'))
for line in csv_reader:
  s1.append(float(line[0]))
  s2.append(float(line[1]))

h1,h2 = [],[]
csv_reader = csv.reader(open('en_r_vsw-01_HTVS_VX6-data-ROC.csv'))
for line in csv_reader:
  h1.append(float(line[0]))
  h2.append(float(line[1]))

r1,r2 = [],[]
csv_reader = csv.reader(open('ROC-random.csv'))
for line in csv_reader:
  r1.append(float(line[0]))
  r2.append(float(line[1]))

#Assign the subplot area; 8,2,3 means 24 rows x 2 columns plot and 3rd image
#This will plot on different spaces in the same figure location
ax2 = plt.subplot(24,1,2)

#Plot x,y as steps with custom mark, color, line width
ax2.plot(x1,x2,'-',linestyle='steps',color='blue',lw=0.5)
ax2.plot(s1,s2,'-',linestyle='steps',color='black',lw=0.5)
ax2.plot(h1,h2,'-',linestyle='steps',color='orange',lw=0.5)
ax2.plot(r1,r2,'-',color='grey',lw=0.25)


##Font property for the labels
#font = FontProperties(size=6)


#Add legend to the image at specifoed position
#ax2.legend(['XP','SP','HTVS','Best','Random','Worst'],2,prop=font)
#ax2.legend(['XP','SP','HTVS'],2,prop=font)

#Draw dotted grid
grid(True)

##Now set title and X/Y labels
#plt.title("TITLE")
#plt.xlabel("1-Specificity")
#plt.ylabel("Sensitivity")

##Set the x and y axis dotted grid ticks, from 0 till 110, every 20 interval 
#plt.xticks(range(0,110,10))
#plt.yticks(range(0,110,20))

#Set the range of X and Y values to be displayed in the plot
#plt.xlim([0.1,101])
#plt.ylim([3.3,100])

##Turn off tick labels
#plt.setp(ax2.get_xticklabels(), visible=False)
#plt.setp(ax2.get_yticklabels(), visible=False)

#Place a text box in upper left in axes coords
textstr = 'VX6, INA' 
#Style and poperties: These are matplotlib.patch.Patch properies
props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
ax2.text(0.6, 0.2, textstr, transform=ax2.transAxes, fontsize=5,
  horizontalalignment='left', verticalalignment='bottom', bbox=props)
 
################################plot2-ends-here###########################################################


####################################Global.Code.Footer################################################

#Save image
imagename = 'en_r_vsw-01-image.png'
#savefig(imagename)
#savefig(imagename,figsize=(16,4))
dpival = 300
savefig(imagename,dpi=dpival)
#savefig(imagename,figsize=(15,10),dpi=dpival)


##Turn off x ticklabels for all but the lower axes
#for ax in ax1, ax2, ax3:
  #setp(ax.get_xticklabels(), visible=False)
  

#width = 3
#height = 10
#plt.figure(figsize=(width, height))
#plt.savefig("figure.png")

#Save figure
#figprops = dict(figsize=(8., 8. / 1.618))                                          # Figure properties
#adjustprops = dict(left=0.1, bottom=0.1, right=0.97, top=0.93, wspace=0.2)       # Subplot properties
#plt.savefig('en_r_vsw-01-image.png',**figprops)
#ax1.subplots_adjust(**adjustprops)
#Tunes the subplot layout

##Save as PDF
#pp = PdfPages('multipage.pdf')
#savefig(pp, format='pdf')
#pp.savefig()
#pp.close()


#Show plot image in a window
#plt.show()

close()