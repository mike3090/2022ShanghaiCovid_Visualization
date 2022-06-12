

//Read the data


const func = function (data) {

  // Add X axis
  var x = d3.scaleLinear()
    .domain([0, 2400])
    .range([0, 900]);
  svg.append("g")
    .attr("transform", "translate(450,860)")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, 1])
    .range([240, 0]);
  svg.append("g")
    .attr("transform", "translate(450,620)")
    .call(d3.axisLeft(y));

  // Add a scale for bubble size
  var z = d3.scaleLinear()
    .domain([0, 3500])
    .range([3, 40]);

  // Add a scale for bubble color
  var myColor = d3.scaleOrdinal()
    .domain(["正面", "负面", "中性"])
    .range(d3.schemeSet2);

  // -1- Create a tooltip div that is hidden by default:
  var tooltip = d3.select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0.0);
  // -2- Create 3 functions to show / update (when mouse move but stay on same circle) / hide the tooltip

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
    .attr("class", "bubbles")
    .attr("transform", "translate(450,610)")
    .attr("cx", function (d) { return x(d.time); })
    .attr("cy", function (d) { return y(0.5) + 2 * d.count * (d.count % 2 - 0.5) * 2; })
    .attr("r", function (d) { return z(d.hot); })
    .style("fill", function (d) { return myColor(d.emo); })
    .attr("opacity", 0.6) //矩形原始透明度为0.4
    .on("mouseover", function (d, i) {
      d3.select(this)
        .attr("opacity", 1);//当鼠标在上，矩形变成全不透明
      tooltip.html(i + 1 + ":" + d.title)//且提示框内部html动态生成
        .style("left", (d3.event.pageX + 10) + "px")//x位置为当前鼠标X坐标向右10px
        .style("top", (d3.event.pageY - 10) + "px")//y位置为当前鼠标Y坐标向上10px
        .style("opacity", 1.0);//不透明
    })
    .on("mouseout", function (d, i) {//当鼠标移出矩形
      d3.select(this)
        .transition()
        .duration(500)
        .attr("opacity", 0.4);//变回0.4的透明度
      tooltip.style("opacity", 0.0);//提示框直接变为全透明
    })
    .on("mousemove", function (d) {//当鼠标移动
      tooltip.style("left", (d3.event.pageX + 10) + "px")//提示框跟着鼠标移动
        .style("top", (d3.event.pageY - 10) + "px");//提示框跟着鼠标移动
    })


}

d3.csv("./opinion_data/2022-03-01.csv", func)