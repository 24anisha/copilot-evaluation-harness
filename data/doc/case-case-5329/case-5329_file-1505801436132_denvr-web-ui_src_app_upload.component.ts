import { Component } from '@angular/core';
import {Observable} from "rxjs/Observable";
import {RequestOptions, Http, Response} from "@angular/http";
import {userService} from './user.service'

// const URL = '/api/';
const URL = 'http://image-server-api:3000/image/';

@Component({
  selector: 'uploader',
  template: `<input type="file" (change)="fileChange($event)" placeholder="Upload file" accept="*">`
})
export class Uploader {
  constructor (private http: Http, private userService : userService) {}
  fileChange(event) {
    let fileList: FileList = event.target.files;
    if(fileList.length > 0) {
        let file: File = fileList[0];
        let formData:FormData = new FormData();
        formData.append('uploadFile', file, file.name);
        let options = new RequestOptions();
        this.http.post(URL + this.userService.getUserId(), formData, options)
            .map(res => res.json())
            .catch(error => Observable.throw(error))
            .subscribe(
                data => console.log('success'),
                error => console.log(error)
            )
    }
}
}