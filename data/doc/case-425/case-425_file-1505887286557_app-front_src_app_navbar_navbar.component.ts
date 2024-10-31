import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LoginService } from 'app/login.service';
import { User } from "app/user/user.entity";
import { Http } from '@angular/http';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  searchedPost: string;
  numEmails:number=0;
  loggedUser: User = {
      id: 0,
      username: "Cargando...",
      userEmail: "Cargando...",
      userBiography: "Cargando...",
      userLocation: "Cargando...",
      userLink: "",
      report: false,
      roles: [],
      userFollowing: [],
      userFollowers: [],
      userPosts: []
    };

  constructor(private router: Router,private loginService: LoginService, private http: Http) {
      this.loggedUser = this.loginService.getUser();
      this.calculateNumEmails();
        //this.loginService.logIn("user1","pass1");
   }

  ngOnInit() {
  }

  onSubmit(){
      this.router.navigate(['/search', this.searchedPost]);
  }

  logOut(){
    this.loginService.logOut();
    this.router.navigate(['/hot']);
  }

  calculateNumEmails(){
    if(this.loginService.isLogged){
        let url=URL + "/messages/";
          this.http.get(url, { withCredentials: true }).subscribe(
            response => {
              let data = response.json();
              for(var i=0; i<data.length; i++){
                if(data[i].messageNew==true){
                  this.numEmails++;
                }
              }
              console.log(data);
          },
            error  => console.error(error)
          );
      }
  }

}