import { Component, OnInit } from "@angular/core";
import { RestrictionSettings } from "../../../../models/models";
import { AnalyzerService } from "../../../../services/analyser.service";

@Component({
	selector: "schedule-editor-analyser-settings",
    templateUrl: "./settings.component.html"
})

export class AnalyserSettingsComponent implements OnInit {
    restrictions: RestrictionSettings[] = [];
    facultyId: number;

    constructor(private analyzerService: AnalyzerService) {}

    ngOnInit(): void {
        this.analyzerService.getRestrictions(this.facultyId)
            .subscribe((restrictions: RestrictionSettings[]) => this.restrictions = restrictions);
    }

    toggleActive(restrictionId: number): void {
        const restriction = this.restrictions.find(x => x.id === restrictionId);
        restriction.active = !restriction.active;
        this.analyzerService.updateRestriction(restriction)
        .connect();

        this.restrictions = this.restrictions;
    }
}