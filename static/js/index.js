function initMap(position) {
    // The location of Uluru
    document.getElementById("loc").defaultValue = "lat: "+position.coords.latitude+", lng: "+position.coords.longitude;
    const pos = { lat: position.coords.latitude, lng: position.coords.longitude };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: pos,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: pos,
      map: map,
    });
}



function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(initMap);
  } else { 
    alert ("Geolocation is not supported by this browser.");
  }
}