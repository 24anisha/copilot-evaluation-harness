import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";

@Injectable()

export class AppHttp {
  constructor(
    private http: HttpClient
  ) {
  }
  get request() {
    return this.http;
  }
  headers(value:any) {
    return new HttpHeaders(value);
  }
  private tmpPost(uri:string,data:any) {
    let headerOption = new HttpHeaders({
      "Content-Type": "application/json"
     });
    // this.http.post(uri, { data }, { headers: headerOption })
    //     .subscribe(res => {
    //         this.message = (<any>res).json.data.username;
    //     });
  }

  // get(uri:string) {
  //   let headers = this.createRequestHeader();
  //   return this.http.get(uri, { headers: headers });
  // }
  // post(uri:string) {
  //   let headers = this.createRequestHeader();
  //   return this.http.post(uri, { data }, { headers: options });
  // }
  // delete(uri:string) {
  //   let headers = this.createRequestHeader();
  //   return this.http.delete(uri, { headers: headers });
  // }
  // private createRequestHeader() {
  //   let headers = new HttpHeaders({
  //       "AuthKey": "my-key",
  //       "AuthToken": "my-token",
  //       "Content-Type": "application/json",
  //    });
  //   return headers;
  // }
}