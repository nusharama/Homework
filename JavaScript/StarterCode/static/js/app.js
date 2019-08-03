
// Step 1: Loop Through `data` and console.log each ufoSightings report object
// data.forEach(function(ufoSightings) {
//     console.log(ufoSightings); 
// });


// // add the code on line 4 below after you set up your botton_function
// // set up a function with this button


// // Step 2:  Use d3 to append one table row `tr` for each ufoSightings report object
// // Don't worry about adding cells or text yet, just try appending the `tr` elements.
// data.forEach(function(ufoSightings) {
//     console.log( );
//     var row = tbody.append('tr'); 
// }); 

// // Step 3:  Use `Object.entries` to console.log each ufoSightings value
// data.forEach(function(ufoSightings) {
//     console.log(ufoSightings);
//     var row = tbody.append('tr');

//     Object.entries(ufoSightings).forEach(function([key, value]) {
//         console.log(key, value);
//     });
// });

// // // Step 4: Use d3 to append 1 cell per weather report value (weekday, date, high, low)
// data.forEach(function(ufoSightings) {
//     console.log(ufoSightings);
//     var row = tbody.append("tr");
 

//     Object.entries(ufoSightings).forEach(function([key, value]) {
//       console.log(key, value);
// // Append a cell to the row for each value
// // in the weather report object
//       var cell = row.append("td");
//     });
//   }); 

//Please ignore code above lines 43 and up. I had the code above to understand each of the steps. Main code for the homework 
//starts from line 45. 

// from data.js
var tableData = data;

// Console.log the data from data.js
console.log(data);


//function to display UFO sightings
//// Get a reference to the table body
//Date function
var tbody = d3.select("tbody");
tbody.html("");
var button = d3.select("#filter-btn");

button.on("click", function() {
    console.log("Button pressed!")
    tbody.html("");
    var newdate = d3.select("#datetime").property("value");
    console.log(newdate);

    var outputData = data.filter(function(filteredData) {
        return(filteredData.datetime == newdate)
    });
    console.log(outputData)
    outputData.forEach(function(ufoSightings) {
        // console.log(ufoSightings);
        var row = tbody.append("tr");
        Object.entries(ufoSightings).forEach(function([key, value]) {
        //   console.log(key, value);
          // Append a cell to the row for each value
          // in the weather report object
          var cell = row.append("td");
          cell.text(value);
        });
      });
});


//City function
var tbody = d3.select("tbody");
tbody.html("");
var button = d3.select("#filter-btn-city");

button.on("click", function() {
    console.log("Button pressed!")
    tbody.html("");
    var newcity = d3.select("#city").property("value");
    console.log(newcity);

    var outputData = data.filter(function(filteredData) {
        return(filteredData.city == newcity)
    });
    console.log(outputData)
    outputData.forEach(function(ufoSightings) {
        // console.log(ufoSightings);
        var row = tbody.append("tr");
        Object.entries(ufoSightings).forEach(function([key, value]) {
        //   console.log(key, value);
          // Append a cell to the row for each value
          // in the weather report object
          var cell = row.append("td");
          cell.text(value);
        });
      });
});

//State function
var tbody = d3.select("tbody");
tbody.html("");
var button = d3.select("#filter-btn-state");

button.on("click", function() {
    console.log("Button pressed!")
    tbody.html("");
    var newstate = d3.select("#state").property("value");
    console.log(newstate);

    var outputData = data.filter(function(filteredData) {
        return(filteredData.state == newstate)
    });
    console.log(outputData)
    outputData.forEach(function(ufoSightings) {
        // console.log(ufoSightings);
        var row = tbody.append("tr");
        Object.entries(ufoSightings).forEach(function([key, value]) {
        //   console.log(key, value);
          // Append a cell to the row for each value
          // in the weather report object
          var cell = row.append("td");
          cell.text(value);
        });
      });
});

 // // Step 5: Use d3 to update each cell's text with
  // // ufoSightings values (weekday, date, high, low)
  data.forEach(function(ufoSightings) {
    // console.log(ufoSightings);
    
    var row = tbody.append("tr");
    Object.entries(ufoSightings).forEach(function([key, value]) {
    //   console.log(key, value);
      // Append a cell to the row for each value
      // in the weather report object
      var cell = row.append("td");
      cell.text(value);
    });
  });

