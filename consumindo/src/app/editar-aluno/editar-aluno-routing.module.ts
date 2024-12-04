import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { EditarAlunoPage } from './editar-aluno.page';

const routes: Routes = [
  {
    path: '',
    component: EditarAlunoPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class EditarAlunoPageRoutingModule {}
