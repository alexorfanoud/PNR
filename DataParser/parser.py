from Api.models import Variable, WorldData
from pandas     import read_excel
from django.core.validators import ValidationError
import numbers

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
                    model=row['Model'] or '',
                    scenario=row['Scenario'] or '',
                    variable=var,
                    _2005=row['2005'] if isinstance(row['2005'], numbers.Number) else 0,
                    _2010=row['2010'] if isinstance(row['2010'], numbers.Number) else 0,
                    _2015=row['2015'] if isinstance(row['2015'], numbers.Number) else 0,
                    _2020=row['2020'] if isinstance(row['2020'], numbers.Number) else 0,
                    _2025=row['2025'] if isinstance(row['2025'], numbers.Number) else 0,
                    _2030=row['2030'] if isinstance(row['2030'], numbers.Number) else 0,
                    _2035=row['2035'] if isinstance(row['2035'], numbers.Number) else 0,
                    _2040=row['2040'] if isinstance(row['2040'], numbers.Number) else 0,
                    _2045=row['2045'] if isinstance(row['2045'], numbers.Number) else 0,
                    _2050=row['2050'] if isinstance(row['2050'], numbers.Number) else 0,
                    _2055=row['2055'] if isinstance(row['2055'], numbers.Number) else 0,
                    _2060=row['2060'] if isinstance(row['2060'], numbers.Number) else 0,
                    _2065=row['2065'] if isinstance(row['2065'], numbers.Number) else 0,
                    _2070=row['2070'] if isinstance(row['2070'], numbers.Number) else 0,
                    _2075=row['2075'] if isinstance(row['2075'], numbers.Number) else 0,
                    _2080=row['2080'] if isinstance(row['2080'], numbers.Number) else 0,
                    _2085=row['2085'] if isinstance(row['2085'], numbers.Number) else 0,
                    _2090=row['2090'] if isinstance(row['2090'], numbers.Number) else 0,
                    _2095=row['2095'] if isinstance(row['2095'], numbers.Number) else 0,
                    _2100=row['2100'] if isinstance(row['2100'], numbers.Number) else 0,
                    )
                w_data.save()
                updated_rows += 1
            except Exception as e:
                exceptions += 1
                pass
    return updated_rows, exceptions