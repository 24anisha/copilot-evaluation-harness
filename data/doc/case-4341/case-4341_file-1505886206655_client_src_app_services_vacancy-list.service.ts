import { Injectable } from '@angular/core';
import { Http, Response, URLSearchParams } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import { Vacancy } from '../classes/vacancy';
import 'rxjs/add/operator/map';

@Injectable()
export class VacancyListService {

  private url: string = 'https://parse-it.in.ua/api/vacancy/';

  constructor(private _http: Http) { }

  getVacancies(): Observable<Vacancy[]> {
    return this._http.get(this.url)
      .map((response: Response) => {
        console.log('------------Vacancy Service --> getVacancies()-----');
        console.log(response.json().vacancies);
        return response.json().vacancies;
      });
  }
  
  getMoreVacancies(counter: number): Observable<Vacancy[]> {
    return this._http.get(this.url + counter)
      .map((response: Response) => {
        console.log('------------------------------------------------------------------------>');
        console.log(`get qith params ${counter} iteration`);
        return response.json().vacancies;
      })
  }
}