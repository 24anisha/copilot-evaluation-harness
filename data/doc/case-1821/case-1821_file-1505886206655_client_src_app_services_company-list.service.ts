import { Injectable } from '@angular/core';
import { Http, Response, URLSearchParams } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import { Company } from '../classes/company';
import 'rxjs/add/operator/map';

@Injectable()
export class CompanyListService {

  private url: string = 'https://parse-it.in.ua/api/company/';

  constructor(private _http: Http) { }

  getCompanies(): Observable<Company[]> {
    return this._http.get(this.url)
      .map((response: Response) => {
        console.log(`-------> CompanyList Service --- getCompanies`);
        console.log(response.json().companies);
        return response.json().companies;
      })
  }

  getMoreCompanies(counter: number): Observable<Company[]> {
    return this._http.get(this.url + counter)
      .map((response: Response) => {
        console.log(`--------======---- getMoreCompanies()`);
        console.log(`get with params ${counter} iteration`);
        return response.json().companies;
      });
  }
}