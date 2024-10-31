import { Component, OnInit, Input, Output, ElementRef, ViewChild } from '@angular/core';
import {ImageCropperComponent, CropperSettings} from 'ng2-img-cropper';
declare var $: any;
@Component({
  selector: 'app-fileupload',
  templateUrl: './fileupload.component.html',
  styleUrls: ['./fileupload.component.css']
})
export class FileuploadComponent implements OnInit {

  defaultType: boolean = false;
  showImagePopUp: boolean = false;
  @ViewChild('fileupload') el: ElementRef;
  data: any;
  cropperSettings: CropperSettings;
  showUploadLink: boolean = false;
  spinLoader: boolean = false;
  hidedefault: boolean = false;
  @ViewChild('cropper', undefined) cropper: ImageCropperComponent;

  constructor() {
    this.cropperSettings = new CropperSettings();
    this.cropperSettings.noFileInput = true;
    this.data = {};
  }

  ngOnInit() {
  }

  imageClick(fileupload) {
    fileupload.click();
  }

  fileChangeEvent(e) {
    const image: any = new Image();
    const file: File = e.target.files[0];
    const fileReader: FileReader = new FileReader();
    const that = this;
    fileReader.onload = function (evt: any) {
      $('.fileuploadmodel').modal('show');
        image.src = evt.target.result;
        that.cropper.setImage(image);
    };
    fileReader.readAsDataURL(file);
}



}