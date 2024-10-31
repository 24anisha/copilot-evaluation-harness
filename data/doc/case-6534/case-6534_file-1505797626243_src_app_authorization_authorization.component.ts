import { Store } from '@ngrx/store';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';

import { AppStore } from './../core/store/app-store';
import { AuthorizationService } from './../core/services';
import { ShowLoaderAction, HideLoaderAction } from '../shared/loader';

@Component({
  selector: 'login',
  templateUrl: './authorization.component.html',
  styleUrls: ['./authorization.component.css']
})
export class AuthorizationComponent implements OnInit {

  constructor(
    private authService: AuthorizationService,
    private router: Router,
    private store: Store<AppStore>
  ) { }

  public ngOnInit() {
    if (this.authService.isAuthenticated()) {
      this.router.navigate(['courses']);
    }
  }

  public submit(form): void {
    this.store.dispatch(new ShowLoaderAction());
    let login = form.value.login;
    let password = form.value.password;
    this.authService.login(login, password).subscribe(() => {
      this.store.dispatch(new HideLoaderAction());
      this.router.navigate(['courses']);
    },
      (err) => this.store.dispatch(new HideLoaderAction()));
  }
}