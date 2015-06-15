$(document).ajaxStart(function() {
  $("#map-canvas").css({opacity: .5});
});

$(document).ajaxStop(function() {
  $("#map-canvas").css({opacity: 1});
});

function addLocations(data, map) {
	var markers = [];
	for (var i = 0; i < data.length; i++) {
		var latLng = new google.maps.LatLng(data[i].lat, data[i].lng);
		var marker = new google.maps.Marker({'position': latLng});
		markers.push(marker);
	}
	var markerCluster = new MarkerClusterer(map, markers);
}

function initialize() {
	var mapOptions = {
		center: {lat: 40.7127, lng: -74.0059},
		zoom: 12
	};
	var map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions);

	$.ajax({
		url: 'http://capstone.cloudapp.net/wifipulling/?columns=lat|lng&distinct=1',
		type: 'GET',
		dataType: 'json',
		error: function(err) {
			console.log('ugh');
			console.log(err);
		},
		success: function(data) {
			console.log(data);
			addLocations(data, map);
		}
	});
	// $.ajax({
	// 	url: 'http://capstone.cloudapp.net/wifipulling/?columns=ssid&distinct=1',
	// 	type: 'GET',
	// 	dataType: 'json',
	// 	error: function(err) {
	// 		console.log('oops');
	// 	},
	// 	success: function(data) {
	// 		console.log('yay');
	// 		for (var i = 0; i < data.length; i++) {
	// 			$('#select').append('<option>' + data[i].ssid + '</option>');
	// 		}
	// 	}
	// });
}




$(document).ready(function() {
	initialize();
});