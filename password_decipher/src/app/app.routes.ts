import { Routes } from '@angular/router';
import { Home } from './pages/home/home';
import { Cipher } from './pages/cipher/cipher';

export const routes: Routes = [
  { path: '', component: Home },
  { path: 'cipher', component: Cipher },
  { path: '**', redirectTo: '' }
];
