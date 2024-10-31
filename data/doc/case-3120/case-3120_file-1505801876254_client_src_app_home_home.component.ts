import { Component, OnInit } from '@angular/core';
import { CookieService } from 'angular2-cookie/core';
import { AuthService } from '../auth/auth-service';
import { Router, ActivatedRoute } from '@angular/router';



@Component({
  selector: 'home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {

  constructor(private CookieService: CookieService, private AuthService: AuthService, private router: Router) { }
  private account;
  private errorMessage;

  ngOnInit() {
    this.announce();
  }

  private getCookie(key: string) {
    return this.CookieService.get(key);
  }


  private announce() {
    let user = this.CookieService.get('User');
    this.account = user;
    console.log(user);
    if (user) {
      return this.AuthService.announceLogin(user);
    }
  }

}