
#Variables 
VADPN = 18 #nominal adapter power voltage
VRST = 5 #voltage the RST pin will be connected to when reset is wanted.
ADPUVLO = 16.8 #voltage to switch off of adapter power at.
CTLT = 0.35 #voltage threshold below which LTC4412 turns on.
Imin = 3.5e-6 #minimum current threshold. This is because LTC4412 contains a current sink to turn the device on if CTL is floating

#Resistor values as numbered in the schematic

R2 = 10000 #common pulldown value
R5 = 10000 #common pulldown value

R1 = (R2*ADPUVLO/CTLT) - R2 #Minimum value R1 can take - based on UVLO for the adapter

R3 = VRST * (R1+R2) / VADPN #maximum value R3 can take - based on current 

R4 = (R5 * VRST / CTLT) - R5 #Maximum value R4 can take - based on VCTL needing to be at least 0.35V when restarting

print("Minimum value of R1 is {}".format(R1))
print("Maximum value of R3 is {}".format(R3))
print("Maximum value of R4 is {}".format(R4))