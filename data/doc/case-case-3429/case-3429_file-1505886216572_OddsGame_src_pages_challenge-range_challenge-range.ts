import {Component} from '@angular/core';
import {NavParams, ModalController, ViewController} from 'ionic-angular';
import {Storage} from '@ionic/storage';

import {DatabaseProvider} from '../../providers/database-provider';


@Component({
    selector: 'page-challenge-range',
    templateUrl: 'challenge-range.html'
})
export class ChallengeRange {
    private challenge: any;
    private user_id: any = 0;

    private guesses: any = [2, 5, 10, 20, 50, 100];
    private guess: number = 0;

    constructor(private storage: Storage, private db: DatabaseProvider, private navParams: NavParams, private viewCtrl: ViewController) {
        this.challenge = navParams.get('challenge');
        this.storage.get('user').then((value) => {
            this.user_id = JSON.parse(value).id;
        });
    }

    selectGuess(guess) {
        this.guess = guess;
    }

    submit() {
        this.db.accept(this.user_id, this.challenge.challenge_id, this.guess);
        this.viewCtrl.dismiss(true); // true = submitted
    }

    cancel() {
        this.viewCtrl.dismiss(false); // false = cancelled
    }
}