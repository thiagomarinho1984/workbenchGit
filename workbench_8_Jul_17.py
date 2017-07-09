__author__ = 'thiagomarinho'

import numpy as np
import pickle as pkl
import math,os,glob

#TODO: INTEGRATE with DJANGO


#===================================================================================================
#======================================000 - NAVAL ARCH=============================================
#===================================================================================================



class DESIGNER_000:
    def __init__(self):
       pass

    #===================================================================================================
    #======================================010 - SEAKEEPING=============================================
    #===================================================================================================

    def CalculateRao(self,wi,wf,N,obj_HULL,units=[],obj_RF=[]):
        #Calculate RAO as function of wave freq.
        pass

    def ResponseSpectrum(self,units=[],obj_RF=[]):
        #Calculate Rigid Body Response Spectrum for a given wave spectrum
        pass

    def DynamicSim(self,units=[],obj_RF=[]):
        #Integrate the motion ODE to calculate states and control trajectories
        pass

    def ForceGradients(self,units=[],obj_RF=[]):
        #Calculate 6DoF Force Gradient as function of state and control vector
        pass

    def NaturalPeriod(self,units=[],obj_RF=[]):
        #Estimates Nrigid Body Natural Period
        pass

    def ExtremeValues(self):
        #Returns a Weibull distribution of maxima and minima
        pass

    #===================================================================================================
    #======================================020 - STABILITY==============================================
    #===================================================================================================

    def StaticEquilibrium(self,units=[]):
        #Calculate the state and controil vector equilibrium position
        pass

    def TankSounding(self,units=[],obj_RF=[]):
        #Calculate tank sounding table
        pass

    def CrossCurves(self,units=[]):
        #Calculate cross curves table
        pass

    def AnimateTrajectory(self,units=[]):
        #Create a blender animation from trajectory vector
        #TODO: Evaluate move to BLENDER API
        pass

    def AssignLoading(self,units=[]):
        #Create Loading Conditions
        pass

    def StaticStability(self,obj_RIGID_BODY,obj_HULL,obj_RULES,units=[]):
        #Calculate GZ curve, Check against criteria
        pass








    #===================================================================================================
    #======================================030 - STATION KEEPPING=======================================
    #===================================================================================================

    #===================================================================================================
    #======================================040 - WEIGHT AND BOUYANCY====================================
    #===================================================================================================
    def GetMassProp(self,obj_RIGID_BODY):
        #Calculates summarized mass properties for RigidBody
        pass

    def GenerateWeightSheet(self,obj_VESSEL):
        #Iterates through low level list of rigid body for mass properties
        #TODO: Write Workflow
        pass

    def GetItemList(self,obj_VESSEL):
        #Returns BOM List within specified location range
        #TODO: WRITE WORKFLOW
        pass

    def WeightAudit(self,obj_VESSEL):
        #User inputs measured items position and mass to update weightsheet
        #TODO: WRITE WORKFLOW
        pass

    def SpecifiedCondition(self,type,input_vector):
        #input vector = Draft marks, or attitude and mean draft or mass
        pass

    def IncliningTest(self,obj_TEST_INCLINING):
        #Provides hydrostatic properties for specified condition
        #Estimate vessel mass properties from Inclining test data
        pass

    def UprightHydrostatic(self,obj_VESSEL_HULL, Draft_i, Draft_f):
        #Hydrostatic properties for a range of draft
        pass

    def MeasureCG(self):
        #Estimate CoG position from load cell measurements
        pass

    #===================================================================================================
    #======================================050 - SOLIDWORKS API=========================================
    #===================================================================================================

    #TODO: Create a separate G-Number for APIS

    def DrawWing(self,obj_VESSEL_WING):
        #Creates a SW drawing of wings
        pass

    def DrawHull(self,obj_VESSEL_HULL):
        #Creates a SW drawing of Hull
        pass

    def DrawStructure(self,obj_VESSEL_STRUCTURE):
        #Creates a SW drawing of Structure
        #REFERENCE FILE: (MARCUS THESIS REQUIREMENTS)
        pass


    def MeasureWing(self,SwFilePath):
        #Creates a python object of a wing
        pass

    def MeasureHull(self,SwFilePath):
        #Creates a python object of a Hull
        pass

    def MeasureStructure(self,SwFilePath):
        #Creates a python object of a Structure
        pass

    #===================================================================================================
    #======================================050 - OPENFOAM API==========================================
    #===================================================================================================

    #===================================================================================================
    #======================================050 - MAXSURF API============================================
    #===================================================================================================

    #===================================================================================================
    #======================================050 - OFFICE API=============================================
    #===================================================================================================


#===================================================================================================
#======================================DESIGNER OBJECT==============================================
#===================================================================================================

# KEEP AT END OF CODE FOR DICTIONARY DEFINITIONS

class REPORTER:
    def __init__(self,obj_design,path=''):
        self.DESIGN=obj_design
        if path =='':
            #TODO: Ask Filename UI - tkinter
            pass
        else:
            self.savePath=path
        #TODO: UI to choose file
        str = '0 - Weight Estimate; 1 - Propulsion Performance; ie: 0'
        cmd = input('Choose report to produce: ' + str)
        #TODO: automate if statements in functions connected to the analysis database
        if cmd == '0' or '':
            pass
        elif cmd == '1':
            str = '0 - Hull Resistance to Advance; 1 - Propeller kT, kQ, J; 2 - HullProp Curve; 3 - MotorHullProp Curve; \n 4 - Burril Diagram; 5 - Range; 6 - Autonomy; 7 - Towing Force; ie [1, 2, 5]'
            cmd = input('Choose output products desired: ' + str)
            cmd2 = list(cmd)

            # TODO: CASE dict for check methods
            # # define the function blocks
            # def zero():
            #     print "You typed zero.\n"
            #
            # def sqr():
            #     print "n is a perfect square\n"
            #
            # def even():
            #     print "n is an even number\n"
            #
            # def prime():
            #     print "n is a prime number\n"
            #
            # # map the inputs to the function blocks
            # options = {0: zero,
            #            1: sqr,
            #            4: sqr,
            #            9: sqr,
            #            2: even,
            #            3: prime,
            #            5: prime,
            #            7: prime,
            #            }

    def ExportTable(self):
        #Exports an array, with header to excel or csv file
        pass

    #TODO: Copy from master thesis
    def plot(self):
        pass

    def plotComp(self):
        pass
