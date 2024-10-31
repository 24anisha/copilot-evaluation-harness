import { Injectable } from '@angular/core';
import { IDoor, IXyScanData, IXyAngleData, IBestDoor, IXy } from '../interfaces';

@Injectable()
export class DoorService {

  constructor() { }

  getDoors(scan: Array<IXyAngleData>, width: number): Array<IDoor> {
    let doors: Array<IDoor> = new Array();

    // sort by angle
    scan.sort((e1, e2) => { return e1.angle - e2.angle });

    scan.reduce((prev, curr) => {
      // space size between two scan points
      let c = Math.sqrt(Math.pow(curr.x - prev.x, 2) + Math.pow(curr.y - prev.y, 2));
      if (c >= width) {
        doors.push({
          r: prev,
          l: curr
        });
      }
      return curr;
    });

    // chceck space size between first and last scan point
    let c = Math.sqrt(Math.pow(scan[0].x - scan[scan.length - 1].x, 2) + Math.pow(scan[0].y - scan[scan.length - 1].y, 2));
    if (c >= width) {
      doors.push({
        r: scan[scan.length - 1],
        l: scan[0]
      });
    }

    return doors;
  }

  getBestDoor(start: IXy, end: IXy, doors: Array<IDoor>): IBestDoor {
    let bestDoor: IBestDoor;

    doors.forEach((door) => {
      let pathLenL: number = Math.sqrt(Math.pow(door.l.x - start.x, 2) + Math.pow(door.l.y - start.y, 2)) + Math.sqrt(Math.pow(end.x - door.l.x, 2) + Math.pow(end.y - door.l.y, 2));
      let pathLenR: number = Math.sqrt(Math.pow(door.r.x - start.x, 2) + Math.pow(door.r.y - start.y, 2)) + Math.sqrt(Math.pow(end.x - door.r.x, 2) + Math.pow(end.y - door.r.y, 2));
      let pathLen: number = Math.min(...[pathLenL, pathLenR]);

      if (!bestDoor || bestDoor.pathLen > pathLen) {
        bestDoor = { door: door, pathLen: pathLen, pathLenL: pathLenL, pathLenR: pathLenR }
      }
    });
    return bestDoor;
  }

}