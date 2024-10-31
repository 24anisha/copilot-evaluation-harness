import { Component, OnInit } from '@angular/core';
import { User } from "app/user/user.entity";
import { LoginService } from "app/login.service";
import { Router, ActivatedRoute } from '@angular/router';
import { Http } from '@angular/http';

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.css']
})
export class ProfilePageComponent implements OnInit {
  private html:string ="posts";
  private isAdminLogged: boolean;

private numFollowers:number;
private numFollowing:number;
  constructor(public loginService: LoginService, private route: ActivatedRoute, private router: Router, private http: Http) {
    this.isAdminLogged = this.loginService.isAdminMethod();
    console.log(this.loginService);
    let url = URL + "/users/" + this.loginService.user.id;
    this.http.get(url).subscribe(
      response => {
        let data = response.json();
          this.numFollowers=data.userFollowers.length;
          this.numFollowing=data.userFollowing.length;
      },
      error => console.error(error)
    );
   }


  ngOnInit() {
  }

  goToMenu(menu:string){
    this.html=menu;
  }

  background():string{
    return "url(/headerimg/"+this.loginService.user.id+")";
  }
}