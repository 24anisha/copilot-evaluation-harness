import { Component, OnInit} from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Http } from '@angular/http';
import { LoginService } from "app/login.service";
import { Post} from 'app/post/post.entity';
import { ApiPostsService } from "app/api-posts.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-hot-page',
  templateUrl: './hot-page.component.html',
  styleUrls: ['./hot-page.component.css']
})
export class HotPageComponent implements OnInit {

  private posts:Post[]=[];


  constructor(private http: Http,private loginService: LoginService, private apiPostsService: ApiPostsService) {
     let url=URL + "/posts/";
      this.http.get(url).subscribe(
        response => {
          let data = response.json();
          for (var i = 0; i < data.length; i++) {
            let post = data[i];
            this.posts.push(post);
        }
        this.posts = this.posts.reverse();
      },
        error => console.error(error)
      );
   }

  ngOnInit() {
  }

}