from Api.models import Variable, WorldData
from pandas     import read_excel

def findSection(variable):
    keywords = {
        'factory'   :   ['Emissions', 'Energy', 'Capacity', 'Carbon'],
        'city'      :   ['Consumption', 'Expenditure', 'Export', 'GDP', 'Import', 'Built-up', 'Population', 'Capital'],
        'farm'      :   ['Agricultural', 'Crop', 'Agriculture'],
        'forest'    :   ['Forest'],
        'atmosphere':   ['Temperature']
    }
    for key in keywords:
        for keyword in keywords[key]:
            if keyword in variable:
                return key
    return 'other'

def parse_excel(data):
    for sheet in data:
        cols = data[sheet].columns
        for index,row in data[sheet].iterrows():
            if index > 50:
                break
            #try block incase of wrong sheet format
            try:
                #variable
                var = Variable(
                    variable=row['Variable'],
                    unit=row['Unit'],
                    section=findSection(row['Variable'])
                )
                var.save()
                #world data
                w_data = WorldData(
                    model=row['Model'], scenario=row['Scenario'], variable=var,
                    _2005=row['2005'],
                    _2010=row['2010'],
                    _2015=row['2015'],
                    _2020=row['2020'],
                    _2025=row['2025'],
                    _2030=row['2030'],
                    _2035=row['2035'],
                    _2040=row['2040'],
                    _2045=row['2045'],
                    _2050=row['2050'],
                    _2055=row['2055'],
                    _2060=row['2060'],
                    _2065=row['2065'],
                    _2070=row['2070'],
                    _2075=row['2075'],
                    _2080=row['2080'],
                    _2085=row['2085'],
                    _2090=row['2090'],
                    _2095=row['2095'],
                    _2100=row['2100'],
                    )
                w_data.save()
            except:
                pass