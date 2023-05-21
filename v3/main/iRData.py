import irsdk

class iRData(object):
    ir = irsdk.IRSDK()
    ir.startup(test_file='datavuelta4.bin')
    if ir.is_connected:
        playerID = ir['PlayerCarIdx']
        trackID = ir['WeekendInfo']['TrackID']
        carID = ir['DriverInfo']['Drivers'][playerID]['CarID']
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
        if len(iRData.ir['SessionInfo']['Sessions']) == 3:
            return 2
        elif len(iRData.ir['SessionInfo']['Sessions']) == 2:
            return 1
        elif len(iRData.ir['SessionInfo']['Sessions']) == 1:
            return 0
    
    def getSesionLaps(self):
        return iRData.ir['SessionInfo']['Sessions'][iRData.getSesion()]['SessionLaps']

    def getParticipantes(self):
        return iRData.ir['SessionInfo']['Sessions'][iRData.getSesion()]['ResultsPositions']