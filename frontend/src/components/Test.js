import React, {useRef, useEffect} from 'react'
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

/* Chart code */
// Themes begin
export default function LineChart({data}) {
    am4core.useTheme(am4themes_animated);

   const chart = useRef(null);
    const yearValuePattern = /\_2\d{3}/
    useEffect(() => {
        console.log("test component useffect")
        
        
    // Themes end

    chart.current = am4core.create("chartdiv", am4charts.XYChart);
    chart.current.hiddenState.properties.opacity = 0; // this creates initial fade-in
    fetch('http://localhost:8000/api/pk/3')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        let mydata = []
        for(let idx in data){
            for(let key in data[idx]){
                if(key.match(yearValuePattern)){
                    console.log(key)
                    let obj = {
                        year: key.substring(1),
                        value: data[idx][key]
                    }
                    console.log(obj)
                    mydata = [...mydata, obj]
                }
            }
        }
        chart.current.data = mydata
        console.log(chart.current.data)

    })
    .catch(e => console.log(e));

    // chart.current.data = [
    //   {
    //     country: "USA",
    //     visits: 23725
    //   },
    //   {
    //     country: "China",
    //     visits: 1882
    //   },
    //   {
    //     country: "Japan",
    //     visits: 1809
    //   },
    //   {
    //     country: "Germany",
    //     visits: 1322
    //   },
    //   {
    //     country: "UK",
    //     visits: 1122
    //   },
    //   {
    //     country: "France",
    //     visits: 1114
    //   },
    //   {
    //     country: "India",
    //     visits: 984
    //   },
    //   {
    //     country: "Spain",
    //     visits: 711
    //   },
    //   {
    //     country: "Netherlands",
    //     visits: 665
    //   },
    //   {
    //     country: "Russia",
    //     visits: 580
    //   },
    //   {
    //     country: "South Korea",
    //     visits: 443
    //   },
    //   {
    //     country: "Canada",
    //     visits: 441
    //   }
    // ];

    let categoryAxis = chart.current.xAxes.push(new am4charts.CategoryAxis());
    categoryAxis.renderer.grid.template.location = 0;
    categoryAxis.dataFields.category = "year";
    categoryAxis.renderer.minGridDistance = 40;
    categoryAxis.fontSize = 11;

    let valueAxis = chart.current.yAxes.push(new am4charts.ValueAxis());
    valueAxis.min = 0;
    valueAxis.max = 10000;
    valueAxis.strictMinMax = true;
    valueAxis.renderer.minGridDistance = 30;

    let series = chart.current.series.push(new am4charts.ColumnSeries());
    series.dataFields.categoryX = "year";
    series.dataFields.valueY = "value";
    series.columns.template.tooltipText = "{valueY.value}";
    series.columns.template.tooltipY = 0;
    series.columns.template.strokeOpacity = 0;

    // as by default columns of the same series are of the same color, we add adapter which takes colors from chart.colors color set
    series.columns.template.adapter.add("fill", function(fill, target) {
    return chart.current.colors.getIndex(target.dataItem.index);
});
    }, []);

    return (
        <div>
            <div ref={chart} id="chartdiv" style={{ width: "100%", height: "500px" }} />
        </div>
    )
}
