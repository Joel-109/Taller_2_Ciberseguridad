import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { JsonPipe } from '@angular/common';
import { NgIf } from '@angular/common';

@Component({
  standalone: true,
  imports: [ReactiveFormsModule, HttpClientModule,JsonPipe,NgIf],
  templateUrl: './cipher.html',
  styleUrls: ['./cipher.scss']
})

export class Cipher{
  apiResult: any = null;
  phrase: String = '';
  constructor(private http: HttpClient) {}
  captureData(
    actionEl: HTMLSelectElement,
    methodEl: HTMLSelectElement,
    textEl: HTMLInputElement,
    keyEl: HTMLInputElement
  ) {

    const action = actionEl.value;
    const method = methodEl.value;
    const text = textEl.value;
    let key = keyEl.value;

    let payload: any = {};
    payload.content = text;


    
    // ----- TU LÓGICA ACTUAL (NO LA TOCAMOS) -----

    if (action === 'cipher') {
      if (method === 'cesar') {
        payload.password = parseInt(key);
        this.http.post('http://localhost:8000/cesar/cipher', payload)
          .subscribe(res => this.apiResult = res);
      } else if (method === 'vigenere') {
        if(key.length == 0){
          payload.password = null
        } else {
          payload.password = key;
        }
        this.http.post('http://localhost:8000/vigerene/cipher', payload)
          .subscribe(res => this.apiResult = res);
      }
    }

    if (action === 'decipher') {
      if (method === 'cesar') {
        payload.password = parseInt(key);
        this.http.post('http://localhost:8000/cesar/decipher', payload)
          .subscribe(res => this.apiResult = res);
      } else if (method === 'vigenere') {
        if(key.length == 0){
          payload.password = null
        } else {
          payload.password = key;
        }
        this.http.post('http://localhost:8000/vigerene/decipher', payload)
          .subscribe(res => this.apiResult = res);
      }
    }

    // ----- 🔥 LIMPIAR CAMPOS (AQUÍ ESTÁ LO QUE QUIERES) -----

    actionEl.value = '';
    methodEl.value = '';
    textEl.value = '';
    keyEl.value = '';
  }

}
