import { Component, OnInit, OnChanges } from '@angular/core';
import { Router } from '@angular/router'
import { FlashMessagesService } from 'angular2-flash-messages';


@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {

  /*
  Dependency injection is a way to supply a new instance of a class with the fully-formed dependencies it requires. Most dependencies are services. Angular uses dependency injection to provide new components with the services they need. Angular can tell which services a component needs by looking at the types of its constructor parameters.
  */
  constructor(
    private router: Router,
    private flashMessagesService: FlashMessagesService
  ) { }

  ngOnInit() {

  }

  loggedIn() {
    if(localStorage.getItem('user')) {
      return true;
    } else {
      return false;
    }
  }

  onLogout() {
    this.flashMessagesService.show('Logged out', {cssClass: 'alert-success', timeout: 3000});
    localStorage.clear();
    this.router.navigate(['/login']);
  }

}