import irsdk

class iRData(object):
    ir = irsdk.IRSDK()
    ir.startup(test_file='datavuelta6.bin')
    if ir.is_connected:
        playerID = ir['PlayerCarIdx']
        trackID = ir['WeekendInfo']['TrackID']
        trackName = ir['WeekendInfo']['TrackDisplayName']
        trackCountry = ir['WeekendInfo']['TrackCountry']
        trackCity = ir['WeekendInfo']['TrackCity']
        trackLength = ir['WeekendInfo']['TrackLengthOfficial']
        trackVariante = ir['WeekendInfo']['TrackConfigName']
        carID = ir['DriverInfo']['Drivers'][playerID]['CarID']
        carName = ir['DriverInfo']['Drivers'][playerID]['CarScreenName']
        if ir['WeekendInfo']['SeriesID']:
            seriesID = ir['WeekendInfo']['SeriesID']
        else:
            seriesID = 0
        totalLaps = ir['SessionInfo']['Sessions'][0]['SessionLaps']
        maxIncidents = ir['WeekendInfo']['WeekendOptions']['IncidentLimit']
        myIncidents = ir['PlayerCarMyIncidentCount']
        sessions = ir['SessionInfo']['Sessions']
        lap = ir['Lap']
        fuelLevel = ir['FuelLevel']

    
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