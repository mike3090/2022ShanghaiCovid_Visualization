const margin = {top: 100, right: 0, bottom: 0, left: 0},
    width = 460 - margin.left - margin.right,
    height = 460 - margin.top - margin.bottom,
    innerRadius = 90,
    outerRadius = Math.min(width, height) / 2;   // the outerRadius goes from the middle of the SVG area to the border

// append the svg object
const svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${width/2+margin.left}, ${height/2+margin.top})`);

d3.csv("2022-03-01_media.csv").then( function(data) {

  // Scales
  const x = d3.scaleBand()
      .range([0, 2 * Math.PI])    // X axis goes from 0 to 2pi = all around the circle. If I stop at 1Pi, it will be around a half circle
      .align(0)                  // This does nothing
      .domain(data.map(d => d.name)); // The domain of the X axis is the list of states.
  const y = d3.scaleRadial()
      .range([innerRadius, outerRadius])   // Domain will be define later.
      .domain([0, 4000]); // Domain of Y is from 0 to the max seen in the data
    var myColor = d3.scaleOrdinal()
      .domain(["网页", "微信", "微博","客户端","论坛","报刊","视频","头条号","搜狐号","问答","其他"])
      .range(d3.schemeSet2);
    
  // Add the bars   
  svg.append("g")
    .selectAll("path")
    .data(data)
    .join("path")
      .attr("fill", function(d){return myColor(d.name)})
      .attr("d", d3.arc()     // imagine your doing a part of a donut plot
          .innerRadius(innerRadius)
          .outerRadius(d => y(d['value']))
          .startAngle(d => x(d.name))
          .endAngle(d => x(d.name) + x.bandwidth())
          .padAngle(0.01)
          .padRadius(innerRadius))

  // Add the labels
  svg.append("g")
      .selectAll("g")
      .data(data)
      .join("g")
        .attr("text-anchor", function(d) { return (x(d.name) + x.bandwidth() / 2 + Math.PI) % (2 * Math.PI) < Math.PI ? "end" : "start"; })
        .attr("transform", function(d) { return "rotate(" + ((x(d.name) + x.bandwidth() / 2) * 180 / Math.PI - 90) + ")"+"translate(" + (y(d['value'])+10) + ",0)"; })
      .append("text")
        .text(function(d){return(d.name)})
        .attr("transform", function(d) { return (x(d.name) + x.bandwidth() / 2 + Math.PI) % (2 * Math.PI) < Math.PI ? "rotate(180)" : "rotate(0)"; })
        .style("font-size", "11px")
        .attr("alignment-baseline", "middle")

});


// set the dimensions and margins of the grap
// The radius of the pieplot is half the width or half the height (smallest one). I subtract a bit of margin.
const radius = Math.min(width, height) / 2 - 120

// append the svg object to the div called 'my_dataviz'

// Create dummy data
const data = {a: 9, b: 20, c:30, d:8, e:12, f:3, g:7, h:14}

// set the color scale
const color = d3.scaleOrdinal()
.domain(["a", "b", "c", "d", "e", "f", "g", "h"])
.range(d3.schemeDark2);

// Compute the position of each group on the pie:
const pie = d3.pie()
.sort(null) // Do not sort group by size
.value(d => d[1])
const data_ready = pie(Object.entries(data))

// The arc generator
const arc = d3.arc()
.innerRadius(radius * 0.5)         // This is the size of the donut hole
.outerRadius(radius * 0.8)

// Another arc that won't be drawn. Just for labels positioning
const outerArc = d3.arc()
.innerRadius(radius * 0.9)
.outerRadius(radius * 0.9)

// Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
svg
.selectAll('allSlices')
.data(data_ready)
.join('path')
.attr('d', arc)
.attr('fill', d => color(d.data[1]))
.attr("stroke", "white")
.style("stroke-width", "2px")
.style("opacity", 0.7)