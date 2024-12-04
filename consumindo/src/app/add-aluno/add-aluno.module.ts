import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AddAlunoPageRoutingModule } from './add-aluno-routing.module';

import { AddAlunoPage } from './add-aluno.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    AddAlunoPageRoutingModule
  ],
  declarations: [AddAlunoPage]
})
export class AddAlunoPageModule {}
