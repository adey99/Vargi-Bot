
"use strict";

let SubmitTray = require('./SubmitTray.js')
let VacuumGripperControl = require('./VacuumGripperControl.js')
let AGVControl = require('./AGVControl.js')
let GetMaterialLocations = require('./GetMaterialLocations.js')
let PopulationControl = require('./PopulationControl.js')
let ConveyorBeltControl = require('./ConveyorBeltControl.js')

module.exports = {
  SubmitTray: SubmitTray,
  VacuumGripperControl: VacuumGripperControl,
  AGVControl: AGVControl,
  GetMaterialLocations: GetMaterialLocations,
  PopulationControl: PopulationControl,
  ConveyorBeltControl: ConveyorBeltControl,
};
