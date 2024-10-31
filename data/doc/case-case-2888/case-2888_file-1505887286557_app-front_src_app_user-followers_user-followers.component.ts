import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';

import { Router, ActivatedRoute } from '@angular/router';
import { Post} from 'app/post/post.entity';
import { User } from  'app/user/user.entity';

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-user-followers',
  templateUrl: './user-followers.component.html',
  styleUrls: ['./user-followers.component.css']
})
export class UserFollowersComponent implements OnInit {

  private html: string = "posts";
  private followers: User[]=[];
  private id:number;

    constructor(private route: ActivatedRoute, private router: Router, private http: Http) {
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
            this.followers = data2.userFollowers;
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