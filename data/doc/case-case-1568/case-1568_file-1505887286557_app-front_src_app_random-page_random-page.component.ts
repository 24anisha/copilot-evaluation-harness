import { Component, OnInit } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Http } from '@angular/http';
import { Post} from 'app/post/post.entity';
import { ApiPostsService } from "app/api-posts.service";
import { LoginService } from "app/login.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-random-page',
  templateUrl: './random-page.component.html',
  styleUrls: ['./random-page.component.css']
})
export class RandomPageComponent implements OnInit {
  
  private posts:Post[]=[];
  private post:Post;

  constructor(private http: Http,private loginService: LoginService, private apiPostsService: ApiPostsService) {
    let url=URL + "/posts/";
      this.http.get(url).subscribe(
        response => {
          let data = response.json();
          for (var i = 0; i < data.length; i++) {
            let p = data[i];
            this.posts.push(p);
        }
        let cont= Math.floor(Math.random() * (this.posts.length));
        this.post= this.posts[cont];
      },
        error => console.error(error)
      );
  
   }

  ngOnInit() {
  }

}