import { Component } from '@angular/core';
import { Http } from '@angular/http';
import { xhrHeaders } from '../../xhr-headers';
import { Observable } from 'rxjs/Rx';

declare const module;

@Component({
	selector: 'form-demo',
	moduleId: module.id,
	templateUrl: 'form.component.html'
})
export class FormComponent {

    constructor(private http:Http) {
    	this.http = http;
        this.previewImage = 'http://cf.gatewaypeople.com/prod/s3fs-public/default_images/thumbnail-default_2.jpg?NJyZzXM0pqsRIPfj5rTWmMa.ofAVPNF0';
        this.file = "";
    }

    readUrl(event) {
	  	if (event.target.files && event.target.files[0]) {
	  		let type = event.target.files[0].type;
	  		let fileSize = event.target.files[0].size;
	  		let allowType = /^image\/(jpg|png|jpeg|bmp|gif|ico)$/;

	  		if (allowType.test(type) && fileSize <= 5242880) {
	  			let reader = new FileReader();

		    	reader.onload = (event) => {
		      		this.previewImage = event.target.result;
		    	}

		    	reader.readAsDataURL(event.target.files[0]);
		    	this.file = event.target.files[0];
	  		} else {
	  			event.target.value = "";
	  			alert('File format invalid or file size over than 5MB !');
	  		}
	  	}
	}

	onSubmit(value: any) {
		let formData = new FormData();
		formData.append("data", value);
    	formData.append("file", this.file);
		
		this.http.post('http://localhost:3000/upload', formData, xhrHeaders())
			.map(res => res.json())
	        .catch(error => Observable.throw(error))
	        .subscribe(
	            data => console.log('success'),
	            error => console.log(error)
	        )
	}
	
}