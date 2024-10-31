import { Component } from '@angular/core';
import { NavController, NavParams, ModalController, ViewController } from 'ionic-angular';

import { Facebook } from '@ionic-native/facebook';

import { Storage } from '@ionic/storage';

import {HomePage} from "../home/home";

import {TabsPage} from "../tabs/tabs";

import { DatabaseProvider } from '../../providers/database-provider';


@Component({
  selector: 'page-login',
  templateUrl: 'login.html'
})
export class Login {

  constructor(public navCtrl: NavController, public fb: Facebook, public storage: Storage, public db: DatabaseProvider, public modalCtrl: ModalController, public viewCtlr: ViewController) {
    //storage.set('user', JSON.stringify({name: "Jane Doe", id: "117195915492023"}));
  }


  login() {
    let context = this;
    this.fb.login(['public_profile', 'email', 'user_friends']).then(function(response) {
      alert('logged in');
      alert(JSON.stringify(response.authResponse));

      this.getdetails();
    }.bind(this), function(error) {
      alert('Error while logging in: ' + error);
    }.bind(this))
  }

  getdetails() {
    this.fb.getLoginStatus().then(function(response) {
      if(response.status == 'connected') {
        let id = response.authResponse.userID;
        this.fb.api("/" + id + "?fields=id,name,gender", ['public_profile', 'email', 'user_friends']).then(function onSuccess(response) {
          this.storage.set('user', JSON.stringify(response));
          this.db.addUser(response.name, response.id);
          this.navCtrl.setRoot(TabsPage);
        }.bind(this), function(error) {
          alert(error);
        })
      }
      else {
        alert('Not logged in!');
      }
    }.bind(this))
  }

  goHome() {
  /*  this.viewCtlr.dismiss().then((value) => {
      console.log(value);
    }, (error) => {
      console.log('error: ' + error);
    }); */
    this.navCtrl.setRoot(TabsPage);
  }
}