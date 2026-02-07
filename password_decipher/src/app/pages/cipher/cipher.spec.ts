import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Cipher } from './cipher';

describe('Cipher', () => {
  let component: Cipher;
  let fixture: ComponentFixture<Cipher>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Cipher]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Cipher);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
