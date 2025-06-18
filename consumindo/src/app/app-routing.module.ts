import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './auth.guard';


const routes: Routes = [
  {
    path: 'Alunos',
    loadChildren: () => import('./home/home.module').then(m => m.HomePageModule),
    canActivate: [AuthGuard]
  },
  {
    path: '',
    redirectTo: 'home-page',
    pathMatch: 'full'
  },
  {
    path: 'Campus',
    loadChildren: () => import('./about/about.module').then(m => m.AboutPageModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'home-page',
    loadChildren: () => import('./home-page/home-page.module').then(m => m.HomePagePageModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'add-aluno',
    loadChildren: () => import('./add-aluno/add-aluno.module').then(m => m.AddAlunoPageModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'editar-aluno/:id',
    loadChildren: () => import('./editar-aluno/editar-aluno.module').then(m => m.EditarAlunoPageModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'login',
    loadChildren: () => import('./login/login.module').then(m => m.LoginPageModule)
    // Não coloque AuthGuard aqui!
  },
];


@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
