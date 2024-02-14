import './style.css';
import {Map, View} from 'ol';
import Feature from 'ol/Feature';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import Polygon from 'ol/geom/Polygon';
import OSM from 'ol/source/OSM';
import { Style, Stroke, Fill } from 'ol/style';


async function fetchCoordinates() {
  try {
    const response = await fetch('./polygon.json');
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`)
    }
    const data = await response.json()
    return data.polygon;
  } catch (err) {
    console.error(`Could not fetch the data ${err}`)
  }
}


fetchCoordinates().then(polygonData => {
  // polygonData coordinates are in format of longitude and latitude which are EPSG:4326 coordinate system
  // transforming to EPSG:3857 bc majority of web map applications use the Web Mercator(EPSG::3857)
  const polygonGeometry = new Polygon([polygonData]).transform('EPSG:4326', 'EPSG:3857');

  // getting representative center and its coordinates
  const centerPoint = polygonGeometry.getInteriorPoint();
  const centerPointCoords = centerPoint.getCoordinates();

  // now these features are suitable for editing
  const vectorSource = new VectorSource({
    features: [new Feature(polygonGeometry)]
  });
  
  // this layer type provides most accurate rendering
  const vectorLayer = new VectorLayer({
    source: vectorSource,
  });

  // adding vector layer styles
  const vectorLayerStyle = new Style({
    stroke: new Stroke({
      color: 'red',
      width: 3 
    }),
    fill: new Fill({
      color: 'rgba(255, 0, 0, 0.15)'
    })
  });

  vectorLayer.setStyle(vectorLayerStyle);

  // initialize and display an interactive map
  // map is equiped with with OpenStreetMap and vector layer that displays a polygon 
  const map = new Map({
    target: 'map',
    layers: [
      new TileLayer({
        source: new OSM()
      }),
      vectorLayer
    ],
    view: new View({
      center: centerPointCoords,
    })
  });

  // map's view dynamically fits the polygon and adjusts according to the device size
  const extent = vectorLayer.getSource().getExtent();

  function adjustMapView() {
    map.getView().fit(extent, {
      size: map.getSize(),
      padding: [100, 100, 100, 100], 
    });
  }

  adjustMapView();

  window.addEventListener('resize', adjustMapView);

});
