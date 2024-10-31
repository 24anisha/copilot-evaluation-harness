import { Component, OnInit, Input, ViewChild, OnChanges, SimpleChanges } from '@angular/core';

@Component( {
	selector   :'life-in-a-box',
	templateUrl:'./life-in-a-box.component.html',
	styleUrls  :[ './life-in-a-box.component.css' ]
} )
export class LifeInABoxComponent implements OnInit, OnChanges {
	public time:string;
	public numOfBoxRows:number;
	public numOfBoxRowsArray:number[];
	public numOfBoxes:number;
	public testvar:any;
	public currentDate:Date;
	public age:number;

	@Input() viewType:string;
	@Input() birthday:string;
	@Input() lifeExpectancy:string;

	constructor() {
	}

	getAge( dateString ) {
		var today     = new Date();
		var birthDate = new Date( dateString );
		var age       = today.getFullYear() - birthDate.getFullYear();
		var m         = today.getMonth() - birthDate.getMonth();
		if( m < 0 || (m === 0 && today.getDate() < birthDate.getDate()) ){
			age--;
		}
		return age;
	}

	createArray( number ) {
		return Array( number ).fill( 1 ).map( ( val, index ) => {
			return index;
		} );
	}

	ngOnInit() {
		this.currentDate       = new Date();
		// this.time  = 'weeks';
		this.numOfBoxRows      = 90;
		this.numOfBoxRowsArray = this.createArray( this.numOfBoxRows );
		this.changeView();
		this.testvar = 'sdf'
	}

	test() {
		// console.log('yo test success!')
	}

	ngOnChanges( changes:any ) {
		// changes.prop contains the old and the new value...
		// console.log('changes', changes);
		if( changes.viewType ){
			this.changeView();
		}
		if( changes.birthday ){

			// this.age = 30;
			this.age = this.getAge( changes.birthday.currentValue )
			// console.log('age!', a);
		}
		if( changes.lifeExpectancy ){

			this.numOfBoxRowsArray = this.createArray( changes.lifeExpectancy.currentValue );
		}

	}

	changeView() {
		if( this.viewType === 'days' ){
			this.numOfBoxes = 365;
		}
		if( this.viewType === 'weeks' ){
			this.numOfBoxes = 52;
		}
		if( this.viewType === 'months' ){
			this.numOfBoxes = 12;
		}
	}

}