import { Component, OnInit, Input } from '@angular/core';

import { Vacancy } from '../../classes/vacancy';
import { VacancyListService } from '../../services/vacancy-list.service';
import { VacancyListPipePipe } from '../../pipes/vacancy-list-pipe.pipe';

@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {

  /* @Input() 
  term:any; */

  vacancies: Vacancy[];
  counter: number = 1;
  errorMessage: string;
  selectedVacancy: Vacancy;

  constructor(private _vacancyListService: VacancyListService) { }

  selectVacancy(id: number): void {
    this.vacancies.forEach(i => {
      if (i.id === id) {
        console.log(`selected vacancy ${i} id is ${i.id} <------------------`);
        this.selectedVacancy = i;
      }
    });
  }

  getVacancies(): void {
    this._vacancyListService.getVacancies()
      .subscribe(
      vacancies => this.vacancies = vacancies,
      error => this.errorMessage = <any>error,
      () => console.log('getting initial amount of vacancies is done')
      )
  }

  showMoreVacancies(): void {
    this._vacancyListService.getMoreVacancies(this.counter)
      .subscribe(
      vacancies => {
        vacancies.forEach(i => {
          this.vacancies.push(i);
        })
        this.counter++;
      },
      error => this.errorMessage = <any>error,
      () => console.log(`getting vacancies by ${this.counter} is done`)
      )
  }

  ngOnInit() {
    this.getVacancies();
  }

}