import {Component, OnInit, ViewChild } from '@angular/core';
import { Location } from '@angular/common'
import { ActivatedRoute, Params } from '@angular/router';
import { ModalComponent } from 'ng2-bs3-modal/ng2-bs3-modal';

import { Curso } from '../curso';
import { CursosService } from '../../../../services/libros/cursos.service';
import { ProfesoresService } from '../../../../services/libros/profesores.service';

@Component({
  selector: 'app-asignar-prof',
  templateUrl: 'asignar-prof.component.html',
  styleUrls: ['asignar-prof.component.css']
})
export class AsignarProfComponent implements OnInit {
  @ViewChild('modal')
  modal: ModalComponent;

  id: number;
  private sub: any;

  curso: any;

  profesores = [
    {"nombre":"Pedro","apellidos":"Fernandez","id":1},
  ];

  constructor(
    private location: Location,
    private cursosService: CursosService,
    private profesoresService: ProfesoresService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
    this.getProfesores();

    this.sub = this.route.params.subscribe(params => {
      this.id = +params['id'];
    });

    this.route.params
      .switchMap((params: Params) => this.cursosService.getCurso(+params['id']))
      .subscribe((curso) => {
        this.curso = curso;
      });

  }
  //../services
  getProfesores() {
    this.profesoresService.getProfesors().subscribe((res) => {
      this.profesores = res;
    })
  }

  saveCurso() {
    this.cursosService.updateCurso(this.curso.curso).subscribe((res) => {
      this.modalOpen();
    });
  }
  //navigation
  goBack(): void {
    this.location.back();
  }
  //modal
  modalOpen(): void {
    this.modal.open();
  }

  modalClose(): void {
    this.modal.close();
    this.goBack();
  }

}