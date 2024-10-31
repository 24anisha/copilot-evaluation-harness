import { Injectable } from "@angular/core";
import { Http, Response } from '@angular/http';
import { Observable } from "rxjs/Observable";

import 'rxjs/Rx';
//import {HttpClient} from "../HttpClient/HttpClient";

@Injectable()
export class PostService {
    constructor(private http: Http) { }
    getPost(id: ConstrainLong) {
        let url = "https://localhost:8080/api/posts/" + id;
        return this.http.get(url).map(
            response => response.json())
            .catch(error => Observable.throw('Server error'));

    }
}