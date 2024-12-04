import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'Alunos',
    loadChildren: () => import('./home/home.module').then(m => m.HomePageModule)
  },
  {
    path: '',
    redirectTo: 'home-page', // Isso vai redirecionar para a rota home-page ao carregar o app
    pathMatch: 'full'
  },
  {
    path: 'Campus',
    loadChildren: () => import('./about/about.module').then(m => m.AboutPageModule)
  },
  {
    path: 'home-page',
    loadChildren: () => import('./home-page/home-page.module').then(m => m.HomePagePageModule)
  },
  {
    path: 'add-aluno',
    loadChildren: () => import('./add-aluno/add-aluno.module').then(m => m.AddAlunoPageModule)
  },
  {
    path: 'editar-aluno/:id', // A rota agora vai chamar o módulo EditarAlunoPageModule
    loadChildren: () => import('./editar-aluno/editar-aluno.module').then(m => m.EditarAlunoPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
