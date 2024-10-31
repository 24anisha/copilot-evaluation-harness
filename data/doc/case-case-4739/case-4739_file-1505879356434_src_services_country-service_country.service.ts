import {Injectable} from '@angular/core';
import {Http} from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()

export class CountryService {

  constructor(private http: Http) {
    this.http = http;
  }

  getAll() {
    let src = '../data/countries.json';
    return this.http
             .get(src)
             .map(response => response.json());
  }
}