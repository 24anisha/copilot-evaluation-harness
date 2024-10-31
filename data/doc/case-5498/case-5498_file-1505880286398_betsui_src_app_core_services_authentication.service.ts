import {Injectable} from "@angular/core";
import {Http, Response} from "@angular/http";
import "rxjs/add/operator/map";
import {ApiService} from "../api.service";
import {User} from "../../+auth/+login/user.model";

@Injectable()
export class AuthenticationService {

    private path: string = 'user/login';
    data: User;

    constructor(private api: ApiService) {
    }

    login(username: string, password: string) {

        // console.log("서비스 함수 진입");
        this.data.username = username;
        this.data.password = password;

        // console.log('service Component post :');
        // console.log('PATH : ' + this.path);
        return this.api.retrievePost(`${this.path}`, this.data);

        /*
         return this.http.post('/user/login', JSON.stringify({username: username, password: password}))
         .map((response: Response) => {
         // login successful if there's a jwt token in the response
         let user = response.json();
         if (user && user.token) {
         // store user details and jwt token in local storage to keep user logged in between page refreshes
         localStorage.setItem('currentUser', JSON.stringify(user));
         }
         });
         */
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
        localStorage.removeItem('token');
        localStorage.removeItem('loginId');
        localStorage.removeItem('loginName');
        localStorage.removeItem('authority');
    }
}