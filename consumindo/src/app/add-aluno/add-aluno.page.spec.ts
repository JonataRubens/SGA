import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AddAlunoPage } from './add-aluno.page';

describe('AddAlunoPage', () => {
  let component: AddAlunoPage;
  let fixture: ComponentFixture<AddAlunoPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(AddAlunoPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
