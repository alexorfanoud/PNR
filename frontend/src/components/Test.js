import React, {useRef, useEffect} from 'react'
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";

export default function LineChart({data}) {
   const chart = useRef(null);

    useEffect(async () => {
        console.log('hello')
        // create chart
        let x = am4core.create("chartdiv", am4charts.XYChart);
        let tempdata = []
        for(let i=0; i<data.length; i++){
            obj = data[i]
            for(let key of Object.keys(obj)){
                //{date: key.split(), value:obj[key]}
                tempdata.push({
                    date: key,
                    value: obj[key]
                })
            }
        }
        // bind data
        x.data = tempdata

        let categoryAxis = x.xAxes.push(new am4charts.DateAxis());
        categoryAxis.dataFields.category = key;
        let valueAxis = x.yAxes.push(new am4charts.ValueAxis());
        let series = x.series.push(new am4charts.LineSeries());
        series.dataFields.categoryX = ""
        series.dataFields.valueY = ""
        chart.current = x
        return () => {
            x.dispose();
        };
    }, []);

    return (
        <div>
            <div ref={chart} id="chartdiv" style={{ width: "100%", height: "500px" }} />
        </div>
    )
}
