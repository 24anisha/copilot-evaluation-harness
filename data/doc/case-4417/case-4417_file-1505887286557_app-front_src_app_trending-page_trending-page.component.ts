import { Component, OnInit} from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Http } from '@angular/http';
import { Post} from 'app/post/post.entity';
import { LoginService } from "app/login.service";
import { ApiPostsService } from "app/api-posts.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-trending-page',
  templateUrl: './trending-page.component.html',
  styleUrls: ['./trending-page.component.css']
})
export class TrendingPageComponent implements OnInit {
 private posts:Post[]=[];

  constructor(private http: Http,private loginService: LoginService, private apiPostsService: ApiPostsService) {
    //Get Posts
      let url=URL + "/posts/trending";
      this.http.get(url).subscribe(
        response => {
          let data = response.json();
          for (var i = 0; i < data.length; i++) {
            let post = data[i];
            this.posts.push(post);
          }
      },
        error => console.error(error)
      );
     
   }
  ngOnInit() {
  }

}