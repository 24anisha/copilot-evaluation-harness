import { IFormCanDeactivate } from './../guards/iform-candeactivate';
import { Observable } from 'rxjs/Rx';
import { AlunoFormComponent } from './aluno-form/aluno-form.component';
import { Injectable } from '@angular/core';

import { CanDeactivate, RouterStateSnapshot, ActivatedRouteSnapshot } from "@angular/router";

@Injectable()
export class AlunosDeactivateGuard implements CanDeactivate<IFormCanDeactivate> {
        
        canDeactivate(
            component: IFormCanDeactivate,
            route: ActivatedRouteSnapshot,
            state: RouterStateSnapshot
        ): Observable<boolean>|Promise<boolean>|boolean {
            console.log("AlunosDeactivateGuard");
            return component.podeDesativar  ();
    }
}