import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Http, RequestOptions, Headers } from '@angular/http';

@Component({
  selector: 'app-signup-page',
  templateUrl: './signup-page.component.html',
  styleUrls: ['./signup-page.component.css']
})
export class SignupPageComponent implements OnInit {

  private username:string;
  private email:string;
  private password:string;
  private error:boolean;
  

  constructor(private http: Http, private router: Router) {
    this.error = false;
    this.username = "";
    this.password ="";
    this.email="";
  }

  ngOnInit() {
  }

  public signUp(){
    const URL = 'http://localhost:8080/api/users/';
    if(this.email==="" ||this.username==="" || this.password===""){
      this.error=true;
    }
    else{
      let data = {username:this.username, userEmail:this.email, userPassword:this.password};
      this.http.post(URL,data).subscribe(
        response => {
          alert("User created.");
          this.router.navigate(['/hot']);
        },
        error => {
          alert("Error creating the user.");
          this.error=true;
        }
      )
    }
  }

}