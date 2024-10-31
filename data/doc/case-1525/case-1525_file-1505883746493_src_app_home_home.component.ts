import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from "@angular/forms";
import { LifeInABoxComponent } from "../life-in-a-box/life-in-a-box.component";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
	public viewType: string = 'weeks';
	public form:FormGroup;
	@ViewChild(LifeInABoxComponent) lifeInABox:LifeInABoxComponent;

  constructor(fb:FormBuilder) {
  	this.form = fb.group({
  		"birthday": '1990-01-01',
  		"lifeExpectancy": 80
	})
  }

  ngOnInit() {
  }

	onSubmit() {
		console.log( 'form submitted', this.form )
	}

	setView(newView: string){
  		console.log('got this event!', newView);
		this.viewType = newView;
	}

}