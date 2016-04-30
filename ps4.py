# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    finalPop1, finalPop2, finalPop3, finalPop4 = [], [], [], []

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(300):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')

    	for b in range(150):
    		pop = patient.update()

    	finalPop1.append(pop)

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(150):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')

    	for b in range(150):
    		pop = patient.update()

    	finalPop2.append(pop)

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(75):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')

    	for b in range(150):
    		pop = patient.update()

    	finalPop3.append(pop)

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	patient.addPrescription('guttagonol')
    	pop = 0

    	for b in range(150):
    		pop = patient.update()

    	finalPop4.append(pop)

    pylab.figure(1)
    pylab.hist(finalPop1, bins = 50)
    pylab.title('Delay of 300 timesteps')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

    pylab.figure(2)
    pylab.hist(finalPop2, bins = 50)
    pylab.title('Delay of 150 timesteps')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

    pylab.figure(3)
    pylab.hist(finalPop3, bins = 50)
    pylab.title('Delay of 75 timesteps')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

    pylab.figure(4)
    pylab.hist(finalPop4, bins = 50)
    pylab.title('No delay')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')
    pylab.show()

#simulationDelayedTreatment(100)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    finalPop1, finalPop2, finalPop3, finalPop4 = [], [], [], []

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(150):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')

    	for b in range(300):
    		pop = patient.update()

    	patient.addPrescription('grimpex')

    	for b in range(150):
    		pop = patient.update()

    	finalPop1.append(pop)

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(150):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')

    	for b in range(150):
    		pop = patient.update()

    	patient.addPrescription('grimpex')

    	for b in range(150):
    		pop = patient.update()

    	finalPop2.append(pop)

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(150):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')

    	for b in range(75):
    		pop = patient.update()

    	patient.addPrescription('grimpex')

    	for b in range(150):
    		pop = patient.update()

    	finalPop3.append(pop)

    for a in range(numTrials):
    	viruses = []

    	for b in range(100):
    		viruses.append(ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005))

    	patient = TreatedPatient(viruses, 1000)
    	pop = 0

    	for b in range(150):
    		pop = patient.update()

    	patient.addPrescription('guttagonol')
    	patient.addPrescription('grimpex')

    	for b in range(150):
    		pop = patient.update()

    	finalPop4.append(pop)

    pylab.figure(1)
    pylab.hist(finalPop1, bins = 50)
    pylab.title('Add the second drug after 300 timesteps')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

    pylab.figure(2)
    pylab.hist(finalPop2, bins = 50)
    pylab.title('Add the second drug after 150 timesteps')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

    pylab.figure(3)
    pylab.hist(finalPop3, bins = 50)
    pylab.title('Add the second drug after 75 timesteps')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')

    pylab.figure(4)
    pylab.hist(finalPop4, bins = 50)
    pylab.title('Add two drugs at the same time')
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')
    pylab.show()

simulationTwoDrugsDelayedTreatment(100)