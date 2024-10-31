import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Address } from 'supplyworks';
import { User, Employer } from 'types';

import { RegisterService } from '../services'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  public employer = new Employer();
  public adminUser = new User();
  public registerForm: FormGroup;
  public registering = false;
  public result = '';

  constructor( private fb: FormBuilder, private registerService: RegisterService ) {
    this.adminUser.isAdmin = true;
    this.buildForm();
   }

  buildForm(): void {
    this.registerForm = this.fb.group({
      name:   ['', Validators.required],
      user: this.fb.group({
        firstName:    ['', Validators.required],
        lastName:     ['', Validators.required],
        mobilePhone:  ['', Validators.required],
        email:        ['', Validators.required],
        password:     ['', Validators.required]
      }),
      address: this.fb.group({
        line1: '',
        line2: '',
        suburb: ''
      })
    });
  }

  doRegister(): void {
    this.registering = true;
    if(this.registerForm.dirty && this.registerForm.valid) {
      const formModel = this.registerForm.value;
      this.employer.name = formModel.name;
      this.adminUser = formModel.user;
      this.employer.address[0] = formModel.address;

      this.registerService.Register(this.employer, this.adminUser)
        .then(res => { this.result = JSON.stringify(res); this.registering = false; })
        .catch( err => { this.result = err; this.registering = false; });
    }
  }

  ngOnInit() {
  }

}