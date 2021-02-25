from Api.models import Variable, WorldData
from pandas     import read_excel
from django.core.validators import ValidationError

def findSection(variable):
    keywords = {
        #price carbon, final energy, value added
        'factory'   :   ['Energy', 'Capacity', 'Carbon'],
        'city'      :   ['Consumption', 'Expenditure', 'Export', 'GDP', 'Import', 'Built-up', 'Population', 'Capital', 'Investment', 'Policy Cost'],
        'farm'      :   ['Agricultural', 'Crop', 'Agriculture'],
        'forest'    :   ['Forest'],
        'atmosphere':   ['Temperature', 'Forcing', 'Sequestration', 'Concentration' 'Emissions']
    }
    for key in keywords:
        for keyword in keywords[key]:
            if keyword in variable:
                return key
    return 'other'

def parse_excel(data):
    updated_rows, exceptions = 0, 0
    for sheet in data:
        for index,row in data[sheet].iterrows():
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
                    _2005=row['2005'] or 0,
                    _2010=row['2010'] or 0,
                    _2015=row['2015'] or 0,
                    _2020=row['2020'] or 0,
                    _2025=row['2025'] or 0,
                    _2030=row['2030'] or 0,
                    _2035=row['2035'] or 0,
                    _2040=row['2040'] or 0,
                    _2045=row['2045'] or 0,
                    _2050=row['2050'] or 0,
                    _2055=row['2055'] or 0,
                    _2060=row['2060'] or 0,
                    _2065=row['2065'] or 0,
                    _2070=row['2070'] or 0,
                    _2075=row['2075'] or 0,
                    _2080=row['2080'] or 0,
                    _2085=row['2085'] or 0,
                    _2090=row['2090'] or 0,
                    _2095=row['2095'] or 0,
                    _2100=row['2100'] or 0,
                    )
                w_data.save()
                updated_rows += 1
            except Exception as e:
                exceptions += 1
                pass
    return updated_rows, exceptions