import os
import subprocess
import sys
from pydicom.dataset import Dataset
import pydicom 

'''
This code creates a NETDICOM class which has many DICOM functions such as:
C-Echo as an SCU or SCP
C-Find as an SCU or SCP
C-Move as an SCU or SCP
C-Get as an SCU or SCP
C-Store as an SCU or SCP

These functionalities are based of of pynetdicom3's following apps:
echoscp.py
echoscu.py
findscp.py
findscu.py
getscp.py
getscu.py
movescp.py
movescu.py
storescp.py
storescu.py

Each function uses the corresponding file(ex. echoscp uses echoscp.py) so the 
proper path to the file must be specified in the function definition

'''
class AppUsage:
    
    def runfile(cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, \
                                   stderr=subprocess.STDOUT)
        while True:
            nextline = process.stdout.readline()
            if nextline == '' and process.poll() is not None:
                break
            sys.stdout.write(nextline)
            sys.stdout.flush()

        output = process.communicate()[0]
        exitCode = process.returncode

        if (exitCode == 0):
            return output
  
    def echoscp(title='PYNETDICOM',port=11113):
        ''' 
        Creates a DICOM AE SCP which listens and responds to echos based upon
        the pynetdicom3 echoscp.py app
        Uses C-Echo
        Usage:
            echoscp(title,port)
            title: is the AE title which may be needed for associations
                    the default name is PYNETDICOM
            port: is the port the scp will listen on
                    the default port is 11113
            echoscp may be called as echoscp() to use default title and port
        '''
        path = os.path.abspath('pynetdicom3')+'/apps/echoscp/echoscp.py'
        cmd = path +' -aet '+'['+title+'] '+str(port)+' -d' 
        AppUsage.runfile(cmd)                     

        
    def echoscu(address='address', title='PYNETDICOM',port=11114):
        ''' 
        Creates a DICOM AE SCU which sends an echo based upon
        the pynetdicom3 echoscu.py app
        Uses C-Echo
        Usage:
            echoscp(address,title,port)
            address: is the address of the AE which you wish to connect
            title: is the AE title which may be needed for associations
                    the set name is PYNETDICOM
            port: is the port the scu will listen on
                    the default port is 11114
            echoscu may be called as echoscu() to use defaults
        '''
        path = os.path.abspath('pynetdicom3')+'/apps/echoscu/echoscu.py'
        cmd = path+' '+address+' -aet '+'['+title+'] '+str(port)+' -d' 

        AppUsage.runfile(cmd)
        
    def findscp(title='PYNETDICOM',port=11115):
        #Will need to set query location in findscp.py
        #may need to edit the way it queries
        ''' 
        Creates a DICOM AE SCP which retrieves and sends data after being quieried
        by a scu AE, and is based on the pynetdicom3 findscp.py app
        Uses C-Find
        Usage:
            echoscp(title,port)
            title: is the AE title which may be needed for associations
                    the default name is PYNETDICOM
            port: is the port the scp will listen on
                    the default port is 11115
            findscp may be called as findscp() to use defaults
        '''
        path = os.path.abspath('pynetdicom3')+'apps/findscp/findscp.py'
        cmd = path +' -aet '+'['+title+'] '+str(port)+' -d' 
                              
        AppUsage.runfile(cmd)
        
    def findscu(name='',ID='',dataset='dataset.dcm',address='address',\
                title='PYNETDICOM',port=11110,\
                model='-P'):

        ''' 
        Creates a DICOM AE SCU which sends a query request based upon
        the pynetdicom3 findscu.py app
        This version only queries the patient level if you do not use a dataset
        Uses C-Find
        Usage:
            findscu(name,ID,dataset,address,title,port,model)
            name: patient name. 
                  If you wish to search by patient name and ID then
                  use findscu(name='name',ID='id').
            ID: patient ID.
                If you wish to search by patient name and ID then
                use findscu(name,ID).
            dataset: dicom file .dcm .
                If you wish to search by a dataset then use 
                findscu(dataset='data.dcm')
            address: is the address of the AE which you wish to connect
            title: is the AE title which may be needed for associations
                    the set name is PYNETDICOM
            port: is the port the scu will listen on
                    the default port is 11110
            model: this is the query model.
                    '-P' will be the patient model
                    '-W' worklist model
                    '-S' study model
        '''
        if dataset == 'dataset.dcm':
            data = pydicom.read_file('dataset.dcm')
            data.PatientsName = name 
            data.PatientID = ID
            data.QueryRetrieveLevel = 'PATIENT'
            data.save_as('dataset.dcm')
            
        path = os.path.abspath('pynetdicom3')+'apps/findscu/findscu.py'
        cmd=path+' '+address+' -aet '+'['+title+'] '+str(port)+' '+dataset+' -d'
                                       
        AppUsage.runfile(cmd)
     
    def getscp(title='PYNETDICOM',port=11115):
        #Will need to set get location in findscp.py
        #may need to edit the way it gets
        ''' 
        Creates a DICOM AE SCP which sends data after being asked
        by a scu AE, and is based on the pynetdicom3 getscp.py app
        Uses C-Get
        Usage:
            getscp(title,port)
            title: is the AE title which may be needed for associations
                    the default name is PYNETDICOM
            port: is the port the scp will listen on
                    the default port is 11115
            getscp may be called as getscp() to use defaults
        '''
        path = os.path.abspath('pynetdicom3')+'/apps/getscp/getscp.py'
        cmd = path +' -aet '+'['+title+'] '+str(port)+' -d' 
                              
        AppUsage.runfile(cmd)
        
    def getscu(name='',ID='',dataset='dataset.dcm',address='address',\
                title='PYNETDICOM',port=11119,\
                model='-P'):
        #may need to edit the place the scu stores the data
        ''' 
        Creates a DICOM AE SCU which sends a get request based upon
        the pynetdicom3 getscu.py app
        This version only queries the patient level if you do not use a dataset
        Uses C-Get
        Usage:
            findscu(name,ID,dataset,address,title,port,model)
            name: patient name. 
                  If you wish to search by patient name and ID then
                  use findscu(name='name',ID='id').
            ID: patient ID.
                If you wish to search by patient name and ID then
                use findscu(name,ID).
            dataset: dicom file .dcm .
                If you wish to search by a dataset then use 
                findscu(dataset='data.dcm')
            address: is the address of the AE which you wish to connect
            title: is the AE title which may be needed for associations
                    the set name is PYNETDICOM
            port: is the port the scu will listen on
                    the default port is 11119
            model: this is the query model.
                    '-P' will be the patient model
                    '-W' worklist model
                    '-S' study model
        '''
        if dataset == 'dataset.dcm':
            data = pydicom.read_file('dataset.dcm')
            data.PatientsName = name 
            data.PatientID = ID
            data.QueryRetrieveLevel = 'PATIENT'
            data.save_as('dataset.dcm')
            
        path = os.path.abspath('pynetdicom3')+'/apps/getscu/getscu.py'
        cmd=path+' '+address+' -aet '+'['+title+'] '+str(port)+' '+dataset+' -d'
        
        AppUsage.runfile(cmd)
        
    def movescp(title='PYNETDICOM',port=11101):
        #Will need to set move location in findscp.py
        #may need to edit the way it moves
        ''' 
        Creates a DICOM AE SCP which sends data after being asked
        by a scu AE, and is based on the pynetdicom3 movescp.py app
        Uses C-Move
        Usage:
            getscp(title,port)
            title: is the AE title which may be needed for associations
                    the default name is PYNETDICOM
            port: is the port the scp will listen on
                    the default port is 11101
            movescp may be called as movescp() to use defaults
        '''
        ''' 
        Creates a DICOM AE SCP which sends data after being asked
        by a scu AE, and is based on the pynetdicom3 getscp.py app
        Uses C-Get
        Usage:
            getscp(title,port)
            title: is the AE title which may be needed for associations
                    the default name is PYNETDICOM
            port: is the port the scp will listen on
                    the default port is 11115
            getscp may be called as getscp() to use defaults
        '''
        path = os.path.abspath('pynetdicom3')+'/apps/movescp/movescp.py'
        cmd = path +' -aet '+'['+title+'] '+str(port)+' -d'
                              
        AppUsage.runfile(cmd)
        
    def movescu(name='',ID='',dataset='dataset.dcm',address='address',\
                title='PYNETDICOM',port=11103,\
                model='-P',other_ae=''):
        #Does not move to other AE yet
        #may need to edit the place the scu stores the data

        ''' 
        Creates a DICOM AE SCU which sends a move request based upon
        the pynetdicom3 movescu.py app
        This version only queries the patient level if you do not use a dataset
        Uses C-Move
        Usage:
            findscu(name,ID,dataset,address,title,port,model)
            name: patient name. 
                  If you wish to search by patient name and ID then
                  use findscu(name,ID).
            ID: patient ID.
                If you wish to search by patient name and ID then
                use findscu(name,ID).
            dataset: dicom file .dcm .
                If you wish to search by a dataset then use 
                findscu(dataset='data.dcm')
            address: is the address of the AE which you wish to connect
            title: is the AE title which may be needed for associations
                    the set name is PYNETDICOM
            port: is the port the scu will listen on
                    the default port is 11103
            model: this is the query model.
                    '-P' will be the patient model
                    '-S' study model
            other_ae: this is the address of the second ae if you with to move
                        the files there
        '''
        if dataset == 'dataset.dcm':
            data = pydicom.read_file('dataset.dcm')
            data.PatientsName = name 
            data.PatientID = ID
            data.QueryRetrieveLevel = 'PATIENT'
            data.save_as('dataset.dcm')
            
        path = os.path.abspath('pynetdicom3')+'/apps/movescu/movescu.py'
        cmd=path+' '+address+' -aet '+'['+title+'] '+str(port)+' '+dataset+' -d' 
                                       
        AppUsage.runfile(cmd)
        
    def storescp(title='PYNETDICOM',port=11102):
        #Will need to set store location in findscp.py
        #may need to edit the way it stores
        ''' 
        Creates a DICOM AE SCP which sends data after being asked
        by a scu AE, and is based on the pynetdicom3 storescp.py app
        Uses C-Get
        Usage:
            getscp(title,port)
            title: is the AE title which may be needed for associations
                    the default name is PYNETDICOM
            port: is the port the scp will listen on
                    the default port is 11102
            getscp may be called as getscp() to use defaults
        '''
        path = os.path.abspath('pynetdicom3')+'/apps/storescp/storescp.py'
        cmd = path +' -aet '+'['+title+'] '+str(port)+' -d' 
                              
        AppUsage.runfile(cmd)
        
    def storescu(dataset,address='address',\
                title='PYNETDICOM',port=11103):
        #may need to edit the place the scu stores the data

        ''' 
        Creates a DICOM AE SCU which sends a store request based upon
        the pynetdicom3 movescu.py app
        This version only queries the patient level if you do not use a dataset
        Uses C-Get
        Usage:
            findscu(name,ID,dataset,address,title,port,model)
            dataset: dicom file .dcm .
            address: is the address of the AE which you wish to connect
            title: is the AE title which may be needed for associations
                    the set name is PYNETDICOM
            port: is the port the scu will listen on
                    the default port is 11103
        '''            
        path = os.path.abspath('pynetdicom3')+'/apps/storescu/storescu.py'
        cmd=path+' '+address+' -aet '+'['+title+'] '+str(port)+' '+dataset+' -d'
                                       
        AppUsage.runfile(cmd)
          