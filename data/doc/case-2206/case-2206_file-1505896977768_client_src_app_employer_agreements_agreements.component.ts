import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

import { AgreementService } from './agreement.service';
import { EmployerService, ErrorService } from '../services';
import { Agreement, AgreementTypes } from 'types';

@Component({
  selector: 'app-agreements',
  templateUrl: './agreements.component.html',
  styleUrls: ['./agreements.component.scss']
})
export class AgreementsComponent implements OnInit {
  // private _agreements: Agreement[];
  private _displayNewAgreement = false;

  constructor(
    // private _service: AgreementService,
    // private _empService: EmployerService,
    private _errorService: ErrorService,
    private _router: Router,
    private _route: ActivatedRoute
  ) { }

  newAgreement():void {
    this._displayNewAgreement = true;
    this._router.navigate(['new'], { relativeTo: this._route });
  }

  ngOnInit():void {
    
  }

  errorHandler(msg: string): void {
    this._errorService.errorHandler(msg);
  }

}