import { Component, OnInit } from "@angular/core";
import { ScheduleCheckResult, CheckResult } from "../../../models/models";
import { GoodResult } from "../../../models/check_results/good-result";
import { BadResult } from "../../../models/check_results/bad-result";
import { UglyResult } from "../../../models/check_results/ugly-result";
import { Result } from "../../../models/check_results/result";
import { Pair } from "../../../models/check-result";

@Component({
	selector: "schedule-editor-analyser",
    templateUrl: "./analyser.component.html"
})

export class AnalyserComponent implements OnInit {
    checkResult: CheckResult;
    details: Pair[];
    combinedResult: Result;

    ngOnInit(): void {
        this.details = Object.keys(this.checkResult.details).map(x => this.checkResult.details[x]);
        const calculated = this.checkResult.calculatedResult;

        this.combinedResult = calculated >= 80
            ? new GoodResult()
            : calculated >= 50
                ? new BadResult()
                : new UglyResult();
    }
}