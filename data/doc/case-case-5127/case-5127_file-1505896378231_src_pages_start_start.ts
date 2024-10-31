import { Component } from '@angular/core';
import { NavController, Events, LoadingController } from 'ionic-angular';

// pages
import { HomePage } from '../home/home';

// utils
import {TranslateService} from '@ngx-translate/core';
import { Network } from '@ionic-native/network';

// services
import { LoginService } from '../../services/login-service';
import { TimerService } from '../../services/timer-service';

@Component({
  selector: 'page-start',
  providers:[LoginService, TimerService],
  templateUrl: 'start.html'
})
export class StartPage {
  loader: any;

  constructor(
    public navCtrl: NavController,
    public translate: TranslateService,
    public loginService: LoginService,
    public timerService: TimerService,
    public network: Network,
    public events: Events,
    public loadingCtrl: LoadingController,
  ) {
  }

  goHomePage(): void{
    let networkState = this.network.type
    let user = this.loginService.serviceCurrentUser();

    if (networkState == 'none'){ // off-line
      if(user){
        console.log(user);
      }else{
        console.log('none user');
      }
    }else{ // on-line
      if(user){
        console.log(user);
      }else{
        this.presentLoading();
        this.loginService.serviceAnonymousLogin();
      }
    }
    console.log(networkState);
  }

  ionViewDidLeave(){
    this.loader.dismiss();
    console.log('Leave StartPage');
  }

  presentLoading() {
    let englishDefault = 'Please wait...'
    let msg: string = '';
    this.translate.get('MobileMessage.Wait').subscribe((res)=>{msg = res});
    this.loader = this.loadingCtrl.create({
      content: msg ==''?englishDefault:msg,
    });
    this.loader.present();
  }
}