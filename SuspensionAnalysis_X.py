# Author: Michael Keller
# Title: Suspension Analysis
# Interpreter: Python 3.7.6

# Imports 
import numpy as np

# Set Material Properties 
# Aluminum 6061
yieldstrenghtAl = 40000 #psi
# High-Strength 17-4 PH Stainless Steel
yieldstrenghtSteel = 145000

# Set Volume Properties 
thickness = 0.25 #inches 
width = 0.375 #inches 
totalLenght = 4.995 #inches 
matingLength = 4.620 #inches
holeDiamter = 0.140 #inches 
tiredeformation = (4.83 - 2)/2 #inches, can be ajusted, based on pepsi can 
numberOfArms = 4

# Assumptions
mass = 15 #lbs 
dropHeight = 10 #ft
deltaVelocity = np.sqrt(2*mass*dropHeight)
acceleration = 32.2 #ft/s 
safetyFactor = 2
stressConcentrationX = holeDiamter/width # = .56
stressConcentrationLine = holeDiamter/thickness # = .3733
stressConcentration = 1.95 #from fig 3 

# Calculations 
forceAverage = (mass*deltaVelocity**2)/(2*tiredeformation)
moment = forceAverage * matingLength
I = numberOfArms*(((width-holeDiamter)*thickness**3)/12)
sigma = safetyFactor*stressConcentration*moment*(thickness/2)/I

# Tests
print('Case 1: Only one wheel touches ground')
if sigma > yieldstrenghtAl:
    print('Aluminum 6061 fails')
elif sigma < yieldstrenghtAl:
    print('Aluminum 6061 Passes')
if sigma > yieldstrenghtSteel:
    print('High-Strength 17-4 PH Stainless Steel fails')
elif sigma < yieldstrenghtSteel:
    print('High-Strength 17-4 PH Stainless Steel Passes')

# Calculations
numberOfArms = 8
I = numberOfArms*(((width-holeDiamter)*thickness**3)/12)
sigma = safetyFactor*stressConcentration*moment*(thickness/2)/I

# Tests 
print('Case 2: Both wheels touch ground at same time')
if sigma > yieldstrenghtAl:
    print('Aluminum 6061 fails')
elif sigma < yieldstrenghtAl:
    print('Aluminum 6061 Passes')
if sigma > yieldstrenghtSteel:
    print('High-Strength 17-4 PH Stainless Steel fails')
elif sigma < yieldstrenghtSteel:
    print('High-Strength 17-4 PH Stainless Steel Passes')