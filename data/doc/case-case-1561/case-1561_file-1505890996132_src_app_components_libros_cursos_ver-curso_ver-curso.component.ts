import { Component, OnInit, ViewChild } from '@angular/core';
import { ModalComponent } from 'ng2-bs3-modal/ng2-bs3-modal';

import { CursosService } from '../../../../services/libros/cursos.service';
import { Curso } from '../curso';

@Component({
  selector: 'app-ver-curso',
  templateUrl: 'ver-curso.component.html',
  styleUrls: ['ver-curso.component.css']
})
export class VerCursoComponent implements OnInit {
  @ViewChild('modal')
  modal: ModalComponent;

  cursos = [];

  selectedCurso_id: number;

  constructor(
    private cursosService: CursosService,
  ) { }

  ngOnInit() {
    this.getCursos();
  }

  getCursos() {
    this.cursosService.getCursos().subscribe((res) => {
      this.cursos = res;
      console.log(res);
    })
  }

  indexOfObj(id: number): number {
    for (let i = 0; i < this.cursos.length; i++) {
      if ( this.cursos[i].curso.id == id) {
        return i;
      }
    }
    return -1;
  }

  modalOpen(id: number): void {
    this.modal.open();
    this.selectedCurso_id = id;
  }

  modalClose(id: number): void {
    this.deleteCurso(id);
  }

  modalDismiss(): void {
    this.modal.dismiss();
  }


  deleteCurso(id: number): void {
    this.cursosService.deleteCurso(id).subscribe(()=>{
      let index = this.indexOfObj(id);
      this.cursos.splice(index,1);
      this.modal.close();
      this.selectedCurso_id = null;
    });
  }

}