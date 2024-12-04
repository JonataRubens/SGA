import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { EditarAlunoPageRoutingModule } from './editar-aluno-routing.module';

import { EditarAlunoPage } from './editar-aluno.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    EditarAlunoPageRoutingModule
  ],
  declarations: [EditarAlunoPage]
})
export class EditarAlunoPageModule {}
