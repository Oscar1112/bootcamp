function initMap() {
    // The location of Uluru
    const paris = { lat: 48.85341 , lng: 2.3488 };
    const dublin = { lat: 53.33306, lng: -6.24889 };
    const madrid = { lat: 40.4165 , lng: -3.70256 };

    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: paris,
    });
    
    
    const marker = new google.maps.Marker({
      position: paris, 
      map: map,
    });

    
    marker.push(
        new google.maps.Marker({
        position: madrid,
        map: map,
        }
        ),
        marker.push(
            new google.maps.Marker({
            position: dublin,
            map: map,
            })
      )

    
  
      );
  }

  window.initMap = initMap;
  
  function geoposiona(){
    const geoloca = navigator.geolocation
  }

