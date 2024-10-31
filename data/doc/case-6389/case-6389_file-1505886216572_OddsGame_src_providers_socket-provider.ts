import { Injectable } from '@angular/core';
import { Network } from 'ionic-native';


import 'rxjs/add/operator/map';
import * as io from 'socket.io-client';
import { server } from './server-info';
import { Storage } from '@ionic/storage';

const URL = server.URL

@Injectable()
export class SocketProvider {
  private socket: any;
  private isConnected: boolean = false;

  constructor(private storage: Storage) {}

  getSocket() {
    return new Promise((resolve, reject) => {
        if(this.isConnected) { // If already connected, return socket or wait until socket is available
          if(this.socket) {
            resolve(this.socket);
          }
          else {
            var interval = setInterval(() => {
              if(this.socket) {
                clearInterval(interval);
                resolve(this.socket);
              }
            }, 50);
          }
        }
        else { // If not connected, make a new connection
          this.isConnected = true;
          this.storage.get('user').then((value) => {
            let userId = JSON.parse(value).id;

            this.socket = io('http://' + server.getURL() + ':3000/', {query: 'data=' + userId});
            this.socket.on('connect', () => {
                resolve(this.socket);
            });
          });
        }
    });
  }


}