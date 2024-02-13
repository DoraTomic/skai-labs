import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import Feature from 'ol/Feature.js';
import users from './polygon.json' assert {type: 'json'}
import Polygon from 'ol/geom/Polygon.js';
import Vector from 'ol/layer/Vector.js'
import Vectors from 'ol/source/Vector.js'
import Style from 'ol/style/Style.js'
import Fill from 'ol/style/Fill.js';
import Stroke from 'ol/style/Stroke.js';

let coordinates = users['polygon']
let polygonFeatureT = new Feature(new Polygon([coordinates]).transform('EPSG:4326', 'EPSG:3857'));
let centroid = polygonFeatureT.getGeometry().getInteriorPoint().getCoordinates();

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new OSM()
    }),
    new Vector({
                   source: new Vectors({
                       features: [polygonFeatureT]
                   }),
                   style: new Style({
                    fill: new Fill({
                      color: 'rgba(165, 80, 51, 0.8)'
                    }),
                    stroke: new Stroke({
                      color: 'orange',
                      width: 2
                    })
                   })
                 }) 
  ],
  view: new View({
    center: [centroid[0], centroid[1]],
    zoom: 8
  })
});
