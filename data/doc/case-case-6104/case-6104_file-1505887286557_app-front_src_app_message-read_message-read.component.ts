import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import  {  Http  }  from  '@angular/http';
import { User } from 'app/user/user.entity';
import { Message } from "app/message/message.entity";
import { LoginService } from "app/login.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-message-read',
  templateUrl: './message-read.component.html',
  styleUrls: ['./message-read.component.css']
})
export class MessageReadComponent implements OnInit {

  private messages: Message[]=[];

  constructor(private route: ActivatedRoute, private router: Router, private http: Http, public loginService: LoginService) {
    let username = route.snapshot.params['name'];
    if(this.loginService.isLogged){
      let url = URL + "/messages/conversations=" + username;
      this.http.get(url, { withCredentials: true }).subscribe(
        response  =>  {
          let  data  =  response.json();
          var j = 0;
          for(var i=(data.length -1); i>=0; i--){
            this.messages[j]=data[i];
            j++;
          }
          console.log(data);
          console.log(this.messages);
        },
        error   =>  console.error(error)
      );
  }
  }

  ngOnInit() {
  }

}