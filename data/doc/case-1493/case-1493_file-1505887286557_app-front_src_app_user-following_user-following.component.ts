import { Component, OnInit } from '@angular/core';
import  {  Http  }  from  '@angular/http';

import { Router, ActivatedRoute } from '@angular/router';
import { Post } from 'app/post/post.entity';
import { User } from 'app/user/user.entity';
import { UserService } from "app/user/user.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-user-following',
  templateUrl: './user-following.component.html',
  styleUrls: ['./user-following.component.css']
})
export class UserFollowingComponent implements OnInit {

  private html: string = "posts";
  private id: number;
  private following: User[]=[];
  constructor(private route: ActivatedRoute, private router: Router, private http: Http, userService: UserService) {
    let userId = route.snapshot.params['name'];
    let url = URL + "/users/name=" + userId;
    this.http.get(url).subscribe(
      response => {
        let data = response.json();
        this.id = data.id;
        let url2 = URL + "/users/" + data.id;
        this.http.get(url2).subscribe(
          response => {
            let data2 = response.json();
            console.log(data2.userFollowing);
            this.following = data2.userFollowing;
          },
          error => console.error(error)
        );
      },
      error => console.error(error)
    );
  }

  ngOnInit() {
  }

  goToMenu(menu: string) {
    this.html = menu;
  }
}