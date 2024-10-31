import { Component } from '@angular/core';
import {faceService} from './face.service';
import {userService} from './user.service';
import {picture} from './picture';

@Component({
  selector: 'faces',
  template: `
          <div class="col-md-2">
          <div class="panel panel-default">
            <div class="panel-body" style="overflow:scroll; height:600px;">
            <p>Faces</p>
                
                 <div *ngFor="let picture of pictures">
                  <img src =   {{picture}}>
                   <br/>
                 </div>
          </div>
        </div>
  `,
  styleUrls: [
    '../assets/css/gallery.css',
    '../assets/css/test.css'
  ],
  providers: [faceService]
})
export class Faces{
  pictures: string[];
  errorMessage: string;
  mode = 'observable';


    constructor(private faceService: faceService, private userService: userService){

    }
    ngOnInit() { this.getPictures(); }
    //this.pictures[1].imageUrl = "alksdjf";
    getPictures(){
            //this.pictures[1].imageUrl = "alksdjf";
           var userId = this.userService.getUserId();
           //console.log(userId);
           this.faceService.getPicture(userId)
                 .subscribe(
                     pictures => {
                        pictures = pictures.replace(/'/g, '"')
                        let pictureArray = JSON.parse(pictures)
                       let pictureUrls = []
                       let i = ""
                       for(i in pictureArray) {
                          pictureUrls.push("https://s3.us-east-2.amazonaws.com/multimedia-term-project/" + pictureArray[i])
                       }
                       console.log(pictureUrls)

                       this.pictures = pictureUrls
                       },
                     error =>  this.errorMessage = <any>error
          );
    }
}