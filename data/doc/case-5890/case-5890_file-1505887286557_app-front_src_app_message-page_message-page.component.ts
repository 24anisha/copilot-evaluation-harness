import { Component, OnInit } from '@angular/core';
import { LoginService } from "app/login.service";
import { Http } from '@angular/http';
import { Router, ActivatedRoute } from '@angular/router';
import { Message } from "app/message/message.entity";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';


const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-message-page',
  templateUrl: './message-page.component.html',
  styleUrls: ['./message-page.component.css']
})
export class MessagePageComponent implements OnInit {

  private messages: Message[];

  constructor(public loginService:LoginService, private route: ActivatedRoute, private router: Router, private http: Http) {
      console.log(this.loginService);
      if(this.loginService.isLogged){
        let url=URL + "/messages/conversations";
          this.http.get(url, { withCredentials: true }).subscribe(
            response => {
              let data = response.json();
              this.messages=data;
              console.log(this.messages);
          },
            error  => console.error(error)
          );
      }
  }

  ngOnInit() {
  }

}