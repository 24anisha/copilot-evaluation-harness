import { Component, OnInit } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute } from '@angular/router';
import { Http } from '@angular/http';
import { Post} from 'app/post/post.entity';
import { ApiPostsService } from "app/api-posts.service";
import { LoginService } from "app/login.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.css']
})
export class SearchPageComponent implements OnInit {
 private posts:Post[]=[];
  private post:Post;
  private title:string;

  constructor(private route: ActivatedRoute, private router: Router,private http: Http, private apiPostsService: ApiPostsService, private loginService: LoginService) {
      this.route.params.subscribe(params => {
        this.title = params['find'];
      });
    let url=URL + "/posts/search="+this.title;
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