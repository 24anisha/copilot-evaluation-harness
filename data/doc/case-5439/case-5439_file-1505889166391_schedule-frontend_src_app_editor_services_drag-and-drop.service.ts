import { Injectable } from "@angular/core";
import { Class } from "../../common/models/models";
import { ClassFrequency, frequencyFromString, frequencyToString, getDay, getNumber } from "../components/helpers";
import { getDayOfWeekName } from "../../common/models/functions";
import { MovingCell, Cell } from "../models/models";

@Injectable()
export class DragAndDropService {
	private dragCell: MovingCell;
	private dropCell: MovingCell;

	dragClass: Class;

	startDrag(c: Class, viewObjectId: number, position: number): void {
		const classFrequency = frequencyFromString(c.frequency);
		this.dragClass = c;
		this.dragCell = {
			viewObjectId: viewObjectId,
			position: position,
			frequency: classFrequency
		};
	}

	addDropItem(c: Class, viewObjectId: number, position: number, frequency: number): void {
		this.dropCell = {
			viewObjectId: viewObjectId,
			position: position,
			frequency: position !== -1
				? frequency
				: frequencyFromString(c.frequency)
		};
	}

	releaseDrop(): void {
		this.dragClass = null;
		this.dragCell = null;
		this.dropCell = null;
	}

	getDropCell(): MovingCell {
		return this.dropCell;
	}

	getDragCell(): MovingCell {
		return this.dragCell;
	}

    addToView(): boolean {
        return this.dragCell.position === -1;
    }

    removeFromView(): boolean {
        return this.dropCell.position === -1;
    }

	changeViewObject(): boolean {
		return this.dragCell.viewObjectId !== this.dropCell.viewObjectId;
    }
}