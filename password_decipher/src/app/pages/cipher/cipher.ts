import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@Component({
  standalone: true,
  imports: [ReactiveFormsModule, HttpClientModule],
  templateUrl: './cipher.html',
  styleUrls: ['./cipher.scss']
})


export class Cipher{
  constructor(private http: HttpClient) {}
  captureData(action: string, method: string, text: string, key: string) {

    let payload : any = {}
    payload.content = text

    if(action == 'cipher'){
      if(method == 'cesar'){
        payload.password = parseInt(key);
        this.http.post('http://localhost:8000/cesar/cipher', payload)
        .subscribe(res => {
          console.log('Respuesta API:', res);
        });
      } else if(method == 'vigerene'){
        payload.password = key;
        this.http.post('http://localhost:8000/vigerene/cipher', payload)
        .subscribe(res => {
          console.log('Respuesta API:', res);
        });
      } 
    } else if(action == 'decipher'){
      if(method == 'cesar'){
        payload.password = parseInt(key);
        this.http.post('http://localhost:8000/cesar/decipher', payload)
        .subscribe(res => {
          console.log('Respuesta API:', res);
        });
      } else if(method == 'vigerene'){
        payload.password = key;
        this.http.post('http://localhost:8000/vigerene/decipher', payload)
        .subscribe(res => {
          console.log('Respuesta API:', res);
        });
      } 
    }
  }
}
