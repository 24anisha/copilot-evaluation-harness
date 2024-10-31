import { Injectable } from '@angular/core';
import { Http, Response }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
import { user } from './user';
import { Headers, RequestOptions } from '@angular/http';
import {serverResponse} from './serverResponse';
import {picture} from './picture';





@Injectable()
  export class faceService{

     //private userUrl = 'http://52.15.89.214:8002/image/:'+userId;  // URL to web API

     constructor (private http: Http) {}

     getPicture(user): Observable<string> {
       var userUrl = 'http://face-api:5000/face/user/'+user;
       //let headers = new Headers({ 'Content-Type': 'application/json' });
       //let options = new RequestOptions({ headers: headers });
       //console.log(this.userUrl);
       return this.http.get(userUrl)
                    .map(res=>res["_body"])
                    .catch(this.handleError);
    }

  private extractData(res: Response) {

  //  console.log(res);
    //let userId = JSON.stringify(res["_body"]);
    //if (userId) {
    //  console.dir(userId);
    //}

  //  return res;
  //console.log(res);
  //  let body = res.json();
  //  console.log(body);
  //  //console.log(body.data);
  //  return body;
    let body = res.json();
    //console.log(body);
    return body.data || { };
 }
 private handleError (error: Response | any) {
   // In a real world app, you might use a remote logging infrastructure
   let errMsg: string;
   if (error instanceof Response) {
     const body = error.json() || '';
     const err = body.error || JSON.stringify(body);
     errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
   } else {
     errMsg = error.message ? error.message : error.toString();
   }
   console.error(errMsg);
   return Observable.throw(errMsg);
 }

}