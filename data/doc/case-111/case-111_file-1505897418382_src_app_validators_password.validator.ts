import { Directive, forwardRef } from '@angular/core';
import { FormControl, NG_VALIDATORS, AbstractControl, ValidatorFn, Validator } from '@angular/forms';


// validation function
function validatePwdMatch() : ValidatorFn {
  return (c: AbstractControl) => {
    
    let isValid = false;
    
    if(c.value){
        isValid = c.value.match("^(?=.*[A-Z])(?=.*[0-9]).{8,}")!== null;
    }
      
    if(isValid) {
      return null;
    } else {
      return {
        criteriaMatch: {
          valid: false
        }
      };
    }

  }
}


@Directive({
  selector: '[pwdValidator][ngModel]',
  providers: [
    { provide: NG_VALIDATORS, useExisting: PwdValidator, multi: true }
  ]
})
export class PwdValidator implements Validator {
  validator: ValidatorFn;
  
  constructor() {
    this.validator = validatePwdMatch();
  }
  
  validate(c: FormControl) {
    return this.validator(c);
  }
  
}