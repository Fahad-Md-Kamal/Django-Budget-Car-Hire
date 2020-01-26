import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Blog } from '../interfaces/blog.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  BASE_URL = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'})

  blogs: Blog[] = [];

  constructor(private http: HttpClient) { }

  getAllBlogs(): Observable<any> {
    return this.http.get(this.BASE_URL+'/api/status/', 
      {headers: this.httpHeaders});
  }
}
