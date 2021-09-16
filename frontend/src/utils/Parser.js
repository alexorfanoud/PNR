export const yearValuePattern = /_2\d{3}/

export const parseData = (dataArray) => {
    let maxVal = 0;
    let parsedData = [];

    for(let idx in dataArray){
        for(let key in dataArray[idx]){

            if(key.match(yearValuePattern)){
                let yearEntry = {
                    year: key.substring(1),
                    value: dataArray[idx][key]
                }
                if(dataArray[idx][key] > maxVal){
                    maxVal = dataArray[idx][key];
                }
                parsedData = [...parsedData, yearEntry]
            }
        }
    }
    return {parsedData: parsedData, maxVal: maxVal, model: dataArray[0]['model'], variable: dataArray[0]['variable'], scenario: dataArray[0]['scenario']}
}