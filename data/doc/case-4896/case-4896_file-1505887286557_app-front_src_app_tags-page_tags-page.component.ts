import { Component, OnInit} from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Http } from '@angular/http';
import { Post} from 'app/post/post.entity';
import { LoginService } from "app/login.service";
import { ApiPostsService } from "app/api-posts.service";

const URL = 'http://localhost:8080/api';

@Component({
  selector: 'app-tags-page',
  templateUrl: './tags-page.component.html',
  styleUrls: ['./tags-page.component.css']
})
export class TagsPageComponent implements OnInit {
private posts:Post[]=[];
private tags:string;


  constructor(private route: ActivatedRoute, private router: Router,private http: Http,private loginService: LoginService, private apiPostsService: ApiPostsService) {
    this.route.params.subscribe(params => {
        this.tags = params['tags'];
      });
     let url=URL + "/posts/tag="+this.tags;
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