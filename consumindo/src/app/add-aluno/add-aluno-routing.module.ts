import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AddAlunoPage } from './add-aluno.page';

const routes: Routes = [
  {
    path: '',
    component: AddAlunoPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AddAlunoPageRoutingModule {}
