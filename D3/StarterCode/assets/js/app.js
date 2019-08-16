// @TODO: YOUR CODE HERE!
// Store width and height parameters to be used in later in the canvas
var svgWidth = 900;
var svgHeight = 600;

// Set svg margins 
var margin = {
  top: 40,
  right: 40,
  bottom: 80,
  left: 90
};

// Create the width and height based svg margins and parameters to fit chart group within the canvas
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


// Create the canvas to append the SVG group that contains the states data
// Give the canvas width and height calling the variables predifined.
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Create the chartGroup that will contain the data
// Use transform attribute to fit it within the canvas
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Load data from data.csv
var file = "assets/data/data.csv"

d3.csv(file).then (successHandle, errorHandle); 

  // Log an error if one exists
  function errorHandle(error) {
    console.log("error in code");
  }
  
// Function takes in argument statesData
function successHandle(statesData) {

  // Loop through the data and pass argument data
  statesData.map(function (data) {
    data.poverty = +data.poverty;
    data.obesity = +data.obesity;
    console.log(statesData)
  });


//  Create scale functions
  // Linear Scale takes the min to be displayed in axis, and the max of the data
  var xLinearScale = d3.scaleLinear()
    .domain([8.1, d3.max(statesData, d => d.poverty)])
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([20, d3.max(statesData, d => d.obesity)])
    .range([height, 0]);

 
// Create axis functions by calling the scale functions
var bottomAxis = d3.axisBottom(xLinearScale)

// Adjust the number of ticks for the bottom axis
.ticks(15);

var leftAxis = d3.axisLeft(yLinearScale);

// Append the axes to the chart group
// Bottom axis moves using height
chartGroup.append("g")
.attr("transform", `translate(0, ${height})`)
.call(bottomAxis);



// Left axis is already at 0,0
// Only append the left axis
chartGroup.append("g")
.call(leftAxis);
// Create Circles for scatter plot
var circlesGroup = chartGroup.selectAll("circle")
.data(statesData)
.enter()
.append("circle")
.attr("cx", d => xLinearScale(d.poverty))
.attr("cy", d => yLinearScale(d.obesity))
.attr("r", "13")
.attr("fill", "#788dc2")
.attr("opacity", ".75")

// Append text to circles
var circlesGroup = chartGroup.selectAll()
.data(statesData)
.enter()
.append("text")
.attr("x", d => xLinearScale(d.poverty))
.attr("y", d => yLinearScale(d.obesity))
.style("font-size", "13px")
.style("text-anchor", "middle")
.style('fill', 'white')
.text(d => (d.abbr))



// // Step 1: Append a div to the body to create tooltips, assign it a class
// var toolTip = d3.select("body").append("div")
//     .attr("class", "toolTip");

    // Step 1: Initialize Tooltip
    var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`<strong> ${d.state}<br>Poverty: ${d.poverty}%<br> Obesity: ${d.obesity}% `);
    
    });

  // Step 2: Create the tooltip in chartGroup.
  chartGroup.call(toolTip);

  // Step 3: Create "mouseover" event listener to display tooltip
  circlesGroup.on("mouseover", function(data) {
    toolTip.show(data, this);
  })
  // Step 4: Create "mouseout" event listener to hide tooltip
    .on("mouseout", function(data) {
      toolTip.hide(data);
    });

  // Create axes labels
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("Obese (%)");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .text("In Poverty (%)");
}

// // When the browser loads, makeResponsive() is called.
// makeResponsive();

// // When the browser window is resized, makeResponsive() is called.
// d3.select(window).on("resize", makeResponsive);

     // Create the rectangles using data binding
// var barsGroup = chartGroup.selectAll("circle ")
// .data(file)
// .enter()
// .append("rect")
// .attr("x", (d, i) => xScale(poverty[i]))
// .attr("y", d => yScale(d))
// .attr("width", xScale.bandwidth())
// .attr("height", d => chartHeight - yScale(d))
// .attr("fill", "green");

