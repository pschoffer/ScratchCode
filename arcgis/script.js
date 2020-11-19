require(['esri/Map', 'esri/views/MapView', 'esri/widgets/BasemapToggle', 'esri/widgets/BasemapGallery'], function (
  Map,
  MapView,
  BasemapToggle,
  BasemapGallery
) {
  var map = new Map({
    basemap: 'satellite',
  });

  var view = new MapView({
    container: 'viewDiv',
    map: map,
    center: [-118.805, 34.027], // longitude, latitude
    zoom: 13,
  });

  var basemapToggle = new BasemapToggle({
    view: view,
    nextBasemap: 'satellite',
  });
  view.ui.add(basemapToggle, 'bottom-right');

  var basemapGallery = new BasemapGallery({
    view: view,
    source: {
      portal: {
        url: 'https://www.arcgis.com',
        useVectorBasemaps: true, // Load vector tile basemaps
      },
    },
  });
  view.ui.add(basemapGallery, 'top-right');
});
