import { Component } from '@angular/core';
import {ChatService, UsersService} from '../app/services/app.service.js';
import "rxjs/add/operator/do";
import "rxjs/add/operator/map";
import {getEnvVariables} from '/env.js';

@Component({
  moduleId: module.id,
  selector: 'task-chat',
  templateUrl: 'chat.component.html',
  providers: [UsersService, ChatService]
})
export class ChatComponent {
  chats = [];
  success = null;
  errors = null;
  constructor(private userService:UsersService, private chatService:ChatService){
    this.user = userService.getUser()
    try{
      this.socket = io.connect('http://' + getEnvVariables().APIIP + ':' + getEnvVariables().CHATPORT + '/')
    }catch(e){
      //set status to warn user
    }
    this.chatService.getChats()
      .subscribe(chats => {
          this.chats = chats;
        });
  }

  submitChat(event){
    var self = this
    var message = $('#chat_textarea').val()

    if(event.which == 13 && event.shiftKey == false){
      this.socket.emit('input', {
        name: this.user.name,
        message: message
      })
      $('#chat_message').append(this.user.name + ": " + message)
    }
  }
}