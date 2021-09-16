import React, {useRef, useEffect, useState} from 'react'
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

import { parseData } from '../utils/Parser.js'

import './LineChart.css'

export default function LineChart({pk}) {

	am4core.useTheme(am4themes_animated);

	const chart = useRef(null);
	const [maxVal, setMaxVal] = useState(0);
	const [variable, setVariable] = useState("");
	const [model, setModel] = useState("");
	const [scenario, setScenario] = useState("");


    useEffect(() => {

		chart.current = am4core.create("chartdiv", am4charts.XYChart);
		chart.current.hiddenState.properties.opacity = 0;

		fetch('http://localhost:8000/api/pk/'+pk)
			.then(response => response.json())
			.then(data => {
				console.log(data)
				let {parsedData, maxVal, model, variable, scenario} = parseData(data)
				chart.current.data = parsedData
				setMaxVal(maxVal*1.2);
				setModel(model);
				setVariable(variable);
				setScenario(scenario);
			})
			.catch(e => console.log(e));

		let categoryAxis = chart.current.xAxes.push(new am4charts.CategoryAxis());
		categoryAxis.renderer.grid.template.location = 0;
		categoryAxis.dataFields.category = "year";
		categoryAxis.renderer.minGridDistance = 40;
		categoryAxis.fontSize = 11;

		let valueAxis = chart.current.yAxes.push(new am4charts.ValueAxis());
		valueAxis.min = 0;
		valueAxis.max = maxVal;
		valueAxis.strictMinMax = true;
		valueAxis.renderer.minGridDistance = 30;

		let series = chart.current.series.push(new am4charts.ColumnSeries());
		series.dataFields.categoryX = "year";
		series.dataFields.valueY = "value";
		series.columns.template.tooltipText = "{valueY.value}";
		series.columns.template.tooltipY = 0;
		series.columns.template.strokeOpacity = 1;

		// as by default columns of the same series are of the same color, we add adapter which takes colors from chart.colors color set
		series.columns.template.adapter.add("fill", function(fill, target) {
		return chart.current.colors.getIndex(target.dataItem.index);
	});
    }, [maxVal]);

    return (
        <div className='chart'>
			variable:{variable}
			model:{model}
			scenario:{scenario}
            <div ref={chart} id="chartdiv" style={{ width: "100%", height: "500px" }} />
        </div>
    )
}
