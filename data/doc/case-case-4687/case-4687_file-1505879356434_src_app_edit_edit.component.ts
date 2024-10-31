import {
  Component,
  Input,
  Output,
  EventEmitter
} from '@angular/core';
import {Router} from '@angular/router-deprecated';
import {
  AddressService,
  Address,
  AppStore
} from '../../addresses';
import {AddressDetail} from '../components/addressdetail/';
import {Store} from '@ngrx/store';

  //-------------------------------------------------------------------
  // MAIN COMPONENT
  //-------------------------------------------------------------------
@Component({
  selector: 'edit',
  providers: [],
  styles: [],
  template: `
  <md-content layout-padding>
    <address-detail
      (saved)="saveAddress($event)"
      (cancelled)="resetAddress($event)"
      [address]="selectedAddress | async">Select an Address
      </address-detail>
  </md-content>
  `,
  directives: [AddressDetail]
})

export class Edit {

  selectedAddress: any;

  constructor(
      private router: Router,
      private addressService: AddressService,
      private store: Store<AppStore>
    ) {
    this.selectedAddress = store.select('selectedAddress');
  }

  ngOnInit() {
    console.log('welcome to edit view');
  }

  resetAddress() {
    let emptyAddress: Address = {
      id: '',
      firstName: '',
      lastName: '',
      email: '',
      country: ''
    };
    this.store.dispatch({type: 'SELECT_ADDRESS', payload: emptyAddress});
  }

  saveAddress(address: Address) {
    this.addressService.saveAddress(address);
    this.resetAddress();
    this.router.parent.navigate(['Address list']);
  }
}