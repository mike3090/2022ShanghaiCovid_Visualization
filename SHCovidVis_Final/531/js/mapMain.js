

var map = new BMap.Map("container",{
    enableRotate: false,
    enableTilt:false
});

//var map2 = new BMap.Map("container2",{
//    enableRotate: false,
//    enableTilt:false
//});

var initPoint = new BMap.Point(121.480,31.236);//lng,lat

map.centerAndZoom(initPoint, 11);
//map2.centerAndZoom(initPoint, 10);

map.enableScrollWheelZoom(true);
var myGeo = new BMap.Geocoder();

x1=120.864463;//westest
x2=121.998464;//eastest(Real: 121.997331); West to east, 90 zones
y1=30.697938;//southest
y2=31.878739;//northest(real: 31.874652); South to North, 123 zones
lineListX=[];
lineListY=[];
var myIcon=new BMap.Icon('dot.png',new BMap.Size(10,10));
for (var i=x1;i<=x2;i=i+0.0126){//~1200m grid
    var line=new BMap.Polyline([new BMap.Point(i,y1),new BMap.Point(i,y2)],{strokeColor:"black", strokeWeight:2, strokeOpacity:0.15})
    lineListX.push(line);
}
for (var i=y1;i<=y2;i=i+0.0096){
    var line=new BMap.Polyline([new BMap.Point(x1,i),new BMap.Point(x2,i)],{strokeColor:"black", strokeWeight:2, strokeOpacity:0.15})
    lineListY.push(line);
}
function showgrids(){
    
    if(map.getZoom()>=12){
        for (var i=0;i<=90;i=i+1){//~1200m grid; 90=(x2-x1)/0.0126
            //var line=new BMap.Polyline([new BMap.Point(i,y1),new BMap.Point(i,y2)],{strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5})
            map.addOverlay(lineListX[i]);
        }
        for (var i=0;i<=123;i=i+1){//123=(y2-y1)/0.0096
            //var line=new BMap.Polyline([new BMap.Point(x1,i),new BMap.Point(x2,i)],{strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5})
            map.addOverlay(lineListY[i]);
        }
    }
}

showgrids();
/*
myGeo.getPoint('黄浦区人民大道200号',function(point){
    if(point){
        console.log(point.lng);
        map.centerAndZoom(point, 11);
        map.addOverlay(new BMap.Marker(point,{title:"gov"}))    
    }
    else{
        alert('nope');
    }
},'上海市')*/

var markerList=[];
var markerClusterer=new BMapLib.MarkerClusterer(map,{markerList:markerList,minClusterSize:4});
//d3.csv("positive_location_data/position_count2.csv").then(function(data){
d3.csv("positive_location_data/position_count2.csv").then(function(data){
    console.log(data.length);
    
    for (var i=0; i<data.length;i++){
        if(data[i].position!=''){
            lng=data[i].lng
            lat=data[i].lat
            pos=data[i].position
            markerList.push(new BMap.Marker(new BMap.Point(lng,lat),{icon:myIcon}));
            //map.addOverlay(new BMap.Circle(new BMap.Point(lng,lat),10,{fillColor:'green'}));
        }
    }
    markerClusterer.addMarkers(markerList);    
})

map.addEventListener("zoomend",function(){
    if(map.getZoom()>=12){
        showgrids();
    }
    else{
        for (var i=0;i<=90;i=i+1){//~1200m grid; 90=(x2-x1)/0.0126
            //var line=new BMap.Polyline([new BMap.Point(i,y1),new BMap.Point(i,y2)],{strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5})
            map.removeOverlay(lineListX[i]);
        }
        for (var i=0;i<=123;i=i+1){//123=(y2-y1)/0.0096
            //var line=new BMap.Polyline([new BMap.Point(x1,i),new BMap.Point(x2,i)],{strokeColor:"blue", strokeWeight:2, strokeOpacity:0.5})
            map.removeOverlay(lineListY[i]);
        }
    }
});
//map.addEventListener("dragend",function(){markerClusterer.clearMarkers(markerList);markerClusterer.addMarkers(markerList)});

/*
var dailyZoneCountData =null;
d3.json("positive_location_data/processed3_3_gridDailyStatistics/dailyZoneCount.json").then(function(data2){
    map.addEventListener('click',function(e){
    //alert(''+e.point.lng+','+e.point.lat);
    lng=e.point.lng;
    lat=e.point.lat;
    i0=0;
    j0=0;
    for (var i=0;i<=90;i=i+1){
        if (x1+i*0.0126<lng && lng<=x1+0.0126+i*0.0126){
            for (var j=0;j<=123;j=j+1){
                if (y1+j*0.0096<lat && lat<=y1+0.0096+j*0.0096){
                    i0=i;
                    j0=j;
                }
            }    
        }
    }
    zoneName="zone"+j0+"_"+i0;
    console.log(data2[zoneName]);    
    });


    for (var i=0;i<90;i=i+3){
        for (var j=0;j<123;j=j+3){
            //console.log(i+" "+j);
            total=0;
            for (var k1=0;k1<3;k1++){
                for (var k2=0;k2<3;k2++){
                    zoneName="zone"+(j+k1)+"_"+(i+k2);
                    dataEach=data2[zoneName];
                    for (var month=3;month<5;month++){
                        if(month==3){
                            for (var day=6;day<32;day++){
                                dayName="day"+month+"_"+day;
                                total=total+dataEach[dayName];
                            }
                        }
                        else if(month==4){
                            for (var day=1;day<31;day++){
                                dayName="day"+month+"_"+day;
                                total=total+dataEach[dayName];
                            }
                        }
                        else if(month==5){
                            for (var day=1;day<13;day++){
                                dayName="day"+month+"_"+day;
                                total=total+dataEach[dayName];
                            }
                        }
                    } 
                }
            }
            
            
            if(total!=0){
                var point0=new BMap.Point(x1+i*0.0126+0.0126+0.0063,y1+j*0.0096+0.0096+0.0048);
                var content=total+"";
                var label=new BMap.Label(content,{position:point0});
                map.addOverlay(label);
            }
        }
    }
});
*/