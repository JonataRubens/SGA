import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EditarAlunoPage } from './editar-aluno.page';

describe('EditarAlunoPage', () => {
  let component: EditarAlunoPage;
  let fixture: ComponentFixture<EditarAlunoPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(EditarAlunoPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
