# -*- coding: utf-8 -*-

import irsdk

class iRData(object):
    ir = irsdk.IRSDK()
    ir.startup()#test_file='./data/datavuelta4.bin')
    playerID = 0
    trackID = 0
    trackName = 0
    trackCountry = 0
    trackCity = 0
    trackLength = 0
    trackVariante = 0
    carID = 0
    carName = 0
    seriesID = 0
    totalLaps = 0
    maxIncidents = 0
    myIncidents = 0
    sessions = 0
    lap = 0
    fuelLevel = 0
    estLap = 0
    def reloadData():
        iRData.playerID = iRData.ir['PlayerCarIdx']
        iRData.trackID = iRData.ir['WeekendInfo']['TrackID']
        iRData.trackName = iRData.ir['WeekendInfo']['TrackDisplayName']
        iRData.trackCountry = iRData.ir['WeekendInfo']['TrackCountry']
        iRData.trackCity = iRData.ir['WeekendInfo']['TrackCity']
        iRData.trackLength = iRData.ir['WeekendInfo']['TrackLengthOfficial']
        iRData.trackVariante = iRData.ir['WeekendInfo']['TrackConfigName']
        iRData.carID = iRData.ir['DriverInfo']['Drivers'][iRData.playerID]['CarID']
        iRData.carName = iRData.ir['DriverInfo']['Drivers'][iRData.playerID]['CarScreenName']
        if iRData.ir['WeekendInfo']['SeriesID']:
            iRData.seriesID = iRData.ir['WeekendInfo']['SeriesID']
        else:
            iRData.seriesID = 0
        iRData.totalLaps = iRData.ir['SessionInfo']['Sessions'][0]['SessionLaps']
        iRData.maxIncidents = iRData.ir['WeekendInfo']['WeekendOptions']['IncidentLimit']
        iRData.myIncidents = iRData.ir['PlayerCarMyIncidentCount']
        iRData.sessions = iRData.ir['SessionInfo']['Sessions']
        iRData.lap = iRData.ir['Lap']
        iRData.fuelLevel = iRData.ir['FuelLevel']
        iRData.estLap = iRData.ir['DriverInfo']['Drivers'][iRData.playerID]['CarClassEstLapTime'] 

    
    
    def getSesion():
        if len(iRData.sessions) == 3:
            return 2
        elif len(iRData.sessions) == 2:
            return 1
        elif len(iRData.sessions) == 1:
            return 0
    
    def getSesionLaps(self):
        return iRData.ir['SessionInfo']['Sessions'][iRData.getSesion()]['SessionLaps']

    def getParticipantes(self):
        return iRData.ir['SessionInfo']['Sessions'][iRData.getSesion()]['ResultsPositions']
    
if __name__ == "__main__":
    data = iRData()  # Crear una instancia de la clase iRData
    data.reloadData()  # Llamar al método reloadData() utilizando la instancia creada
