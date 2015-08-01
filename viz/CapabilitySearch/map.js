// Adding 500 Data Points
var map ;
var infoWindow = new google.maps.InfoWindow();
// var batch = 100000;
var polylines = [];

function initialize(){
    var mapOptions = {
        zoom :11,
        center: new google.maps.LatLng(40.7307, -73.996094),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    } //mapoption ending 

    map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

}

//this will draw polygon using all border's coordinates of current ssid points
function calculateAndDrawPolygon(polylines, circles, ssids) {
    var points = [];

    for (var i=0; i < circles.length; i++) {
        var paths = circles[i].getPath().getArray();
        for(var c = 0; c < paths.length; c++) {
            points.push(paths[c]);
        }
    }
    points.sort(sortPointY);
    points.sort(sortPointX);

    // DrawHull(polylines, points, ssids);
}

function sortPointX(a,b) { return a.lng() - b.lng(); }
function sortPointY(a,b) { return a.lat() - b.lat(); }

function DrawHull(polylines, points, ssids) {
    var hullPoints = [];
    chainHull_2D( points, points.length, hullPoints );
    var polyline = new google.maps.Polygon({
        map: map,
        paths:hullPoints,
        fillColor:"#FF0000",
        strokeWidth:0,
        fillOpacity:0.5,
        strokeColor:"#0000FF",
        strokeOpacity:0,
        zIndex: -99999
    });

    polylines.push(polyline);

    var bounds = new google.maps.LatLngBounds();
    var i;

    for (i = 0; i < hullPoints.length; i++) {
        bounds.extend(hullPoints[i]);
    }

    var label = new Label({
        map: map,
        text: ssid,
        position: bounds.getCenter()
    }); //add polygon label

}



//draw circle using polygon - gives ability to get border's points coordinates
function drawCircle(point, radius, dir) {
    var d2r = Math.PI / 180;   // degrees to radians
    var r2d = 180 / Math.PI;   // radians to degrees
    var earthsradius = 3963; // 3963 is the radius of the earth in miles

    var points = 32;

    // find the raidus in lat/lon
    var rlat = (radius / earthsradius) * r2d;
    var rlng = rlat / Math.cos(point.lat() * d2r);

    var extp = new Array();
    if (dir==1) {
        var start=0;
        var end=points+1; // one extra here makes sure we connect the path
    } else {
        var start=points+1;
        var end=0;
    }
    for (var i=start; (dir==1 ? i < end : i > end); i=i+dir)
    {
        var theta = Math.PI * (i / (points/2));
        ey = point.lng() + (rlng * Math.cos(theta)); // center a + radius x * cos(theta)
        ex = point.lat() + (rlat * Math.sin(theta)); // center b + radius y * sin(theta)
        extp.push(new google.maps.LatLng(ex, ey));
    }
    return extp;
}

function changemap() {
    var mapOptions = {
        zoom: 15,
        center: new google.maps.LatLng(40.7307, -73.996094),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }; //map option ending

    map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

}

// function removeDuplicated(arr){

//   var n, y, x, i, r;


//   var arrResult = {},
//   nonDuplicatedArray = [];
//   for (i = 0, n = arr.length; i < n; i++) {
//       var item = arr[i];
//       arrResult[item.lat + " - " + item.lng] = item;
//   }
//   i = 0;
//   for (var item in arrResult) {
//     nonDuplicatedArray[i++] = arrResult[item];
//   }

//   return nonDuplicatedArray//this array only contains lat|lng attribute 

// }

function showcaps(){
    $.ajax({
        url: "http://capstone.cloudapp.net/wifipulling/?caps="+document.getElementById('caps').value+"&amp;batch="+document.getElementById('batch').value+"&amp;offset="+document.getElementById('offset').value,
        dataType:"text",

        success: function(data) { //when load data is success, the function will be execuated

            changemap(); //update map

            json = $.parseJSON(data);

            //group points by received ssids
            groupbyssid = _.groupBy(json,function(d){return d.ssid});

            //console.log(groupbyssid);

            //for every ssid - add circles and combine them into polygon
            _.each(groupbyssid, function (network) {

                // console.log(network);

                var circles = [];
                var filterdata = [];
                var leveldata = [];
                var resolution = 4;
                var showdata=[];
                var colorlist = [];

                _.each(network, function (obj) {

                    var mylat = parseFloat((obj.lat).toFixed(6));
                    var mylng = parseFloat((obj.lng).toFixed(6));//truncate lat|lng data

                    var filterbycolumns = {
                        'location': [mylat, mylng],
                        'level': obj.level,
                        'time': obj.time,
                        'ssid': obj.ssid
                    };
                    filterdata.push(filterbycolumns)
                });

                console.log('filter');
                console.log(filterdata);

                // No need to group by time, just get max level for the ssid
                // var groupbytime = _.groupBy(filterdata, function (d) {
                //     return d.time
                // });

                // console.log('time');
                // console.log(groupbytime);


                // _.each(filterdata, function (obj) {
                    var highestlevel = _.max(filterdata, function (d) {
                        return d.level
                    });
                    leveldata.push(highestlevel);

                // });


                // console.log(leveldata)//array of  object for each time highest

                var groupbylocation = _.groupBy(leveldata, function (d) {
                    return d.location
                });


                //console.log(groupbylocation);


                for (key in groupbylocation) {

                    var ssid = groupbylocation[key][0].ssid;
                    var len = groupbylocation[key].length;
                    var mid = key.indexOf(',')
                    var newlat = parseFloat(key.substring(0, key.indexOf(',')));
                    var lngstr = key.substring(key.indexOf('-'))
                    var newlng = parseFloat(lngstr);///HERE IS KIND OF TRICKY!!!

                    var sumlevel = 0;
                    len = groupbylocation[key].length;
                    // console.log(groupbylocation[key]);
                    for (var k = 0; k < len; k++) {
                        sumlevel += groupbylocation[key][k].level;
                    }
                    var avglevel = sumlevel / len;
                    var finalrecord = {'lat': newlat, 'lng': newlng, 'level': avglevel, 'measurement': len, 'ssid': ssid};
                    showdata.push(finalrecord);
                }
                ;


                //console.log(showdata);

                /*
                function changemap() {
                    var mapOptions = {
                        zoom: 15,
                        center: new google.maps.LatLng(showdata[0].lat, showdata[0].lng),
                        mapTypeId: google.maps.MapTypeId.ROADMAP
                    } //mapoption ending

                    map = new google.maps.Map(document.getElementById('map-canvas'),
                        mapOptions);

                }

                changemap();
                */

                map.setCenter(new google.maps.LatLng(showdata[0].lat, showdata[0].lng) );

                showdata = _.sortBy(showdata, function (obj) {
                    return obj.level
                });//sorted by level

                //console.log(showdata);

                var a = colorlist.length;//use index to
                _.each(showdata, function (obj) {
                    // console.log(obj);
                    a += -1;
                    var h = get_h(obj.level, -100, -30);
                    var rgb = HSVtoRGB(h / 360.0, 1.0, 1.0);
                    var color = rgbToHex(rgb['r'], rgb['g'], rgb['b']);

                    var circle = new google.maps.Polygon({
                        map: map,
                        paths: [drawCircle(new google.maps.LatLng(obj.lat, obj.lng), 1 / ((-1) * obj.level), 1)],
                        strokeColor: color,
                        strokeOpacity: 0.05,
                        strokeWeight: 2,
                        fillColor: color,
                        fillOpacity: 0.35,
                        ssid: obj.ssid
                    });

                    circles.push(circle);

                });//for each ends

                calculateAndDrawPolygon(polylines, circles);

                //console.log(rects);
                var addCirclesListener = function (i) {
                    var bounds = new google.maps.LatLngBounds();

                    var paths = circles[i].getPath().getArray();
                    for (var c = 0; c < paths.length; c++) {
                        bounds.extend(paths[c]);
                    }

                    google.maps.event.addListener(circles[i], 'click', function () {


                        var contentString = "<b>SSID</b>: " + showdata[i].ssid.toString()+ "<br/>";
                        contentString = contentString + "<b>Average</b>: " + showdata[i].level.toFixed(2).toString() + " dB<br/>";
                        contentString = contentString + "<b>Measurements</b>: " + showdata[i].measurement.toString();

                        infoWindow.setContent(contentString);

                        infoWindow.setPosition(bounds.getCenter());
                        infoWindow.open(map);

                    });//google map addListener

                    google.maps.event.addListener(circles[i], 'center_changed', function () {
                        label.setPosition(bounds.getCenter());
                    });
                };//add listener
                for (i = 0; i < circles.length; i++) {
                    addCirclesListener(i);
                }

                //console.log("Next SSID");
                //console.log("-----------------------------------------------");
            });

			
			document.getElementById('ssids').innerText = Object.keys(groupbyssid).join(', ');
			//calculateAndDrawPolygon(polylines, circles, Object.keys(groupbyssid).join());
        }//success function ending


    });//ajax ending

}//show maps function ending




google.maps.event.addDomListener(window, 'load', initialize);
